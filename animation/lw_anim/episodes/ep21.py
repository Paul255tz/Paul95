"""Episode 21 - The Boardroom.

Syllabus F1(a)-(c): the role of directors; executive and non-executive, de jure,
de facto and shadow directors; appointment, vacation of office, removal and
disqualification (Company Directors Disqualification Act 1986); the powers of
the board, the managing director and individual directors to bind the company.
UK Companies Act 2006 model. Setting: Safari Solar Limited's first board
meeting; Amara joins as a non-executive director nominated by the bank.
"""
from ._kit import (DISPLAY_NAMES, SERIES, VOICES, Line, Pause, Scene, Sfx,  # noqa: F401
                   quiz_scene, recap_scene, title_scene)

EPISODE = "Episode 21"
EPISODE_TITLE = "The Boardroom"
SLUG = "episode21_the_boardroom"

SCENES = [
    title_scene(21, EPISODE_TITLE, "Syllabus F1(a)–(c)", ("people", "gavel")),

    Scene("s1", "The first board meeting", "", [
        Pause("open", 1.0),
        Line("kito1", "KITO", "Welcome to Safari Solar's first board meeting! I'm managing "
             "director, Nia is finance director, and Amara joins us from the bank.", gap=0.4),
        Line("amara1", "AMARA", "As a non-executive director. I'm here to challenge, not to "
             "run the factory.", gap=0.4),
        Line("lex1", "LEX", "Directors manage the company's business, collectively, as a "
             "board. They act as the company's agents, and the articles give them their "
             "powers."),
        Pause("hold", 1.2),
    ], spec={"tpl": "talk", "bg": "boardroom", "syl": "F1(a)",
             "cast": [{"who": "KITO", "x": 960, "y": 1000, "s": 0.88, "talk_pose": "present",
                       "mood": "happy"},
                      {"who": "NIA", "x": 640, "y": 1000, "s": 0.85},
                      {"who": "AMARA", "x": 1300, "y": 1000, "s": 0.85},
                      {"who": "LEX", "x": 230, "y": 1040, "s": 0.85, "enter": "lex1",
                       "from": "left"}]}),

    Scene("s2", "Kinds of director", "", [
        Pause("open", 1.0),
        Line("lex2a", "LEX", "A director is anyone occupying the position of director, "
             "whatever they're called.", gap=0.3),
        Sfx("pop"),
        Line("lex2b", "LEX", "Executive directors work in the business, usually under "
             "service contracts, like Kito and Nia.", gap=0.25),
        Sfx("pop"),
        Line("lex2c", "LEX", "Non-executive directors bring independent judgement, "
             "monitor the executives, and are central to good corporate governance.",
             gap=0.25),
        Sfx("pop"),
        Line("lex2d", "LEX", "A de jure director is validly appointed.", gap=0.25),
        Sfx("pop"),
        Line("lex2e", "LEX", "A de facto director acts as a director without a valid "
             "appointment, and is treated as one.", gap=0.25),
        Sfx("pop"),
        Line("lex2f", "LEX", "A shadow director is someone whose instructions the directors "
             "are accustomed to follow. Professional advice alone doesn't count.", gap=0.25),
        Sfx("pop"),
        Line("lex2g", "LEX", "And an alternate director stands in for a director who can't "
             "attend, if the articles allow.", gap=0.4),
        Line("nia2", "NIA", "So a hidden boss pulling the strings can still owe directors' "
             "duties."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "white", "layout": "grid", "cols": 3,
             "heading": "Types of director", "syl": "F1(a)", "cell_h": 290, "ts": 34,
             "items": [{"at": "lex2b", "text": "Executive", "sub": "Works in the business",
                        "icon": "laptop", "color": "#0f8b8d"},
                       {"at": "lex2c", "text": "Non-executive", "sub": "Independent challenge",
                        "icon": "eye", "color": "#7768ae"},
                       {"at": "lex2d", "text": "De jure", "sub": "Validly appointed",
                        "icon": "seal", "color": "#3bb273"},
                       {"at": "lex2e", "text": "De facto", "sub": "Acts as one, no valid "
                                                                  "appointment",
                        "icon": "person", "color": "#f2a541"},
                       {"at": "lex2f", "text": "Shadow", "sub": "Board accustomed to obey "
                                                                "them",
                        "icon": "mask", "color": "#e4572e"},
                       {"at": "lex2g", "text": "Alternate", "sub": "Stands in, if articles "
                                                                   "allow",
                        "icon": "people", "color": "#2b86c5"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia2"}]}),

    Scene("s3", "Appointment", "", [
        Pause("open", 1.0),
        Line("lex3a", "LEX", "A private company needs at least one director, and a public "
             "company at least two. At least one must be a real person, aged at least "
             "sixteen.", gap=0.3),
        Line("lex3b", "LEX", "The first directors are named in the registration documents. "
             "After that, the articles decide. Under the model articles, directors are "
             "appointed by ordinary resolution, or by the board.", gap=0.3),
        Line("lex3c", "LEX", "In a public company, each appointment at a general meeting "
             "needs its own resolution, unless members unanimously agree otherwise. Many "
             "listed companies put every director up for re-election each year.", gap=0.3),
        Line("lex3d", "LEX", "The registrar must be told within fourteen days. And in the "
             "UK, directors must now verify their identity with Companies House.", gap=0.4),
        Line("amara3", "AMARA", "And under our loan agreement, the bank may nominate one "
             "director."),
        Pause("hold", 1.4),
    ], spec={"tpl": "timeline", "bg": "studio", "heading": "Becoming a director",
             "syl": "F1(b)", "cw": 300,
             "events": [{"at": "lex3a", "label": "Eligibility", "sub": "1 (private) or 2 "
                                                                      "(plc) · a person, "
                                                                      "16+",
                         "icon": "person", "color": "#0f8b8d"},
                        {"at": "lex3b", "label": "Appointed", "sub": "Ordinary resolution or "
                                                                     "by the board",
                         "icon": "ballot", "color": "#7768ae"},
                        {"at": "lex3c", "label": "plc rules", "sub": "Separate resolutions · "
                                                                    "often annual election",
                         "icon": "company", "color": "#f2a541"},
                        {"at": "lex3d", "label": "Tell the registrar", "sub": "14 days · "
                                                                              "identity "
                                                                              "verified",
                         "icon": "envelope", "color": "#3bb273"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "AMARA", "x": 1810, "s": 0.55, "y": 1120, "enter": "amara3"}]}),

    Scene("s4", "Leaving, and being removed", "", [
        Pause("open", 1.0),
        Line("lex4a", "LEX", "A director leaves office by resigning, by retiring, on death, "
             "on disqualification or bankruptcy, on medical grounds under the articles, or "
             "by removal.", gap=0.4),
        Line("lex4b", "LEX", "Members can always remove a director by ordinary resolution, "
             "whatever the articles or any contract say.", gap=0.3),
        Sfx("pop"),
        Line("lex4c", "LEX", "Special notice of the resolution must reach the company at "
             "least twenty-eight days before the meeting.", gap=0.25),
        Sfx("pop"),
        Line("lex4d", "LEX", "The company tells the members, usually with twenty-one days' "
             "notice.", gap=0.25),
        Sfx("pop"),
        Line("lex4e", "LEX", "The director may circulate written representations, and speak "
             "at the meeting.", gap=0.25),
        Sfx("pop"),
        Line("lex4f", "LEX", "And it must be a meeting. A written resolution cannot remove a "
             "director.", gap=0.4),
        Line("lex4g", "LEX", "A removed director may still claim compensation for breach of "
             "a service contract, as in Southern Foundries against Shirlaw."),
        Pause("hold", 1.4),
    ], spec={"tpl": "timeline", "bg": "studio_red", "heading": "Removing a director",
             "syl": "F1(b)", "cw": 300,
             "events": [{"at": "lex4c", "label": "Special notice", "sub": "28 days to the "
                                                                         "company",
                         "icon": "envelope", "color": "#e4572e"},
                        {"at": "lex4d", "label": "Notice to members", "sub": "Usually 21 "
                                                                            "days",
                         "icon": "megaphone", "color": "#f2a541"},
                        {"at": "lex4e", "label": "Director's say", "sub": "Written reps · "
                                                                         "speak",
                         "icon": "mic", "color": "#7768ae"},
                        {"at": "lex4f", "label": "Ordinary resolution", "sub": "At a meeting, "
                                                                              "never written",
                         "icon": "ballot", "color": "#0f8b8d"}],
             "cast": [{"who": "LEX", "x": 250}],
             "pops": [{"kind": "chip", "at": "lex4g", "x": 1200, "y": 980,
                       "text": "Southern Foundries v Shirlaw (1940): damages for breach",
                       "color": "#1f3a5f", "size": 30}]}),

    Scene("s5", "Weighted votes", "", [
        Pause("open", 1.0),
        Line("kito5", "KITO", "So the shareholders could fire me anytime?", gap=0.3),
        Line("lex5a", "LEX", "In principle. But look at Bushell against Faith.", gap=0.3),
        Line("lex5b", "LEX", "Three siblings held a hundred shares each. The articles said "
             "that on a resolution to remove a director, that director's shares carried "
             "three votes each.", gap=0.3),
        Line("lex5c", "LEX", "When the other two tried to remove their brother, he had three "
             "hundred votes against their two hundred. The House of Lords upheld the "
             "clause.", gap=0.4),
        Sfx("sparkle"),
        Pause("stamp", 1.2),
        Line("lex5d", "LEX", "So in small private companies, weighted voting rights can "
             "protect a director from removal."),
        Pause("hold", 1.4),
    ], spec={"tpl": "case", "bg": "boardroom", "name": "Bushell v Faith",
             "year": "House of Lords · 1970", "syl": "F1(b)",
             "rows": [{"at": "lex5b", "label": "Facts", "text": "Articles: director's shares "
                                                                "get 3 votes each on his "
                                                                "removal",
                       "color": "#7768ae"},
                      {"at": "lex5c", "label": "Held", "text": "Valid: 300 votes beat 200",
                       "color": "#3bb273"},
                      {"at": "lex5d", "label": "Point", "text": "Weighted voting can block "
                                                                "removal",
                       "color": "#0f8b8d"}],
             "stamp": {"at": "stamp", "text": "WEIGHTED VOTES OK", "color": "#3bb273"},
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "KITO", "x": 1810, "s": 0.55, "y": 1120}]}),

    Scene("s6", "Disqualification", "", [
        Pause("open", 1.0),
        Line("lex6a", "LEX", "Under the Company Directors Disqualification Act, a court can "
             "ban unfit people from acting as directors.", gap=0.3),
        Sfx("pop"),
        Line("lex6b", "LEX", "After a conviction for a serious offence connected with a "
             "company: up to fifteen years.", gap=0.25),
        Sfx("pop"),
        Line("lex6c", "LEX", "For persistent breaches of filing rules, three defaults in "
             "five years: up to five years.", gap=0.25),
        Sfx("pop"),
        Line("lex6d", "LEX", "For fraud in a winding up, or fraudulent or wrongful trading: "
             "up to fifteen years.", gap=0.25),
        Sfx("pop"),
        Line("lex6e", "LEX", "And for unfit conduct as a director of an insolvent company, a "
             "court must disqualify, for at least two years and up to fifteen.", gap=0.4),
        Line("lex6f", "LEX", "A disqualified person cannot act as a director, or take part in "
             "managing a company, without the court's permission. Breach is a crime, with "
             "personal liability for the company's debts."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "heading": "CDDA 1986: grounds and bans",
             "syl": "F1(b)", "row": 125, "ts": 38,
             "items": [{"at": "lex6b", "text": "Serious company offence", "sub": "Up to 15 "
                                                                                 "years",
                        "icon": "handcuffs", "color": "#e4572e"},
                       {"at": "lex6c", "text": "Persistent filing defaults",
                        "sub": "3 in 5 years · up to 5 years", "icon": "calendar",
                        "color": "#f2a541"},
                       {"at": "lex6d", "text": "Fraud, fraudulent or wrongful trading",
                        "sub": "Up to 15 years", "icon": "mask", "color": "#7768ae"},
                       {"at": "lex6e", "text": "Unfit director of insolvent company",
                        "sub": "Mandatory: 2 to 15 years", "icon": "warning",
                        "color": "#0f8b8d"}],
             "cast": [{"who": "LEX", "x": 250}],
             "pops": [{"kind": "chip", "at": "lex6f", "x": 1190, "y": 950,
                       "text": "Breach: a crime + personal liability for debts",
                       "color": "#e4572e", "size": 32}]}),

    Scene("s7", "Who can bind the company?", "", [
        Pause("open", 1.0),
        Line("lex7a", "LEX", "The articles give management power to the board, acting "
             "collectively. Members can only direct them by special resolution.", gap=0.3),
        Line("lex7b", "LEX", "The board can delegate to committees, or to a managing "
             "director, who has authority to make the usual management contracts.",
             gap=0.3),
        Line("lex7c", "LEX", "An individual director has no authority alone, unless it is "
             "delegated, or the company lets them appear to have it, as in Freeman and "
             "Lockyer.", gap=0.4),
        Line("lex7d", "LEX", "Outsiders get extra protection. For a third party dealing in "
             "good faith, the directors' power to bind the company is free of limits in the "
             "constitution.", gap=0.3),
        Line("lex7e", "LEX", "And under the rule in Turquand's case, an outsider may assume "
             "the company's internal procedures were followed."),
        Pause("hold", 1.4),
    ], spec={"tpl": "flow", "bg": "studio_teal", "heading": "Powers to bind the company",
             "syl": "F1(c)",
             "nodes": [{"id": "m", "x": 760, "y": 250, "label": "Members",
                        "icon": "people", "color": "#7768ae", "at": "lex7a", "w": 260},
                       {"id": "b", "x": 1150, "y": 470, "label": "Board (collective)",
                        "icon": "company", "color": "#0f8b8d", "at": ["lex7a", 0.5], "w": 300},
                       {"id": "md", "x": 760, "y": 760, "label": "Managing director",
                        "icon": "key", "color": "#f2a541", "at": "lex7b", "w": 270},
                       {"id": "d", "x": 1150, "y": 840, "label": "Individual director",
                        "icon": "person", "color": "#5b6670", "at": "lex7c", "w": 270},
                       {"id": "t", "x": 1620, "y": 470, "label": "Third party (good faith)",
                        "icon": "handshake", "color": "#3bb273", "at": "lex7d", "w": 300}],
             "edges": [{"from": "m", "to": "b", "at": ["lex7a", 3.0], "label": "special "
                                                                              "resolution",
                        "dashed": True},
                       {"from": "b", "to": "md", "at": "lex7b", "label": "delegates"},
                       {"from": "b", "to": "d", "at": "lex7c", "label": "only if delegated",
                        "dashed": True},
                       {"from": "b", "to": "t", "at": "lex7d", "label": "binds",
                        "color": "#3bb273"}],
             "cast": [{"who": "LEX", "x": 250}],
             "pops": [{"kind": "chip", "at": "lex7e", "x": 1620, "y": 720,
                       "text": "Turquand (1856): indoor management rule",
                       "color": "#1f3a5f", "size": 30}]}),

    quiz_scene("s8", "Quick check",
               "Members want to remove a director. Which statement is correct?",
               ["They need a special resolution", "They can use a written resolution",
                "An ordinary resolution with special notice, at a meeting",
                "Only the court can remove a director"], 2,
               "Quick check. Members want to remove a director. Which statement is correct?",
               "An ordinary resolution, with special notice, at a meeting.",
               syl="F1(b)"),

    quiz_scene("s9", "Quick check",
               "Someone is not appointed, but the board habitually follows their "
               "instructions. They are…",
               ["A shadow director", "An alternate director", "A non-executive director",
                "A company secretary"], 0,
               "And someone not appointed, whose instructions the board habitually follows, "
               "is called what?",
               "A shadow director.",
               think=4.0, syl="F1(a)"),

    recap_scene("s10", [
        ("Executive, non-executive, de facto, shadow.", "Exec · NED · de facto · shadow"),
        ("Appointed under the articles; registrar told.", "Appointment"),
        ("Removed by ordinary resolution with special notice.", "Removal: OR + special "
                                                                "notice"),
        ("Disqualification: up to fifteen years.", "CDDA: up to 15 years"),
        ("Board, MD, and apparent authority.", "Board · MD · apparent authority"),
    ], [
        Line("lex10", "LEX", "Next time, the heart of it all: the duties every director owes "
             "the company.", gap=0.3),
        Line("amara10", "AMARA", "The part the bank cares about most.", gap=0.6),
    ], next_ep=22, next_title="Directors' Duties", next_icon="shield"),
]
