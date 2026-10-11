"""Shared helpers for writing episodes: title, quiz and recap scenes."""
from ..beats import DISPLAY_NAMES, SERIES, VOICES, Line, Pause, Scene, Sfx  # noqa: F401


def title_scene(ep, title, syl, emblem=("globe", "gavel"), cast=None, say_title=None):
    return Scene("title", "Title", "", [
        Sfx("jingle"),
        Pause("logo", 2.6),
        Line("n1", "NARRATOR", "The Law Behind the Deal.", gap=0.25),
        Line("n2", "NARRATOR", f"Episode {ep}. {say_title or title}"),
        Pause("hold", 1.6),
    ], spec={"tpl": "title", "ep": ep, "title": title, "syl": syl, "emblem": list(emblem),
             **({"cast": cast} if cast else {})})


def quiz_scene(key, title, question, options, answer, ask, reply, why=None, why_who="LEX",
               think=5.0, syl=None, bg="studio_purple"):
    """Auditor's 'Quick check': the question is read aloud, then a countdown, then the answer.

    `ask` is what the Auditor says (usually the question), `reply` names the answer and
    `why` is an optional one-line explanation spoken by `why_who`.
    """
    beats = [Pause("open", 0.8), Sfx("whoosh"), Pause("in", 0.6),
             Line("q", "AUDITOR", ask, gap=0.3)]
    beats += [Sfx("tick", float(i)) for i in range(int(think))]
    beats += [Pause("think", think), Sfx("ding"), Line("a", "AUDITOR", reply, gap=0.4)]
    spec = {"tpl": "quiz", "question": question, "options": options, "answer": answer,
            "bg": bg}
    if why:
        beats.append(Line("x", why_who, why[1] if isinstance(why, tuple) else why, gap=0.4))
        spec["why"] = why[0] if isinstance(why, tuple) else why
        spec["why_at"] = "x"
    beats.append(Pause("hold", 1.4))
    if syl:
        spec["syl"] = syl
    return Scene(key, title, "", beats, spec=spec)


def recap_scene(key, cards, outro, next_ep=None, next_title=None, next_icon="globe",
                final_sub=None, extra=None):
    """cards: list of (spoken_text, card_text[, say]). Nia reads them; `outro` is a list
    of Line objects (Lex's sign-off, Cargo's joke...) before the narrator's teaser."""
    beats = [Pause("open", 1.0)]
    spec_cards = []
    for i, cd in enumerate(cards):
        spoken, label = cd[0], cd[1]
        say = cd[2] if len(cd) > 2 else None
        beats += [Sfx("pin"), Line(f"r{i}", "NIA", spoken, say=say, gap=0.3)]
        spec_cards.append({"at": f"r{i}", "text": label})
    beats += outro
    if next_ep:
        beats += [Sfx("jingle"),
                  Line("n3", "NARRATOR", f"Next time: Episode {next_ep}. {next_title}.", gap=0.6),
                  Pause("end", 3.6)]
        nxt = {"at": "n3", "ep": next_ep, "title": next_title, "icon": next_icon}
    else:
        beats += [Sfx("jingle"),
                  Line("n3", "NARRATOR", "That's the whole syllabus. Good luck in your exam!",
                       gap=0.6),
                  Pause("end", 4.0)]
        nxt = {"at": "n3", "final": True, "title": next_title or "You're exam ready!",
               "sub": final_sub or "", "icon": next_icon}
    spec = {"tpl": "recap", "cards": spec_cards, "next": nxt,
            "heading": "EPISODE RECAP"}
    if extra:
        spec.update(extra)
    return Scene(key, "Episode recap", "", beats, spec=spec)
