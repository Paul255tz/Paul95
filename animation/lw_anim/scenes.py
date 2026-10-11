"""Scene drawing for Pilot Episode 1. Each draw_* function paints one frame at
scene-local time t using the voice-driven timeline in `st`."""
from __future__ import annotations

import math

import skia

from . import props as P
from .characters import draw_cargo, draw_person, mini_person, pose_track
from .gfx import (H, W, alpha_layer, at, circle, clamp, col, ease_in_out, ease_out,
                  ease_out_back, ellipse, fill, lerp, lin_grad, line, pop_scale, prog,
                  rad_grad, rect, shade, stroke, text, text_block, text_width, window)


class ST:
    """Scene timeline helper."""

    def __init__(self, sc):
        self.sc = sc
        self.ev = sc["events"]
        self.lines = sc["lines"]
        self.dur = sc["dur"]

    def at(self, k):
        return self.ev[k][0]

    def end(self, k):
        return self.ev[k][1]

    def p(self, k, t, d=0.5):
        return prog(t, self.at(k), d)

    def on(self, k, t):
        return t >= self.at(k)

    def during(self, k, t):
        return self.at(k) <= t <= self.end(k)

    def mouth(self, who, t):
        for ln in self.lines:
            if ln["who"] == who and ln["t0"] <= t <= ln["t1"]:
                env = ln["env"]
                i = (t - ln["t0"]) * 60
                i0 = int(i)
                if i0 + 1 >= len(env):
                    return env[-1] if env else 0.0
                f = i - i0
                return env[i0] * (1 - f) + env[i0 + 1] * f
        return 0.0

    def talking(self, who, t):
        return any(ln["who"] == who and ln["t0"] <= t <= ln["t1"] for ln in self.lines)


def person(c, st, t, who, x, y, s=1.0, pose="idle", mood="neutral", look=0.0, **kw):
    talking = st.talking(who, t)
    if talking and mood == "neutral":
        mood = "smile"
    return draw_person(c, x, y, who, s, pose=pose, mouth=st.mouth(who, t), mood=mood,
                       look=look, t=t, talking=talking, **kw)


def dim(c, a):
    if a > 0:
        c.drawRect(skia.Rect.MakeWH(W, H), fill("#0b1622", a))


# ============================================================== TITLE
def draw_title(c, t, st):
    c.drawRect(skia.Rect.MakeWH(W, H), lin_grad(0, 0, 0, H, ["#13233a", "#1f3a5f"]))
    with at(c, W / 2, 380, rot=t * 6):
        for i in range(12):
            with at(c, 0, 0, rot=i * 30):
                P.draw_path(c, P.poly([(0, 0), (-80, -1400), (80, -1400)]),
                            fc="#ffffff", a=0.04)
    c.drawCircle(W / 2, 330, 420, rad_grad(W / 2, 330, 420, ["#0f8b8d66", "#0f8b8d00"]))
    # emblem: globe + gavel
    k = pop_scale(t, 0.3, 0.6)
    if k > 0:
        with at(c, W / 2, 240, k):
            P.globe(c, 0, 0, 110, t)
            P.gavel(c, 95, 40, 0.9, -35 + 8 * math.sin(t * 2))
    k = pop_scale(t, 0.9, 0.6)
    if k > 0:
        with at(c, W / 2, 470, k):
            text(c, "THE LAW BEHIND THE DEAL", 0, 0, 104, "#ffffff", 700, "center",
                 outline="#0b1622", outline_w=14)
    bw = 900 * ease_out(prog(t, 1.3, 0.6))
    rect(c, W / 2 - bw / 2, 500, bw, 10, fc="accent", r=5)
    a = ease_in_out(prog(t, 1.6, 0.6))
    text(c, "ACCA LW-GLO  ·  Corporate and Business Law – Global  ·  2026–27", W / 2, 570,
         34, "#cfe3f7", 500, "center", a=a)
    k = pop_scale(t, st.at("n2"), 0.5)
    if k > 0:
        with at(c, W / 2, 650, k):
            P.chip(c, 0, 0, "EPISODE 1", "#0f8b8d", 34)
        with at(c, W / 2, 770, pop_scale(t, st.at("n2") + 0.5, 0.5)):
            text(c, "Who Makes the Rules?", 0, 0, 92, "accent", 700, "center",
                 outline="#0b1622", outline_w=12)
    # cast peeking from the bottom
    up = ease_out_back(prog(t, 1.0, 0.9), 1.4)
    y0 = 1130 + (1 - up) * 400
    tt = t
    draw_person(c, 260, y0 + 10, "NIA", 0.42, pose="wave", mood="happy", t=tt, look=0.5)
    draw_person(c, 560, y0, "KITO", 0.42, pose="cheer", mood="excited", t=tt)
    draw_cargo(c, 960, y0 - 10 + (1 - up) * 50, 0.5, mood="happy", t=tt)
    draw_person(c, 1360, y0, "LEX", 0.42, pose="present", mood="happy", t=tt, look=-0.4)
    draw_person(c, 1660, y0 + 10, "AUDITOR", 0.42, pose="clipboard", mood="smile", t=tt,
                look=-0.6)


# ============================================================== SCENE 1
def draw_s1(c, t, st):
    P.office_bg(c, t)
    # Nia behind the desk
    tk = st.at("kito_in")
    look = -0.4 if t < st.at("invoice") + 0.9 else (0.0 if t < tk else 0.9)
    mood = "neutral"
    if tk <= t < st.at("kito1") + 0.6:
        mood = "surprised"
    if st.during("nia1", t):
        mood = "thinking"
    if t >= st.at("lex1"):
        look = -0.8
        mood = "happy" if t > st.at("lex1b") else "surprised"
    pose = pose_track(t, [(0, "idle"), (st.at("nia1"), "think"), (st.end("nia1"), "idle")])
    person(c, st, t, "NIA", 790, 1020, 0.95, pose=pose, mood=mood, look=look)
    P.desk(c, 440, 760, 700)
    # invoice drop
    ti = st.at("invoice")
    if t >= ti:
        k = ease_out(prog(t, ti, 0.9))
        y = lerp(-150, 738, k)
        rot = lerp(-40, 8, k) + (0 if k >= 1 else 12 * math.sin(t * 9))
        sy = 1.0 if k < 1 else 1 - 0.5 * ease_out(prog(t, ti + 0.9, 0.25))
        with at(c, 1010 - 60 * k, y, sy=sy, sx=1):
            P.paper(c, 0, 0, 130, 170, rot, "INVOICE", "#e4572e", 5, 0.8)
    # legal book + mini Lex
    tb = st.at("book")
    if t >= tb:
        ok = ease_out(prog(t, tb, 0.6))
        glow = 0.9 * ease_in_out(prog(t, tb, 0.5))
        P.legal_book(c, 600, 758, 0.75, ok, glow)
        rise = ease_out_back(prog(t, tb + 0.35, 0.7), 1.2)
        if rise > 0:
            c.save()
            c.clipRect(skia.Rect.MakeLTRB(0, 0, W, 748))
            person(c, st, t, "LEX", 600, 748 + (1 - rise) * 260 + 120, 0.38,
                   pose="point" if t > st.at("lex1b") else "wave", mood="happy",
                   look=0.6)
            c.restore()
            P.sparkles(c, 600, 610, 120, t, 7, a=0.8 * glow)
    # Kito rushes in
    if t >= tk - 0.05:
        k = ease_out(prog(t, tk, 0.9))
        x = lerp(2200, 1420, k)
        run = abs(math.sin(t * 14)) * 22 * (1 - k)
        k1_end = st.end("kito1")
        pose = pose_track(t, [(0, "wave_paper"), (k1_end + 0.2, "hips")])
        kmood = "angry" if t < k1_end + 0.3 else "thinking"
        if t > st.at("lex1"):
            kmood = "surprised"

        def contract(cc, hands):
            if t < k1_end + 0.25:
                hx, hy = hands["R"]
                P.paper(cc, hx + 10, hy - 50, 120, 150, 10 * math.sin(t * 10),
                        "CONTRACT", "#1f3a5f", 4, 0.9)

        person(c, st, t, "KITO", x, 1015, 0.98, pose=pose, mood=kmood,
               look=-0.9 if t < st.at("lex1") else -1.0, bob=run, prop=contract)
    # caption card
    tc = st.at("lex1b")
    if t >= tc:
        a = ease_in_out(prog(t, tc, 0.4))
        dim(c, 0.25 * a)
        P.card(c, 520, 225, 680, 220, "CIVIL DISPUTE", "= remedy for a private wrong",
               "#0f8b8d", a=a, s=pop_scale(t, tc, 0.5), title_size=44, body_size=40)
        P.card(c, 1260, 225, 680, 220, "CRIMINAL CASE", "= prosecution for an offence",
               "#7768ae", a=a, s=pop_scale(t, tc + 0.25, 0.5), title_size=44,
               body_size=40)


# ============================================================== SCENE 2
def _door(c, cx, label, color, interior, open_k, t):
    w, h = 400, 560
    x0, y0 = cx - w / 2, 900 - h
    rect(c, x0 - 18, y0 - 18, w + 36, h + 18, fc=shade(color, -0.35), r=14)
    c.save()
    c.clipRect(skia.Rect.MakeXYWH(x0, y0, w, h))
    interior(c, x0, y0, w, h, t)
    c.restore()
    # door leaf hinged on the left
    k = ease_in_out(open_k)
    lw = w * (1 - 0.85 * k)
    skew = 30 * k
    leaf = P.poly([(x0, y0), (x0 + lw, y0 - skew), (x0 + lw, y0 + h + skew * 0.2),
                   (x0, y0 + h)])
    P.draw_path(c, leaf, fc=color, sc=shade(color, -0.35), sw=5)
    if lw > 60:
        sx = lw / w
        for i, yy in enumerate((y0 + 60, y0 + 310)):
            rect(c, x0 + 40 * sx, yy, (w - 80) * sx, 200, sc=shade(color, -0.25), sw=5,
                 r=10)
        circle(c, x0 + lw - 40 * sx, y0 + h / 2, 14, fc="#ffd166", sc="#b07b0e", sw=3)
    P.chip(c, cx, y0 - 60, label, color, 42)


def _civil_room(c, x, y, w, h, t):
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), lin_grad(0, y, 0, y + h, ["#e3f7f5", "#bfe9e4"]))
    rect(c, x + w / 2 - 110, y + 120, 220, 90, fc="#8c5a3c", r=8)
    mini_person(c, x + w / 2, y + 130, 0.55, "#1b1b1b", skin="#c98b62", head_item="wig")
    rect(c, x + w / 2 - 110, y + 130, 220, 80, fc="#8c5a3c", r=8)
    mini_person(c, x + 90, y + h - 30, 0.9, "#e07a5f", skin="#8d5a3b", arm_up=0.6)
    mini_person(c, x + w - 90, y + h - 30, 0.9, "#3d405b", skin="#e8b48f", arm_up=0.6)
    P.paper(c, x + 140, y + h - 170, 70, 90, -10, "", "#e4572e", 3)
    P.paper(c, x + w - 140, y + h - 170, 70, 90, 10, "", "#e4572e", 3)
    ph = (t * 0.5) % 1
    P.coin_stack(c, lerp(x + w - 120, x + 120, ease_in_out(ph)), y + 290 - 60 * math.sin(
        math.pi * ph), 0.6, 1)


def _criminal_room(c, x, y, w, h, t):
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), lin_grad(0, y, 0, y + h, ["#efeaff", "#d8d0f5"]))
    rect(c, x + w / 2 - 110, y + 120, 220, 90, fc="#5e3b25", r=8)
    mini_person(c, x + w / 2, y + 130, 0.55, "#1b1b1b", skin="#e8b48f", head_item="wig")
    rect(c, x + w / 2 - 110, y + 130, 220, 80, fc="#5e3b25", r=8)
    mini_person(c, x + 90, y + h - 30, 0.9, "#1f3a5f", skin="#a86f4c",
                arm_up=0.5 + 0.3 * math.sin(t * 3))
    mini_person(c, x + w - 90, y + h - 30, 0.9, "#8a96a3", skin="#c98b62")
    with at(c, x + w - 90, y + h - 260, 1 + 0.06 * math.sin(t * 4)):
        circle(c, 0, 0, 34, fc="#ffffff", sc="#7768ae", sw=4)
        text(c, "?", 0, 16, 46, "#7768ae", 700, "center")


def draw_s2(c, t, st):
    P.studio_bg(c, t)
    o1 = prog(t, st.at("lex2a") - 0.1, 0.8)
    o2 = prog(t, st.at("lex2b") - 0.1, 0.8)
    _door(c, 1010, "CIVIL", "#0f8b8d", _civil_room, o1, t)
    _door(c, 1540, "CRIMINAL", "#7768ae", _criminal_room, o2, t)
    # standards of proof
    for cx, key, label, colr, tilt in (
            (1010, "lex2a", "Balance of probabilities", "#0f8b8d", 4),
            (1540, "lex2b", "Beyond reasonable doubt", "#7768ae", 14)):
        tp = st.at(key) + 2.2
        if t >= tp:
            s = pop_scale(t, tp, 0.5)
            P.chip(c, cx, 975, label, colr, 34, s=s)
    if t >= st.at("lex2a") + 1.0:
        with alpha_layer(c, ease_in_out(st.p("lex2a", t - 1.0, 0.5))):
            P.coin_stack(c, 1240, 860, 0.55, 2)
    # banner
    if t >= st.at("lex2c"):
        s = pop_scale(t, st.at("lex2c") + 0.6, 0.5)
        if s > 0:
            with at(c, 960, 95, s):
                P.chip(c, 0, 0, "Classify the facts, then choose the rule", "accent",
                       44, fg="#1d2b3a")
    lpose = pose_track(t, [(0, "idle"), (st.at("lex2a"), "point"), (st.end("lex2b"), "idle"),
                           (st.at("lex2c"), "present")])
    person(c, st, t, "LEX", 470, 1005, 0.95, pose=lpose, mood="happy",
           look=0.8 if t < st.end("lex2b") else -0.6)
    npose = pose_track(t, [(0, "idle"), (st.at("nia2"), "think"), (st.end("nia2"), "idle")])
    person(c, st, t, "NIA", 165, 1015, 0.88, pose=npose,
           mood="thinking" if st.during("nia2", t) else "neutral",
           look=0.9 if not st.during("lex2c", t) else 0.8)


# ============================================================== SCENE 3
def _rise(c, t, t0, draw, x, base=830):
    k = ease_out_back(prog(t, t0, 0.9), 1.1)
    if k <= 0:
        return
    c.save()
    c.clipRect(skia.Rect.MakeLTRB(0, 0, W, base + 2))
    with at(c, 0, (1 - k) * 420):
        draw()
    c.restore()


def draw_s3(c, t, st):
    c.drawRect(skia.Rect.MakeWH(W, H), lin_grad(0, 0, 0, 830, ["#8fd3ff", "#e3f6ff"]))
    for i in range(3):
        cx = (i * 640 + t * 20) % (W + 300) - 150
        for dx, r in ((0, 40), (40, 52), (90, 36)):
            circle(c, cx + dx, 120 + i * 60, r, fc="#ffffff", a=0.9)
    c.drawRect(skia.Rect.MakeLTRB(0, 830, W, H), lin_grad(0, 830, 0, H, ["#a9d18e", "#7fb069"]))
    for i in range(-6, 16):
        line(c, 960 + i * 140, 830, 960 + i * 340 - 600, H, "#ffffff", 3, 0.25)
    for yy in (870, 930, 1010):
        line(c, 0, yy, W, yy, "#ffffff", 3, 0.25)
    items = [
        ("lex3a", 900, P.parliament, "LEGISLATURE", "makes", "#0f8b8d"),
        ("lex3b", 1300, P.office_block, "EXECUTIVE", "implements", "#7768ae"),
        ("lex3c", 1700, P.courthouse, "JUDICIARY", "interprets / applies", "#e4572e"),
    ]
    for key, x, fn, lab, sub, colr in items:
        t0 = st.at(key) - 0.4
        hl = window(t, st.at(key), st.end(key), 0.3)
        if key == "lex3c":
            hl = max(hl, window(t, st.at("lex3d"), st.end("lex3d"), 0.3))
        _rise(c, t, t0, lambda fn=fn, x=x, hl=hl: fn(c, x, 830, 1.0, hl), x)
        s = pop_scale(t, t0 + 0.6, 0.5)
        if s > 0:
            with at(c, x, 900, s):
                P.chip(c, 0, 0, lab, colr, 34)
                text(c, sub, 0, 64, 32, "#1d2b3a", 650, "center")
    if t >= st.at("lex3d"):
        k = ease_out(st.p("lex3d", t, 1.2))
        with alpha_layer(c, k * (1 - prog(t, st.at("summary") + 0.2, 0.5))):
            P.sparkles(c, 1700, 680, 150, t, 8)
            with at(c, 1700, 470 - 60 * k):
                P.paper(c, 0, 0, 170, 120, 0, "PRINCIPLE", "#e4572e", 2)
    kpose = pose_track(t, [(0, "idle"), (st.at("kito3"), "think"), (st.end("kito3"), "hips")])
    person(c, st, t, "KITO", 620, 1015, 0.9, pose=kpose,
           mood="thinking" if st.during("kito3", t) else "neutral",
           look=-0.8 if st.during("kito3", t) or st.during("lex3d", t) else 0.8)
    lpose = pose_track(t, [(0, "idle"), (st.at("lex3a") - 0.3, "point_up"),
                           (st.end("lex3c"), "idle"), (st.at("lex3d"), "present")])
    person(c, st, t, "LEX", 215, 1015, 0.95, pose=lpose, mood="happy", look=0.8)
    if t >= st.at("summary") - 0.2:
        s = pop_scale(t, st.at("summary") - 0.2, 0.5)
        with at(c, 960, 110, s):
            P.card(c, 0, 0, 1700, 120, None, None, fc="#1d2b3a")
            x = -800
            for lab, sub, colr in (("Legislature", "makes", "#9fe3df"),
                                   ("Executive", "implements", "#c9c1ff"),
                                   ("Judiciary", "interprets / applies", "#ffb4a2")):
                wdt = text(c, lab, x, 16, 44, colr, 700)
                wdt += text(c, f" = {sub}", x + wdt, 16, 44, "#ffffff", 500)
                x += wdt + 70


# ============================================================== SCENE 4
def _ladder(c, x, y, a):
    with alpha_layer(c, a):
        labels = ["Supreme Court", "Appeal Court", "High Court", "Lower courts"]
        for i, lab in enumerate(labels):
            w = 300 - i * 0
            yy = y + i * 105
            rect(c, x - w / 2, yy, w, 78, fc=P.mix("#1f3a5f", "#9fc3e6", i / 3), r=16)
            text(c, lab, x, yy + 50, 32, "#ffffff", 650, "center")
        P.arrow(c, x + 190, y + 30, x + 190, y + 380, "accent", 10, 30)
        with at(c, x + 230, y + 220, rot=90):
            text(c, "binds", 0, 0, 30, "#1d2b3a", 650, "center")


def _panel(c, cx, cy, title, colr, s, draw, t):
    if s <= 0:
        return
    with at(c, cx, cy, s):
        rect(c, -175 + 8, -280 + 12, 350, 560, fc="#000000", a=0.15, r=24)
        rect(c, -175, -280, 350, 560, fc="#ffffff", sc="#1d2b3a", sw=6, r=24)
        rect(c, -175, -280, 350, 86, fc=colr, r=24)
        rect(c, -175, -220, 350, 26, fc=colr)
        text(c, title, 0, -222, 42, "#ffffff", 700, "center")
        draw(c, t)


def _p_reverse(c, t):
    for i in range(3):
        rect(c, -130 + i * 90, 160 - i * 90, 90 + (2 - i) * 0, 90 + i * 90, fc="#dfe5ea",
             sc="#8a96a3", sw=3)
    text(c, "Trial", -85, 200, 26, "#5b6670", 650, "center")
    text(c, "Appeal", 95, 50, 26, "#5b6670", 650, "center")
    k = ease_in_out((t * 0.4) % 1)
    px, py = lerp(-85, 95, k), lerp(110, -70, k)
    P.paper(c, px, py, 70, 90, 0, "", "#0f8b8d", 3)
    text(c, "same case", 0, 260, 30, "#1d2b3a", 650, "center")
    P.cross(c, -40, 140, 0.8)


def _p_overrule(c, t):
    P.paper(c, -70, -60, 120, 150, -6, "Case A", "#8a96a3", 4)
    line(c, -130, -130, -10, 10, "#e4572e", 9)
    line(c, -10, -130, -130, 10, "#e4572e", 9)
    P.arrow(c, -40, 60, 40, 60, "#1d2b3a", 8, 22)
    with at(c, 70, 110, 1 + 0.05 * math.sin(t * 4)):
        P.paper(c, 0, 0, 120, 150, 6, "Case B", "#7768ae", 4)
    text(c, "later case,", 0, 220, 28, "#1d2b3a", 650, "center")
    text(c, "rule changes", 0, 256, 28, "#1d2b3a", 650, "center")


def _p_distinguish(c, t):
    P.paper(c, -85, -30, 120, 160, -4, "Earlier", "#8a96a3", 0)
    P.paper(c, 85, -30, 120, 160, 4, "Now", "#ffb627", 0)
    circle(c, -85, -10, 22, fc="#0f8b8d")
    rect(c, -105, 30, 40, 40, fc="#0f8b8d", r=4)
    circle(c, 85, -10, 22, fc="#0f8b8d")
    P.draw_path(c, P.poly([(85, 25), (110, 70), (60, 70)]), fc="#e4572e")
    text(c, "≠", 0, 10, 80, "#e4572e", 700, "center", family="Nunito")
    text(c, "material facts", 0, 200, 28, "#1d2b3a", 650, "center")
    text(c, "differ", 0, 236, 28, "#1d2b3a", 650, "center")


def draw_s4(c, t, st):
    P.studio_bg(c, t, "#eaf4ff", "#cfe3f7")
    phase_b = st.at("panels")
    fa = 1 - ease_in_out(prog(t, phase_b - 0.3, 0.5))
    if fa > 0:
        with alpha_layer(c, fa):
            tc = st.at("card")
            s = pop_scale(t, tc, 0.6)
            move = ease_in_out(prog(t, st.at("lex4c") + 2.2, 1.2))
            cx, cy = lerp(1080, 1080, move), lerp(360, 610, move)
            cs = lerp(1.0, 0.62, move)
            # new case folder
            if t >= st.at("lex4c") + 0.6:
                fs = pop_scale(t, st.at("lex4c") + 0.6, 0.5)
                with at(c, 1080, 800, fs):
                    rect(c, -300, -150, 220, 50, fc="#e9b44c", r=12)
                    rect(c, -300, -120, 600, 230, fc="#f2c46d", sc="#b07b0e", sw=5, r=16)
                    text(c, "NEW CASE", -270, 90, 40, "#7a5208", 700)
            if s > 0:
                with at(c, cx, cy, s * cs):
                    c.drawCircle(0, 0, 420, rad_grad(0, 0, 420, ["#fff3b0aa", "#fff3b000"]))
                    rect(c, -300, -200, 600, 400, fc="#ffffff", sc="accent", sw=8, r=28)
                    rect(c, -300, -200, 600, 80, fc="accent", r=28)
                    rect(c, -300, -150, 600, 30, fc="accent")
                    text(c, "EARLIER DECISION", 0, -142, 40, "#1d2b3a", 700, "center")
                    P.gavel(c, -230, -50, 0.5, -30)
                    ra = 0.35 + 0.65 * ease_in_out(st.p("lex4a", t, 0.4))
                    hl = window(t, st.at("lex4a"), st.end("lex4a"), 0.3)
                    if hl:
                        rect(c, -180, -96, 460, 120, fc="accent", a=0.25 * hl, r=14)
                    text(c, "RATIO DECIDENDI", -160, -50, 40, "#0f8b8d", 700, a=ra)
                    text(c, "legal reason necessary", -160, -6, 30, "ink", 500, a=ra)
                    ob = ease_in_out(st.p("lex4b", t, 0.5))
                    text(c, "obiter dicta", -160, 80, 36, "#8a96a3", 650, a=ob)
                    text(c, "additional observations", -160, 120, 28, "#8a96a3", 500,
                         a=ob)
                    if ob > 0:
                        P.chip(c, 170, 70, "persuasive", "#dfe5ea", 22, fg="#5b6670",
                               a=ob)
                    P.sparkles(c, 0, 0, 330, t, 10, a=0.6)
            la = ease_in_out(st.p("lex4c", t, 0.6))
            if la > 0:
                _ladder(c, 1640, 300, la)
            for i, (lab, dt) in enumerate((("Superior court", 4.0),
                                           ("Similar material facts", 5.4))):
                tt0 = min(st.at("lex4c") + dt, st.end("lex4c") - 0.2)
                ks = pop_scale(t, tt0, 0.4)
                if ks > 0:
                    with at(c, 1450, 760 + i * 80, ks):
                        P.check(c, -20, 0, 0.9)
                        text(c, lab, 20, 12, 34, "ink", 650)
    # phase B: three comic panels
    for key, cx, title, colr, fn in (("lex4d", 870, "REVERSE", "#0f8b8d", _p_reverse),
                                     ("lex4e", 1265, "OVERRULE", "#7768ae", _p_overrule),
                                     ("lex4f", 1660, "DISTINGUISH", "#e4572e",
                                      _p_distinguish)):
        tp = st.at(key) - 0.1
        if t >= tp:
            s = pop_scale(t, tp, 0.5)
            hl = window(t, st.at(key), st.end(key), 0.3)
            _panel(c, cx, 470 - 10 * hl, title, colr, s * (1 + 0.04 * hl), fn, t)
    if t >= st.at("lex4g"):
        s = pop_scale(t, st.at("lex4g") + 0.3, 0.5)
        with at(c, 1265, 900, s):
            P.chip(c, 0, 0, "Read the facts · Court hierarchy · What was necessary?",
                   "accent", 36, fg="#1d2b3a")
    lpose = pose_track(t, [(0, "idle"), (st.at("lex4a"), "point"), (st.end("lex4c"), "idle"),
                           (st.at("lex4d"), "point"), (st.at("lex4g"), "present")])
    person(c, st, t, "LEX", 230, 1010, 0.95, pose=lpose, mood="happy", look=0.8)
    npose = pose_track(t, [(0, "idle"), (st.at("lex4c") + 1.8, "point"),
                           (st.at("lex4c") + 4.0, "idle")])
    person(c, st, t, "NIA", 530, 1015, 0.9, pose=npose,
           mood="excited" if st.during("lex4c", t) else "neutral", look=0.9)


# ============================================================== SCENE 5
def draw_s5(c, t, st):
    P.studio_bg(c, t, "#fff1ea", "#ffd9c7")
    grid_t = st.at("lex5b") - 0.2
    ga = 1 - ease_in_out(prog(t, grid_t - 0.4, 0.4))
    if ga > 0:
        with alpha_layer(c, ga):
            rect(c, 860, 760, 300, 40, fc="#8a96a3", r=8)
            rect(c, 890, 800, 240, 100, fc="#6c7a89", r=8)
            P.machine(c, 1010, 760, 1.0, t, ghost=True)
            r = skia.Rect.MakeXYWH(830, 500, 360, 280)
            p = stroke("#1d2b3a", 5)
            p.setPathEffect(skia.DashPathEffect.Make([18, 12], t * 30))
            c.drawRoundRect(r, 20, 20, p)
            text(c, "?", 1010, 690, 140, "#e4572e", 700, "center")
            P.chip(c, 1010, 440, "Unique custom machine", "#1f3a5f", 34)
            if t >= st.at("lex5a"):
                k = pop_scale(t, st.at("lex5a") + 0.3, 0.5)
                with at(c, 1360, 640, k):
                    P.coin_stack(c, 0, 60, 1.2, 4)
                    text(c, "≠", -170, 40, 120, "#e4572e", 700, "center", family="Nunito")
                    P.chip(c, -40, 170, "Damages not always adequate", "#e4572e", 28)
    tiles = [("lex5b", 820, 300, "Specific performance", lambda: P.truck(c, 0, 40, 1.0, t)),
             ("lex5c", 1260, 300, "Injunction", lambda: P.stop_sign(c, 0, -10, 0.9)),
             ("lex5d", 820, 660, "Rescission", lambda: P.rewind_contract(c, 0, -10, 0.8, t)),
             ("lex5e", 1260, 660, "Rectification", lambda: P.pencil_fix(c, 0, -10, 0.8, t))]
    for key, x, y, lab, icon in tiles:
        tp = st.at(key) - 0.1
        if t >= tp:
            s = pop_scale(t, tp, 0.5)
            hl = window(t, st.at(key), st.end(key) + 0.2, 0.2)
            with at(c, x, y, s * (1 + 0.05 * hl)):
                rect(c, -200 + 8, -165 + 12, 400, 330, fc="#000000", a=0.12, r=26)
                rect(c, -200, -165, 400, 330, fc="#ffffff", sc="accent" if hl else "#dfe5ea",
                     sw=8, r=26)
                with at(c, 0, -20, 0.95):
                    icon()
                text(c, lab, 0, 140, 36, "#1d2b3a", 700, "center")
    if t >= st.at("lex5f"):
        s = pop_scale(t, st.at("lex5f") + 0.4, 0.4)
        with at(c, 1040, 480, 1.6 - 0.6 * s if s > 0 else 0, rot=-10):
            if s > 0:
                with alpha_layer(c, min(1, s)):
                    rect(c, -360, -70, 720, 140, fc="#ffffff", a=0.85, r=18)
                    rect(c, -360, -70, 720, 140, sc="#e4572e", sw=10, r=18)
                    text(c, "DISCRETIONARY", 0, 6, 64, "#e4572e", 700, "center")
                    text(c, "not automatic", 0, 52, 36, "#e4572e", 650, "center")
    # characters
    kpose = pose_track(t, [(0, "hold_r"), (st.end("kito5") + 0.3, "idle"),
                           (st.at("lex5f"), "hips")])

    def money(cc, hands):
        if t < st.end("kito5") + 0.4:
            hx, hy = hands["R"]
            P.cash(cc, hx, hy - 10, 0.8, 10 * math.sin(t * 6))

    person(c, st, t, "KITO", 230, 1015, 0.95, pose=kpose,
           mood="angry" if t < st.end("kito5") else "thinking",
           look=0.9 if t > st.end("nia5a") else 0.6, prop=money)
    npose = pose_track(t, [(0, "idle"), (st.at("nia5a"), "present"), (st.end("nia5a"), "idle"),
                           (st.at("nia5b"), "think")])
    person(c, st, t, "NIA", 510, 1015, 0.9, pose=npose,
           mood="worried" if st.during("nia5a", t) else
           ("thinking" if st.during("nia5b", t) else "neutral"),
           look=-0.9 if t < st.end("nia5a") else 0.9)
    lpose = pose_track(t, [(0, "idle"), (st.at("lex5b") - 0.3, "point_l"),
                           (st.end("lex5e"), "idle"), (st.at("lex5f"), "present")])
    lx = lerp(2150, 1730, ease_out(prog(t, 0.2, 1.0)))
    person(c, st, t, "LEX", lx, 1010, 0.95, pose=lpose, mood="happy", look=-0.8)


# ============================================================== SCENE 6
def _org_positions():
    names = [("UN", "#4f9dd0"), ("UNCITRAL", "#0f8b8d"), ("WTO", "#7768ae"),
             ("ICC", "#e4572e"), ("UNIDROIT", "#3bb273"), ("OECD", "#f2a541")]
    out = []
    for i, (n, colr) in enumerate(names):
        ang = -math.pi / 2 + i * 2 * math.pi / len(names)
        out.append((n, colr, 960 + math.cos(ang) * 420, 470 + math.sin(ang) * 320))
    return out


def draw_s6(c, t, st):
    P.night_bg(c, t)
    P.globe(c, 960, 470, 250, t)
    focus = {"UNCITRAL": "lex6c", "WTO": "lex6d", "ICC": "lex6e"}
    any_focus = any(st.during(k, t) for k in focus.values())
    for i, (n, colr, x, y) in enumerate(_org_positions()):
        tp = st.at("lex6a") + 0.6 + i * 0.35
        if t < tp:
            continue
        s = pop_scale(t, tp, 0.5)
        hl = window(t, st.at(focus[n]), st.end(focus[n]), 0.3) if n in focus else 0
        a = 1.0 if not any_focus or hl > 0.5 else 0.45
        line(c, 960 + (x - 960) * 0.62, 470 + (y - 470) * 0.66, x, y, "#ffffff", 3, 0.3 * a)
        if hl:
            c.drawCircle(x, y, 140, rad_grad(x, y, 140, ["#ffe08a88", "#ffe08a00"], a=hl))
        P.chip(c, x, y, n, colr, 40, a=a, s=s * (1 + 0.25 * hl))
    descs = {"lex6c": "Harmonised commercial-law texts",
             "lex6d": "Framework for trade cooperation",
             "lex6e": "Commercial rules (incl. Incoterms) · dispute resolution"}
    for k, d in descs.items():
        a = window(t, st.at(k) + 0.2, st.end(k) + 0.2, 0.3)
        if a > 0:
            P.chip(c, 960, 965, d, "#ffffff", 38, a=a, fg="#1d2b3a")
    ca = window(t, st.at("lex6b"), st.at("cargo_in") - 0.3, 0.4)
    if ca > 0:
        P.card(c, 1690, 330, 400, 200, "TREATY / CONVENTION", "create shared rules", "#0f8b8d",
               a=ca, s=pop_scale(t, st.at("lex6b"), 0.5), title_size=32, body_size=36)
        P.card(c, 1690, 590, 400, 200, "MODEL LAW", "a template to adopt", "#7768ae",
               a=ca, s=pop_scale(t, st.at("lex6b") + 2.0, 0.5), title_size=32,
               body_size=36)
    if t >= st.at("cargo_in") - 0.1:
        k = ease_out(prog(t, st.at("cargo_in") - 0.1, 1.0))
        draw_cargo(c, lerp(2250, 1650, k), 1000, 0.8, mouth=st.mouth("CARGO", t),
                   mood="surprised" if st.during("cargo6", t) else "happy", look=-1, t=t,
                   talking=st.talking("CARGO", t))
    if t >= st.at("lex6f"):
        s = pop_scale(t, st.at("lex6f") + 0.6, 0.5)
        with at(c, 960, 965, s):
            P.chip(c, 0, 0, "Court or arbitration? Agreement + applicable law", "accent",
                   38, fg="#1d2b3a")
    lpose = pose_track(t, [(0, "idle"), (st.at("lex6a"), "present"), (st.at("lex6c"), "point"),
                           (st.end("lex6e"), "idle"), (st.at("lex6f"), "present")])
    person(c, st, t, "LEX", 230, 1010, 0.95, pose=lpose, mood="happy", look=0.8)


# ============================================================== SCENE 7
def draw_s7(c, t, st):
    c.save()
    c.clipRect(skia.Rect.MakeXYWH(0, 0, 960, H))
    P.courtroom(c, 0, 0, 960, H, t)
    c.restore()
    c.save()
    c.clipRect(skia.Rect.MakeXYWH(960, 0, 960, H))
    P.arb_room(c, 960, 0, 960, H, t)
    c.restore()
    rect(c, 952, 0, 16, H, fc="#1d2b3a")
    hl_c = window(t, st.at("lex7a"), st.end("lex7a"), 0.3)
    hl_a = window(t, st.at("lex7b"), st.end("lex7b"), 0.3)
    P.chip(c, 480, 70, "COURT", "#1f3a5f", 44, s=1 + 0.1 * hl_c)
    P.chip(c, 1440, 70, "ARBITRATION", "#0f8b8d", 44, s=1 + 0.1 * hl_a)
    for i, lab in enumerate(["Formal", "Usually public"]):
        tp = st.at("lex7a") + 0.8 + i * 1.2
        s = pop_scale(t, tp, 0.4)
        if s > 0:
            w = text_width(lab, 32, weight=650) + 38
            P.chip(c, 40 + w / 2, 170 + i * 80, lab, "#ffffff", 32, s=s, fg="#1d2b3a")
    tags = ["Private", "Flexible", "Specialist expertise", "Can be expensive",
            "Limited grounds to challenge"]
    span = st.end("lex7b") - st.at("lex7b")
    for i, lab in enumerate(tags):
        tp = st.at("lex7b") + 0.4 + i * span / 5.5
        s = pop_scale(t, tp, 0.4)
        if s > 0:
            colr = "#ffffff" if i < 3 else "#ffe1d6"
            w = text_width(lab, 30, weight=650) + 36
            x0 = 1000 if i % 2 == 0 else 1330
            P.chip(c, x0 + w / 2, 170 + (i // 2) * 80, lab, colr, 30, s=s, fg="#1d2b3a")
    # Lex & Nia
    lpose = pose_track(t, [(0, "idle"), (st.at("lex7a"), "point_l"), (st.at("lex7b"), "point"),
                           (st.end("lex7b"), "idle"), (st.at("lex7c"), "present")])
    person(c, st, t, "LEX", 960, 1100, 0.78, pose=lpose, mood="happy",
           look=-0.8 if st.during("lex7a", t) else 0.8)
    if t >= st.at("nia7") - 0.6:
        k = ease_out(prog(t, st.at("nia7") - 0.6, 0.6))
        person(c, st, t, "NIA", lerp(-200, 200, k), 1100, 0.78,
               pose="think" if st.during("nia7", t) else "idle", mood="thinking", look=0.9)
    # mediation overlay
    ma = window(t, st.at("lex7c") - 0.2, st.at("aud_in") - 0.3, 0.4)
    if ma > 0:
        dim(c, 0.35 * ma)
        with alpha_layer(c, ma), at(c, 960, 470, pop_scale(t, st.at("lex7c") - 0.2, 0.5)):
            rect(c, -470, -300, 940, 600, fc="#ffffff", r=32)
            rect(c, -470, -300, 940, 90, fc="#f2a541", r=32)
            rect(c, -470, -240, 940, 30, fc="#f2a541")
            text(c, "MEDIATION", 0, -236, 50, "#ffffff", 700, "center")
            ellipse(c, 0, 150, 300, 50, fc="#c39a6e")
            mini_person(c, -230, 170, 1.0, "#e07a5f", skin="#8d5a3b")
            mini_person(c, 230, 170, 1.0, "#3d405b", skin="#e8b48f")
            mini_person(c, 0, 120, 1.05, "#f2a541", skin="#5e3b25", mood="happy")
            for sg in (-1, 1):
                with at(c, sg * 140, -90 + 6 * math.sin(t * 3 + sg)):
                    rect(c, -60, -36, 120, 72, fc="#eef3f7", sc="#8a96a3", sw=3, r=20)
                    text(c, "…", 0, 10, 40, "#5b6670", 700, "center")
            text(c, "helps the parties negotiate", 0, 220, 38, "ink", 650, "center")
            text(c, "does not normally impose a decision", 0, 268, 34, "#e4572e", 650,
                 "center")
    # quiz
    qa = ease_in_out(prog(t, st.at("aud_in") - 0.1, 0.5))
    if qa > 0:
        dim(c, 0.55 * qa)
        k = ease_out(prog(t, st.at("aud_in") - 0.1, 0.8))
        person(c, st, t, "AUDITOR", lerp(-250, 300, k), 1020, 0.95,
               pose="clipboard", mood="smile" if t > st.at("aud2") else "neutral",
               look=0.6)
        with alpha_layer(c, qa), at(c, 1170, 380, pop_scale(t, st.at("aud_in"), 0.5)):
            rect(c, -620, -250, 1240, 500, fc="#ffffff", r=32)
            rect(c, -620, -250, 1240, 90, fc="#1d2b3a", r=32)
            rect(c, -620, -190, 1240, 30, fc="#1d2b3a")
            text(c, "QUICK CHECK", -580, -188, 46, "accent", 700)
            text_block(c, "Which mechanism usually has a third party impose a binding "
                       "decision under the parties' agreement?", -580, -150, 1160, 46,
                       "ink", 600)
            ans = t >= st.at("aud2") - 0.15
            for i, opt in enumerate(["Court", "Arbitration", "Mediation"]):
                x = -380 + i * 380
                good = ans and opt == "Arbitration"
                colr = "#3bb273" if good else ("#dfe5ea" if not ans else "#eef1f4")
                fg = "#ffffff" if good else ("#1d2b3a" if not ans else "#9aa5b0")
                s = 1 + (0.12 * ease_out_back(prog(t, st.at("aud2") - 0.15, 0.4))
                         if good else 0)
                P.chip(c, x, 160, opt, colr, 44, fg=fg, s=s)
                if good:
                    P.check(c, x + 170, 120, ease_out_back(prog(t, st.at("aud2"), 0.4)))
        # countdown ring
        tt0, tt1 = st.at("think"), st.end("think")
        if tt0 - 0.2 <= t <= tt1 + 0.3:
            rem = clamp((tt1 - t) / (tt1 - tt0))
            with at(c, 1700, 820):
                circle(c, 0, 0, 80, fc="#ffffff")
                r = skia.Rect.MakeXYWH(-66, -66, 132, 132)
                c.drawArc(r, -90, 360 * rem, False, stroke("accent", 16))
                n = max(1, math.ceil(rem * 4))
                text(c, str(n), 0, 24, 70, "ink", 700, "center")
                text(c, "PAUSE & THINK", 0, 130, 32, "#ffffff", 700, "center")
        if t >= st.at("aud2") - 0.15:
            s = pop_scale(t, st.at("aud2") - 0.15, 0.5)
            with at(c, 1170, 820, s):
                P.chip(c, 0, 0, "Answer: ARBITRATION", "#3bb273", 56)


# ============================================================== SCENE 8
RECAP = [("nia8a", "Civil vs criminal", "#0f8b8d", 520, 270, -4),
         ("nia8b", "Legislature · Executive · Judiciary", "#7768ae", 800, 260, 3),
         ("nia8c", "Ratio vs obiter", "#e4572e", 1080, 275, -2),
         ("nia8d", "Damages vs equitable remedies", "#f2a541", 660, 500, 2),
         ("nia8e", "Court vs ADR", "#3bb273", 940, 505, -3)]


def draw_s8(c, t, st):
    win = (1400, 110, 460, 400)
    P.office_bg(c, t, harbour=True, window=win, sign=False)
    # passing ship inside the window
    ts = st.at("ship") - 0.6
    if t >= ts:
        c.save()
        c.clipRect(skia.Rect.MakeXYWH(*win))
        k = prog(t, ts, 7.0)
        sx = lerp(win[0] - 260, win[0] + win[2] + 260, k)
        P.ship(c, sx, win[1] + win[3] * 0.62 + 30, 0.42, t, mouth=st.mouth("CARGO", t),
               talking=st.talking("CARGO", t))
        c.restore()
        wx, wy, ww, wh = win
        line(c, wx + ww / 2, wy, wx + ww / 2, wy + wh, "#ffffff", 10)
        line(c, wx, wy + wh / 2, wx + ww, wy + wh / 2, "#ffffff", 10)
    P.corkboard(c, 380, 120, 840, 540)
    text(c, "EPISODE 1 RECAP", 800, 175, 44, "#5e3b25", 700, "center")
    for key, lab, colr, x, y, rot in RECAP:
        tp = st.at(key) - 0.25
        if t < tp:
            continue
        k = ease_out_back(prog(t, tp, 0.45), 1.6)
        with at(c, x, lerp(y - 140, y, k), rot=rot * k):
            with alpha_layer(c, min(1, k * 2)):
                rect(c, -125 + 6, -80 + 8, 250, 160, fc="#000000", a=0.18, r=10)
                rect(c, -125, -80, 250, 160, fc="#fffdf5", r=10)
                rect(c, -125, -80, 250, 26, fc=colr, r=10)
                rect(c, -125, -64, 250, 10, fc=colr)
                text_block(c, lab, 0, -50, 220, 32, "ink", 650, "center")
                P.pushpin(c, 0, -66, colr)
    npose = pose_track(t, [(0, "idle"), (st.at("nia8a") - 0.3, "point_up"),
                           (st.end("nia8e"), "idle"), (st.at("cargo8"), "wave")])
    person(c, st, t, "NIA", 220, 1015, 0.95, pose=npose, mood="happy",
           look=0.8 if t < st.at("ship") else 1.0)
    lpose = pose_track(t, [(0, "idle"), (st.at("lex8"), "present"), (st.at("ship"), "point")])
    person(c, st, t, "LEX", 1270, 1010, 0.95, pose=lpose, mood="happy",
           look=-0.8 if t < st.at("lex8") else 0.8)
    # end card
    te = st.at("n3") - 0.4
    if t >= te:
        k = ease_in_out(prog(t, te, 0.7))
        c.save()
        c.clipRect(skia.Rect.MakeLTRB(0, H * (1 - k), W, H))
        c.drawRect(skia.Rect.MakeWH(W, H), lin_grad(0, 0, 0, H, ["#13233a", "#1f3a5f"]))
        text(c, "NEXT TIME", W / 2, 200, 44, "#9fe3df", 700, "center")
        P.chip(c, W / 2, 290, "EPISODE 2", "#0f8b8d", 38)
        text(c, "The Contract Across the Ocean", W / 2, 440, 96, "accent", 700, "center",
             outline="#0b1622", outline_w=12)
        P.waves(c, 860, t, "#2b86c5")
        P.ship(c, lerp(700, 1150, prog(t, te, 12)), 880, 0.75, t)
        P.waves(c, 900, t + 1.3, "#1b5f93")
        text(c, "Learning aid · fictional characters and hypothetical facts · verify "
             "against current ACCA documents", W / 2, 1040, 28, "#cfe3f7", 500, "center")
        c.restore()


DRAW = {"title": draw_title, "s1": draw_s1, "s2": draw_s2, "s3": draw_s3, "s4": draw_s4,
        "s5": draw_s5, "s6": draw_s6, "s7": draw_s7, "s8": draw_s8}


def overlay(c, t, sc, index):
    """Scene chip + dip-to-navy transitions."""
    if sc["key"] != "title":
        a = window(t, 0.4, 3.6, 0.4)
        if a > 0:
            label = f"SCENE {index}  ·  {sc['title']}"
            w = text_width(label, 30, weight=650) + 50
            with alpha_layer(c, a):
                rect(c, 30, 30, w, 60, fc="#1d2b3a", a=0.85, r=30)
                text(c, label, 55, 71, 30, "#ffffff", 650)
    fade_in = 1 - ease_in_out(prog(t, 0, 0.35))
    fade_out = ease_in_out(prog(t, sc["dur"] - 0.3, 0.3))
    a = max(fade_in, fade_out)
    if a > 0:
        c.drawRect(skia.Rect.MakeWH(W, H), fill("#0b1622", a))
