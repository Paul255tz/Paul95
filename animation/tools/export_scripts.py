#!/usr/bin/env python3
"""Export every episode's script to a readable Markdown screenplay.

    python animation/tools/export_scripts.py            # writes animation/scripts/*.md

Each screenplay lists the scenes in order with the visual template, what appears
on screen, every spoken line with its speaker, sound cues, and the interactive
"Quick check" pauses with their answers. Timings come from the last build's
timeline (animation/build/epNN/timeline.json) when available.
"""
from __future__ import annotations

import importlib
import json
import os
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)

from lw_anim.beats import DISPLAY_NAMES, Line, Pause, Sfx  # noqa: E402

TEMPLATE_NAMES = {
    "title": "Title card", "talk": "Character scene", "board": "Teaching board",
    "compare": "Side-by-side comparison", "flow": "Animated diagram",
    "stack": "Priority waterfall", "route": "Route map (risk and costs)",
    "case": "Case file", "timeline": "Timeline", "quiz": "Quick check (interactive)",
    "recap": "Recap corkboard",
}
BGS = {"office": "SafariTech office, Dar es Salaam", "harbour": "SafariTech office with "
       "harbour view", "port": "Port of Dar es Salaam", "bank": "Bank (Nairobi)",
       "boardroom": "Boardroom", "court": "Courtroom", "arbitration": "Arbitration room",
       "classroom": "Classroom", "studio": "Studio", "studio_teal": "Studio",
       "studio_purple": "Studio", "studio_red": "Studio", "globe": "Night sky", "night":
       "Night"}


def load(ep):
    if ep == 1:
        return importlib.import_module("lw_anim.script_ep1")
    return importlib.import_module(f"lw_anim.episodes.ep{ep:02d}")


def episodes():
    d = os.path.join(HERE, "lw_anim", "episodes")
    return [1] + sorted(int(f[2:4]) for f in os.listdir(d)
                        if f.startswith("ep") and f.endswith(".py"))


def fmt_time(x):
    return f"{int(x // 60)}:{int(x % 60):02d}"


def on_screen(spec):
    out = []
    tpl = spec.get("tpl")
    if spec.get("heading"):
        out.append(f"**Heading:** {spec['heading']}")
    if tpl in ("board",):
        for it in spec.get("items", []):
            out.append(f"- {it['text']}" + (f" — {it['sub']}" if it.get("sub") else ""))
    elif tpl == "compare":
        for col in spec["cols"]:
            out.append(f"- **{col['title']}:** " + "; ".join(i["text"] for i in col["items"]))
    elif tpl == "flow":
        out.append("- Nodes: " + "; ".join(n["label"] for n in spec["nodes"]))
        edges = [f"{e['from']} → {e['to']}" + (f" ({e['label']})" if e.get("label") else "")
                 for e in spec.get("edges", [])]
        if edges:
            out.append("- Arrows: " + "; ".join(edges))
    elif tpl == "stack":
        for i, tr in enumerate(spec["tiers"], 1):
            out.append(f"{i}. {tr['label']}" + (f" — {tr['sub']}" if tr.get("sub") else ""))
        if spec.get("pour"):
            out.append("- Animated: money pours down the tiers in order of priority")
    elif tpl == "route":
        for tm in spec["terms"]:
            out.append(f"- **{tm['code']}** {tm.get('name', '')}: {tm.get('note', '')}")
    elif tpl == "timeline":
        for ev in spec["events"]:
            out.append(f"- {ev['label']}" + (f" — {ev['sub']}" if ev.get("sub") else ""))
    elif tpl == "case":
        out.append(f"- **{spec['name']}** ({spec.get('year', '')})")
        for r in spec.get("rows", []):
            out.append(f"  - {r['label']}: {r['text']}")
        if spec.get("stamp"):
            out.append(f"  - Stamp: {spec['stamp']['text']}")
    elif tpl == "quiz":
        out.append(f"**Question:** {spec['question']}")
        for i, o in enumerate(spec["options"]):
            mark = " ✅" if i == spec["answer"] else ""
            out.append(f"- {'ABCD'[i]}. {o}{mark}")
        if spec.get("why"):
            out.append(f"- *Why:* {spec['why']}")
    elif tpl == "recap":
        out.append("- Recap cards: " + " · ".join(cd["text"] for cd in spec["cards"]))
    for p in spec.get("pops", []):
        if p.get("kind") == "card":
            out.append(f"- Pop-up card **{p.get('title', '')}**: {p.get('body', '')}")
        elif p.get("kind") in ("chip", "stamp"):
            out.append(f"- Caption: {p['text']}")
    return out


def export(ep, out_dir):
    S = load(ep)
    tl_path = os.path.join(HERE, "build", f"ep{ep:02d}", "timeline.json")
    tl = None
    if os.path.exists(tl_path):
        with open(tl_path) as f:
            tl = json.load(f)
    lines = [f"# {S.SERIES} — {S.EPISODE}: {S.EPISODE_TITLE}", ""]
    if tl:
        lines += [f"*Runtime: {fmt_time(tl['total'])}* · Video: "
                  f"[`{S.SLUG}.mp4`](../output/{S.SLUG}.mp4)", ""]
    doc = (S.__doc__ or "").strip()
    if doc:
        lines += ["> " + doc.replace("\n", " ").split(" - ", 1)[-1], ""]
    lines += ["**Cast:** " + ", ".join(sorted({DISPLAY_NAMES[b.who] for sc in S.SCENES
                                              for b in sc.beats if isinstance(b, Line)})),
              ""]
    for i, sc in enumerate(S.SCENES):
        spec = getattr(sc, "spec", None) or {}
        start = ""
        if tl and i < len(tl["scenes"]):
            start = f" `{fmt_time(tl['scenes'][i]['start'])}`"
        head = "Title" if sc.key == "title" else f"Scene {i}: {sc.title}"
        lines += [f"## {head}{start}", ""]
        meta = []
        if spec.get("tpl"):
            meta.append(TEMPLATE_NAMES.get(spec["tpl"], spec["tpl"]))
        if spec.get("bg") and spec.get("tpl") not in ("quiz", "route"):
            meta.append(BGS.get(spec["bg"], spec["bg"]))
        if spec.get("syl"):
            meta.append(f"Syllabus {spec['syl']}")
        if meta:
            lines += ["*" + " · ".join(meta) + "*", ""]
        vis = on_screen(spec) if spec else []
        if vis:
            lines += ["**On screen**", ""] + vis + [""]
        lines += ["**Script**", ""]
        for b in sc.beats:
            if isinstance(b, Line):
                lines.append(f"- **{DISPLAY_NAMES[b.who].upper()}:** {b.text}")
            elif isinstance(b, Pause) and b.id == "think":
                lines.append(f"- ⏸ *PAUSE AND THINK — {b.dur:.0f}-second countdown*")
            elif isinstance(b, Pause) and b.dur >= 3 and b.id not in ("logo", "end"):
                lines.append(f"- *({b.id}: {b.dur:.1f}s visual beat)*")
            elif isinstance(b, Sfx) and b.kind in ("jingle", "horn", "door", "whoosh"):
                lines.append(f"- *SFX: {b.kind}*")
        lines.append("")
    name = f"{S.SLUG}.md"
    with open(os.path.join(out_dir, name), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return S, name, (tl["total"] if tl else None)


def main():
    out_dir = os.path.join(HERE, "scripts")
    os.makedirs(out_dir, exist_ok=True)
    rows = []
    for ep in episodes():
        S, name, total = export(ep, out_dir)
        rows.append((ep, S.EPISODE_TITLE, name, total, S.SLUG))
        print("wrote", name)
    idx = ["# Episode scripts", "",
           "Screenplays for every episode of *The Law Behind the Deal*, exported from the "
           "source scripts in `lw_anim/`. Regenerate with "
           "`python animation/tools/export_scripts.py`.", "",
           "| # | Episode | Runtime | Script | Video |", "|---|---|---|---|---|"]
    for ep, title, name, total, slug in rows:
        rt = fmt_time(total) if total else "—"
        idx.append(f"| {ep} | {title} | {rt} | [script]({name}) | "
                   f"[mp4](../output/{slug}.mp4) |")
    with open(os.path.join(out_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(idx) + "\n")


if __name__ == "__main__":
    main()
