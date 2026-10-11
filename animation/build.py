#!/usr/bin/env python3
"""Build THE LAW BEHIND THE DEAL - Episode 1 as an MP4 with natural neural voices.

    python animation/build.py --models /path/to/kokoro-models      # full render
    python animation/build.py --preview 12.5 40 95                 # still frames

Steps: synthesise each line with Kokoro TTS -> lay out the voice-driven
timeline -> mix voice, music and sound effects -> render every scene with
skia in parallel -> concatenate, mux audio and add an SRT subtitle track.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from lw_anim import audio as A  # noqa: E402
from lw_anim import script_ep1 as S  # noqa: E402
from lw_anim.voice import SR, Voice, build_timeline, save_timeline  # noqa: E402


def _surface(width, height):
    import skia
    return skia.Surface(width, height)


def _draw(c, scenes, idx, t_local, width):
    from lw_anim import scenes as SC
    from lw_anim.gfx import W
    sc = scenes[idx]
    c.save()
    c.scale(width / W, width / W)
    st = SC.ST(sc)
    SC.DRAW[sc["key"]](c, t_local, st)
    SC.overlay(c, t_local, sc, idx)
    c.restore()


def render_scene(args):
    idx, tl_path, out_path, fps, width, height = args
    import numpy as np
    with open(tl_path) as f:
        tl = json.load(f)
    sc = tl["scenes"][idx]
    n_frames = round((sc["start"] + sc["dur"]) * fps) - round(sc["start"] * fps)
    first = round(sc["start"] * fps)
    surf = _surface(width, height)
    c = surf.getCanvas()
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgba",
           "-s", f"{width}x{height}", "-r", str(fps), "-i", "-", "-c:v", "libx264",
           "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-tune", "animation",
           out_path]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    buf = np.empty((height, width, 4), dtype=np.uint8)
    for i in range(n_frames):
        t_local = (first + i) / fps - sc["start"]
        c.clear(0xFF000000)
        _draw(c, tl["scenes"], idx, t_local, width)
        surf.readPixels(_info(width, height), buf)
        proc.stdin.write(buf.tobytes())
    proc.stdin.close()
    proc.wait()
    return idx, n_frames


def _info(w, h):
    import skia
    return skia.ImageInfo.Make(w, h, skia.kRGBA_8888_ColorType, skia.kPremul_AlphaType)


def srt_time(x):
    ms = int(round(x * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def write_srt(tl, path):
    n = 0
    with open(path, "w", encoding="utf-8") as f:
        for sc in tl["scenes"]:
            for ln in sc["lines"]:
                n += 1
                who = S.DISPLAY_NAMES[ln["who"]]
                f.write(f"{n}\n{srt_time(sc['start'] + ln['t0'])} --> "
                        f"{srt_time(sc['start'] + ln['t1'] + 0.25)}\n{who}: {ln['text']}\n\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", default=os.environ.get("KOKORO_MODELS",
                                                       os.path.join(HERE, "models")))
    ap.add_argument("--build", default=os.path.join(HERE, "build"))
    ap.add_argument("--out", default=os.path.join(HERE, "output"))
    ap.add_argument("--fps", type=int, default=24)
    ap.add_argument("--width", type=int, default=1280)
    ap.add_argument("--jobs", type=int, default=os.cpu_count() or 2)
    ap.add_argument("--preview", type=float, nargs="*",
                    help="render PNG stills at these global times (seconds) and exit")
    ap.add_argument("--no-music", action="store_true")
    a = ap.parse_args()
    height = a.width * 9 // 16
    os.makedirs(a.build, exist_ok=True)
    os.makedirs(a.out, exist_ok=True)

    voice = Voice(a.models, os.path.join(a.build, "voice_cache"))
    tl, clips = build_timeline(S.SCENES, S.VOICES, voice)
    tl_path = os.path.join(a.build, "timeline.json")
    save_timeline(tl, tl_path)
    print(f"timeline: {tl['total']:.1f}s across {len(tl['scenes'])} scenes")
    for sc in tl["scenes"]:
        print(f"  {sc['key']:6s} start {sc['start']:7.2f}s  dur {sc['dur']:6.2f}s  "
              f"{sc['title']}")

    if a.preview is not None:
        import skia
        surf = _surface(a.width, height)
        for gt in a.preview:
            idx = max(i for i, sc in enumerate(tl["scenes"]) if sc["start"] <= gt)
            c = surf.getCanvas()
            c.clear(0xFF000000)
            _draw(c, tl["scenes"], idx, gt - tl["scenes"][idx]["start"], a.width)
            p = os.path.join(a.build, f"preview_{gt:07.2f}.png")
            surf.makeImageSnapshot().save(p, skia.kPNG)
            print("wrote", p)
        return

    # audio
    import soundfile as sf
    mix = A.mix(tl["total"], clips, tl["sfx"], music=not a.no_music)
    wav = os.path.join(a.build, "mix.wav")
    sf.write(wav, mix, SR)
    srt = os.path.join(a.out, "episode1_who_makes_the_rules.srt")
    write_srt(tl, srt)

    # video segments in parallel (longest scenes first)
    order = sorted(range(len(tl["scenes"])), key=lambda i: -tl["scenes"][i]["dur"])
    jobs = [(i, tl_path, os.path.join(a.build, f"seg_{i:02d}.mp4"), a.fps, a.width, height)
            for i in order]
    with Pool(a.jobs) as pool:
        for idx, n in pool.imap_unordered(render_scene, jobs):
            print(f"  rendered scene {tl['scenes'][idx]['key']} ({n} frames)")
    lst = os.path.join(a.build, "segments.txt")
    with open(lst, "w") as f:
        for i in range(len(tl["scenes"])):
            f.write(f"file '{os.path.abspath(os.path.join(a.build, f'seg_{i:02d}.mp4'))}'\n")
    out = os.path.join(a.out, "episode1_who_makes_the_rules.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
                    "-i", lst, "-i", wav, "-i", srt, "-map", "0:v", "-map", "1:a",
                    "-map", "2:s", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k",
                    "-c:s", "mov_text", "-metadata:s:s:0", "language=eng",
                    "-metadata", f"title={S.SERIES} - {S.EPISODE}: {S.EPISODE_TITLE}",
                    "-movflags", "+faststart", "-t", str(tl["total"]), out], check=True)
    print("wrote", out)


if __name__ == "__main__":
    main()
