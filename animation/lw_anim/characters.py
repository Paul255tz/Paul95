"""Parametric 2D cartoon cast for THE LAW BEHIND THE DEAL.

Every character is drawn in local coordinates with the feet at (0, 0) and the
body extending upwards (negative y); a person is ~640 units tall at scale 1.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field

import skia

from .gfx import (at, circle, col, draw_path, ellipse, fill, lerp, line, poly,
                  rect, shade, soft_shadow, stroke)


# ---------------------------------------------------------------- specs
@dataclass
class Look:
    skin: str
    hair: str
    hair_style: str
    top: str
    bottom: str
    shoes: str = "#2b2b2b"
    collar: str = "blazer"   # blazer | shirt | suit_bow | suit_tie
    shirt: str = "#ffffff"
    tie: str = "#c0392b"
    glasses: str | None = None   # round | square
    beard: bool = False
    earrings: bool = False
    seed: float = 0.0
    head_scale: float = 1.0
    width: float = 1.0


CAST = {
    "NIA": Look(skin="#8d5a3b", hair="#1c1410", hair_style="puff", top="#0f8b8d",
                bottom="#2d3142", collar="blazer", shirt="#fff3d6", earrings=True,
                seed=0.3, width=0.92),
    "KITO": Look(skin="#5e3b25", hair="#120c08", hair_style="short", top="#f28c28",
                 bottom="#3d405b", collar="shirt", shirt="#f28c28", seed=1.7,
                 width=1.05),
    "LEX": Look(skin="#c98b62", hair="#d9d9d9", hair_style="prof", top="#1f3a5f",
                bottom="#1f3a5f", collar="suit_bow", tie="#ffb627", glasses="round",
                beard=True, seed=2.9, width=1.08),
    "AUDITOR": Look(skin="#e8b48f", hair="#5a4632", hair_style="neat", top="#6c7a89",
                    bottom="#4a5562", collar="suit_tie", tie="#0f8b8d",
                    glasses="square", seed=4.1, width=0.98),
    "HANS": Look(skin="#f1c7a5", hair="#d8b25a", hair_style="short", top="#3d405b",
                 bottom="#2d3142", collar="suit_tie", tie="#e4572e", seed=5.3,
                 width=1.02),
    "AMARA": Look(skin="#6b4226", hair="#1c1410", hair_style="neat", top="#7768ae",
                  bottom="#2d3142", collar="blazer", shirt="#fdf0ff", earrings=True,
                  seed=6.2, width=0.94),
}

POSES = {
    "idle": {"L": (8, -8), "R": (8, -8)},
    "point": {"L": (8, -8), "R": (100, 12)},
    "point_up": {"L": (8, -8), "R": (140, 8)},
    "point_l": {"L": (100, 12), "R": (8, -8)},
    "present": {"L": (55, -30), "R": (95, 20)},
    "wave": {"L": (8, -8), "R": (150, 25)},
    "hips": {"L": (40, -105), "R": (40, -105)},
    "think": {"L": (25, -95), "R": (-40, -150)},
    "hold": {"L": (10, -75), "R": (10, -75)},
    "hold_r": {"L": (8, -8), "R": (12, -80)},
    "wave_paper": {"L": (8, -8), "R": (160, 10)},
    "shrug": {"L": (55, -125), "R": (55, -125)},
    "cheer": {"L": (150, 15), "R": (150, 15)},
    "demand": {"L": (40, -105), "R": (115, 30)},
    "clipboard": {"L": (15, -95), "R": (8, -8)},
}


def blend_pose(a, b, k):
    pa, pb = POSES.get(a, a), POSES.get(b, b)
    return {s: (lerp(pa[s][0], pb[s][0], k), lerp(pa[s][1], pb[s][1], k)) for s in "LR"}


def pose_track(t, keys, dur=0.35):
    """keys: list of (time, pose_name) sorted; returns blended pose at t."""
    cur = keys[0][1]
    prev = cur
    start = -1e9
    for kt, name in keys:
        if t >= kt:
            prev, cur, start = cur, name, kt
    k = min(1.0, max(0.0, (t - start) / dur))
    k = k * k * (3 - 2 * k)
    return blend_pose(prev, cur, k)


def blink(t, seed):
    ph = (t + seed * 1.37) % 4.1
    if ph < 0.13:
        return 1 - abs(ph - 0.065) / 0.065 * 0.95 - 0.05
    return 1.0


# ---------------------------------------------------------------- face parts
def draw_mouth(c, x, y, m, mood, s=1.0):
    """m: openness 0..1."""
    if m < 0.06:
        p = skia.Path()
        if mood in ("happy", "smile", "excited"):
            p.moveTo(x - 20 * s, y - 3 * s)
            p.quadTo(x, y + 14 * s, x + 20 * s, y - 3 * s)
        elif mood in ("worried", "angry"):
            p.moveTo(x - 16 * s, y + 6 * s)
            p.quadTo(x, y - 6 * s, x + 16 * s, y + 6 * s)
        else:
            p.moveTo(x - 15 * s, y + 1 * s)
            p.quadTo(x, y + 6 * s, x + 15 * s, y + 1 * s)
        c.drawPath(p, stroke("#3a1f17", 5 * s))
        return
    w = (16 + 8 * m) * s
    h = (5 + 22 * m) * s
    top = y - 4 * s
    p = skia.Path()
    p.moveTo(x - w, top)
    p.quadTo(x, top - 5 * s, x + w, top)
    p.quadTo(x + w * 0.9, top + h * 1.6, x, top + h * 1.6)
    p.quadTo(x - w * 0.9, top + h * 1.6, x - w, top)
    p.close()
    c.drawPath(p, fill("#5a1d1d"))
    c.save()
    c.clipPath(p, doAntiAlias=True)
    rect(c, x - w, top - 2 * s, 2 * w, 6 * s, fc="#ffffff")
    ellipse(c, x, top + h * 1.6, w * 0.6, h * 0.55, fc="#e06b6b")
    c.restore()
    c.drawPath(p, stroke("#3a1f17", 3.5 * s))


def draw_eyes(c, x, y, spread, look, bl, mood, s=1.0, size=1.0):
    for sg in (-1, 1):
        ex = x + sg * spread
        rx, ry = 15 * s * size, 18 * s * size * bl
        ellipse(c, ex, y, rx, max(ry, 1.5 * s), fc="#ffffff", sc="#2a1a14", sw=3 * s)
        if bl > 0.3:
            circle(c, ex + look * 6 * s, y + 2 * s, 8.5 * s * size, fc="#1b1b1b")
            circle(c, ex + look * 6 * s + 3 * s, y - 2 * s, 2.8 * s * size, fc="#ffffff")
    # brows
    for sg in (-1, 1):
        bx = x + sg * spread
        by = y - 28 * s
        inner, outer = 0.0, 0.0
        if mood == "angry":
            inner, outer = 8, -4
        elif mood == "worried":
            inner, outer = -8, 2
        elif mood in ("surprised", "excited"):
            inner, outer = -8, -8
        elif mood == "thinking":
            inner, outer = (-6, -6) if sg > 0 else (2, 0)
        line(c, bx - sg * 14 * s, by + inner * s, bx + sg * 14 * s, by + outer * s,
             "#2a1a14", 6 * s)


# ---------------------------------------------------------------- person
def _arm(c, sx, sy, sg, a1, a2, look: Look, s):
    l1, l2 = 100 * s, 95 * s
    d1 = math.radians(a1)
    ex = sx + sg * math.sin(d1) * l1
    ey = sy + math.cos(d1) * l1
    d2 = math.radians(a1 + a2)
    hx = ex + sg * math.sin(d2) * l2
    hy = ey + math.cos(d2) * l2
    p = skia.Path()
    p.moveTo(sx, sy)
    p.lineTo(ex, ey)
    p.lineTo(hx, hy)
    c.drawPath(p, stroke(shade(look.top, -0.25), 40 * s))
    c.drawPath(p, stroke(look.top, 32 * s))
    circle(c, hx, hy, 17 * s, fc=look.skin, sc=shade(look.skin, -0.35), sw=3 * s)
    return hx, hy


def draw_person(c, x, y, name, s=1.0, pose="idle", mouth=0.0, mood="neutral",
                look=0.0, t=0.0, flip=False, prop=None, lean=0.0, bob=0.0,
                talking=False):
    """Returns dict with hand positions (canvas coordinates relative to x,y)."""
    L = CAST[name]
    pz = POSES.get(pose, pose) if isinstance(pose, str) else pose
    breathe = math.sin(t * 2.1 + L.seed) * 0.008
    talk_bob = (math.sin(t * 9 + L.seed) * 4 * mouth) if talking else 0
    hands = {}
    with at(c, x, y, s, sx=-s if flip else s):
        soft_shadow(c, 0, 0, 120 * L.width, 18)
        c.save()
        c.translate(0, -bob)
        c.rotate(lean)
        w = L.width
        # legs + shoes
        for sg in (-1, 1):
            rect(c, sg * 38 * w - 24, -235, 48, 222, fc=L.bottom, r=16)
            ellipse(c, sg * 42 * w + sg * 8, -12, 38, 16, fc=L.shoes)
        # neck
        rect(c, -18, -455, 36, 50, fc=shade(L.skin, -0.12), r=10)
        # torso
        c.save()
        c.translate(0, -230)
        c.scale(1, 1 + breathe)
        tor = poly([(-70 * w, 0), (70 * w, 0), (88 * w, -195), (-88 * w, -195)])
        r = skia.Path()
        r.addRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(-92 * w, -215, 92 * w, 10),
                                         40, 40))
        tor = skia.Op(tor, r, skia.PathOp.kIntersect_PathOp) or tor
        draw_path(c, tor, fc=L.top, sc=shade(L.top, -0.3), sw=4)
        # collar / outfit details
        if L.collar in ("blazer", "suit_bow", "suit_tie"):
            draw_path(c, poly([(-34, -196), (34, -196), (0, -110)]), fc=L.shirt)
            draw_path(c, poly([(-34, -196), (-6, -112), (-30, -130), (-54, -186)]),
                      fc=shade(L.top, -0.15))
            draw_path(c, poly([(34, -196), (6, -112), (30, -130), (54, -186)]),
                      fc=shade(L.top, -0.15))
            if L.collar == "suit_bow":
                draw_path(c, poly([(0, -188), (-22, -200), (-22, -176)]), fc=L.tie)
                draw_path(c, poly([(0, -188), (22, -200), (22, -176)]), fc=L.tie)
                circle(c, 0, -188, 6, fc=shade(L.tie, -0.2))
            if L.collar == "suit_tie":
                draw_path(c, poly([(-8, -192), (8, -192), (12, -125), (0, -110),
                                   (-12, -125)]), fc=L.tie)
            for i in range(2):
                circle(c, 0 + 2, -70 + i * 34, 4.5, fc=shade(L.top, -0.35))
        else:
            draw_path(c, poly([(-30, -198), (0, -170), (30, -198), (16, -205),
                               (0, -186), (-16, -205)]), fc=shade(L.top, 0.25))
            for i in range(4):
                circle(c, 0, -160 + i * 38, 4, fc=shade(L.top, -0.35))
        c.restore()
        # arms
        sy = -405
        for side, sg in (("L", -1), ("R", 1)):
            a1, a2 = pz[side]
            hands[side] = _arm(c, sg * 78 * w, sy, sg, a1, a2, L, 1.0)
        # head
        hy = -540 + talk_bob * 0.4
        hs = L.head_scale
        with at(c, 0, hy, hs):
            _draw_head(c, L, mouth, mood, look, t)
        c.restore()
        if prop:
            prop(c, hands)
    return hands


def _draw_head(c, L: Look, mouth, mood, look, t):
    # back hair
    if L.hair_style == "puff":
        circle(c, 0, -60, 108, fc=L.hair)
        circle(c, -70, -30, 70, fc=L.hair)
        circle(c, 70, -30, 70, fc=L.hair)
        circle(c, 0, -150, 62, fc=L.hair)
    # ears
    for sg in (-1, 1):
        ellipse(c, sg * 78, 6, 16, 22, fc=L.skin, sc=shade(L.skin, -0.3), sw=3)
        if L.earrings:
            circle(c, sg * 80, 34, 8, fc="#ffb627", sc="#b07b0e", sw=2)
    # face
    ellipse(c, 0, 0, 80, 90, fc=L.skin, sc=shade(L.skin, -0.3), sw=4)
    # cheeks
    for sg in (-1, 1):
        ellipse(c, sg * 46, 30, 14, 9, fc="#e8746a", a=0.25)
    # hair front
    if L.hair_style == "puff":
        p = skia.Path()
        p.moveTo(-80, -10)
        p.quadTo(-70, -95, 0, -94)
        p.quadTo(70, -95, 80, -10)
        p.quadTo(40, -58, 0, -56)
        p.quadTo(-40, -58, -80, -10)
        draw_path(c, p, fc=L.hair)
    elif L.hair_style == "short":
        p = skia.Path()
        p.moveTo(-80, -18)
        p.quadTo(-82, -100, 0, -100)
        p.quadTo(82, -100, 80, -18)
        p.quadTo(60, -62, 0, -64)
        p.quadTo(-60, -62, -80, -18)
        draw_path(c, p, fc=L.hair)
    elif L.hair_style == "neat":
        p = skia.Path()
        p.moveTo(-82, -6)
        p.quadTo(-86, -104, 6, -100)
        p.quadTo(84, -96, 80, -10)
        p.quadTo(70, -52, 20, -60)
        p.quadTo(-20, -40, -82, -6)
        draw_path(c, p, fc=L.hair)
        line(c, -24, -95, -6, -58, shade(L.hair, -0.3), 4)
    elif L.hair_style == "prof":
        for sg in (-1, 1):
            ellipse(c, sg * 74, -34, 22, 34, fc=L.hair)
        ellipse(c, 0, -84, 36, 8, fc=shade(L.skin, 0.25), a=0.6)
    if L.beard:
        p = skia.Path()
        p.moveTo(-74, 16)
        p.quadTo(-70, 104, 0, 112)
        p.quadTo(70, 104, 74, 16)
        p.quadTo(50, 50, 0, 46)
        p.quadTo(-50, 50, -74, 16)
        draw_path(c, p, fc=L.hair)
        # moustache
        ellipse(c, -16, 36, 20, 8, fc=L.hair)
        ellipse(c, 16, 36, 20, 8, fc=L.hair)
    # eyes / nose / mouth
    bl = blink(t, L.seed)
    draw_eyes(c, look * 6, -12, 31, look, bl, mood)
    p = skia.Path()
    p.moveTo(look * 8 - 2, 4)
    p.quadTo(look * 8 + 9, 22, look * 8 - 4, 24)
    c.drawPath(p, stroke(shade(L.skin, -0.4), 4))
    draw_mouth(c, look * 6, 52 if L.beard else 48, mouth, mood)
    if L.glasses:
        gc = "#2a2a2a"
        for sg in (-1, 1):
            gx = look * 6 + sg * 31
            if L.glasses == "round":
                circle(c, gx, -12, 24, sc=gc, sw=4)
            else:
                rect(c, gx - 25, -32, 50, 38, sc=gc, sw=4, r=8)
        line(c, look * 6 - 7, -14, look * 6 + 7, -14, gc, 4)


# ---------------------------------------------------------------- Captain Cargo
def draw_cargo(c, x, y, s=1.0, mouth=0.0, mood="happy", look=0.0, t=0.0, talking=False):
    bob = math.sin(t * 2.4) * 6
    with at(c, x, y, s):
        soft_shadow(c, 0, 0, 160, 20)
        c.translate(0, -bob - 10)
        Wc, Hc = 300, 190
        body = "#d9480f"
        rect(c, -Wc / 2, -Hc, Wc, Hc, fc=body, sc=shade(body, -0.35), sw=6, r=10)
        for i in range(1, 12):
            xx = -Wc / 2 + i * Wc / 12
            line(c, xx, -Hc + 12, xx, -12, shade(body, -0.18), 5)
        rect(c, -Wc / 2 + 6, -Hc + 6, Wc - 12, 16, fc=shade(body, 0.12), r=6)
        # face plate
        rect(c, -95, -Hc + 34, 190, 130, fc=shade(body, 0.08), r=24)
        bl = blink(t, 6.0)
        draw_eyes(c, look * 5, -Hc + 82, 40, look, bl, mood, s=1.25, size=1.0)
        draw_mouth(c, look * 5, -Hc + 140, mouth, mood, s=1.4)
        # little arms
        wave = math.sin(t * 3) * 12
        for sg in (-1, 1):
            p = skia.Path()
            p.moveTo(sg * Wc / 2, -Hc / 2)
            p.quadTo(sg * (Wc / 2 + 40), -Hc / 2 - 10 - wave * (sg > 0),
                     sg * (Wc / 2 + 52), -Hc / 2 - 50 - wave * (sg > 0))
            c.drawPath(p, stroke(shade(body, -0.35), 14))
            circle(c, sg * (Wc / 2 + 52), -Hc / 2 - 50 - wave * (sg > 0), 15, fc="#ffffff",
                   sc="#555555", sw=3)
        # captain hat
        with at(c, 10, -Hc - 4, rot=-6):
            ellipse(c, 0, 0, 92, 16, fc="#1f3a5f")
            p = skia.Path()
            p.moveTo(-74, -4)
            p.quadTo(-80, -70, 0, -74)
            p.quadTo(80, -70, 74, -4)
            p.close()
            draw_path(c, p, fc="#ffffff", sc="#c8ced6", sw=4)
            rect(c, -74, -22, 148, 18, fc="#1f3a5f", r=4)
            circle(c, 0, -46, 14, fc="#ffb627", sc="#b07b0e", sw=3)


# ---------------------------------------------------------------- little figures
def mini_person(c, x, y, s, body, skin="#a86f4c", head_item=None, mood="neutral",
                arm_up=0.0):
    """A small simplified figure for background vignettes."""
    with at(c, x, y, s):
        soft_shadow(c, 0, 0, 34, 6)
        rect(c, -22, -70, 44, 70, fc=shade(body, -0.25), r=12)
        rect(c, -28, -130, 56, 70, fc=body, r=18)
        line(c, 26, -120, 26 + 30 * arm_up, -95 - 40 * arm_up, body, 14)
        circle(c, 0, -160, 30, fc=skin, sc=shade(skin, -0.3), sw=3)
        circle(c, -10, -164, 4, fc="#1b1b1b")
        circle(c, 10, -164, 4, fc="#1b1b1b")
        p = skia.Path()
        if mood == "happy":
            p.moveTo(-10, -150)
            p.quadTo(0, -142, 10, -150)
        else:
            p.moveTo(-8, -148)
            p.lineTo(8, -148)
        c.drawPath(p, stroke("#3a1f17", 3))
        if head_item == "wig":
            for i in range(-2, 3):
                circle(c, i * 13, -186, 13, fc="#f4f4f4", sc="#bbbbbb", sw=2)
            for sg in (-1, 1):
                for j in range(3):
                    circle(c, sg * 30, -176 + j * 14, 11, fc="#f4f4f4", sc="#bbbbbb", sw=2)
