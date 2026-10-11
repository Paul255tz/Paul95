"""Episode 26 - Administration: The Rescue.

Syllabus G1(d)-(e): administration as an alternative to liquidation; how an
administrator is appointed; the effects of appointment; and the administrator's
powers and duties (UK Insolvency Act 1986, Schedule B1 model). Kenya's
Insolvency Act 2015 also provides for administration. Setting: Amara's bank
holds a floating charge over Kilimanjaro Retail and considers a rescue.
"""
from ._kit import (DISPLAY_NAMES, SERIES, VOICES, Line, Pause, Scene, Sfx,  # noqa: F401
                   quiz_scene, recap_scene, title_scene)

EPISODE = "Episode 26"
EPISODE_TITLE = "Administration: The Rescue"
SLUG = "episode26_administration_the_rescue"

SCENES = [
    title_scene(26, EPISODE_TITLE, "Syllabus G1(d)–(e)", ("umbrella", "company")),

    Scene("s1", "A rescue instead?", "", [
        Pause("open", 1.0),
        Line("amara1", "AMARA", "Kito, wait before you petition. Our bank lends to "
             "Kilimanjaro Retail too. Its shops are good. It just has too much debt.",
             gap=0.4),
        Line("kito1", "KITO", "So what, you'd rather save it?", gap=0.4),
        Line("amara1b", "AMARA", "If we can. We hold a floating charge over the whole "
             "business, so we can appoint an administrator.", gap=0.4),
        Line("lex1", "LEX", "Administration is the rescue route. It gives a struggling "
             "company breathing space, under an insolvency practitioner's control."),
        Pause("hold", 1.2),
    ], spec={"tpl": "talk", "bg": "bank", "syl": "G1(d)",
             "cast": [{"who": "AMARA", "x": 1450, "y": 1040, "s": 0.92},
                      {"who": "KITO", "x": 960, "y": 1040, "s": 0.92, "mood": "thinking"},
                      {"who": "LEX", "x": 420, "y": 1040, "s": 0.88, "enter": "lex1",
                       "from": "left"}],
             "pops": [{"kind": "icon", "icon": "umbrella", "x": 1200, "y": 280, "s": 1.2,
                       "at": "lex1", "color": "#3bb273", "float": True,
                       "label": "Breathing space"}]}),

    Scene("s2", "The purpose of administration", "", [
        Pause("open", 1.0),
        Line("lex2a", "LEX", "An administrator must pursue one objective, in a strict "
             "order.", gap=0.3),
        Sfx("pop"),
        Line("lex2b", "LEX", "First: rescue the company as a going concern.", gap=0.25),
        Sfx("pop"),
        Line("lex2c", "LEX", "If that's not reasonably practicable: achieve a better result "
             "for the creditors as a whole than an immediate winding up would.", gap=0.25),
        Sfx("pop"),
        Line("lex2d", "LEX", "And only if neither is practicable: realise property to pay "
             "the secured or preferential creditors, without unnecessarily harming the "
             "creditors as a whole.", gap=0.4),
        Line("nia2", "NIA", "So the company itself comes first. Selling it off is the last "
             "resort."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "heading": "Purpose: a strict hierarchy",
             "syl": "G1(d)", "row": 160, "ts": 42,
             "items": [{"at": "lex2b", "text": "Rescue the company", "sub": "As a going "
                                                                            "concern",
                        "icon": "umbrella", "color": "#3bb273"},
                       {"at": "lex2c", "text": "Better result for creditors",
                        "sub": "Than an immediate winding up", "icon": "chart",
                        "color": "#f2a541"},
                       {"at": "lex2d", "text": "Realise property", "sub": "For secured or "
                                                                          "preferential "
                                                                          "creditors",
                        "icon": "moneybag", "color": "#e4572e"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia2"}]}),

    Scene("s3", "Three ways to appoint", "", [
        Pause("open", 1.0),
        Line("lex3a", "LEX", "An administrator can be appointed in three ways.", gap=0.3),
        Line("lex3b", "LEX", "By court order, on application by the company, its directors, "
             "or creditors. The court must be satisfied the company is, or is likely to "
             "become, unable to pay its debts, and that administration is reasonably likely "
             "to achieve its purpose.", gap=0.3),
        Line("lex3c", "LEX", "Out of court, by a qualifying floating charge holder, a lender "
             "with a floating charge over the whole, or substantially the whole, of the "
             "company's property. Like Amara's bank.", gap=0.3),
        Line("lex3d", "LEX", "Or out of court, by the company or its directors. They must "
             "give the floating charge holder notice, so it can appoint its own choice "
             "instead.", gap=0.4),
        Line("amara3", "AMARA", "Which is why banks like that floating charge. It gives us "
             "control of who runs the rescue."),
        Pause("hold", 1.4),
    ], spec={"tpl": "flow", "bg": "studio_teal", "heading": "Appointing an administrator",
             "syl": "G1(e)",
             "nodes": [{"id": "adm", "x": 1150, "y": 760, "label": "Administrator "
                                                                  "(insolvency "
                                                                  "practitioner)",
                        "icon": "person", "color": "#1f3a5f", "at": "lex3a", "w": 380,
                        "h": 200},
                       {"id": "court", "x": 680, "y": 300, "label": "Court order",
                        "icon": "court", "color": "#7768ae", "at": "lex3b", "w": 260},
                       {"id": "qfch", "x": 1150, "y": 300, "label": "Floating charge holder",
                        "icon": "bank", "color": "#0f8b8d", "at": "lex3c", "w": 300},
                       {"id": "dirs", "x": 1620, "y": 300, "label": "Company or directors",
                        "icon": "people", "color": "#f2a541", "at": "lex3d", "w": 290}],
             "edges": [{"from": "court", "to": "adm", "at": ["lex3b", 0.6],
                        "label": "insolvent + likely to work"},
                       {"from": "qfch", "to": "adm", "at": ["lex3c", 0.6],
                        "label": "out of court"},
                       {"from": "dirs", "to": "adm", "at": ["lex3d", 0.6],
                        "label": "notice to charge holder"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "AMARA", "x": 1810, "s": 0.55, "y": 1120, "enter": "amara3"}]}),

    Scene("s4", "The moratorium", "", [
        Pause("open", 1.0),
        Line("lex4a", "LEX", "Appointment brings a moratorium, a legal shield around the "
             "company.", gap=0.3),
        Sfx("pop"),
        Line("lex4b", "LEX", "No winding-up order or resolution can be made, and pending "
             "petitions are dismissed or suspended.", gap=0.2),
        Sfx("pop"),
        Line("lex4c", "LEX", "No security can be enforced, and no goods repossessed, "
             "without the administrator's consent or the court's permission.", gap=0.2),
        Sfx("pop"),
        Line("lex4d", "LEX", "Legal proceedings against the company are frozen on the same "
             "basis.", gap=0.2),
        Sfx("pop"),
        Line("lex4e", "LEX", "Any administrative receiver must leave office.", gap=0.2),
        Sfx("pop"),
        Line("lex4f", "LEX", "And the directors stay in office, but can only use their "
             "management powers with the administrator's consent.", gap=0.4),
        Line("kito4", "KITO", "So I can't petition, or sue Kilimanjaro, while the "
             "administrator works. I'll wait."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "white", "heading": "Effects of appointment",
             "syl": "G1(e)", "row": 116, "ts": 38,
             "items": [{"at": "lex4b", "text": "No winding up", "sub": "Petitions dismissed "
                                                                      "or suspended",
                        "icon": "cross", "color": "#e4572e"},
                       {"at": "lex4c", "text": "No enforcing security or repossessing",
                        "icon": "lock", "color": "#7768ae"},
                       {"at": "lex4d", "text": "Legal proceedings frozen", "icon": "shield",
                        "color": "#2b86c5"},
                       {"at": "lex4e", "text": "Administrative receiver leaves",
                        "icon": "door", "color": "#f2a541"},
                       {"at": "lex4f", "text": "Directors need the administrator's consent",
                        "icon": "people", "color": "#0f8b8d"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "KITO", "x": 1810, "s": 0.55, "y": 1120, "enter": "kito4"}]}),

    Scene("s5", "The administrator at work", "", [
        Pause("open", 1.0),
        Line("lex5a", "LEX", "The administrator is an officer of the court, and acts as "
             "the company's agent. They must act in the interests of the creditors as a "
             "whole, as quickly and efficiently as reasonably practicable.", gap=0.3),
        Line("lex5b", "LEX", "First, notify the company, the creditors and the registrar, "
             "and get a statement of affairs from the directors.", gap=0.25),
        Line("lex5c", "LEX", "Within eight weeks, send proposals to the creditors, who "
             "decide whether to approve them.", gap=0.25),
        Line("lex5d", "LEX", "Then manage the business in line with the proposals. The "
             "administrator can sell assets, appoint or remove directors, pay creditors, and "
             "challenge earlier transactions.", gap=0.25),
        Line("lex5e", "LEX", "Administration ends automatically after one year, unless "
             "extended by the creditors or the court. Or earlier, when its purpose is "
             "achieved, often moving into a liquidation or a creditors' arrangement.",
             gap=0.4),
        Line("amara5", "AMARA", "And Kilimanjaro's shops kept trading the whole time."),
        Pause("hold", 1.4),
    ], spec={"tpl": "timeline", "bg": "studio", "heading": "Administration timeline",
             "syl": "G1(e)", "cw": 290,
             "events": [{"at": "lex5a", "label": "Appointed", "sub": "Officer of the court · "
                                                                    "company's agent",
                         "icon": "person", "color": "#1f3a5f"},
                        {"at": "lex5b", "label": "Notify + statement", "sub": "Creditors, "
                                                                             "registrar · "
                                                                             "directors' "
                                                                             "statement",
                         "icon": "envelope", "color": "#0f8b8d"},
                        {"at": "lex5c", "label": "Proposals", "sub": "Within 8 weeks · "
                                                                     "creditors decide",
                         "icon": "doc", "color": "#7768ae"},
                        {"at": "lex5d", "label": "Manage", "sub": "Sell, appoint, pay, "
                                                                  "challenge",
                         "icon": "key", "color": "#f2a541"},
                        {"at": "lex5e", "label": "Ends", "sub": "After 1 year unless "
                                                                "extended",
                         "icon": "hourglass", "color": "#e4572e"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "AMARA", "x": 1810, "s": 0.55, "y": 1120, "enter": "amara5"}]}),

    Scene("s6", "Why choose administration?", "", [
        Pause("open", 1.0),
        Line("lex6a", "LEX", "Compared with liquidation, administration has real "
             "advantages.", gap=0.3),
        Line("lex6b", "LEX", "The company may survive. Creditors are held back, giving time "
             "to plan. Creditors often recover more, and keep a customer. Members may keep "
             "shares in a viable company. And jobs can be saved.", gap=0.4),
        Line("lex6c", "LEX", "Liquidation is final. The company is broken up, its staff "
             "dismissed, and it is dissolved.", gap=0.4),
        Line("nia6", "NIA", "Kenya's Insolvency Act of 2015 introduced administration too, "
             "for the same reasons."),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio_purple", "heading": "Administration vs "
                                                                 "liquidation",
             "syl": "G1(d)", "ts": 33,
             "cols": [{"title": "Administration", "icon": "umbrella", "color": "#3bb273",
                       "at": "lex6b",
                       "items": [{"at": ["lex6b", 0.5], "text": "Company may survive",
                                  "good": True},
                                 {"at": ["lex6b", 2.5], "text": "Moratorium: time to plan",
                                  "good": True},
                                 {"at": ["lex6b", 5.5], "text": "Often better returns",
                                  "good": True},
                                 {"at": ["lex6b", 10.0], "text": "Jobs can be saved",
                                  "good": True}]},
                      {"title": "Liquidation", "icon": "fire", "color": "#e4572e",
                       "at": "lex6c",
                       "items": [{"at": ["lex6c", 0.5], "text": "Final", "bad": True},
                                 {"at": ["lex6c", 2.0], "text": "Business broken up",
                                  "bad": True},
                                 {"at": ["lex6c", 3.5], "text": "Staff dismissed",
                                  "bad": True},
                                 {"at": ["lex6c", 4.5], "text": "Company dissolved",
                                  "bad": True}]}],
             "vs": True,
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia6"}]}),

    quiz_scene("s7", "Quick check",
               "What is the FIRST objective an administrator must pursue?",
               ["Pay the floating charge holder", "Rescue the company as a going concern",
                "Sell the assets quickly", "Pay the shareholders"], 1,
               "Quick check. What is the first objective an administrator must pursue?",
               "Rescue the company as a going concern.",
               syl="G1(d)"),

    quiz_scene("s8", "Quick check",
               "During administration, a supplier wants to repossess goods under a retention "
               "of title clause. What does it need?",
               ["Nothing; it can just take them", "The administrator's consent or the "
                "court's permission", "A special resolution of members",
                "The registrar's approval"], 1,
               "And during administration, what does a supplier need to repossess its goods?",
               "The administrator's consent, or the court's permission.",
               think=4.0, syl="G1(e)"),

    recap_scene("s9", [
        ("Rescue first, then better result, then realise.", "Purpose hierarchy"),
        ("Court, charge holder, or directors appoint.", "3 appointment routes"),
        ("Moratorium freezes creditors.", "Moratorium"),
        ("Proposals within eight weeks.", "Proposals: 8 weeks"),
        ("Ends after one year unless extended.", "Ends: 1 year"),
    ], [
        Line("lex9", "LEX", "We've reached the final section: corporate crime. Next time, "
             "insider dealing, and market abuse.", gap=0.3),
        Line("aud9", "AUDITOR", "My favourite topic. Watch closely.", gap=0.6),
    ], next_ep=27, next_title="Insiders and Market Abuse", next_icon="eye"),
]
