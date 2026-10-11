"""Small drawing toolkit on top of skia-python.

All scenes are authored in a 1920x1080 logical space; the renderer scales the
canvas to the requested output size.
"""
from __future__ import annotations

import math
import os
from functools import lru_cache

import skia

W, H = 1920, 1080
ASSETS = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")

# ---------------------------------------------------------------- palette
PALETTE = {
    "ink": "#1d2b3a",
    "navy": "#1f3a5f",
    "teal": "#0f8b8d",
    "teal_l": "#9fe3df",
    "accent": "#ffb627",   # rule being taught
    "mistake": "#e4572e",  # common mistake
    "cream": "#fff8ec",
    "paper": "#ffffff",
    "sky": "#bfe6ff",
    "wall": "#f4ead9",
    "floor": "#c9a27a",
    "grey": "#8a96a3",
    "grey_l": "#dfe5ea",
    "green": "#3bb273",
    "purple": "#7768ae",
}


def col(c, a: float = 1.0) -> int:
    """Hex string (or int) -> skia colour int with alpha multiplier."""
    if isinstance(c, int):
        base = c
    else:
        c = PALETTE.get(c, c).lstrip("#")
        if len(c) == 8:  # CSS-style RRGGBBAA
            c = c[6:] + c[:6]
        else:
            c = "ff" + c
        base = int(c, 16)
    alpha = int(((base >> 24) & 0xFF) * max(0.0, min(1.0, a)))
    return (alpha << 24) | (base & 0xFFFFFF)


def mix(c1, c2, k: float) -> int:
    a, b = col(c1), col(c2)
    out = 0
    for sh in (24, 16, 8, 0):
        x = (a >> sh) & 0xFF
        y = (b >> sh) & 0xFF
        out |= int(x + (y - x) * k) << sh
    return out


def shade(c, k: float) -> int:
    """k<0 darkens, k>0 lightens."""
    return mix(c, "#000000" if k < 0 else "#ffffff", abs(k))


# ---------------------------------------------------------------- easing
def clamp(x, a=0.0, b=1.0):
    return a if x < a else b if x > b else x


def prog(t, t0, dur):
    if dur <= 0:
        return 1.0 if t >= t0 else 0.0
    return clamp((t - t0) / dur)


def ease_in_out(x):
    x = clamp(x)
    return x * x * (3 - 2 * x)


def ease_out(x):
    x = clamp(x)
    return 1 - (1 - x) ** 3


def ease_in(x):
    x = clamp(x)
    return x ** 3


def ease_out_back(x, s=1.70158):
    x = clamp(x)
    x -= 1
    return x * x * ((s + 1) * x + s) + 1


def lerp(a, b, k):
    return a + (b - a) * k


def window(t, t0, t1, fade=0.35):
    """1 inside [t0, t1], fading in/out over `fade` seconds."""
    if t < t0 or t > t1 + fade:
        return 0.0
    return ease_in_out(prog(t, t0, fade)) * (1 - ease_in_out(prog(t, t1, fade)))


# ---------------------------------------------------------------- paints
def fill(c, a=1.0, aa=True):
    return skia.Paint(Color=col(c, a), AntiAlias=aa, Style=skia.Paint.kFill_Style)


def stroke(c, w=4.0, a=1.0, cap=skia.Paint.kRound_Cap):
    p = skia.Paint(Color=col(c, a), AntiAlias=True, Style=skia.Paint.kStroke_Style,
                   StrokeWidth=w)
    p.setStrokeCap(cap)
    p.setStrokeJoin(skia.Paint.kRound_Join)
    return p


def shape(c: skia.Canvas, draw, fc=None, sc=None, sw=4.0, a=1.0):
    """Call draw(paint) for fill and/or stroke."""
    if fc is not None:
        draw(fill(fc, a))
    if sc is not None:
        draw(stroke(sc, sw, a))


def rect(c, x, y, w, h, fc=None, sc=None, sw=4.0, a=1.0, r=0.0):
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), r, r)
    shape(c, lambda p: c.drawRRect(rr, p), fc, sc, sw, a)


def circle(c, x, y, r, fc=None, sc=None, sw=4.0, a=1.0):
    shape(c, lambda p: c.drawCircle(x, y, r, p), fc, sc, sw, a)


def ellipse(c, x, y, rx, ry, fc=None, sc=None, sw=4.0, a=1.0):
    r = skia.Rect.MakeLTRB(x - rx, y - ry, x + rx, y + ry)
    shape(c, lambda p: c.drawOval(r, p), fc, sc, sw, a)


def line(c, x1, y1, x2, y2, color="ink", w=4.0, a=1.0):
    c.drawLine(x1, y1, x2, y2, stroke(color, w, a))


def poly(pts, close=True) -> skia.Path:
    p = skia.Path()
    p.moveTo(*pts[0])
    for q in pts[1:]:
        p.lineTo(*q)
    if close:
        p.close()
    return p


def draw_path(c, path, fc=None, sc=None, sw=4.0, a=1.0):
    shape(c, lambda p: c.drawPath(path, p), fc, sc, sw, a)


def lin_grad(x0, y0, x1, y1, colors, a=1.0):
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeLinear(
        [skia.Point(x0, y0), skia.Point(x1, y1)], [col(k, a) for k in colors]))
    return p


def rad_grad(x, y, r, colors, a=1.0):
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeRadial(
        skia.Point(x, y), r, [col(k, a) for k in colors]))
    return p


def soft_shadow(c, x, y, rx, ry, a=0.18):
    ellipse(c, x, y, rx, ry, fc="#000000", a=a)


# ---------------------------------------------------------------- text
def _tag(s):
    return (ord(s[0]) << 24) | (ord(s[1]) << 16) | (ord(s[2]) << 8) | ord(s[3])


@lru_cache(maxsize=None)
def typeface(family="Fredoka", weight=500):
    path = os.path.join(ASSETS, "fonts", f"{family}.ttf")
    tf = skia.Typeface.MakeFromFile(path)
    coord = skia.FontArguments.VariationPosition.Coordinate(_tag("wght"), float(weight))
    vp = skia.FontArguments.VariationPosition(
        skia.FontArguments.VariationPosition.Coordinates([coord]))
    fa = skia.FontArguments()
    fa.setVariationDesignPosition(vp)
    return tf.makeClone(fa)


@lru_cache(maxsize=None)
def font(size, family="Fredoka", weight=500):
    f = skia.Font(typeface(family, weight), size)
    f.setSubpixel(True)
    f.setEdging(skia.Font.Edging.kAntiAlias)
    return f


def text_width(s, size, family="Fredoka", weight=500):
    return font(size, family, weight).measureText(s)


def text(c, s, x, y, size=48, color="ink", weight=500, align="left", a=1.0,
         family="Fredoka", outline=None, outline_w=8):
    """Draw a single line; y is the baseline."""
    f = font(size, family, weight)
    w = f.measureText(s)
    if align == "center":
        x -= w / 2
    elif align == "right":
        x -= w
    blob = skia.TextBlob.MakeFromString(s, f)
    if outline:
        c.drawTextBlob(blob, x, y, stroke(outline, outline_w, a))
    c.drawTextBlob(blob, x, y, fill(color, a))
    return w


def wrap(s, size, max_w, family="Fredoka", weight=500):
    words, lines, cur = s.split(), [], ""
    for wd in words:
        trial = (cur + " " + wd).strip()
        if text_width(trial, size, family, weight) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


def text_block(c, s, x, y, max_w, size=40, color="ink", weight=500, align="left",
               a=1.0, leading=1.25, family="Fredoka"):
    """Wrapped paragraph; y is the top. Returns total height."""
    lines = wrap(s, size, max_w, family, weight)
    for i, ln in enumerate(lines):
        text(c, ln, x, y + size + i * size * leading, size, color, weight, align, a,
             family)
    return len(lines) * size * leading


# ---------------------------------------------------------------- transforms
class at:
    """Context manager: translate/scale/rotate around a point."""

    def __init__(self, c, x=0.0, y=0.0, s=1.0, rot=0.0, sx=None, sy=None):
        self.c, self.x, self.y = c, x, y
        self.sx = s if sx is None else sx
        self.sy = s if sy is None else sy
        self.rot = rot

    def __enter__(self):
        self.c.save()
        self.c.translate(self.x, self.y)
        if self.rot:
            self.c.rotate(self.rot)
        if self.sx != 1 or self.sy != 1:
            self.c.scale(self.sx, self.sy)
        return self.c

    def __exit__(self, *a):
        self.c.restore()


class alpha_layer:
    """Draw children with a global opacity."""

    def __init__(self, c, a):
        self.c, self.a = c, clamp(a)

    def __enter__(self):
        if self.a < 0.999:
            self.c.saveLayerAlpha(None, int(255 * self.a))
        else:
            self.c.save()
        return self.c

    def __exit__(self, *a):
        self.c.restore()


def pop_scale(t, t0, dur=0.45):
    """Scale factor for a 'pop in' entrance."""
    return ease_out_back(prog(t, t0, dur), 2.2)


def wobble(t, speed=1.0, amp=1.0, seed=0.0):
    return amp * math.sin(t * speed * 2 * math.pi + seed)
