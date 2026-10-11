"""Neural text-to-speech (Kokoro-82M via kokoro-onnx) and the episode timeline.

Each spoken line is synthesised once and cached as a WAV file. Line durations
drive the timing of every scene, so the animation always matches the voice.
"""
from __future__ import annotations

import hashlib
import json
import os

import numpy as np
import soundfile as sf

from .beats import Line, Pause, Sfx

SR = 24000
FPS_ENV = 60  # resolution of the lip-sync envelope


class Voice:
    def __init__(self, model_dir, cache_dir):
        self.model_dir = model_dir
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)
        self._k = None

    def _kokoro(self):
        if self._k is None:
            from kokoro_onnx import Kokoro
            self._k = Kokoro(os.path.join(self.model_dir, "kokoro-v1.0.onnx"),
                             os.path.join(self.model_dir, "voices-v1.0.bin"))
        return self._k

    def line(self, text, voice, speed):
        key = hashlib.sha1(f"{voice}|{speed}|{text}".encode()).hexdigest()[:16]
        path = os.path.join(self.cache_dir, f"{key}.wav")
        if not os.path.exists(path):
            samples, sr = self._kokoro().create(text, voice=voice, speed=speed,
                                                lang="en-gb" if voice.startswith("b")
                                                else "en-us")
            assert sr == SR
            samples = _trim(np.asarray(samples, dtype=np.float32))
            sf.write(path, samples, SR)
        audio, _ = sf.read(path, dtype="float32")
        return audio


def _trim(x, thresh=0.01, pad=0.04):
    idx = np.where(np.abs(x) > thresh)[0]
    if len(idx) == 0:
        return x
    a = max(0, idx[0] - int(pad * SR))
    b = min(len(x), idx[-1] + int(pad * SR))
    return x[a:b]


def envelope(audio):
    """Mouth-openness envelope (0..1) sampled at FPS_ENV."""
    hop = SR // FPS_ENV
    n = len(audio) // hop + 1
    pad = np.pad(audio, (0, n * hop - len(audio)))
    rms = np.sqrt((pad.reshape(n, hop) ** 2).mean(axis=1))
    rms = rms / (np.percentile(rms, 95) + 1e-6)
    env = np.clip((rms - 0.12) * 1.3, 0, 1)
    # gentle smoothing so the mouth does not flicker
    k = np.array([0.25, 0.5, 0.25])
    env = np.convolve(env, k, mode="same")
    return env.round(3).tolist()


def build_timeline(scenes, voices, voice: Voice, lead=0.6, tail=0.4):
    """Lay out every scene; returns (timeline dict, list of (start, audio))."""
    t = 0.0
    out_scenes, clips, sfx = [], [], []
    for sc in scenes:
        st = t
        cur = lead if sc.key != "title" else 0.3
        events, lines = {}, []
        for b in sc.beats:
            if isinstance(b, Sfx):
                sfx.append({"t": round(st + cur + b.offset, 3), "kind": b.kind})
            elif isinstance(b, Pause):
                events[b.id] = [round(cur, 3), round(cur + b.dur, 3)]
                cur += b.dur
            elif isinstance(b, Line):
                v, spd = voices[b.who]
                audio = voice.line(b.say or b.text, v, spd)
                d = len(audio) / SR
                events[b.id] = [round(cur, 3), round(cur + d, 3)]
                lines.append({"id": b.id, "who": b.who, "text": b.text,
                              "t0": round(cur, 3), "t1": round(cur + d, 3),
                              "env": envelope(audio)})
                clips.append((st + cur, audio))
                cur += d + b.gap
        cur += tail
        out_scenes.append({"key": sc.key, "title": sc.title, "clock": sc.clock,
                           "start": round(st, 3), "dur": round(cur, 3),
                           "events": events, "lines": lines,
                           "spec": getattr(sc, "spec", None)})
        t += cur
    return {"total": round(t, 3), "scenes": out_scenes, "sfx": sfx}, clips


def save_timeline(tl, path):
    with open(path, "w") as f:
        json.dump(tl, f)
