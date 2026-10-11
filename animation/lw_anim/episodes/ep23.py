"""Episode 23 - Secretary and Auditor.

Syllabus F2(a)-(b): appointment, duties and powers of the company secretary;
appointment, duties and rights of the auditor, and the auditor's removal or
resignation. UK Companies Act 2006 model, with an East African comparison.
Setting: Safari Solar Limited grows, and the Auditor takes centre stage.
"""
from ._kit import (DISPLAY_NAMES, SERIES, VOICES, Line, Pause, Scene, Sfx,  # noqa: F401
                   quiz_scene, recap_scene, title_scene)

EPISODE = "Episode 23"
EPISODE_TITLE = "Secretary and Auditor"
SLUG = "episode23_secretary_and_auditor"

SCENES = [
    title_scene(23, EPISODE_TITLE, "Syllabus F2", ("magnifier", "doc")),

    Scene("s1", "Two more officers", "", [
        Pause("open", 1.0),
        Line("kito1", "KITO", "Safari Solar is booming. Do we need a company secretary? And "
             "an auditor?", gap=0.4),
        Sfx("whoosh"),
        Line("aud1", "AUDITOR", "Allow me to introduce myself properly. I'm an auditor. And "
             "today, you'll learn exactly what I can, and must, do.", gap=0.4),
        Line("lex1", "LEX", "Let's start with the secretary, the company's chief "
             "administrative officer."),
        Pause("hold", 1.2),
    ], spec={"tpl": "talk", "bg": "office", "syl": "F2",
             "cast": [{"who": "KITO", "x": 960, "y": 1030, "s": 0.92, "mood": "thinking"},
                      {"who": "AUDITOR", "x": 1450, "y": 1030, "s": 0.92, "enter": "aud1",
                       "pose": "clipboard", "talk_pose": "present"},
                      {"who": "LEX", "x": 420, "y": 1030, "s": 0.88, "enter": "lex1",
                       "from": "left"}]}),

    Scene("s2", "Does a company need a secretary?", "", [
        Pause("open", 1.0),
        Line("lex2a", "LEX", "In the UK, a private company does not need a secretary, "
             "unless its articles require one. The directors then handle the paperwork.",
             gap=0.3),
        Line("lex2b", "LEX", "A public company must have one, appointed by the directors, "
             "who must make sure the secretary is suitably qualified.", gap=0.3),
        Line("lex2c", "LEX", "For example, a member of a recognised body like ACCA, a lawyer, "
             "someone who was a public company secretary for three of the last five years, "
             "or someone the directors judge capable.",
             say="For example, a member of a recognised body like A.C.C.A., a lawyer, "
                 "someone who was a public company secretary for three of the last five "
                 "years, or someone the directors judge capable.", gap=0.4),
        Line("nia2", "NIA", "East Africa is stricter. In Tanzania, every company must have a "
             "secretary, and in Kenya, larger private companies must too."),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio", "heading": "The company secretary",
             "syl": "F2(a)", "ts": 33,
             "cols": [{"title": "Private company", "icon": "house", "color": "#0f8b8d",
                       "at": "lex2a",
                       "items": [{"at": ["lex2a", 0.5], "text": "Optional (UK)"},
                                 {"at": ["lex2a", 4.0], "text": "Unless the articles "
                                                               "require one"},
                                 {"at": "nia2", "text": "Tanzania: every company · Kenya: "
                                                        "larger companies"}]},
                      {"title": "Public company", "icon": "company", "color": "#7768ae",
                       "at": "lex2b",
                       "items": [{"at": ["lex2b", 0.5], "text": "Must have one"},
                                 {"at": ["lex2b", 2.0], "text": "Appointed by the directors"},
                                 {"at": "lex2c", "text": "Qualified: ACCA, lawyer, 3 of 5 "
                                                         "years, or capable"}]}],
             "vs": True,
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia2"}]}),

    Scene("s3", "What the secretary does", "", [
        Pause("open", 1.0),
        Line("lex3a", "LEX", "The directors decide the secretary's duties, but they are "
             "mainly administrative.", gap=0.3),
        Sfx("pop"),
        Line("lex3b", "LEX", "Keeping the statutory registers and records.", gap=0.2),
        Sfx("pop"),
        Line("lex3c", "LEX", "Filing documents with the registrar, like the confirmation "
             "statement, accounts and charges.", gap=0.2),
        Sfx("pop"),
        Line("lex3d", "LEX", "Organising meetings, sending notices, and taking minutes.",
             gap=0.2),
        Sfx("pop"),
        Line("lex3e", "LEX", "And advising the board on governance and compliance, "
             "including inducting new non-executive directors.", gap=0.4),
        Line("lex3f", "LEX", "A secretary has apparent authority for administrative "
             "contracts. In Panorama Developments against Fidelis Furnishing Fabrics, a "
             "secretary hired cars, claiming they were for company business, then used them "
             "himself. The company still had to pay.", gap=0.3),
        Line("aud3", "AUDITOR", "But not authority for big commercial deals, like buying a "
             "factory."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "heading": "Secretary's role",
             "syl": "F2(a)", "row": 120, "ts": 40,
             "items": [{"at": "lex3b", "text": "Statutory registers and records",
                        "icon": "book", "color": "#0f8b8d"},
                       {"at": "lex3c", "text": "Filings with the registrar",
                        "icon": "envelope", "color": "#2b86c5"},
                       {"at": "lex3d", "text": "Meetings, notices, minutes", "icon": "mic",
                        "color": "#7768ae"},
                       {"at": "lex3e", "text": "Governance advice · NED induction",
                        "icon": "bulb", "color": "#f2a541"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "AUDITOR", "x": 1810, "s": 0.55, "y": 1120, "enter": "aud3",
                       "pose": "clipboard"}],
             "pops": [{"kind": "card", "at": "lex3f", "until": "aud3", "x": 1190, "y": 470,
                       "w": 960, "h": 300, "title": "Panorama v Fidelis (1971)",
                       "body": "Secretary has apparent authority for administrative "
                               "contracts, like hiring cars", "color": "#1f3a5f",
                       "dim": True, "bs": 36}]}),

    Scene("s4", "Appointing an auditor", "", [
        Pause("open", 1.0),
        Line("aud4a", "AUDITOR", "Every company must have its accounts audited, unless it is "
             "exempt, for example as a small or dormant company.", gap=0.3),
        Sfx("pop"),
        Line("aud4b", "AUDITOR", "The directors appoint the first auditor, and fill casual "
             "vacancies.", gap=0.2),
        Sfx("pop"),
        Line("aud4c", "AUDITOR", "After that, the members appoint by ordinary resolution. "
             "For a public company, that is at the meeting where the accounts are laid. A "
             "private company's auditor is often deemed reappointed.", gap=0.2),
        Sfx("pop"),
        Line("aud4d", "AUDITOR", "If no one appoints an auditor, the Secretary of State can.",
             gap=0.4),
        Line("aud4e", "AUDITOR", "To be eligible, I must belong to a recognised supervisory "
             "body, like ACCA, and be independent. No officer or employee of the company, or "
             "their partner or employee, may audit it.",
             say="To be eligible, I must belong to a recognised supervisory body, like "
                 "A.C.C.A., and be independent. No officer or employee of the company, or "
                 "their partner or employee, may audit it."),
        Pause("hold", 1.4),
    ], spec={"tpl": "timeline", "bg": "studio_teal", "heading": "Appointing the auditor",
             "syl": "F2(b)", "cw": 300,
             "events": [{"at": "aud4a", "label": "Audit required", "sub": "Unless exempt "
                                                                         "(small, dormant)",
                         "icon": "magnifier", "color": "#0f8b8d"},
                        {"at": "aud4b", "label": "Directors", "sub": "First auditor · "
                                                                     "casual vacancy",
                         "icon": "people", "color": "#2b86c5"},
                        {"at": "aud4c", "label": "Members", "sub": "Ordinary resolution · "
                                                                   "private often deemed "
                                                                   "reappointed",
                         "icon": "ballot", "color": "#7768ae"},
                        {"at": "aud4d", "label": "Secretary of State", "sub": "If no one "
                                                                              "else does",
                         "icon": "parliament", "color": "#f2a541"}],
             "cast": [{"who": "AUDITOR", "x": 250, "pose": "clipboard",
                       "talk_pose": "present"}],
             "pops": [{"kind": "chip", "at": "aud4e", "x": 1200, "y": 980,
                       "text": "Eligible: recognised body member + independent",
                       "color": "#3bb273", "size": 32}]}),

    Scene("s5", "Rights and duties", "", [
        Pause("open", 1.0),
        Line("aud5a", "AUDITOR", "My rights let me do the job.", gap=0.25),
        Line("aud5b", "AUDITOR", "Access to the company's books and records at all times. "
             "Information and explanations from officers and staff. Misleading me is a "
             "crime.", gap=0.25),
        Line("aud5c", "AUDITOR", "Notice of, and attendance at, general meetings, and the "
             "right to be heard. And copies of proposed written resolutions.", gap=0.4),
        Line("aud5d", "AUDITOR", "My main duty is to report to the members on whether the "
             "accounts give a true and fair view, and are properly prepared.", gap=0.25),
        Line("aud5e", "AUDITOR", "I also report whether the directors' report is consistent "
             "with the accounts, and for quoted companies, on parts of the remuneration "
             "report.", gap=0.25),
        Line("aud5f", "AUDITOR", "And I report by exception if proper accounting records "
             "were not kept, or I didn't get the information I needed.", gap=0.4),
        Line("kito5", "KITO", "So you're not checking every lamp, just whether the accounts "
             "are true and fair."),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio_purple", "heading": "Auditor's rights and duties",
             "syl": "F2(b)", "ts": 32,
             "cols": [{"title": "Rights", "icon": "key", "color": "#0f8b8d", "at": "aud5a",
                       "items": [{"at": "aud5b", "text": "Access to books at all times"},
                                 {"at": ["aud5b", 3.5], "text": "Information and "
                                                               "explanations"},
                                 {"at": "aud5c", "text": "Notice of, attend and speak at "
                                                         "meetings"},
                                 {"at": ["aud5c", 4.5], "text": "Copies of written "
                                                               "resolutions"}]},
                      {"title": "Duties", "icon": "magnifier", "color": "#7768ae",
                       "at": "aud5d",
                       "items": [{"at": ["aud5d", 0.5], "text": "Report: true and fair "
                                                               "view?"},
                                 {"at": "aud5e", "text": "Directors' report consistent?"},
                                 {"at": ["aud5e", 4.0], "text": "Quoted: remuneration report"},
                                 {"at": "aud5f", "text": "By exception: records, "
                                                         "information"}]}],
             "vs": True,
             "cast": [{"who": "AUDITOR", "x": 250, "pose": "clipboard",
                       "talk_pose": "present"},
                      {"who": "KITO", "x": 1810, "s": 0.55, "y": 1120, "enter": "kito5"}]}),

    Scene("s6", "Who can sue the auditor?", "", [
        Pause("open", 1.0),
        Line("lex6a", "LEX", "An auditor's report is relied on by many people. But who can "
             "sue if it's negligent?", gap=0.3),
        Line("lex6b", "LEX", "In Caparo Industries against Dickman, an investor bought "
             "shares relying on audited accounts, then sued the auditors.", gap=0.3),
        Line("lex6c", "LEX", "The House of Lords held the auditors owed their duty to the "
             "company, and to the members as a body, to help them oversee the directors. "
             "Not to individual investors making investment decisions.", gap=0.4),
        Sfx("sparkle"),
        Pause("stamp", 1.2),
        Line("aud6", "AUDITOR", "Which is why I write my report to the members."),
        Pause("hold", 1.2),
    ], spec={"tpl": "case", "bg": "court", "name": "Caparo Industries plc v Dickman",
             "year": "House of Lords · 1990", "syl": "F2(b)",
             "rows": [{"at": "lex6b", "label": "Facts", "text": "Investor relied on audited "
                                                                "accounts to buy shares",
                       "color": "#7768ae"},
                      {"at": "lex6c", "label": "Held", "text": "Duty owed to the company and "
                                                               "members as a body only",
                       "color": "#e4572e"}],
             "stamp": {"at": "stamp", "text": "NO DUTY TO INVESTOR", "color": "#e4572e"},
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "AUDITOR", "x": 1810, "s": 0.55, "y": 1120, "enter": "aud6",
                       "pose": "clipboard"}]}),

    Scene("s7", "Removal and resignation", "", [
        Pause("open", 1.0),
        Line("aud7a", "AUDITOR", "Members can remove me at any time, by ordinary resolution "
             "with special notice, at a meeting. Not by written resolution.", gap=0.25),
        Line("aud7b", "AUDITOR", "I may send written representations to the members, and "
             "speak at the meeting. The company tells the registrar within fourteen days.",
             gap=0.4),
        Line("aud7c", "AUDITOR", "If I resign, I give written notice to the registered "
             "office.", gap=0.25),
        Line("aud7d", "AUDITOR", "And I must deposit a statement of the circumstances "
             "connected with my leaving, so creditors and members can see if something is "
             "wrong. I may even require the directors to call a meeting, to explain.",
             gap=0.4),
        Line("nia7", "NIA", "So an auditor can't be quietly pushed out, or quietly walk "
             "away."),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio", "heading": "When the auditor leaves",
             "syl": "F2(b)", "ts": 33,
             "cols": [{"title": "Removal", "icon": "door", "color": "#e4572e",
                       "at": "aud7a",
                       "items": [{"at": ["aud7a", 1.5], "text": "Ordinary resolution + "
                                                               "special notice"},
                                 {"at": ["aud7a", 5.5], "text": "At a meeting, never written"},
                                 {"at": "aud7b", "text": "Written reps · right to speak"},
                                 {"at": ["aud7b", 5.0], "text": "Registrar told in 14 days"}]},
                      {"title": "Resignation", "icon": "envelope", "color": "#7768ae",
                       "at": "aud7c",
                       "items": [{"at": ["aud7c", 0.5], "text": "Written notice to "
                                                               "registered office"},
                                 {"at": "aud7d", "text": "Statement of circumstances"},
                                 {"at": ["aud7d", 7.0], "text": "May requisition a meeting"}]}],
             "vs": True,
             "cast": [{"who": "AUDITOR", "x": 250, "pose": "clipboard",
                       "talk_pose": "present"},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia7"}]}),

    quiz_scene("s8", "Quick check",
               "Following Caparo v Dickman, to whom does a statutory auditor owe a duty of "
               "care for the audit report?",
               ["Any investor who reads it", "The company and the members as a body",
                "The company's bank", "The general public"], 1,
               "Quick check. Following Caparo against Dickman, to whom does an auditor owe a "
               "duty of care for the report?",
               "The company, and the members as a body.",
               syl="F2(b)"),

    quiz_scene("s9", "Quick check",
               "Which company must have a qualified company secretary under UK law?",
               ["Every private company", "Every public company",
                "Only companies with an auditor", "Only dormant companies"], 1,
               "And under UK law, which company must have a qualified secretary?",
               "Every public company.",
               think=4.0, syl="F2(a)"),

    recap_scene("s10", [
        ("Secretary: optional for private, required for public.", "Secretary: plc must"),
        ("Secretary has administrative authority.", "Panorama: admin authority"),
        ("Auditors appointed by directors, then members.", "Auditor appointment"),
        ("Rights: books, information, meetings.", "Auditor rights"),
        ("Caparo: duty to the members as a body.", "Caparo (1990)"),
    ], [
        Line("lex10", "LEX", "Next time, the members have their say: meetings, notices, "
             "votes, and resolutions.", gap=0.3),
        Line("kito10", "KITO", "I'll bring the snacks!", gap=0.6),
    ], next_ep=24, next_title="Meetings and Resolutions", next_icon="ballot"),
]
