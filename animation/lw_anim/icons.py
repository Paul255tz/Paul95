"""Flat icon library for the template engine.

Each icon is drawn centred on (x, y) inside a box of roughly 100x100 units at
s=1. `color` is the accent; most icons also use ink outlines and white fills.
"""
from __future__ import annotations

import math

import skia

from . import props as P
from .gfx import (at, circle, draw_path, ellipse, line, poly, rect, shade, stroke,
                  text)

INK = "#1d2b3a"


def _doc(c, color, title_lines=4, fold=True):
    rect(c, -36, -46, 72, 92, fc="#ffffff", sc=INK, sw=4, r=6)
    rect(c, -36, -46, 72, 18, fc=color, r=6)
    for i in range(title_lines):
        line(c, -24, -12 + i * 14, 24 - (14 if i == title_lines - 1 else 0), -12 + i * 14,
             "#b8c2cc", 5)


def i_doc(c, color):
    _doc(c, color)


def i_contract(c, color):
    _doc(c, color, 3)
    p = skia.Path()
    p.moveTo(-22, 34)
    p.cubicTo(-12, 22, -4, 44, 6, 30)
    p.cubicTo(12, 22, 16, 36, 24, 30)
    c.drawPath(p, stroke(color, 4))


def i_bill(c, color):  # bill of lading / negotiable document
    _doc(c, color, 3)
    with at(c, 0, 26, 0.32):
        P.ship(c, 0, 20, 0.6)


def i_ship(c, color):
    with at(c, 0, 30):
        draw_path(c, poly([(-52, -20), (52, -20), (38, 12), (-40, 12)]), fc=color,
                  sc=shade(color, -0.35), sw=4)
        for i, cc in enumerate(["#e4572e", "#ffb627", "#0f8b8d"]):
            rect(c, -36 + i * 24, -46, 22, 26, fc=cc, sc=INK, sw=2, r=2)
        rect(c, 22, -64, 18, 44, fc="#ffffff", sc=INK, sw=3, r=3)
        rect(c, 25, -76, 12, 12, fc="#e4572e", r=2)


def i_container(c, color):
    rect(c, -50, -32, 100, 64, fc=color, sc=shade(color, -0.35), sw=4, r=4)
    for i in range(1, 8):
        line(c, -50 + i * 12.5, -24, -50 + i * 12.5, 24, shade(color, -0.2), 3)


def i_truck(c, color):
    rect(c, -52, -36, 66, 50, fc=color, sc=INK, sw=4, r=6)
    draw_path(c, poly([(16, -20), (38, -20), (52, 0), (52, 14), (16, 14)]), fc="#ffffff",
              sc=INK, sw=4)
    for xx in (-34, 32):
        circle(c, xx, 20, 12, fc=INK)
        circle(c, xx, 20, 5, fc="#ffffff")


def i_plane(c, color):
    with at(c, 0, 0, rot=-20):
        ellipse(c, 0, 0, 54, 10, fc=color, sc=INK, sw=3)
        draw_path(c, poly([(-6, -4), (10, -4), (-14, -44), (-26, -44)]), fc=color, sc=INK, sw=3)
        draw_path(c, poly([(-6, 4), (10, 4), (-14, 44), (-26, 44)]), fc=color, sc=INK, sw=3)
        draw_path(c, poly([(-44, -2), (-36, -2), (-50, -22), (-56, -22)]), fc=color, sc=INK,
                  sw=3)


def i_factory(c, color):
    draw_path(c, poly([(-50, 40), (-50, -6), (-24, -22), (-24, -6), (2, -22), (2, -6),
                       (28, -22), (28, 40)]), fc=color, sc=INK, sw=4)
    rect(c, 32, -50, 16, 90, fc=shade(color, -0.2), sc=INK, sw=4)
    for i in range(3):
        rect(c, -42 + i * 24, 10, 14, 14, fc="#ffffff", r=2)
    circle(c, 46, -62, 8, fc="#c8ced6", a=0.8)
    circle(c, 56, -74, 10, fc="#c8ced6", a=0.6)


def i_warehouse(c, color):
    draw_path(c, poly([(-52, -10), (0, -44), (52, -10), (52, 42), (-52, 42)]), fc=color,
              sc=INK, sw=4)
    rect(c, -26, 4, 52, 38, fc="#ffffff", sc=INK, sw=3)
    for i in range(3):
        line(c, -26, 14 + i * 10, 26, 14 + i * 10, "#b8c2cc", 3)


def i_crane(c, color):
    rect(c, -30, -50, 10, 92, fc=color, sc=INK, sw=3)
    rect(c, -44, -56, 96, 10, fc=color, sc=INK, sw=3)
    line(c, 34, -46, 34, -6, INK, 3)
    rect(c, 22, -6, 26, 18, fc="#e4572e", sc=INK, sw=2)
    rect(c, -50, 36, 100, 10, fc="#2b86c5", r=4)


def i_bank(c, color):
    draw_path(c, poly([(-54, -18), (0, -50), (54, -18)]), fc=color, sc=INK, sw=4)
    for i in range(4):
        rect(c, -40 + i * 24, -12, 12, 44, fc="#ffffff", sc=INK, sw=3)
    rect(c, -56, 32, 112, 12, fc=color, sc=INK, sw=4, r=2)


def i_coin(c, color="#ffb627"):
    for i, (dx, dy) in enumerate(((-16, 18), (14, 10), (-2, -12))):
        ellipse(c, dx, dy + 8, 30, 12, fc=shade("#ffb627", -0.25))
        ellipse(c, dx, dy, 30, 12, fc="#ffd166", sc="#b07b0e", sw=3)


def i_cash(c, color):
    for i in range(3):
        rect(c, -48 + i * 4, -26 + i * 8, 96, 50, fc="#7cc48f", sc="#2f7d4a", sw=3, r=6)
    circle(c, 8, 12, 14, sc="#2f7d4a", sw=3)
    text(c, "$", 8, 22, 26, "#2f7d4a", 700, "center")


def i_moneybag(c, color):
    ellipse(c, 0, 14, 44, 38, fc="#d9a066", sc=INK, sw=4)
    draw_path(c, poly([(-14, -24), (14, -24), (22, -44), (-22, -44)]), fc="#d9a066",
              sc=INK, sw=4)
    line(c, -16, -24, 16, -24, color, 6)
    text(c, "$", 0, 30, 40, INK, 700, "center")


def i_card(c, color):
    rect(c, -50, -32, 100, 64, fc=color, sc=INK, sw=4, r=8)
    rect(c, -50, -18, 100, 12, fc=INK)
    rect(c, -38, 8, 24, 16, fc="#ffd166", r=3)


def i_transfer(c, color):  # bank-to-bank arrow
    i_bank_small(c, -34, color)
    i_bank_small(c, 34, color)
    P.arrow(c, -14, 0, 16, 0, color, 6, 16)


def i_bank_small(c, x, color):
    with at(c, x, 0, 0.5):
        i_bank(c, color)


def i_globe(c, color):
    P.globe(c, 0, 0, 46, 0.0)


def i_gavel(c, color):
    P.gavel(c, -6, 6, 0.75, -35)


def i_scales(c, color):
    with at(c, 0, 26, 0.75):
        P.scales(c, 0, 0, 1.0, 0, color)


def i_court(c, color):
    with at(c, 0, 40, 0.42):
        P.courthouse(c, 0, 0, 1.0)


def i_parliament(c, color):
    with at(c, 0, 40, 0.42):
        P.parliament(c, 0, 0, 1.0)


def i_company(c, color):
    rect(c, -38, -50, 76, 96, fc=color, sc=INK, sw=4, r=4)
    for r_ in range(4):
        for k in range(3):
            rect(c, -28 + k * 20, -40 + r_ * 20, 12, 12, fc="#dff3ff")
    rect(c, -10, 26, 20, 20, fc=INK)


def i_house(c, color):
    draw_path(c, poly([(-46, -2), (0, -44), (46, -2)]), fc="#e4572e", sc=INK, sw=4)
    rect(c, -36, -4, 72, 46, fc=color, sc=INK, sw=4)
    rect(c, -8, 14, 16, 28, fc=INK)


def i_person(c, color):
    circle(c, 0, -24, 20, fc="#e8b48f", sc=INK, sw=4)
    p = skia.Path()
    p.moveTo(-36, 44)
    p.quadTo(-36, -2, 0, -2)
    p.quadTo(36, -2, 36, 44)
    p.close()
    draw_path(c, p, fc=color, sc=INK, sw=4)


def i_people(c, color):
    for dx, cc, s in ((-28, shade(color, 0.3), 0.75), (28, shade(color, 0.3), 0.75),
                      (0, color, 0.95)):
        with at(c, dx, 6 if s < 0.9 else 4, s):
            i_person(c, cc)


def i_handshake(c, color):
    with at(c, 0, 0, rot=-10):
        rect(c, -56, -6, 40, 24, fc="#7768ae", r=6)
        rect(c, 16, -6, 40, 24, fc="#0f8b8d", r=6)
        ellipse(c, -6, 4, 26, 18, fc="#c98b62", sc=INK, sw=3)
        ellipse(c, 8, 0, 24, 16, fc="#8d5a3b", sc=INK, sw=3)


def i_chain(c, color):
    for i in range(3):
        with at(c, -32 + i * 32, 0, rot=0 if i % 2 == 0 else 90):
            rect(c, -22, -13, 44, 26, sc=color, sw=8, r=13)


def i_lock(c, color):
    c.drawArc(skia.Rect.MakeXYWH(-24, -48, 48, 52), 180, 180, False, stroke(INK, 9))
    line(c, -24, -22, -24, -4, INK, 9)
    line(c, 24, -22, 24, -4, INK, 9)
    rect(c, -38, -8, 76, 54, fc=color, sc=INK, sw=4, r=8)
    circle(c, 0, 14, 8, fc=INK)
    rect(c, -3, 14, 6, 16, fc=INK)


def i_key(c, color):
    circle(c, -26, 0, 20, sc=color, sw=10)
    line(c, -6, 0, 48, 0, color, 10)
    line(c, 30, 0, 30, 16, color, 8)
    line(c, 44, 0, 44, 14, color, 8)


def i_shield(c, color):
    p = skia.Path()
    p.moveTo(0, -50)
    p.lineTo(42, -34)
    p.quadTo(42, 20, 0, 50)
    p.quadTo(-42, 20, -42, -34)
    p.close()
    draw_path(c, p, fc=color, sc=INK, sw=4)
    p2 = skia.Path()
    p2.moveTo(-16, 0)
    p2.lineTo(-4, 14)
    p2.lineTo(18, -14)
    c.drawPath(p2, stroke("#ffffff", 8))


def i_clock(c, color):
    circle(c, 0, 0, 46, fc="#ffffff", sc=color, sw=7)
    line(c, 0, 0, 0, -30, INK, 6)
    line(c, 0, 0, 22, 8, INK, 6)
    circle(c, 0, 0, 5, fc=INK)


def i_calendar(c, color):
    rect(c, -44, -40, 88, 84, fc="#ffffff", sc=INK, sw=4, r=8)
    rect(c, -44, -40, 88, 22, fc=color, r=8)
    for r_ in range(3):
        for k in range(4):
            rect(c, -34 + k * 19, -10 + r_ * 17, 11, 10, fc="#b8c2cc", r=2)


def i_hourglass(c, color):
    rect(c, -32, -50, 64, 8, fc=INK, r=3)
    rect(c, -32, 42, 64, 8, fc=INK, r=3)
    draw_path(c, poly([(-26, -42), (26, -42), (4, 0), (26, 42), (-26, 42), (-4, 0)]),
              fc="#ffffff", sc=INK, sw=4)
    draw_path(c, poly([(-16, 40), (16, 40), (0, 22)]), fc=color)
    draw_path(c, poly([(-12, -30), (12, -30), (0, -6)]), fc=color)


def i_warning(c, color="#ffb627"):
    draw_path(c, poly([(0, -48), (50, 40), (-50, 40)]), fc="#ffd166", sc=INK, sw=5)
    line(c, 0, -14, 0, 14, INK, 9)
    circle(c, 0, 28, 5, fc=INK)


def i_check(c, color):
    P.check(c, 0, 0, 1.6, color if color != "#ffffff" else "#3bb273")


def i_cross(c, color):
    P.cross(c, 0, 0, 1.6)


def i_star(c, color):
    pts = []
    for i in range(10):
        r = 48 if i % 2 == 0 else 20
        a = math.radians(-90 + i * 36)
        pts.append((math.cos(a) * r, math.sin(a) * r))
    draw_path(c, poly(pts), fc="#ffd166", sc="#b07b0e", sw=4)


def i_flag(c, color):
    line(c, -30, -50, -30, 50, INK, 6)
    p = skia.Path()
    p.moveTo(-28, -46)
    p.quadTo(0, -60, 20, -44)
    p.quadTo(36, -34, 48, -40)
    p.lineTo(48, 0)
    p.quadTo(36, 6, 20, -4)
    p.quadTo(0, -20, -28, -6)
    p.close()
    draw_path(c, p, fc=color, sc=INK, sw=3)


def i_book(c, color):
    rect(c, -40, -46, 80, 92, fc=color, sc=INK, sw=4, r=6)
    rect(c, -40, 34, 80, 12, fc="#ffffff", sc=INK, sw=3)
    rect(c, -26, -32, 52, 16, fc="#ffffff", a=0.8, r=3)


def i_scroll(c, color):
    rect(c, -34, -40, 68, 80, fc="#fff3d6", sc=INK, sw=4)
    for yy in (-40, 40):
        ellipse(c, 0, yy, 42, 9, fc="#e9c46a", sc=INK, sw=4)
    for i in range(4):
        line(c, -22, -20 + i * 13, 22, -20 + i * 13, "#c9a27a", 4)


def i_stamp(c, color):
    rect(c, -12, -50, 24, 34, fc=INK, r=8)
    rect(c, -36, -18, 72, 18, fc=shade(color, -0.2), sc=INK, sw=3, r=4)
    rect(c, -46, 18, 92, 30, sc=color, sw=5, r=4)
    text(c, "OK", 0, 42, 26, color, 700, "center")


def i_magnifier(c, color):
    circle(c, -10, -10, 32, fc="#dff3ff", sc=INK, sw=8)
    line(c, 14, 14, 46, 46, INK, 12)


def i_chart(c, color):
    line(c, -46, 44, 46, 44, INK, 5)
    line(c, -46, 44, -46, -46, INK, 5)
    for i, h in enumerate((20, 38, 56, 80)):
        rect(c, -36 + i * 21, 40 - h, 15, h, fc=color, r=2)


def i_chartdown(c, color):
    line(c, -46, 44, 46, 44, INK, 5)
    line(c, -46, 44, -46, -46, INK, 5)
    p = skia.Path()
    p.moveTo(-40, -36)
    p.lineTo(-14, -6)
    p.lineTo(4, -18)
    p.lineTo(38, 30)
    c.drawPath(p, stroke("#e4572e", 7))
    P.arrow(c, 20, 6, 40, 32, "#e4572e", 7, 14)


def i_pie(c, color):
    circle(c, 0, 0, 46, fc="#dfe5ea", sc=INK, sw=4)
    p = skia.Path()
    p.moveTo(0, 0)
    p.arcTo(skia.Rect.MakeXYWH(-46, -46, 92, 92), -90, 130, False)
    p.close()
    draw_path(c, p, fc=color, sc=INK, sw=4)


def i_ballot(c, color):
    rect(c, -44, -6, 88, 52, fc=color, sc=INK, sw=4, r=6)
    rect(c, -26, -2, 52, 8, fc=INK, r=3)
    with at(c, 0, -22, rot=-8):
        rect(c, -22, -26, 44, 42, fc="#ffffff", sc=INK, sw=3)
        P.check(c, 0, -6, 0.5)


def i_megaphone(c, color):
    draw_path(c, poly([(-40, -14), (20, -42), (20, 42), (-40, 14)]), fc=color, sc=INK, sw=4)
    rect(c, -52, -16, 16, 32, fc=INK, r=4)
    for i in range(2):
        c.drawArc(skia.Rect.MakeXYWH(14 + i * 10, -30 - i * 8, 40, 60 + i * 16), -50, 100,
                  False, stroke(INK, 4))


def i_bulb(c, color):
    circle(c, 0, -12, 34, fc="#ffd166", sc=INK, sw=4)
    rect(c, -16, 20, 32, 24, fc="#c8ced6", sc=INK, sw=3, r=4)
    line(c, -10, -8, 0, 6, "#b07b0e", 4)
    line(c, 0, 6, 10, -8, "#b07b0e", 4)


def i_envelope(c, color):
    rect(c, -48, -32, 96, 64, fc="#ffffff", sc=INK, sw=4, r=6)
    p = skia.Path()
    p.moveTo(-46, -30)
    p.lineTo(0, 6)
    p.lineTo(46, -30)
    c.drawPath(p, stroke(color, 5))


def i_laptop(c, color):
    rect(c, -40, -36, 80, 54, fc=INK, r=6)
    rect(c, -34, -30, 68, 42, fc=color, r=3)
    draw_path(c, poly([(-52, 22), (52, 22), (44, 34), (-44, 34)]), fc="#8a96a3", sc=INK, sw=3)


def i_crown(c, color):
    draw_path(c, poly([(-46, 30), (-46, -24), (-22, 2), (0, -36), (22, 2), (46, -24),
                       (46, 30)]), fc="#ffd166", sc="#b07b0e", sw=4)
    for xx in (-22, 0, 22):
        circle(c, xx, 16, 6, fc="#e4572e")


def i_umbrella(c, color):
    p = skia.Path()
    p.moveTo(-50, 0)
    p.quadTo(0, -64, 50, 0)
    for k in range(4):
        p.quadTo(37.5 - k * 25, -12, 25 - k * 25, 0)
    p.close()
    draw_path(c, p, fc=color, sc=INK, sw=4)
    line(c, 0, 0, 0, 38, INK, 5)
    c.drawArc(skia.Rect.MakeXYWH(-14, 28, 14, 20), 0, 180, False, stroke(INK, 5))


def i_box(c, color):
    draw_path(c, poly([(-44, -20), (0, -40), (44, -20), (0, 0)]), fc=shade("#d9a066", 0.2),
              sc=INK, sw=4)
    draw_path(c, poly([(-44, -20), (0, 0), (0, 46), (-44, 26)]), fc="#d9a066", sc=INK, sw=4)
    draw_path(c, poly([(44, -20), (0, 0), (0, 46), (44, 26)]), fc=shade("#d9a066", -0.15),
              sc=INK, sw=4)


def i_eye(c, color):
    p = skia.Path()
    p.moveTo(-50, 0)
    p.quadTo(0, -44, 50, 0)
    p.quadTo(0, 44, -50, 0)
    draw_path(c, p, fc="#ffffff", sc=INK, sw=4)
    circle(c, 0, 0, 18, fc=color)
    circle(c, 0, 0, 8, fc=INK)


def i_handcuffs(c, color):
    for xx in (-24, 24):
        circle(c, xx, 10, 22, sc="#8a96a3", sw=9)
    line(c, -8, -14, 8, -14, "#8a96a3", 6)


def i_mask(c, color):
    p = skia.Path()
    p.moveTo(-50, -14)
    p.quadTo(0, -30, 50, -14)
    p.quadTo(46, 24, 14, 20)
    p.quadTo(0, 8, -14, 20)
    p.quadTo(-46, 24, -50, -14)
    draw_path(c, p, fc=INK)
    ellipse(c, -22, -2, 12, 8, fc="#ffffff")
    ellipse(c, 22, -2, 12, 8, fc="#ffffff")


def i_washer(c, color):  # money laundering
    rect(c, -42, -48, 84, 96, fc="#ffffff", sc=INK, sw=4, r=10)
    rect(c, -42, -48, 84, 18, fc="#dfe5ea", sc=INK, sw=4, r=10)
    circle(c, 0, 10, 28, fc="#9fe3df", sc=INK, sw=5)
    text(c, "$", 0, 22, 32, "#2f7d4a", 700, "center")


def i_gift(c, color):
    rect(c, -40, -12, 80, 56, fc=color, sc=INK, sw=4, r=4)
    rect(c, -46, -28, 92, 18, fc=shade(color, 0.15), sc=INK, sw=4, r=4)
    rect(c, -6, -28, 12, 72, fc="#ffd166")
    for sg in (-1, 1):
        ellipse(c, sg * 14, -38, 14, 9, sc="#ffd166", sw=6)


def i_veil(c, color):  # corporate veil
    i_company(c, "#7768ae")
    p = skia.Path()
    p.moveTo(-56, -56)
    p.lineTo(56, -56)
    for k in range(6):
        p.quadTo(56 - k * 18.7 - 9, 66, 56 - (k + 1) * 18.7, 50)
    p.close()
    draw_path(c, p, fc="#9fe3df", a=0.7)
    line(c, -58, -56, 58, -56, INK, 6)


def i_tree(c, color):  # group structure
    rect(c, -18, -50, 36, 26, fc=color, sc=INK, sw=3, r=4)
    line(c, 0, -24, 0, -6, INK, 4)
    line(c, -34, -6, 34, -6, INK, 4)
    for xx in (-34, 34):
        line(c, xx, -6, xx, 14, INK, 4)
        rect(c, xx - 16, 14, 32, 24, fc=shade(color, 0.3), sc=INK, sw=3, r=4)


def i_percent(c, color):
    circle(c, -22, -22, 14, sc=color, sw=8)
    circle(c, 22, 22, 14, sc=color, sw=8)
    line(c, 30, -36, -30, 36, color, 9)


def i_tag(c, color):
    draw_path(c, poly([(-46, -24), (20, -24), (48, 0), (20, 24), (-46, 24)]), fc=color,
              sc=INK, sw=4)
    circle(c, 22, 0, 6, fc="#ffffff")


def i_receipt(c, color):
    pts = [(-34, -48), (34, -48), (34, 48)]
    for k in range(6):
        pts.append((34 - k * 11.3 - 5.6, 40 if k % 2 == 0 else 48))
    pts.append((-34, 48))
    draw_path(c, poly(pts), fc="#ffffff", sc=INK, sw=4)
    for i in range(4):
        line(c, -22, -32 + i * 16, 22, -32 + i * 16, "#b8c2cc", 4)


def i_scissors(c, color):
    for sg in (-1, 1):
        circle(c, -32, sg * 18, 14, sc=color, sw=7)
        line(c, -20, sg * 12, 44, -sg * 14, INK, 7)


def i_ladder(c, color):
    line(c, -26, -50, -26, 50, color, 8)
    line(c, 26, -50, 26, 50, color, 8)
    for i in range(5):
        line(c, -26, -38 + i * 19, 26, -38 + i * 19, color, 6)


def i_fire(c, color):
    p = skia.Path()
    p.moveTo(0, 48)
    p.cubicTo(-48, 40, -40, -8, -8, -48)
    p.cubicTo(-6, -20, 10, -16, 14, -30)
    p.cubicTo(48, 0, 40, 44, 0, 48)
    draw_path(c, p, fc="#e4572e", sc=INK, sw=4)
    ellipse(c, 2, 24, 14, 20, fc="#ffd166")


def i_mic(c, color):
    rect(c, -16, -50, 32, 58, fc=color, sc=INK, sw=4, r=16)
    c.drawArc(skia.Rect.MakeXYWH(-28, -20, 56, 50), 0, 180, False, stroke(INK, 5))
    line(c, 0, 30, 0, 46, INK, 5)
    line(c, -16, 46, 16, 46, INK, 5)


def i_brain(c, color):  # knowledge / mind
    for dx, dy, r in ((-18, -10, 26), (16, -14, 28), (-14, 16, 24), (18, 14, 24)):
        circle(c, dx, dy, r, fc="#f6a5c0", sc=INK, sw=3)
    line(c, 0, -34, 0, 34, INK, 3)


def i_signpost(c, color):  # choice of law / which way?
    line(c, 0, -50, 0, 50, INK, 7)
    draw_path(c, poly([(-4, -44), (40, -44), (52, -32), (40, -20), (-4, -20)]), fc=color,
              sc=INK, sw=3)
    draw_path(c, poly([(4, -8), (-40, -8), (-52, 4), (-40, 16), (4, 16)]), fc="#7768ae",
              sc=INK, sw=3)


def i_pen(c, color):
    with at(c, 0, 0, rot=40):
        rect(c, -10, -50, 20, 80, fc=color, sc=INK, sw=4, r=4)
        draw_path(c, poly([(-10, 30), (10, 30), (0, 52)]), fc="#e9c46a", sc=INK, sw=3)


def i_seal(c, color):
    pts = []
    for i in range(24):
        r = 46 if i % 2 == 0 else 38
        a = math.radians(i * 15)
        pts.append((math.cos(a) * r, math.sin(a) * r))
    draw_path(c, poly(pts), fc=color, sc=shade(color, -0.35), sw=3)
    circle(c, 0, 0, 26, sc="#ffffff", sw=4)


def i_door(c, color):
    rect(c, -32, -50, 64, 100, fc=color, sc=INK, sw=4, r=4)
    circle(c, 18, 2, 6, fc="#ffd166")


def i_question(c, color):
    circle(c, 0, 0, 46, fc=color)
    text(c, "?", 0, 24, 70, "#ffffff", 700, "center")


ICONS = {k[2:]: v for k, v in globals().items() if k.startswith("i_") and callable(v)}


def icon(c, name, x, y, s=1.0, color="#0f8b8d", a=1.0, rot=0.0):
    from .gfx import alpha_layer
    fn = ICONS[name]
    with alpha_layer(c, a), at(c, x, y, s, rot=rot):
        fn(c, color)
