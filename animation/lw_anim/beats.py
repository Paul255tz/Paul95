"""Script building blocks shared by every episode."""
from dataclasses import dataclass, field


@dataclass
class Line:
    id: str
    who: str
    text: str
    say: str | None = None
    gap: float = 0.35   # silence after the line


@dataclass
class Pause:
    id: str
    dur: float


@dataclass
class Sfx:
    kind: str
    offset: float = 0.0


@dataclass
class Scene:
    key: str
    title: str
    clock: str
    beats: list = field(default_factory=list)
    spec: dict | None = None   # visual layout for the template engine (episodes 2+)


# Voice cast (Kokoro-82M voices)
VOICES = {
    "NARRATOR": ("af_bella", 1.0),
    "NIA": ("af_heart", 1.0),
    "KITO": ("am_puck", 1.05),
    "LEX": ("bm_george", 0.95),
    "CARGO": ("am_fenrir", 0.98),
    "AUDITOR": ("bf_emma", 0.95),
    "HANS": ("am_michael", 0.98),
    "AMARA": ("bf_isabella", 0.97),
}

DISPLAY_NAMES = {
    "NARRATOR": "Narrator",
    "NIA": "Nia",
    "KITO": "Kito",
    "LEX": "Professor Lex",
    "CARGO": "Captain Cargo",
    "AUDITOR": "The Auditor",
    "HANS": "Hans",
    "AMARA": "Amara",
}

SERIES = "THE LAW BEHIND THE DEAL"
