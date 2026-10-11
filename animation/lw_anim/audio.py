"""Procedural music bed, sound effects and the final mix (no external samples)."""
from __future__ import annotations

import numpy as np

SR = 24000
rng = np.random.default_rng(7)


def _t(d):
    return np.arange(int(d * SR)) / SR


def _env(n, a=0.005, r=0.2):
    t = np.arange(n) / SR
    e = np.minimum(1, t / max(a, 1e-4)) * np.exp(-t / max(r, 1e-4))
    return e


def note(f, d, r=0.5, harm=(1, 0.35, 0.12)):
    t = _t(d)
    y = sum(h * np.sin(2 * np.pi * f * (i + 1) * t) for i, h in enumerate(harm))
    return y * _env(len(t), 0.004, r)


def midi(m):
    return 440 * 2 ** ((m - 69) / 12)


def _noise(d):
    return rng.standard_normal(int(d * SR))


def _smooth(x, k):
    k = max(1, int(k))
    return np.convolve(x, np.ones(k) / k, mode="same")


def sfx(kind):
    if kind == "pop":
        t = _t(0.12)
        f = 420 + 900 * t / 0.12
        return 0.5 * np.sin(2 * np.pi * np.cumsum(f) / SR) * _env(len(t), 0.002, 0.04)
    if kind == "paper":
        n = _noise(0.3)
        n = n - _smooth(n, 6)
        return 0.25 * n * _env(len(n), 0.01, 0.08)
    if kind == "whoosh":
        d = 0.6
        n = _noise(d)
        out = np.zeros_like(n)
        seg = len(n) // 12
        for i in range(12):
            k = int(40 - 3 * i)
            out[i * seg:(i + 1) * seg] = _smooth(n, k)[i * seg:(i + 1) * seg]
        e = np.sin(np.pi * np.linspace(0, 1, len(n))) ** 2
        return 0.9 * out * e
    if kind == "door":
        t = _t(0.35)
        th = np.sin(2 * np.pi * 90 * t) * _env(len(t), 0.002, 0.08)
        cr = np.sin(2 * np.pi * (300 + 120 * np.sin(2 * np.pi * 7 * t)) * t) * 0.15 \
            * _env(len(t), 0.05, 0.15)
        return 0.6 * th + cr
    if kind == "rise":
        t = _t(0.7)
        f = 180 + 260 * (t / 0.7) ** 1.5
        y = np.sin(2 * np.pi * np.cumsum(f) / SR) + 0.3 * np.sin(4 * np.pi * np.cumsum(f) / SR)
        return 0.18 * y * np.sin(np.pi * t / 0.7)
    if kind == "sparkle":
        out = np.zeros(int(0.9 * SR))
        for i, m in enumerate([88, 93, 96, 100, 103]):
            s = note(midi(m), 0.4, 0.12, (1, 0.2))
            o = int(i * 0.09 * SR)
            out[o:o + len(s)] += s[:len(out) - o]
        return 0.18 * out
    if kind == "tick":
        t = _t(0.05)
        return 0.35 * np.sin(2 * np.pi * 1800 * t) * _env(len(t), 0.001, 0.008)
    if kind == "ding":
        return 0.35 * (note(midi(88), 1.4, 0.5, (1, 0.4, 0.2)) +
                       0.6 * note(midi(95), 1.4, 0.4, (1, 0.2)))
    if kind == "pin":
        t = _t(0.12)
        return 0.4 * np.sin(2 * np.pi * 220 * t) * _env(len(t), 0.001, 0.025) + \
            0.12 * _noise(0.12) * _env(len(t), 0.001, 0.01)
    if kind == "horn":
        t = _t(1.6)
        saw = sum(np.sin(2 * np.pi * 98 * k * t) / k for k in range(1, 8))
        saw += 0.6 * sum(np.sin(2 * np.pi * 147 * k * t) / k for k in range(1, 6))
        e = np.minimum(1, t / 0.15) * np.minimum(1, (1.6 - t) / 0.4)
        return 0.12 * saw * e
    if kind == "jingle":
        return jingle()
    raise ValueError(kind)


def jingle():
    out = np.zeros(int(3.6 * SR))
    seq = [60, 64, 67, 72, 76, 79]
    for i, m in enumerate(seq):
        s = note(midi(m), 1.2, 0.35, (1, 0.5, 0.2, 0.08))
        o = int(i * 0.12 * SR)
        out[o:o + len(s)] += 0.5 * s
    o = int(0.85 * SR)
    for m in (60, 64, 67, 72):
        s = note(midi(m), 2.6, 1.0, (1, 0.3, 0.1))
        out[o:o + len(s)] += 0.3 * s
    return 0.4 * out


def music_bed(total):
    """Light marimba-style loop, I-vi-IV-V at 96 bpm."""
    beat = 60 / 96
    chords = [(48, 60, 64, 67), (45, 57, 60, 64), (41, 57, 60, 65), (43, 55, 59, 62)]
    n = int(total * SR) + SR * 2
    out = np.zeros(n)
    bar = 0
    t = 0.0
    while t < total:
        ch = chords[bar % 4]
        pattern = [ch[1], ch[2], ch[3], ch[2], ch[1] + 12, ch[3], ch[2], ch[3]]
        for i, m in enumerate(pattern):
            s = note(midi(m), 0.6, 0.18, (1, 0.25, 0.05))
            o = int((t + i * beat / 2) * SR)
            if o + len(s) < n:
                out[o:o + len(s)] += 0.10 * s
        b = note(midi(ch[0]), beat * 4, 0.9, (1, 0.4, 0.1))
        o = int(t * SR)
        if o + len(b) < n:
            out[o:o + len(b)] += 0.10 * b
        t += beat * 4
        bar += 1
    return out[: int(total * SR)]


def mix(total, clips, sfx_events, music=True):
    n = int(total * SR) + SR
    voice = np.zeros(n, dtype=np.float64)
    for start, audio in clips:
        o = int(start * SR)
        voice[o:o + len(audio)] += audio[: n - o]
    fx = np.zeros(n)
    for ev in sfx_events:
        s = sfx(ev["kind"])
        o = int(ev["t"] * SR)
        fx[o:o + len(s)] += s[: n - o]
    out = voice * 1.0 + fx * 0.8
    if music:
        bed = np.zeros(n)
        bed[: int(total * SR)] = music_bed(total)
        speaking = _smooth((np.abs(voice) > 0.01).astype(float), int(0.4 * SR))
        duck = 1.0 - 0.6 * np.clip(speaking * 3, 0, 1)
        out += bed * duck * 0.55
    # fade in/out and limiter
    fade = int(0.5 * SR)
    out[:fade] *= np.linspace(0, 1, fade)
    out[int(total * SR) - fade:int(total * SR)] *= np.linspace(1, 0, fade)
    out = out[: int(total * SR)]
    peak = np.max(np.abs(out)) + 1e-9
    out = np.tanh(out / peak * 1.2) / np.tanh(1.2) * 0.92
    return out.astype(np.float32)
