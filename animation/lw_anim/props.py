"""Backgrounds, objects and diagram pieces shared by the scenes."""
from __future__ import annotations

import math

import skia

from .gfx import (H, W, alpha_layer, at, circle, clamp, col, draw_path, ease_out,
                  ease_out_back, ellipse, fill, lin_grad, line, mix, poly, prog,
                  rad_grad, rect, shade, soft_shadow, stroke, text, text_block,
                  text_width)


# ---------------------------------------------------------------- backgrounds
def studio_bg(c, t, top="#fff4e0", bottom="#ffe2b8", dots="#ffffff"):
    c.drawRect(skia.Rect.MakeWH(W, H), lin_grad(0, 0, 0, H, [top, bottom]))
    for i in range(14):
        for j in range(8):
            x = i * 150 + (j % 2) * 75 + (t * 6) % 150
            y = j * 150 + 40
            circle(c, x, y, 5, fc=dots, a=0.35)
    rect(c, 0, 900, W, 180, fc=shade(bottom, -0.08))
    rect(c, 0, 900, W, 8, fc=shade(bottom, -0.18))


def night_bg(c, t):
    c.drawRect(skia.Rect.MakeWH(W, H), lin_grad(0, 0, 0, H, ["#13233a", "#24426b"]))
    for i in range(70):
        x = (i * 263.7) % W
        y = (i * 137.3) % 860
        tw = 0.4 + 0.6 * (0.5 + 0.5 * math.sin(t * 2 + i))
        circle(c, x, y, 2 + (i % 3), fc="#ffffff", a=0.35 * tw)
    rect(c, 0, 900, W, 180, fc="#1a2f4d")
    rect(c, 0, 900, W, 8, fc="#2e4f7c")


def skyline(c, x, y, w, h, t, harbour=False):
    """Contents of an office window (clipped by caller)."""
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h),
               lin_grad(0, y, 0, y + h, ["#8fd3ff", "#e3f6ff"]))
    circle(c, x + w * 0.8, y + h * 0.22, 46, fc="#ffd166")
    for i in range(3):
        cx = x + ((i * 230 + t * 18) % (w + 240)) - 120
        cy = y + 60 + i * 38
        for dx, r in ((0, 26), (26, 34), (58, 24)):
            circle(c, cx + dx, cy, r, fc="#ffffff", a=0.9)
    base = y + h * (0.62 if harbour else 0.78)
    import random
    rnd = random.Random(3)
    bx = x - 10
    while bx < x + w:
        bw = rnd.randint(50, 110)
        bh = rnd.randint(70, 210)
        colr = rnd.choice(["#7aa6c2", "#5f8aa8", "#94b8cf", "#6f97b3"])
        rect(c, bx, base - bh, bw, bh + 2, fc=colr)
        for wy in range(int(base - bh + 14), int(base - 10), 26):
            for wx in range(int(bx + 10), int(bx + bw - 14), 22):
                rect(c, wx, wy, 10, 12, fc="#dff3ff", a=0.7)
        bx += bw + 6
    if harbour:
        c.drawRect(skia.Rect.MakeLTRB(x, base, x + w, y + h),
                   lin_grad(0, base, 0, y + h, ["#2b86c5", "#1b5f93"]))
        for i in range(6):
            yy = base + 18 + i * 22
            off = (t * 40 + i * 50) % 80
            for k in range(-1, int(w / 80) + 2):
                line(c, x + k * 80 + off, yy, x + k * 80 + off + 30, yy, "#ffffff", 3, 0.4)
    else:
        rect(c, x, base, w, y + h - base, fc="#9bbf7a")


def office_bg(c, t, harbour=False, window=(1180, 120, 600, 430), sign=True):
    c.drawRect(skia.Rect.MakeWH(W, H), lin_grad(0, 0, 0, 860, ["#fbf3e4", "#f1e2c8"]))
    # wall stripes
    for i in range(0, W, 120):
        rect(c, i, 0, 60, 860, fc="#ffffff", a=0.18)
    # window
    wx, wy, ww, wh = window
    rect(c, wx - 18, wy - 18, ww + 36, wh + 36, fc="#ffffff", sc="#d5c3a3", sw=6, r=12)
    c.save()
    c.clipRect(skia.Rect.MakeXYWH(wx, wy, ww, wh))
    skyline(c, wx, wy, ww, wh, t, harbour)
    c.restore()
    line(c, wx + ww / 2, wy, wx + ww / 2, wy + wh, "#ffffff", 10)
    line(c, wx, wy + wh / 2, wx + ww, wy + wh / 2, "#ffffff", 10)
    rect(c, wx - 30, wy + wh + 14, ww + 60, 18, fc="#e9dcc4", r=6)
    if sign:
        # company logo on the wall
        rect(c, 120, 110, 430, 120, fc="#0f8b8d", r=24)
        circle(c, 190, 170, 36, fc="#ffb627")
        draw_path(c, poly([(160, 182), (190, 140), (220, 182)]), fc="#0f8b8d")
        text(c, "SafariTech", 250, 172, 52, "#ffffff", 650)
        text(c, "TRADING LTD", 252, 208, 26, "#d8fbf8", 600)
    # floor
    c.drawRect(skia.Rect.MakeLTRB(0, 860, W, H), lin_grad(0, 860, 0, H, ["#d7b48c", "#c39a6e"]))
    rect(c, 0, 852, W, 14, fc="#b88d62")
    # plant
    plant(c, 90, 900, 1.0)


def plant(c, x, y, s):
    with at(c, x, y, s):
        for i, a in enumerate((-50, -25, 0, 25, 50, -12, 12)):
            with at(c, 0, -90, rot=a):
                ellipse(c, 0, -70, 20, 70, fc="#3bb273" if i % 2 else "#2e9a60")
        draw_path(c, poly([(-50, -100), (50, -100), (38, 0), (-38, 0)]), fc="#e07a5f",
                  sc=shade("#e07a5f", -0.25), sw=4)


def desk(c, x, y, w=640):
    rect(c, x, y, w, 34, fc="#8c5a3c", r=8)
    rect(c, x + 10, y + 28, w - 20, 210, fc="#a26d4a", r=6)
    rect(c, x + 30, y + 60, w * 0.38, 70, fc="#8c5a3c", r=6)
    rect(c, x + 30, y + 150, w * 0.38, 70, fc="#8c5a3c", r=6)
    circle(c, x + 30 + w * 0.19, y + 95, 7, fc="#e9c46a")
    circle(c, x + 30 + w * 0.19, y + 185, 7, fc="#e9c46a")
    # laptop + mug
    rect(c, x + w - 250, y - 120, 190, 120, fc="#3d405b", r=10)
    rect(c, x + w - 240, y - 110, 170, 98, fc="#9fe3df", r=6)
    rect(c, x + w - 270, y - 6, 230, 10, fc="#2d3142", r=4)
    rect(c, x + w - 30, y - 58, 40, 58, fc="#e4572e", r=8)
    c.drawArc(skia.Rect.MakeXYWH(x + w + 2, y - 48, 26, 30), -90, 180, False,
              stroke("#e4572e", 7))


# ---------------------------------------------------------------- documents
def paper(c, x, y, w=150, h=200, rot=0.0, title="", accent="#0f8b8d", lines=5, s=1.0,
          stamp=None):
    with at(c, x, y, s, rot=rot):
        rect(c, -w / 2 + 6, -h / 2 + 8, w, h, fc="#000000", a=0.15, r=8)
        rect(c, -w / 2, -h / 2, w, h, fc="#ffffff", sc="#c9c9c9", sw=3, r=8)
        rect(c, -w / 2, -h / 2, w, 36, fc=accent, r=8)
        rect(c, -w / 2, -h / 2 + 20, w, 16, fc=accent)
        if title:
            text(c, title, 0, -h / 2 + 27, 22, "#ffffff", 650, "center")
        for i in range(lines):
            ly = -h / 2 + 60 + i * (h - 80) / max(lines, 1)
            line(c, -w / 2 + 18, ly, w / 2 - 18 - (30 if i == lines - 1 else 0), ly,
                 "#c4ccd4", 6)
        if stamp:
            with at(c, w * 0.18, h * 0.22, rot=-14):
                rect(c, -60, -24, 120, 48, sc=stamp[1], sw=5, r=8)
                text(c, stamp[0], 0, 10, 26, stamp[1], 700, "center")


def legal_book(c, x, y, s, k, glow=0.0):
    """k: 0 closed .. 1 open."""
    with at(c, x, y, s):
        if glow > 0:
            c.drawCircle(0, -60, 220, rad_grad(0, -60, 220, ["#fff3b0", "#fff3b000"],
                                               a=glow))
        soft_shadow(c, 0, 6, 150, 18)
        if k < 0.5:
            kk = k / 0.5
            rect(c, -110, -40, 220, 40, fc="#7a2e2e", r=6)
            with at(c, 0, -40, sy=1 - kk):
                rect(c, -110, -120, 220, 120, fc="#9b3a3a", sc="#5e2020", sw=4, r=8)
                text(c, "LAW", 0, -50, 46, "#ffd166", 700, "center")
        else:
            kk = (k - 0.5) / 0.5
            for sg in (-1, 1):
                p = skia.Path()
                p.moveTo(0, -10)
                p.quadTo(sg * 60, -30 - 30 * kk, sg * 140, -20 - 20 * kk)
                p.lineTo(sg * 140, 4)
                p.quadTo(sg * 60, -6, 0, 10)
                p.close()
                draw_path(c, p, fc="#fffaf0", sc="#9b3a3a", sw=5)
                for i in range(4):
                    yy = -14 - 4 * kk + i * 6
                    line(c, sg * 30, yy - 8 * kk, sg * 110, yy - 18 * kk, "#c9b9a0", 3)


# ---------------------------------------------------------------- cards / ui
def card(c, x, y, w, h, title=None, body=None, accent="#0f8b8d", a=1.0, s=1.0,
         title_size=40, body_size=34, body_color="ink", align="left", fc="#ffffff"):
    """A keyword card; (x, y) is the centre."""
    with alpha_layer(c, a), at(c, x, y, s):
        rect(c, -w / 2 + 8, -h / 2 + 12, w, h, fc="#000000", a=0.16, r=26)
        rect(c, -w / 2, -h / 2, w, h, fc=fc, r=26)
        top = -h / 2 + 24
        if title:
            rect(c, -w / 2, -h / 2, w, title_size + 34, fc=accent, r=26)
            rect(c, -w / 2, -h / 2 + 30, w, title_size + 4, fc=accent)
            text(c, title, 0 if align == "center" else -w / 2 + 30,
                 -h / 2 + title_size + 10, title_size, "#ffffff", 650, align)
            top = -h / 2 + title_size + 50
        if body:
            text_block(c, body, 0 if align == "center" else -w / 2 + 30, top - 8,
                       w - 60, body_size, body_color, 500, align)


def chip(c, x, y, label, color="#0f8b8d", size=32, a=1.0, s=1.0, fg="#ffffff"):
    w = text_width(label, size, weight=650) + size * 1.2
    with alpha_layer(c, a), at(c, x, y, s):
        rect(c, -w / 2, -size * 0.85, w, size * 1.7, fc=color, r=size * 0.85)
        text(c, label, 0, size * 0.35, size, fg, 650, "center")
    return w


def arrow(c, x1, y1, x2, y2, color="ink", w=8, head=26, k=1.0, a=1.0):
    if k <= 0:
        return
    x2 = x1 + (x2 - x1) * k
    y2 = y1 + (y2 - y1) * k
    line(c, x1, y1, x2, y2, color, w, a)
    ang = math.atan2(y2 - y1, x2 - x1)
    p = poly([(x2 + math.cos(ang) * 6, y2 + math.sin(ang) * 6),
              (x2 - math.cos(ang - 0.45) * head, y2 - math.sin(ang - 0.45) * head),
              (x2 - math.cos(ang + 0.45) * head, y2 - math.sin(ang + 0.45) * head)])
    draw_path(c, p, fc=color, a=a)


def check(c, x, y, s=1.0, color="#3bb273", a=1.0):
    with at(c, x, y, s):
        circle(c, 0, 0, 26, fc=color, a=a)
        p = skia.Path()
        p.moveTo(-12, 0)
        p.lineTo(-3, 10)
        p.lineTo(13, -10)
        c.drawPath(p, stroke("#ffffff", 7, a))


def cross(c, x, y, s=1.0, color="#e4572e", a=1.0):
    with at(c, x, y, s):
        circle(c, 0, 0, 26, fc=color, a=a)
        line(c, -10, -10, 10, 10, "#ffffff", 7, a)
        line(c, -10, 10, 10, -10, "#ffffff", 7, a)


def sparkles(c, x, y, r, t, n=8, color="#ffd166", a=1.0):
    for i in range(n):
        ang = i / n * 2 * math.pi + t * 0.8
        rr = r + 14 * math.sin(t * 3 + i)
        px, py = x + math.cos(ang) * rr, y + math.sin(ang) * rr
        sz = 8 + 5 * math.sin(t * 5 + i * 1.7)
        with at(c, px, py, rot=t * 90 + i * 20):
            draw_path(c, poly([(0, -sz * 1.6), (sz * 0.4, -sz * 0.4), (sz * 1.6, 0),
                               (sz * 0.4, sz * 0.4), (0, sz * 1.6), (-sz * 0.4, sz * 0.4),
                               (-sz * 1.6, 0), (-sz * 0.4, -sz * 0.4)]), fc=color, a=a)


# ---------------------------------------------------------------- legal icons
def gavel(c, x, y, s=1.0, rot=-30):
    with at(c, x, y, s, rot=rot):
        rect(c, -8, -10, 16, 120, fc="#8c5a3c", r=6)
        rect(c, -50, -50, 100, 44, fc="#a26d4a", sc="#6b4430", sw=4, r=10)
        rect(c, -58, -54, 14, 52, fc="#e9c46a", r=4)
        rect(c, 44, -54, 14, 52, fc="#e9c46a", r=4)


def scales(c, x, y, s=1.0, tilt=0.0, color="#ffb627"):
    with at(c, x, y, s):
        rect(c, -6, -160, 12, 160, fc=shade(color, -0.25))
        rect(c, -50, -6, 100, 14, fc=shade(color, -0.25), r=6)
        with at(c, 0, -150, rot=tilt):
            rect(c, -120, -6, 240, 12, fc=color, r=6)
            for sg in (-1, 1):
                with at(c, sg * 110, 0, rot=-tilt):
                    line(c, 0, 0, -30, 70, shade(color, -0.3), 3)
                    line(c, 0, 0, 30, 70, shade(color, -0.3), 3)
                    p = skia.Path()
                    p.moveTo(-44, 70)
                    p.quadTo(0, 110, 44, 70)
                    p.close()
                    draw_path(c, p, fc=color, sc=shade(color, -0.3), sw=3)
        circle(c, 0, -160, 14, fc=color)


def coin_stack(c, x, y, s=1.0, n=3):
    with at(c, x, y, s):
        for i in range(n):
            ellipse(c, 0, -i * 16, 46, 16, fc="#f2b632", sc="#b07b0e", sw=3)
        text(c, "$", 0, -(n - 1) * 16 + 10, 26, "#b07b0e", 700, "center")


def cash(c, x, y, s=1.0, rot=0):
    with at(c, x, y, s, rot=rot):
        for i in range(3):
            with at(c, i * 8, -i * 8, rot=i * 4):
                rect(c, -60, -32, 120, 64, fc="#5cb85c", sc="#2e7d32", sw=3, r=6)
                circle(c, 0, 0, 18, sc="#2e7d32", sw=3)
                text(c, "$", 0, 9, 26, "#2e7d32", 700, "center")


def machine(c, x, y, s=1.0, t=0.0, ghost=False):
    a = 0.35 if ghost else 1.0
    with alpha_layer(c, a), at(c, x, y, s):
        rect(c, -150, -230, 300, 230, fc="#5f8aa8", sc="#3a5d75", sw=6, r=18)
        rect(c, -120, -200, 130, 90, fc="#bfe6ff", sc="#3a5d75", sw=4, r=10)
        for i in range(3):
            circle(c, 60 + (i % 2) * 40, -170 + i * 40, 14,
                   fc=["#e4572e", "#ffb627", "#3bb273"][i])
        for cx, sp in ((-70, 1), (40, -1)):
            with at(c, cx, -60, rot=t * 90 * sp):
                circle(c, 0, 0, 38, fc="#8a96a3", sc="#5b6670", sw=4)
                for k in range(8):
                    with at(c, 0, 0, rot=k * 45):
                        rect(c, -8, -50, 16, 16, fc="#8a96a3")
                circle(c, 0, 0, 12, fc="#5b6670")
        rect(c, -170, -10, 340, 20, fc="#3a5d75", r=6)


def stop_sign(c, x, y, s=1.0):
    with at(c, x, y, s):
        pts = [(math.cos(math.radians(22.5 + i * 45)) * 90,
                math.sin(math.radians(22.5 + i * 45)) * 90) for i in range(8)]
        draw_path(c, poly(pts), fc="#e4572e", sc="#ffffff", sw=8)
        text(c, "STOP", 0, 16, 46, "#ffffff", 700, "center")


def truck(c, x, y, s=1.0, t=0.0):
    with at(c, x, y, s):
        rect(c, -120, -110, 160, 100, fc="#ffb627", sc="#b07b0e", sw=4, r=10)
        rect(c, 40, -80, 80, 70, fc="#0f8b8d", sc="#0b6466", sw=4, r=10)
        rect(c, 64, -70, 40, 28, fc="#bfe6ff", r=5)
        for wx in (-80, 70):
            with at(c, wx, -6, rot=t * 300):
                circle(c, 0, 0, 22, fc="#2d3142")
                rect(c, -3, -16, 6, 32, fc="#8a96a3")


def rewind_contract(c, x, y, s=1.0, t=0.0):
    with at(c, x, y, s):
        paper(c, 0, 0, 120, 160, 0, "DEAL", "#7768ae", 4)
        r = skia.Rect.MakeXYWH(-95, -95, 190, 190)
        c.drawArc(r, -40 - t * 60, -260, False, stroke("#e4572e", 10))
        ang = math.radians(-40 - t * 60 - 260)
        hx, hy = math.cos(ang) * 95, math.sin(ang) * 95
        with at(c, hx, hy, rot=math.degrees(ang) - 90):
            draw_path(c, poly([(0, -18), (18, 8), (-18, 8)]), fc="#e4572e")


def pencil_fix(c, x, y, s=1.0, t=0.0):
    with at(c, x, y, s):
        paper(c, 0, 0, 140, 170, 0, "TERMS", "#0f8b8d", 0)
        line(c, -50, -20, 40, -20, "#c4ccd4", 6)
        line(c, -50, 10, 0, 10, "#e4572e", 6)
        line(c, -54, 10, 4, 10, "#e4572e", 3)
        line(c, -50, 40, 46, 40, "#3bb273", 6)
        with at(c, 50 + 10 * math.sin(t * 6), 20, rot=40):
            rect(c, -10, -90, 20, 90, fc="#ffb627", sc="#b07b0e", sw=3)
            draw_path(c, poly([(-10, 0), (10, 0), (0, 22)]), fc="#f4d6a0")
            rect(c, -10, -104, 20, 16, fc="#e07a5f", r=4)


# ---------------------------------------------------------------- buildings
def parliament(c, x, y, s=1.0, hl=0.0):
    with at(c, x, y, s):
        if hl:
            c.drawCircle(0, -150, 230, rad_grad(0, -150, 230, ["#ffe08a", "#ffe08a00"], a=hl))
        rect(c, -150, -150, 300, 150, fc="#f2e3c6", sc="#b59b72", sw=5)
        for i in range(6):
            rect(c, -130 + i * 50, -140, 22, 140, fc="#fff6e4", sc="#c8b088", sw=3)
        rect(c, -170, -170, 340, 26, fc="#e3cfa8", sc="#b59b72", sw=4, r=4)
        c.drawArc(skia.Rect.MakeXYWH(-90, -260, 180, 180), 180, 180, True,
                  fill("#4f9dd0"))
        c.drawArc(skia.Rect.MakeXYWH(-90, -260, 180, 180), 180, 180, True,
                  stroke("#2f6f99", 5))
        rect(c, -3, -300, 6, 50, fc="#555")
        draw_path(c, poly([(3, -300), (50, -288), (3, -276)]), fc="#e4572e")


def office_block(c, x, y, s=1.0, hl=0.0):
    with at(c, x, y, s):
        if hl:
            c.drawCircle(0, -160, 230, rad_grad(0, -160, 230, ["#ffe08a", "#ffe08a00"], a=hl))
        rect(c, -130, -320, 260, 320, fc="#7aa6c2", sc="#4b7894", sw=5, r=6)
        for r_ in range(6):
            for k in range(4):
                rect(c, -105 + k * 56, -295 + r_ * 46, 40, 30, fc="#dff3ff", r=4)
        rect(c, -35, -70, 70, 70, fc="#3d405b", r=4)
        rect(c, -4, -360, 8, 40, fc="#555")
        draw_path(c, poly([(4, -360), (48, -348), (4, -336)]), fc="#3bb273")


def courthouse(c, x, y, s=1.0, hl=0.0):
    with at(c, x, y, s):
        if hl:
            c.drawCircle(0, -150, 230, rad_grad(0, -150, 230, ["#ffe08a", "#ffe08a00"], a=hl))
        rect(c, -150, -30, 300, 30, fc="#d9d4cc", sc="#9a948a", sw=4)
        for i in range(5):
            rect(c, -125 + i * 58, -200, 28, 170, fc="#f4f1ec", sc="#b9b2a6", sw=3)
        rect(c, -160, -224, 320, 28, fc="#e7e2d9", sc="#9a948a", sw=4)
        draw_path(c, poly([(-170, -224), (170, -224), (0, -310)]), fc="#efeae2",
                  sc="#9a948a", sw=5)
        with at(c, 0, -246, 0.28):
            scales(c, 0, 0, 1.0, 0, "#b07b0e")


# ---------------------------------------------------------------- globe & ship
def globe(c, x, y, r, t):
    c.drawCircle(x, y, r + 30, rad_grad(x, y, r + 30, ["#9fe3df55", "#9fe3df00"]))
    c.drawCircle(x, y, r, rad_grad(x - r * 0.3, y - r * 0.3, r * 1.4,
                                   ["#5fb6ff", "#2a7fc9", "#1b5f93"]))
    c.save()
    pth = skia.Path()
    pth.addCircle(x, y, r)
    c.clipPath(pth, doAntiAlias=True)
    lands = [(-0.6, -0.35, 0.32, 0.22), (-0.45, 0.2, 0.18, 0.34), (0.15, -0.3, 0.22, 0.2),
             (0.2, 0.15, 0.2, 0.36), (0.75, -0.25, 0.36, 0.2), (0.9, 0.35, 0.16, 0.12),
             (1.4, -0.1, 0.25, 0.3)]
    span = 2.4
    for lx, ly, rx, ry in lands:
        px = ((lx + t * 0.12) % span) - span / 2
        sq = math.cos(px * math.pi / 2.0)
        if sq <= 0.05:
            continue
        ellipse(c, x + px * r, y + ly * r, rx * r * sq, ry * r, fc="#5cc27a")
        ellipse(c, x + px * r + rx * r * 0.3 * sq, y + ly * r - ry * r * 0.3,
                rx * r * 0.5 * sq, ry * r * 0.5, fc="#78d48f")
    for k in range(-2, 3):
        ellipse(c, x, y + k * r * 0.33, r * math.sqrt(1 - (k * 0.33) ** 2), 4,
                sc="#ffffff", sw=2, a=0.25)
    c.restore()
    circle(c, x, y, r, sc="#ffffff", sw=5, a=0.6)


def ship(c, x, y, s=1.0, t=0.0, mouth=0.0, talking=False):
    from .characters import draw_cargo
    bob = math.sin(t * 2.2) * 6
    with at(c, x, y + bob, s, rot=math.sin(t * 1.7) * 1.5):
        rect(c, -300, -120, 120, 70, fc="#3bb273", sc="#2a7f52", sw=4, r=6)
        rect(c, -170, -120, 120, 70, fc="#1f3a5f", sc="#132a46", sw=4, r=6)
        rect(c, -300, -180, 120, 60, fc="#ffb627", sc="#b07b0e", sw=4, r=6)
        rect(c, 180, -200, 90, 150, fc="#ffffff", sc="#c8ced6", sw=4, r=8)
        for i in range(3):
            rect(c, 195 + i * 25, -180, 16, 16, fc="#8fd3ff", r=3)
        rect(c, 220, -250, 26, 50, fc="#e4572e")
        draw_cargo(c, 40, -60, 0.62, mouth=mouth, t=t, talking=talking)
        p = poly([(-360, -60), (330, -60), (280, 40), (-320, 40)])
        draw_path(c, p, fc="#e4572e", sc="#a83a1c", sw=6)
        rect(c, -340, -10, 650, 14, fc="#ffffff", a=0.8)
        text(c, "SAFARITECH", -20, 32, 30, "#ffffff", 700, "center")


def waves(c, y, t, color="#2b86c5", amp=14, a=1.0):
    p = skia.Path()
    p.moveTo(0, H)
    for x in range(0, W + 40, 40):
        p.lineTo(x, y + amp * math.sin(x / 90 + t * 2))
    p.lineTo(W, H)
    p.close()
    draw_path(c, p, fc=color, a=a)


# ---------------------------------------------------------------- courtrooms
def courtroom(c, x, y, w, h, t):
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), lin_grad(0, y, 0, y + h, ["#e9d8bd", "#d8c09b"]))
    rect(c, x, y + h - 170, w, 170, fc="#b88d62")
    # bench
    rect(c, x + w / 2 - 230, y + 230, 460, 170, fc="#8c5a3c", sc="#5e3b25", sw=5, r=8)
    rect(c, x + w / 2 - 250, y + 216, 500, 26, fc="#6b4430", r=6)
    from .characters import mini_person
    mini_person(c, x + w / 2, y + 236, 0.9, "#1b1b1b", skin="#c98b62", head_item="wig")
    rect(c, x + w / 2 - 230, y + 236, 460, 170, fc="#8c5a3c", sc="#5e3b25", sw=5, r=8)
    with at(c, x + w / 2, y + 140, 0.35):
        scales(c, 0, 0, 1.0, math.sin(t) * 3, "#b07b0e")
    # public gallery
    for i in range(6):
        mini_person(c, x + 80 + i * (w - 160) / 5, y + h - 40, 0.7,
                    ["#e07a5f", "#3d405b", "#81b29a", "#f2cc8f", "#7768ae", "#0f8b8d"][i],
                    skin=["#8d5a3b", "#e8b48f", "#5e3b25", "#c98b62", "#a86f4c", "#e8b48f"][i])
    rect(c, x + 20, y + h - 70, w - 40, 22, fc="#6b4430", r=6)


def arb_room(c, x, y, w, h, t):
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), lin_grad(0, y, 0, y + h, ["#e6f4f1", "#cfe7e2"]))
    rect(c, x, y + h - 170, w, 170, fc="#a7c4bc")
    # private: closed door with lock
    rect(c, x + w - 170, y + 60, 120, 230, fc="#7a5c45", sc="#5e3b25", sw=5, r=8)
    with at(c, x + w - 110, y + 175):
        rect(c, -20, -6, 40, 34, fc="#ffb627", r=6)
        c.drawArc(skia.Rect.MakeXYWH(-14, -26, 28, 36), 180, 180, False,
                  stroke("#b07b0e", 6))
    from .characters import mini_person
    # table
    mini_person(c, x + w / 2 - 170, y + h - 150, 0.85, "#e07a5f", skin="#8d5a3b")
    mini_person(c, x + w / 2 + 170, y + h - 150, 0.85, "#3d405b", skin="#e8b48f")
    mini_person(c, x + w / 2, y + h - 190, 0.95, "#0f8b8d", skin="#5e3b25", mood="happy")
    # expert badge
    with at(c, x + w / 2 + 2, y + h - 300):
        circle(c, 0, 0, 18, fc="#ffb627", sc="#b07b0e", sw=3)
        draw_path(c, poly([(math.cos(math.radians(-90 + i * 36)) * (11 if i % 2 == 0 else 5),
                            math.sin(math.radians(-90 + i * 36)) * (11 if i % 2 == 0 else 5))
                           for i in range(10)]), fc="#ffffff")
    ellipse(c, x + w / 2, y + h - 130, 260, 46, fc="#8c5a3c", sc="#5e3b25", sw=5)


def corkboard(c, x, y, w, h):
    rect(c, x - 16, y - 16, w + 32, h + 32, fc="#8c5a3c", r=14)
    rect(c, x, y, w, h, fc="#d9a066", r=6)
    for i in range(60):
        circle(c, x + (i * 97.3) % w, y + (i * 53.7) % h, 3, fc="#b07b48", a=0.6)


def pushpin(c, x, y, color="#e4572e"):
    circle(c, x + 3, y + 4, 12, fc="#000000", a=0.2)
    circle(c, x, y, 12, fc=color, sc=shade(color, -0.3), sw=3)
    circle(c, x - 4, y - 4, 4, fc="#ffffff", a=0.7)
