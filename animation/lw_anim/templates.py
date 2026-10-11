"""Data-driven scene templates used by Episodes 2 onwards.

A scene's `spec` dict picks a template (`tpl`) and describes what appears and
when. Timing is never hard-coded: every element names a *cue*, which is a
line or pause id from the script. A cue can be

    "lex3"          the start of that line / pause
    "lex3$"         its end
    ["lex3", 0.8]   0.8 s after its start (offset may be negative)
    2.5             an absolute scene time in seconds

so the pictures always stay in sync with the voices.

Layout convention (1920x1080): a presenter usually stands on the left
(x < 460) and the teaching graphic fills the content zone to the right.
"""
from __future__ import annotations

import math

import skia

from . import props as P
from .characters import draw_cargo, draw_person, mini_person, pose_track
from .gfx import (H, W, alpha_layer, at, circle, clamp, col, ease_in_out, ease_out,
                  ease_out_back, ellipse, fill, lerp, lin_grad, line, pop_scale, prog,
                  rad_grad, rect, shade, stroke, text, text_block, text_width, window,
                  wrap)
from .icons import icon

INK = "#1d2b3a"
TEAL = "#0f8b8d"
CX0, CX1 = 480, 1880          # content zone
PALETTE = ["#0f8b8d", "#7768ae", "#e4572e", "#f2a541", "#3bb273", "#2b86c5",
           "#d64f8a", "#5b6670"]


# ================================================================ timing
def cue(st, ref, default=None):
    if ref is None:
        return default
    if isinstance(ref, (int, float)):
        return float(ref)
    if isinstance(ref, (list, tuple)):
        return cue(st, ref[0]) + float(ref[1])
    if ref.endswith("$"):
        return st.end(ref[:-1])
    return st.at(ref)


def active(st, ref, t):
    """True while the line/pause named by ref is playing."""
    if not isinstance(ref, str):
        return False
    k = ref.rstrip("$")
    if k not in st.ev:
        return False
    return st.at(k) <= t <= st.end(k)


def timed(st, t, keys, default):
    val = default
    for ref, v in keys or []:
        if t >= cue(st, ref):
            val = v
    return val


def appear(st, t, ref, dur=0.45):
    """(scale, alpha) of an element that pops in at `ref`; ref None = always."""
    if ref is None:
        return 1.0, 1.0
    t0 = cue(st, ref)
    if t < t0:
        return 0.0, 0.0
    return pop_scale(t, t0, dur), clamp((t - t0) / 0.2)


def gone(st, t, ref, fade=0.35):
    """Alpha multiplier for an element that leaves at `ref` (None = never)."""
    if ref is None:
        return 1.0
    return 1 - ease_in_out(prog(t, cue(st, ref), fade))


# ================================================================ cast
def _speaker(st, t, cast):
    for m in cast:
        if st.talking(m["who"], t):
            return m
    return None


def cast_x(st, t, m):
    x = m.get("x", 260)
    if "enter" in m:
        t_in = cue(st, m["enter"])
        side = m.get("from", "right" if x > W / 2 else "left")
        x0 = W + 260 if side == "right" else -260
        x = lerp(x0, x, ease_out(prog(t, t_in, 0.8)))
    if "exit" in m:
        t_out = cue(st, m["exit"])
        side = m.get("to", "right" if x > W / 2 else "left")
        x1 = W + 300 if side == "right" else -300
        x = lerp(x, x1, ease_in_out(prog(t, t_out, 0.8)))
    return x


def draw_cast(c, st, t, cast, focus_x=None):
    if not cast:
        return
    spk = _speaker(st, t, cast)
    for m in cast:
        who = m["who"]
        if "enter" in m and t < cue(st, m["enter"]) - 0.02:
            continue
        if "exit" in m and t > cue(st, m["exit"]) + 0.9:
            continue
        x = cast_x(st, t, m)
        y, s = m.get("y", 1060), m.get("s", 0.82)
        # gaze: towards the speaker, else towards the focus / screen centre
        if "look" in m:
            look = timed(st, t, m.get("looks"), m["look"])
        else:
            if spk is not None and spk is not m:
                tx = cast_x(st, t, spk)
            else:
                tx = focus_x if focus_x is not None else W / 2
            look = clamp((tx - x) / 500, -1, 1)
            if m.get("flip"):
                look = -look
        mood = timed(st, t, m.get("moods"), m.get("mood", "neutral"))
        base = m.get("pose", "idle")
        if "poses" in m:
            keys = [(0, base)] + [(cue(st, r), p) for r, p in m["poses"]]
        else:
            tp = m.get("talk_pose", "present" if who == "LEX" else "idle")
            keys = [(0, base)]
            if tp != base:
                for ln in st.lines:
                    if ln["who"] == who:
                        keys += [(ln["t0"] - 0.15, tp), (ln["t1"] + 0.3, base)]
                keys.sort(key=lambda k: k[0])
        pose = pose_track(t, keys)
        bob = 0.0
        if "enter" in m:
            k = prog(t, cue(st, m["enter"]), 0.8)
            bob = abs(math.sin(t * 14)) * 20 * (1 - k) if k < 1 else 0.0
        if who == "CARGO":
            draw_cargo(c, x, y, s * 1.15, mouth=st.mouth(who, t), mood=mood if mood != "neutral"
                       else "happy", look=look, t=t, talking=st.talking(who, t))
            continue
        talking = st.talking(who, t)
        if talking and mood == "neutral":
            mood = "smile"
        draw_person(c, x, y, who, s, pose=pose, mouth=st.mouth(who, t), mood=mood,
                    look=look, t=t, talking=talking, flip=m.get("flip", False), bob=bob)


# ================================================================ backgrounds
def _wall(c, top, bottom, floor_top="#d7b48c", floor_bot="#c39a6e", fy=860):
    c.drawRect(skia.Rect.MakeWH(W, H), lin_grad(0, 0, 0, fy, [top, bottom]))
    c.drawRect(skia.Rect.MakeLTRB(0, fy, W, H), lin_grad(0, fy, 0, H, [floor_top, floor_bot]))
    rect(c, 0, fy - 8, W, 14, fc=shade(floor_top, -0.15))


def bg_classroom(c, t):
    _wall(c, "#eef5f8", "#dbe9f0", "#c9b08f", "#b39270")
    for i in range(0, W, 160):
        rect(c, i, 0, 4, 852, fc="#ffffff", a=0.4)


def bg_bank(c, t):
    _wall(c, "#f7f1e6", "#eadfcb", "#d9d2c5", "#bfb6a6")
    for x in (120, 520, 1400, 1800):
        rect(c, x - 40, 60, 80, 790, fc="#fffaf0", sc="#d8ccb4", sw=4)
        rect(c, x - 58, 40, 116, 30, fc="#efe4cf", sc="#d8ccb4", sw=4, r=4)
        rect(c, x - 58, 830, 116, 26, fc="#efe4cf", sc="#d8ccb4", sw=4, r=4)
        for k in range(-2, 3):
            line(c, x + k * 13, 90, x + k * 13, 820, "#e7dcc6", 3)
    with at(c, 960, 360):
        circle(c, 0, 0, 230, fc="#b9c2cb", sc="#6c7a89", sw=10)
        circle(c, 0, 0, 170, fc="#cfd6dd", sc="#8a96a3", sw=8)
        with at(c, 0, 0, rot=t * 8):
            for i in range(6):
                with at(c, 0, 0, rot=i * 60):
                    rect(c, -8, -150, 16, 110, fc="#8a96a3", r=6)
        circle(c, 0, 0, 40, fc="#6c7a89")
    for i in range(0, W, 120):
        line(c, i, 868, i - 200, H, "#ffffff", 3, 0.35)


def bg_boardroom(c, t):
    _wall(c, "#5e4636", "#4a3628", "#8c5a3c", "#6b4430")
    for i in range(0, W, 140):
        rect(c, i + 8, 0, 124, 852, fc="#ffffff", a=0.04, r=6)
    wx, wy, ww, wh = 620, 80, 680, 380
    rect(c, wx - 16, wy - 16, ww + 32, wh + 32, fc="#2d2018", r=10)
    c.save()
    c.clipRect(skia.Rect.MakeXYWH(wx, wy, ww, wh))
    P.skyline(c, wx, wy, ww, wh, t)
    c.restore()
    line(c, wx + ww / 2, wy, wx + ww / 2, wy + wh, "#2d2018", 10)
    for x, colr in ((260, "#e9c46a"), (1620, "#9fe3df")):
        rect(c, x - 90, 140, 180, 220, fc="#2d2018", r=6)
        rect(c, x - 76, 154, 152, 192, fc=colr, a=0.6, r=4)
        circle(c, x, 230, 38, fc="#ffffff", a=0.5)
    # long table
    ellipse(c, W / 2, 900, 820, 70, fc="#3a281d")
    ellipse(c, W / 2, 884, 800, 62, fc="#7a4f35", sc="#3a281d", sw=6)


def bg_port(c, t):
    c.drawRect(skia.Rect.MakeWH(W, H), lin_grad(0, 0, 0, 640, ["#8fd3ff", "#e3f6ff"]))
    circle(c, 1620, 150, 70, fc="#ffd166")
    for i in range(3):
        cx = ((i * 640 + t * 22) % (W + 400)) - 200
        for dx, r in ((0, 36), (40, 48), (88, 34)):
            circle(c, cx + dx, 120 + i * 50, r, fc="#ffffff", a=0.9)
    c.drawRect(skia.Rect.MakeLTRB(0, 600, W, H), lin_grad(0, 600, 0, H, ["#2b86c5", "#1b5f93"]))
    for i in range(8):
        yy = 630 + i * 50
        off = (t * 40 + i * 60) % 120
        for k in range(-1, 18):
            line(c, k * 120 + off, yy, k * 120 + off + 40, yy, "#ffffff", 3, 0.35)
    # quay on the left
    rect(c, 0, 560, 1120, 520, fc="#9aa5b0")
    rect(c, 0, 552, 1120, 16, fc="#6c7a89")
    rect(c, 1104, 560, 16, 520, fc="#6c7a89")
    for i, colr in enumerate(["#e4572e", "#0f8b8d", "#f2a541", "#7768ae", "#3bb273"]):
        for j in range(2):
            with at(c, 90 + i * 120, 520 - j * 70):
                rect(c, -55, -32, 110, 64, fc=shade(colr, -0.05 * j), sc=shade(colr, -0.35),
                     sw=3, r=3)
    with at(c, 640, 552):
        rect(c, -14, -420, 28, 420, fc="#f2a541", sc="#b07b0e", sw=3)
        rect(c, -260, -430, 420, 26, fc="#f2a541", sc="#b07b0e", sw=3)
        line(c, -200, -404, -200, -260 + 30 * math.sin(t), "#1d2b3a", 3)
    P.ship(c, 1500 + 20 * math.sin(t * 0.4), 690, 0.9, t)


def bg_globe(c, t):
    c.drawRect(skia.Rect.MakeWH(W, H), lin_grad(0, 0, 0, H, ["#13233a", "#1f3a5f"]))
    for i in range(60):
        x = (i * 263.7) % W
        y = (i * 137.3) % H
        tw = 0.4 + 0.6 * (0.5 + 0.5 * math.sin(t * 2 + i))
        circle(c, x, y, 2 + (i % 3), fc="#ffffff", a=0.3 * tw)


def bg_studio(c, t):
    P.studio_bg(c, t)


def bg_studio_teal(c, t):
    P.studio_bg(c, t, top="#e3f6f4", bottom="#bfe6e1")


def bg_studio_purple(c, t):
    P.studio_bg(c, t, top="#f1edfb", bottom="#d9d1f2")


def bg_studio_red(c, t):
    P.studio_bg(c, t, top="#fdece6", bottom="#f6cbbd")


def bg_night(c, t):
    P.night_bg(c, t)


def bg_office(c, t):
    P.office_bg(c, t)


def bg_harbour(c, t):
    P.office_bg(c, t, harbour=True)


def bg_court(c, t):
    P.courtroom(c, 0, 0, W, H, t)


def bg_arbitration(c, t):
    P.arb_room(c, 0, 0, W, H, t)


BGS = {k[3:]: v for k, v in globals().items() if k.startswith("bg_")}


def draw_bg(c, t, spec):
    BGS[spec.get("bg", "studio")](c, t)


def fit_size(s, size, max_w, family="Fredoka", weight=500):
    """Shrink a font size so a single line fits in max_w."""
    w = text_width(s, size, family, weight)
    return size if w <= max_w else size * max_w / w


# ================================================================ pops (extras)
def draw_pops(c, st, t, pops):
    """Floating extras: cards, icons, chips and stamps with their own cues."""
    for p in pops or []:
        s, a = appear(st, t, p.get("at"))
        a *= gone(st, t, p.get("until"))
        if a <= 0:
            continue
        if p.get("dim"):
            c.drawRect(skia.Rect.MakeWH(W, H), fill("#0b1622", 0.35 * a))
        kind = p.get("kind", "card")
        x, y = p.get("x", 1180), p.get("y", 300)
        colr = p.get("color", TEAL)
        if kind == "card":
            P.card(c, x, y, p.get("w", 640), p.get("h", 220), p.get("title"), p.get("body"),
                   colr, a=a, s=s, title_size=p.get("ts", 42), body_size=p.get("bs", 36),
                   align=p.get("align", "left"))
        elif kind == "icon":
            bob = math.sin(t * 2 + x) * 6 if p.get("float") else 0
            icon(c, p["icon"], x, y + bob, p.get("s", 1.0) * s, colr, a)
            if p.get("label"):
                P.chip(c, x, y + 70 * p.get("s", 1.0) + 34, p["label"], "#ffffff",
                       p.get("ls", 30), a=a, s=s, fg=INK)
        elif kind == "chip":
            P.chip(c, x, y, p["text"], colr, p.get("size", 36), a=a, s=s,
                   fg=p.get("fg", "#ffffff"))
        elif kind == "stamp":
            k = ease_out_back(prog(t, cue(st, p["at"]), 0.35), 2.0)
            with alpha_layer(c, a), at(c, x, y, lerp(2.2, 1.0, k), rot=p.get("rot", -10)):
                w = text_width(p["text"], p.get("size", 56), weight=700) + 70
                h = p.get("size", 56) * 1.7
                rect(c, -w / 2, -h / 2, w, h, sc=colr, sw=9, r=14)
                text(c, p["text"], 0, p.get("size", 56) * 0.36, p.get("size", 56), colr, 700,
                     "center")
        elif kind == "text":
            text_block(c, p["text"], x, y, p.get("w", 800), p.get("size", 40),
                       p.get("fg", INK), 650, p.get("align", "left"), a=a)


# ================================================================ heading
def heading(c, st, t, spec, y=88, x=None):
    h = spec.get("heading")
    if not h:
        return
    a = ease_in_out(prog(t, 0.3, 0.5))
    x = CX0 + (CX1 - CX0) / 2 if x is None else x
    w = text_width(h, 52, weight=700) + 80
    with alpha_layer(c, a):
        rect(c, x - w / 2, y - 50, w, 84, fc=INK, r=42)
        text(c, h, x, y + 8, 52, "#ffffff", 700, "center")


# ================================================================ TALK
def draw_talk(c, t, st, spec):
    draw_bg(c, t, spec)
    for d in spec.get("decor", []):
        s, a = appear(st, t, d.get("at"))
        if a > 0:
            icon(c, d["icon"], d["x"], d["y"], d.get("s", 1.0) * s, d.get("color", TEAL), a)
    draw_cast(c, st, t, spec.get("cast"))
    draw_pops(c, st, t, spec.get("pops"))


# ================================================================ BOARD
def _board_frame(c, x, y, w, h, chalk):
    rect(c, x + 10, y + 14, w, h, fc="#000000", a=0.18, r=18)
    if chalk:
        rect(c, x - 18, y - 18, w + 36, h + 36, fc="#8c5a3c", r=18)
        rect(c, x, y, w, h, fc="#2f5d50", r=8)
        for i in range(30):
            circle(c, x + (i * 173.3) % w, y + (i * 97.1) % h, 30 + (i % 4) * 10,
                   fc="#ffffff", a=0.015)
        rect(c, x - 10, y + h + 10, w + 20, 16, fc="#6b4430", r=6)
    else:
        rect(c, x - 14, y - 14, w + 28, h + 28, fc="#c8ced6", r=18)
        rect(c, x, y, w, h, fc="#ffffff", r=10)
        rect(c, x + 40, y + h + 6, w - 80, 14, fc="#aab4be", r=6)


def draw_board(c, t, st, spec):
    draw_bg(c, t, {"bg": spec.get("bg", "classroom")})
    chalk = spec.get("style", "white") == "chalk"
    bx, by, bw, bh = spec.get("box", (520, 70, 1340, 760))
    _board_frame(c, bx, by, bw, bh, chalk)
    fg = "#ffffff" if chalk else INK
    sub_fg = "#cfe7df" if chalk else "#5b6670"
    title = spec.get("heading")
    top = by + 30
    if title:
        text(c, title, bx + bw / 2, by + 78, 54, "#ffd166" if chalk else INK, 700, "center")
        line(c, bx + bw / 2 - 200, by + 100, bx + bw / 2 + 200, by + 100,
             "#ffd166" if chalk else TEAL, 6)
        top = by + 130
    items = spec.get("items", [])
    layout = spec.get("layout", "list")
    n = max(1, len(items))
    if layout == "list":
        row = min(spec.get("row", 132), (by + bh - 30 - top) / n)
        ts = spec.get("ts", 44 if row >= 110 else 38)
        for i, it in enumerate(items):
            s, a = appear(st, t, it.get("at"))
            if a <= 0:
                continue
            y = top + i * row + row / 2
            colr = it.get("color", PALETTE[i % len(PALETTE)])
            hl = window(t, cue(st, it["at"]), st.end(it["at"].rstrip("$"))
                        if isinstance(it.get("at"), str) and it["at"].rstrip("$") in st.ev
                        else -1, 0.25) if it.get("at") else 0
            with alpha_layer(c, a):
                if hl > 0:
                    rect(c, bx + 24, y - row / 2 + 6, bw - 48, row - 12, fc=colr,
                         a=0.16 * hl, r=16)
                with at(c, bx + 90, y, s):
                    circle(c, 0, 0, 46, fc=colr)
                    if it.get("icon"):
                        icon(c, it["icon"], 0, 0, 0.62, "#ffffff")
                    else:
                        text(c, str(it.get("n", i + 1)), 0, 16, 46, "#ffffff", 700, "center")
                tx = bx + 160
                avail = bx + bw - 30 - tx
                ts_i = fit_size(it["text"], ts, avail, weight=650)
                if it.get("sub"):
                    text(c, it["text"], tx, y - 4, ts_i, fg, 650)
                    ss = fit_size(it["sub"], ts * 0.68, avail, family="Nunito")
                    text(c, it["sub"], tx, y + ts * 0.85, ss, sub_fg, 500,
                         family="Nunito")
                else:
                    text(c, it["text"], tx, y + ts_i * 0.36, ts_i, fg, 650)
    else:  # grid of cards
        cols = spec.get("cols", 3)
        rows = math.ceil(n / cols)
        gw = (bw - 60) / cols
        gh = min(spec.get("cell_h", 300), (by + bh - 30 - top) / rows)
        for i, it in enumerate(items):
            s, a = appear(st, t, it.get("at"))
            if a <= 0:
                continue
            r_, k = divmod(i, cols)
            cx = bx + 30 + gw * k + gw / 2
            cy = top + gh * r_ + gh / 2
            colr = it.get("color", PALETTE[i % len(PALETTE)])
            hl = 1.0 if it.get("at") and active(st, it["at"], t) else 0.0
            with alpha_layer(c, a), at(c, cx, cy, s * (1 + 0.04 * hl)):
                w, h = gw - 30, gh - 24
                rect(c, -w / 2 + 6, -h / 2 + 8, w, h, fc="#000000", a=0.12, r=20)
                rect(c, -w / 2, -h / 2, w, h, fc=shade(colr, 0.86) if not chalk else
                     shade(colr, -0.25), sc=colr, sw=6 if hl else 3, r=20)
                isz = min(0.9, h / 300)
                iy = -h / 2 + 70 * isz + 14
                if it.get("icon"):
                    icon(c, it["icon"], 0, iy, isz, colr)
                ty = iy + 66 * isz + 14 if it.get("icon") else -h / 2 + 20
                ts = spec.get("ts", 40)
                for j, ln in enumerate(wrap(it["text"], ts, w - 30, weight=650)[:2]):
                    text(c, ln, 0, ty + ts + j * ts * 1.1, ts, fg, 650, "center")
                if it.get("sub"):
                    nl = len(wrap(it["text"], ts, w - 30, weight=650)[:2])
                    text_block(c, it["sub"], 0, ty + ts * 1.1 * nl + 8, w - 70, ts * 0.78,
                               sub_fg, 500, "center", family="Nunito")
    draw_cast(c, st, t, spec.get("cast", [{"who": "LEX", "x": 250}]), focus_x=bx + bw / 2)
    draw_pops(c, st, t, spec.get("pops"))


# ================================================================ COMPARE
def draw_compare(c, t, st, spec):
    draw_bg(c, t, {"bg": spec.get("bg", "studio")})
    heading(c, st, t, spec)
    cols = spec["cols"]
    n = len(cols)
    x0, x1 = spec.get("x0", CX0), spec.get("x1", CX1)
    top, bottom = spec.get("top", 170), spec.get("bottom", 870)
    gap = 40
    cw = (x1 - x0 - gap * (n - 1)) / n
    ts = spec.get("ts", 36)
    # fit the card height to the tallest column
    need = 0
    for colspec in cols:
        hh = 130
        for it in colspec.get("items", []):
            hh += len(wrap(it["text"], ts, cw - 90, weight=600)) * ts * 1.2 + 30
        need = max(need, hh + 20)
    bottom = min(bottom, top + max(need, 360))
    for k, colspec in enumerate(cols):
        s, a = appear(st, t, colspec.get("at"))
        if a <= 0:
            continue
        cx = x0 + k * (cw + gap)
        colr = colspec.get("color", PALETTE[k])
        with alpha_layer(c, a), at(c, cx + cw / 2, top, s, sy=s):
            rect(c, -cw / 2 + 8, 12, cw, bottom - top, fc="#000000", a=0.14, r=26)
            rect(c, -cw / 2, 0, cw, bottom - top, fc="#ffffff", r=26)
            rect(c, -cw / 2, 0, cw, 96, fc=colr, r=26)
            rect(c, -cw / 2, 60, cw, 36, fc=colr)
            hx = 0
            if colspec.get("icon"):
                tw = text_width(colspec["title"], 42, weight=700)
                hx = 30
                icon(c, colspec["icon"], hx - tw / 2 - 42, 48, 0.48, "#ffffff")
            text(c, colspec["title"], hx, 64, 42, "#ffffff", 700, "center")
        y = top + 130
        for it in colspec.get("items", []):
            si, ai = appear(st, t, it.get("at"))
            lines_ = wrap(it["text"], ts, cw - 90, weight=600)
            hgt = len(lines_) * ts * 1.2 + 22
            if ai > 0:
                hl = 1.0 if it.get("at") and active(st, it["at"], t) else 0.0
                with alpha_layer(c, ai * a):
                    if hl:
                        rect(c, cx + 14, y - 10, cw - 28, hgt, fc=colr, a=0.15, r=12)
                    with at(c, cx + 42, y + ts * 0.55, si):
                        if it.get("bad"):
                            P.cross(c, 0, 0, 0.6)
                        elif it.get("good"):
                            P.check(c, 0, 0, 0.6)
                        else:
                            circle(c, 0, 0, 10, fc=colr)
                    for j, ln in enumerate(lines_):
                        text(c, ln, cx + 70, y + ts * 0.9 + j * ts * 1.2, ts, INK, 600)
            y += hgt + 8
    if spec.get("vs") and n == 2:
        s, a = appear(st, t, cols[1].get("at"))
        if a > 0:
            with at(c, x0 + cw + gap / 2, top + 48, s):
                circle(c, 0, 0, 46, fc=INK, sc="#ffffff", sw=6)
                text(c, "VS", 0, 14, 38, "#ffd166", 700, "center")
    draw_cast(c, st, t, spec.get("cast", [{"who": "LEX", "x": 250}]),
              focus_x=(x0 + x1) / 2)
    draw_pops(c, st, t, spec.get("pops"))


# ================================================================ FLOW
def _node_box(nd):
    w = nd.get("w", 250)
    h = nd.get("h", 190 if nd.get("icon") else 110)
    return nd["x"] - w / 2, nd["y"] - h / 2, w, h


def _edge_point(nd, tx, ty):
    """Point on the node's box boundary towards (tx, ty)."""
    x, y, w, h = _node_box(nd)
    cx, cy = x + w / 2, y + h / 2
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0:
        return cx, cy
    sx = (w / 2 + 12) / abs(dx) if dx else 1e9
    sy = (h / 2 + 12) / abs(dy) if dy else 1e9
    k = min(sx, sy)
    return cx + dx * k, cy + dy * k


def _quad(p0, p1, p2, u):
    a = (1 - u) ** 2
    b = 2 * (1 - u) * u
    d = u * u
    return (a * p0[0] + b * p1[0] + d * p2[0], a * p0[1] + b * p1[1] + d * p2[1])


def draw_flow(c, t, st, spec):
    draw_bg(c, t, {"bg": spec.get("bg", "studio")})
    heading(c, st, t, spec)
    nodes = {nd["id"]: nd for nd in spec["nodes"]}
    # edges under nodes
    for e in spec.get("edges", []):
        a_, b_ = nodes[e["from"]], nodes[e["to"]]
        t0 = cue(st, e.get("at"), 0.0)
        if t < t0:
            continue
        k = ease_in_out(prog(t, t0, 0.7))
        bend = e.get("bend", 0)
        mx, my = (a_["x"] + b_["x"]) / 2, (a_["y"] + b_["y"]) / 2
        dx, dy = b_["x"] - a_["x"], b_["y"] - a_["y"]
        ln_ = math.hypot(dx, dy) or 1
        ctrl = (mx - dy / ln_ * bend, my + dx / ln_ * bend)
        p0 = _edge_point(a_, *ctrl)
        p2 = _edge_point(b_, *ctrl)
        colr = e.get("color", INK)
        hl = active(st, e.get("at"), t)
        wdt = 9 if hl else 7
        steps = 24
        pts = [_quad(p0, ctrl, p2, k * i / steps) for i in range(steps + 1)]
        path = skia.Path()
        path.moveTo(*pts[0])
        for q in pts[1:]:
            path.lineTo(*q)
        pnt = stroke(colr, wdt)
        if e.get("dashed"):
            pnt.setPathEffect(skia.DashPathEffect.Make([22, 14], -t * 40))
        c.drawPath(path, pnt)
        if k > 0.98:
            tx, ty = pts[-1]
            px, py = pts[-3]
            ang = math.atan2(ty - py, tx - px)
            hd = 26
            P.draw_path(c, P.poly([(tx + math.cos(ang) * 4, ty + math.sin(ang) * 4),
                                   (tx - math.cos(ang - 0.45) * hd, ty - math.sin(ang - 0.45) * hd),
                                   (tx - math.cos(ang + 0.45) * hd, ty - math.sin(ang + 0.45) * hd)]),
                        fc=colr)
            if e.get("label"):
                lx, ly = _quad(p0, ctrl, p2, 0.5)
                lx += e.get("lx", 0)
                ly += e.get("ly", 0)
                s_ = pop_scale(t, t0 + 0.6, 0.4)
                P.chip(c, lx, ly, e["label"], e.get("lcolor", "#ffffff"), e.get("ls", 28),
                       s=s_, fg=INK if e.get("lcolor", "#ffffff") == "#ffffff" else "#ffffff")
        # travelling token
        if e.get("token"):
            tt0 = cue(st, e.get("move", e.get("at")), t0) + 0.5
            u = ease_in_out(prog(t, tt0, e.get("tdur", 1.6)))
            if 0 < u < 1 or (u >= 1 and e.get("stay")):
                tx, ty = _quad(p0, ctrl, p2, u)
                a_tok = 1.0 if e.get("stay") else 1 - prog(u, 0.85, 0.15)
                icon(c, e["token"], tx, ty - 10, e.get("ts", 0.55), e.get("tcolor", TEAL),
                     a_tok)
    for nd in spec["nodes"]:
        s, a = appear(st, t, nd.get("at"))
        if a <= 0:
            continue
        x, y, w, h = _node_box(nd)
        colr = nd.get("color", TEAL)
        hl = 1.0 if nd.get("at") and active(st, nd["at"], t) else 0.0
        with alpha_layer(c, a), at(c, x + w / 2, y + h / 2, s * (1 + 0.05 * hl)):
            rect(c, -w / 2 + 6, -h / 2 + 10, w, h, fc="#000000", a=0.15, r=22)
            rect(c, -w / 2, -h / 2, w, h, fc="#ffffff", sc=colr, sw=8 if hl else 5, r=22)
            ly = 0
            if nd.get("icon"):
                icon(c, nd["icon"], 0, -h / 2 + 62, 0.8, colr)
                ly = 40
            ts = nd.get("ts", 32)
            lines_ = wrap(nd["label"], ts, w - 26, weight=650)
            y0 = ly - (len(lines_) - 1) * ts * 0.55
            for j, ln in enumerate(lines_):
                text(c, ln, 0, y0 + ts * 0.36 + j * ts * 1.1, ts, INK, 650, "center")
            if nd.get("tag"):
                P.chip(c, 0, -h / 2 - 4, nd["tag"], colr, 24)
    draw_cast(c, st, t, spec.get("cast", []), focus_x=(CX0 + CX1) / 2)
    draw_pops(c, st, t, spec.get("pops"))


# ================================================================ STACK (priority waterfall)
def draw_stack(c, t, st, spec):
    draw_bg(c, t, {"bg": spec.get("bg", "studio")})
    heading(c, st, t, spec)
    tiers = spec["tiers"]
    n = len(tiers)
    x0, x1 = spec.get("x0", 560), spec.get("x1", 1820)
    top = spec.get("top", 200)
    bottom = spec.get("bottom", 1000)
    th = min(110, (bottom - top) / n)
    pour = spec.get("pour")
    for i, tr in enumerate(tiers):
        s, a = appear(st, t, tr.get("at"))
        if a <= 0:
            continue
        y = top + i * th
        colr = tr.get("color", PALETTE[i % len(PALETTE)])
        hl = 1.0 if tr.get("at") and active(st, tr["at"], t) else 0.0
        with alpha_layer(c, a), at(c, (x0 + x1) / 2, y + th / 2, s):
            w = x1 - x0
            rect(c, -w / 2, -th / 2 + 6, w, th - 12, fc="#ffffff", sc=colr, sw=7 if hl else 4,
                 r=16)
            # fill level from the pour
            if pour:
                fk = _fill_level(st, t, pour, i)
                if fk > 0:
                    fw = (w - 300) * fk
                    rect(c, w / 2 - 290, -th / 2 + 18, fw, th - 36, fc="#ffd166", r=10)
                    for j in range(int(fw // 46)):
                        circle(c, w / 2 - 270 + j * 46, 0, 15, fc="#ffb627", sc="#b07b0e", sw=2)
                rect(c, w / 2 - 290, -th / 2 + 18, w - 300, th - 36, sc="#d0d7de", sw=3, r=10)
            rect(c, -w / 2, -th / 2 + 6, 90, th - 12, fc=colr, r=16)
            text(c, str(tr.get("n", i + 1)), -w / 2 + 45, 16, 46, "#ffffff", 700, "center")
            ts = spec.get("ts", 34 if th > 90 else 30)
            ts = fit_size(tr["label"], ts, w - 420, weight=700)
            if tr.get("sub"):
                text(c, tr["label"], -w / 2 + 110, -2, ts, INK, 700)
                text(c, tr["sub"], -w / 2 + 110, ts * 0.95, ts * 0.72, "#5b6670", 500,
                     family="Nunito")
            else:
                text(c, tr["label"], -w / 2 + 110, ts * 0.36, ts, INK, 700)
            if pour:
                fk = _fill_level(st, t, pour, i)
                done = t > _tier_end(st, pour, i)
                if done:
                    target = pour["fills"][i]
                    lab, cc = (("PAID IN FULL", "#3bb273") if target >= 0.999 else
                               ("PART PAID", "#f2a541") if target > 0 else
                               ("NOTHING LEFT", "#e4572e"))
                    P.chip(c, w / 2 - 290 + (w - 300) / 2, 0, lab, cc, 26,
                           s=pop_scale(t, _tier_end(st, pour, i), 0.35))
    if pour:
        t0 = cue(st, pour["at"])
        if t >= t0 - 0.5:
            a = clamp((t - t0 + 0.5) / 0.4)
            with alpha_layer(c, a), at(c, x1 - 140, top - 70):
                icon(c, "moneybag", -120, 0, 0.9)
                text(c, pour.get("label", "Assets realised"), -60, 12, 34, INK, 700)
    draw_cast(c, st, t, spec.get("cast", [{"who": "LEX", "x": 250}]))
    draw_pops(c, st, t, spec.get("pops"))


def _tier_end(st, pour, i):
    t0 = cue(st, pour["at"])
    d = pour.get("dur", 1.1)
    return t0 + (i + 1) * d


def _fill_level(st, t, pour, i):
    t0 = cue(st, pour["at"]) + i * pour.get("dur", 1.1)
    return pour["fills"][i] * ease_in_out(prog(t, t0, pour.get("dur", 1.1)))


# ================================================================ ROUTE (Incoterms / risk)
STATIONS = [("Seller's premises", "factory"), ("Handed to carrier", "truck"),
            ("Alongside ship", "crane"), ("On board vessel", "ship"),
            ("Destination port", "crane"), ("Buyer's place", "warehouse")]
SX = [300, 560, 820, 1060, 1340, 1640]


def draw_route(c, t, st, spec):
    c.drawRect(skia.Rect.MakeWH(W, H), lin_grad(0, 0, 0, H, ["#e8f6ff", "#cdebf9"]))
    heading(c, st, t, spec, y=80, x=W / 2)
    base = 470
    # land / sea strip
    rect(c, 140, base - 40, 760, 120, fc="#9bbf7a", r=30)
    rect(c, 1260, base - 40, 520, 120, fc="#9bbf7a", r=30)
    c.drawRect(skia.Rect.MakeLTRB(880, base - 20, 1280, base + 80),
               lin_grad(0, base, 0, base + 80, ["#2b86c5", "#1b5f93"]))
    for k in range(5):
        off = (t * 30 + k * 40) % 80
        line(c, 880 + k * 80 + off, base + 30, 880 + k * 80 + off + 26, base + 30, "#ffffff",
             3, 0.5)
    stations = spec.get("stations", STATIONS)
    sx = spec.get("sx", SX)
    for i, (lab, ic) in enumerate(stations):
        with at(c, sx[i], base - 110):
            circle(c, 0, 0, 62, fc="#ffffff", sc="#8a96a3", sw=4)
            icon(c, ic, 0, 0, 0.72, TEAL)
        lines_ = wrap(lab, 30, 230, weight=650)
        for j, ln in enumerate(lines_):
            text(c, ln, sx[i], base + 112 + j * 34, 30, INK, 650, "center")
        circle(c, sx[i], base + 20, 14, fc=INK)
    line(c, sx[0], base + 20, sx[-1], base + 20, INK, 5)
    # current term
    terms = spec["terms"]
    cur = None
    for tm in terms:
        if t >= cue(st, tm["at"]) - 0.1:
            cur = tm
    prev = None
    for tm in terms:
        if cur is not None and tm is cur:
            break
        prev = tm
    if cur is not None:
        t0 = cue(st, cur["at"]) - 0.1
        k = ease_in_out(prog(t, t0, 0.9))

        def pos(v):
            i0 = int(math.floor(v))
            i1 = min(len(sx) - 1, i0 + 1)
            return lerp(sx[i0], sx[i1], v - i0)

        rp = cur["risk"]
        cp = cur.get("cost", rp)
        rp0 = prev["risk"] if prev is not None else 0
        cp0 = prev.get("cost", prev["risk"]) if prev is not None else 0
        rx = pos(lerp(rp0, rp, k))
        cx_ = pos(lerp(cp0, cp, k))
        # cost bar (seller pays carriage up to here)
        yb = 700
        text(c, "COSTS", 140, yb + 12, 32, "#5b6670", 700)
        rect(c, sx[0], yb - 27, sx[-1] - sx[0], 54, fc="#7768ae", r=27)
        rect(c, sx[0], yb - 27, max(54, cx_ - sx[0]), 54, fc=TEAL, r=27)
        text(c, "seller pays", sx[0] + 24, yb + 11, 30, "#ffffff", 650)
        text(c, "buyer pays", sx[-1] - 24, yb + 11, 30, "#ffffff", 650, "right")
        yr = 790
        text(c, "RISK", 140, yr + 12, 32, "#5b6670", 700)
        rect(c, sx[0], yr - 27, sx[-1] - sx[0], 54, fc="#e9d5f5", r=27)
        rect(c, sx[0], yr - 27, max(54, rx - sx[0]), 54, fc="#9fe3df", r=27)
        text(c, "seller's risk", sx[0] + 24, yr + 11, 30, INK, 650)
        text(c, "buyer's risk", sx[-1] - 24, yr + 11, 30, INK, 650, "right")
        # risk flag on the route
        with at(c, rx, base + 20):
            line(c, 0, 0, 0, -150, "#e4572e", 6)
            P.draw_path(c, P.poly([(0, -150), (90, -128), (0, -106)]), fc="#e4572e")
            text(c, "RISK", 34, -122, 22, "#ffffff", 700, "center")
        # big term label
        s = pop_scale(t, t0, 0.5)
        with at(c, 960, 930, s):
            w = text_width(cur["code"], 64, weight=700) + 60
            rect(c, -w - 20, -48, w, 96, fc=cur.get("color", INK), r=26)
            text(c, cur["code"], -w / 2 - 20, 22, 64, "#ffffff", 700, "center")
            text(c, cur.get("name", ""), 0, -6, 38, INK, 700)
            if cur.get("note"):
                text(c, cur["note"], 0, 34, 28, "#5b6670", 600, family="Nunito")
        if cur.get("insure"):
            icon(c, "umbrella", cx_ - 10, base - 230, 0.6 * pop_scale(t, t0 + 0.5, 0.4),
                 "#3bb273")
    draw_cast(c, st, t, spec.get("cast", []))
    draw_pops(c, st, t, spec.get("pops"))


# ================================================================ CASE FILE
def draw_case(c, t, st, spec):
    draw_bg(c, t, {"bg": spec.get("bg", "office")})
    c.drawRect(skia.Rect.MakeWH(W, H), fill("#0b1622", 0.25))
    s, a = appear(st, t, spec.get("at", 0.3), 0.6)
    fx, fy, fw, fh = spec.get("box", (560, 90, 1280, 820))
    with alpha_layer(c, a), at(c, fx + fw / 2, fy + fh / 2, s):
        x, y = -fw / 2, -fh / 2
        rect(c, x + 12, y + 16, fw, fh, fc="#000000", a=0.25, r=18)
        rect(c, x + 60, y - 40, 300, 70, fc="#e2b86b", r=14)
        text(c, "CASE FILE", x + 210, y + 4, 34, "#6b4430", 700, "center")
        rect(c, x, y, fw, fh, fc="#efc77f", r=18)
        rect(c, x + 30, y + 30, fw - 60, fh - 60, fc="#fffdf5", r=10)
        text(c, spec["name"], 0, y + 110, 56, INK, 700, "center")
        if spec.get("year"):
            text(c, spec["year"], 0, y + 160, 34, "#8a6d3b", 600, "center")
        yy = y + 200
        for row in spec.get("rows", []):
            sr, ar = appear(st, t, row.get("at"))
            if ar <= 0:
                continue
            colr = row.get("color", TEAL)
            with alpha_layer(c, ar):
                P.chip(c, x + 140, yy + 30, row["label"], colr, 30)
                h = text_block(c, row["text"], x + 250, yy - 6, fw - 330, 36, INK, 600)
            yy += max(h, 70) + 26
    if spec.get("stamp"):
        sp = spec["stamp"]
        t0 = cue(st, sp["at"])
        if t >= t0:
            k = ease_out_back(prog(t, t0, 0.35), 2.0)
            colr = sp.get("color", "#e4572e")
            with at(c, sp.get("x", fx + fw - 260), sp.get("y", fy + fh - 120), lerp(2.4, 1, k),
                    rot=-9):
                w = text_width(sp["text"], 48, weight=700) + 60
                rect(c, -w / 2, -44, w, 88, sc=colr, sw=8, r=12)
                text(c, sp["text"], 0, 17, 48, colr, 700, "center")
    draw_cast(c, st, t, spec.get("cast", [{"who": "LEX", "x": 250}]), focus_x=fx + fw / 2)
    draw_pops(c, st, t, spec.get("pops"))


# ================================================================ TIMELINE
def draw_timeline(c, t, st, spec):
    draw_bg(c, t, {"bg": spec.get("bg", "studio")})
    heading(c, st, t, spec)
    evs = spec["events"]
    n = len(evs)
    w = spec.get("cw", 300)
    x0 = max(spec.get("x0", 640), CX0 + w / 2)
    x1 = min(spec.get("x1", 1740), W - 30 - w / 2)
    y = spec.get("y", 570)
    h = spec.get("ch", 250)
    off = h / 2 + 70
    line(c, x0 - 40, y, x1 + 40, y, "#8a96a3", 10)
    cur = -1
    for i, ev in enumerate(evs):
        if t >= cue(st, ev.get("at"), 0):
            cur = i
    for i, ev in enumerate(evs):
        x = x0 + (x1 - x0) * (i / max(1, n - 1))
        s, a = appear(st, t, ev.get("at"))
        colr = ev.get("color", PALETTE[i % len(PALETTE)])
        circle(c, x, y, 20, fc=colr if a > 0 else "#c8ced6", sc="#ffffff", sw=5)
        if a <= 0:
            continue
        up = i % 2 == 0
        sg = 1 if up else -1
        cy = y - sg * off
        hl = 1.0 if ev.get("at") and active(st, ev["at"], t) else 0.0
        with alpha_layer(c, a), at(c, x, cy, s * (1 + 0.04 * hl)):
            line(c, 0, sg * h / 2, 0, sg * (off - 20), colr, 5)
            rect(c, -w / 2 + 6, -h / 2 + 8, w, h, fc="#000000", a=0.12, r=18)
            rect(c, -w / 2, -h / 2, w, h, fc="#ffffff", sc=colr, sw=7 if hl else 4, r=18)
            icon(c, ev.get("icon", "calendar"), 0, -h / 2 + 56, 0.66, colr)
            lab = wrap(ev["label"], 34, w - 30, weight=700)
            for j, ln in enumerate(lab):
                text(c, ln, 0, -h / 2 + 140 + j * 38, 34, INK, 700, "center")
            if ev.get("sub"):
                text_block(c, ev["sub"], 0, -h / 2 + 116 + 38 * len(lab), w - 30, 27,
                           "#5b6670", 500, "center", family="Nunito")
    if cur >= 0:
        x = x0 + (x1 - x0) * (cur / max(1, n - 1))
        icon(c, spec.get("marker", "flag"), x + 10, y - 50, 0.55, "#e4572e")
    draw_cast(c, st, t, spec.get("cast", [{"who": "LEX", "x": 250}]))
    draw_pops(c, st, t, spec.get("pops"))


# ================================================================ QUIZ
def draw_quiz(c, t, st, spec):
    draw_bg(c, t, {"bg": spec.get("bg", "studio_purple")})
    c.drawRect(skia.Rect.MakeWH(W, H), fill("#0b1622", 0.35))
    q, think, ans = spec.get("q", "q"), spec.get("think", "think"), spec.get("a", "a")
    s, a = appear(st, t, q, 0.5)
    k = ease_out(prog(t, cue(st, q) - 0.8, 0.8))
    draw_person(c, lerp(-250, 280, k), 1040, "AUDITOR", 0.9, pose="clipboard",
                mouth=st.mouth("AUDITOR", t),
                mood="smile" if t > cue(st, ans) else ("smile" if st.talking("AUDITOR", t)
                                                       else "neutral"),
                look=0.6, t=t, talking=st.talking("AUDITOR", t))
    opts = spec["options"]
    good_i = spec["answer"]
    revealed = t >= cue(st, ans) - 0.15
    with alpha_layer(c, a), at(c, 1180, 400, s):
        rect(c, -640, -320, 1280, 640, fc="#ffffff", r=32)
        rect(c, -640, -320, 1280, 90, fc=INK, r=32)
        rect(c, -640, -260, 1280, 30, fc=INK)
        text(c, spec.get("title", "QUICK CHECK"), -600, -258, 46, "#ffd166", 700)
        hq = text_block(c, spec["question"], -600, -220, 1200, 42, INK, 600)
        oy = -220 + hq + 30
        rows = len(opts)
        oh = min(86, (300 - oy + 20) / max(1, rows) + 40)
        for i, opt in enumerate(opts):
            y = oy + i * (oh + 6)
            good = revealed and i == good_i
            fc_ = "#3bb273" if good else ("#eef1f4" if revealed else "#e6ecf1")
            fg = "#ffffff" if good else ("#9aa5b0" if revealed else INK)
            sc_ = 1 + (0.03 * ease_out_back(prog(t, cue(st, ans) - 0.15, 0.4)) if good else 0)
            with at(c, 0, y + oh / 2, sc_):
                rect(c, -600, -oh / 2, 1200, oh, fc=fc_, r=20)
                circle(c, -550, 0, 26, fc="#ffffff" if not good else "#2f8d5a",
                       sc=INK if not good else None, sw=3)
                text(c, "ABCD"[i], -550, 12, 32, INK if not good else "#ffffff", 700,
                     "center")
                text(c, opt, -500, 13, 36 if len(opt) < 60 else 30, fg, 600)
                if good:
                    P.check(c, 560, 0, 1.0 * ease_out_back(prog(t, cue(st, ans), 0.4)))
    tt0, tt1 = cue(st, think), cue(st, think + "$")
    if tt0 - 0.2 <= t <= tt1 + 0.3:
        rem = clamp((tt1 - t) / max(0.1, tt1 - tt0))
        with at(c, 1760, 900):
            circle(c, 0, 0, 80, fc="#ffffff")
            c.drawArc(skia.Rect.MakeXYWH(-66, -66, 132, 132), -90, 360 * rem, False,
                      stroke("#ffb627", 16))
            nsec = max(1, math.ceil(rem * (tt1 - tt0)))
            text(c, str(nsec), 0, 24, 70, INK, 700, "center")
            text(c, "PAUSE & THINK", 0, 130, 30, "#ffffff", 700, "center")
    if spec.get("why") and t >= cue(st, spec.get("why_at", ans)) + 0.2:
        s2 = pop_scale(t, cue(st, spec.get("why_at", ans)) + 0.2, 0.5)
        with at(c, 1180, 860, s2):
            w = 1180
            h = 120
            rect(c, -w / 2, -h / 2, w, h, fc="#3bb273", r=24)
            text_block(c, spec["why"], 0, -h / 2 + 10, w - 60, 34, "#ffffff", 650, "center")
    draw_pops(c, st, t, spec.get("pops"))


# ================================================================ RECAP
def draw_recap(c, t, st, spec):
    win = (1400, 110, 460, 400)
    P.office_bg(c, t, harbour=True, window=win, sign=False)
    cards = spec["cards"]
    n = len(cards)
    bx, by, bw, bh = 380, 120, 900, 560
    P.corkboard(c, bx, by, bw, bh)
    text(c, spec.get("heading", "EPISODE RECAP"), bx + bw / 2, by + 56, 44, "#5e3b25", 700,
         "center")
    cols = 3 if n > 4 else 2
    rows = math.ceil(n / cols)
    cw, ch = 260, 170 if rows > 1 else 220
    for i, cd in enumerate(cards):
        tp = cue(st, cd["at"]) - 0.25
        if t < tp:
            continue
        r_, k = divmod(i, cols)
        in_row = min(cols, n - r_ * cols)
        x = bx + bw / 2 + (k - (in_row - 1) / 2) * (cw + 20)
        y = by + 110 + ch / 2 + r_ * (ch + 40) + (40 if rows == 1 else 0)
        rot = [-4, 3, -2, 2, -3, 4][i % 6]
        colr = cd.get("color", PALETTE[i % len(PALETTE)])
        kk = ease_out_back(prog(t, tp, 0.45), 1.6)
        with at(c, x, lerp(y - 140, y, kk), rot=rot * kk), alpha_layer(c, min(1, kk * 2)):
            rect(c, -cw / 2 + 6, -ch / 2 + 8, cw, ch, fc="#000000", a=0.18, r=10)
            rect(c, -cw / 2, -ch / 2, cw, ch, fc="#fffdf5", r=10)
            rect(c, -cw / 2, -ch / 2, cw, 26, fc=colr, r=10)
            rect(c, -cw / 2, -ch / 2 + 16, cw, 10, fc=colr)
            text_block(c, cd["text"], 0, -ch / 2 + 32, cw - 34, 30, INK, 650, "center")
            P.pushpin(c, 0, -ch / 2 + 14, colr)
    npose = [(0, "idle")]
    if cards:
        npose += [(cue(st, cards[0]["at"]) - 0.3, "point_up"), (cue(st, cards[-1]["at"] + "$")
                                                                if isinstance(cards[-1]["at"], str)
                                                                else 0, "idle")]
    cast = spec.get("cast", [{"who": "NIA", "x": 220, "s": 0.95, "y": 1015,
                              "poses": [(r, p) for r, p in npose[1:]]},
                             {"who": "LEX", "x": 1270, "s": 0.95, "y": 1010}])
    # anyone else who speaks in the sign-off walks on for their line
    seen = {m["who"] for m in cast} | {"NARRATOR"}
    guests = []
    for ln in st.lines:
        if ln["who"] not in seen:
            seen.add(ln["who"])
            guests.append({"who": ln["who"], "x": 1560 + 220 * len(guests), "y": 1070,
                           "s": 0.62 if ln["who"] != "CARGO" else 0.5,
                           "enter": ["", 0.0], "_t0": ln["t0"] - 0.7, "from": "right"})
    for g in guests:
        g["enter"] = g.pop("_t0")
    draw_cast(c, st, t, cast + guests)
    draw_pops(c, st, t, spec.get("pops"))
    nxt = spec.get("next")
    if nxt:
        te = cue(st, nxt["at"]) - 0.4
        if t >= te:
            k = ease_in_out(prog(t, te, 0.7))
            c.save()
            c.clipRect(skia.Rect.MakeLTRB(0, H * (1 - k), W, H))
            c.drawRect(skia.Rect.MakeWH(W, H), lin_grad(0, 0, 0, H, ["#13233a", "#1f3a5f"]))
            if nxt.get("final"):
                text(c, "SERIES COMPLETE", W / 2, 200, 44, "#9fe3df", 700, "center")
                text(c, nxt["title"], W / 2, 420, 92, "#ffb627", 700, "center",
                     outline="#0b1622", outline_w=12)
                P.sparkles(c, W / 2, 360, 420, t, 12)
                text(c, nxt.get("sub", ""), W / 2, 520, 40, "#ffffff", 600, "center")
            else:
                text(c, "NEXT TIME", W / 2, 200, 44, "#9fe3df", 700, "center")
                P.chip(c, W / 2, 290, f"EPISODE {nxt['ep']}", TEAL, 38)
                text(c, nxt["title"], W / 2, 440, 92, "#ffb627", 700, "center",
                     outline="#0b1622", outline_w=12)
            icn = nxt.get("icon", "globe")
            icon(c, icn, W / 2, 680, 1.6 + 0.04 * math.sin(t * 2), TEAL)
            text(c, "Learning aid · fictional characters and hypothetical facts · verify "
                 "against current ACCA documents", W / 2, 1040, 28, "#cfe3f7", 500, "center")
            c.restore()


# ================================================================ TITLE
def draw_title(c, t, st, spec):
    c.drawRect(skia.Rect.MakeWH(W, H), lin_grad(0, 0, 0, H, ["#13233a", "#1f3a5f"]))
    with at(c, W / 2, 380, rot=t * 6):
        for i in range(12):
            with at(c, 0, 0, rot=i * 30):
                P.draw_path(c, P.poly([(0, 0), (-80, -1400), (80, -1400)]), fc="#ffffff",
                            a=0.04)
    c.drawCircle(W / 2, 330, 420, rad_grad(W / 2, 330, 420, ["#0f8b8d66", "#0f8b8d00"]))
    k = pop_scale(t, 0.3, 0.6)
    if k > 0:
        em = spec.get("emblem", ["globe", "gavel"])
        with at(c, W / 2, 240, k):
            icon(c, em[0], -70 if len(em) > 1 else 0, 0, 2.0, TEAL)
            if len(em) > 1:
                icon(c, em[1], 90, 30, 1.4 + 0.05 * math.sin(t * 2), "#ffb627")
    k = pop_scale(t, 0.9, 0.6)
    if k > 0:
        with at(c, W / 2, 470, k):
            text(c, "THE LAW BEHIND THE DEAL", 0, 0, 104, "#ffffff", 700, "center",
                 outline="#0b1622", outline_w=14)
    bw = 900 * ease_out(prog(t, 1.3, 0.6))
    rect(c, W / 2 - bw / 2, 500, bw, 10, fc="#ffb627", r=5)
    a = ease_in_out(prog(t, 1.6, 0.6))
    text(c, spec.get("strap", "ACCA LW-GLO  ·  Corporate and Business Law – Global  ·  2026–27"),
         W / 2, 570, 34, "#cfe3f7", 500, "center", a=a)
    t2 = cue(st, spec.get("cue", "n2"))
    k = pop_scale(t, t2, 0.5)
    if k > 0:
        with at(c, W / 2, 650, k):
            P.chip(c, 0, 0, f"EPISODE {spec['ep']}", TEAL, 34)
        with at(c, W / 2, 770, pop_scale(t, t2 + 0.5, 0.5)):
            text(c, spec["title"], 0, 0, 88, "#ffb627", 700, "center", outline="#0b1622",
                 outline_w=12)
        if spec.get("syl"):
            P.chip(c, W / 2, 850, spec["syl"], "#ffffff", 30, s=pop_scale(t, t2 + 0.9, 0.5),
                   fg=INK)
    up = ease_out_back(prog(t, 1.0, 0.9), 1.4)
    y0 = 1130 + (1 - up) * 400
    cast = spec.get("cast", ["NIA", "KITO", "CARGO", "LEX", "AUDITOR"])
    xs = [260 + i * (1400 / max(1, len(cast) - 1)) for i in range(len(cast))]
    for who, x in zip(cast, xs):
        if who == "CARGO":
            draw_cargo(c, x, y0 - 10 + (1 - up) * 50, 0.5, mood="happy", t=t)
        else:
            pose = {"NIA": "wave", "KITO": "cheer", "LEX": "present", "AUDITOR": "clipboard",
                    "HANS": "wave", "AMARA": "present"}.get(who, "idle")
            draw_person(c, x, y0 + 10, who, 0.42, pose=pose, mood="happy", t=t,
                        look=0.5 if x < W / 2 else -0.5)


# ================================================================ dispatch
DRAW = {"talk": draw_talk, "board": draw_board, "compare": draw_compare, "flow": draw_flow,
        "stack": draw_stack, "route": draw_route, "case": draw_case,
        "timeline": draw_timeline, "quiz": draw_quiz, "recap": draw_recap,
        "title": draw_title}


def draw_scene(c, t, st, spec):
    DRAW[spec["tpl"]](c, t, st, spec)


def overlay(c, t, sc, index):
    """Scene chip, syllabus reference and dip-to-navy transitions."""
    spec = sc.get("spec") or {}
    if spec.get("tpl") != "title":
        a = window(t, 0.4, 3.6, 0.4)
        if a > 0:
            label = f"SCENE {index}  ·  {sc['title']}"
            w = text_width(label, 30, weight=650) + 50
            with alpha_layer(c, a):
                rect(c, 30, 30, w, 60, fc=INK, a=0.85, r=30)
                text(c, label, 55, 71, 30, "#ffffff", 650)
                if spec.get("syl"):
                    sw_ = text_width(spec["syl"], 26, weight=650) + 40
                    rect(c, W - 30 - sw_, 34, sw_, 52, fc="#ffb627", r=26)
                    text(c, spec["syl"], W - 30 - sw_ / 2, 69, 26, INK, 650, "center")
    fade_in = 1 - ease_in_out(prog(t, 0, 0.35))
    fade_out = ease_in_out(prog(t, sc["dur"] - 0.3, 0.3))
    a = max(fade_in, fade_out)
    if a > 0:
        c.drawRect(skia.Rect.MakeWH(W, H), fill("#0b1622", a))
