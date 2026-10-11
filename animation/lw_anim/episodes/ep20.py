"""Episode 20 - Keeping the Capital.

Syllabus E3(a)-(b): the doctrine of capital maintenance and capital reduction,
and the rules on distributing dividends in private and public companies.
UK Companies Act 2006 model. Setting: Kito wants a big dividend after
Safari Solar's first year.
"""
from ._kit import (DISPLAY_NAMES, SERIES, VOICES, Line, Pause, Scene, Sfx,  # noqa: F401
                   quiz_scene, recap_scene, title_scene)

EPISODE = "Episode 20"
EPISODE_TITLE = "Keeping the Capital"
SLUG = "episode20_keeping_the_capital"

SCENES = [
    title_scene(20, EPISODE_TITLE, "Syllabus E3", ("shield", "coin")),

    Scene("s1", "A dividend from the loan?", "", [
        Pause("open", 1.0),
        Line("kito1", "KITO", "We have five hundred thousand dollars in the bank! Let's pay "
             "ourselves a big dividend.", gap=0.4),
        Sfx("whoosh"),
        Line("aud1", "AUDITOR", "Most of that is the bank's loan, and your share capital. "
             "Neither is profit.", gap=0.4),
        Line("lex1", "LEX", "This is capital maintenance. Creditors lend to a limited "
             "company trusting that its capital stays in the business, as a buffer. So the "
             "law stops it being handed back to members."),
        Pause("hold", 1.2),
    ], spec={"tpl": "talk", "bg": "office", "syl": "E3",
             "cast": [{"who": "KITO", "x": 1000, "y": 1030, "s": 0.95, "mood": "excited",
                       "talk_pose": "cheer", "moods": [["aud1", "surprised"]]},
                      {"who": "AUDITOR", "x": 1500, "y": 1030, "s": 0.92, "enter": "aud1",
                       "pose": "clipboard", "talk_pose": "clipboard"},
                      {"who": "LEX", "x": 420, "y": 1030, "s": 0.88, "enter": "lex1",
                       "from": "left"}],
             "pops": [{"kind": "icon", "icon": "moneybag", "x": 1250, "y": 280, "s": 1.1,
                       "at": ["kito1", 0.6], "until": "lex1", "label": "$500,000"},
                      {"kind": "icon", "icon": "shield", "x": 1250, "y": 280, "s": 1.2,
                       "at": ["lex1", 2.0], "label": "Creditors' buffer",
                       "color": "#0f8b8d"}]}),

    Scene("s2", "The creditors' buffer", "", [
        Pause("open", 1.0),
        Line("lex2a", "LEX", "In Trevor against Whitworth, the court said a company's "
             "capital must not be returned to members, except as the law allows.", gap=0.3),
        Line("lex2b", "LEX", "The buffer is share capital plus the undistributable "
             "reserves.", gap=0.25),
        Sfx("pop"),
        Line("lex2c", "LEX", "Share capital itself.", gap=0.2),
        Sfx("pop"),
        Line("lex2d", "LEX", "The share premium account.", gap=0.2),
        Sfx("pop"),
        Line("lex2e", "LEX", "The capital redemption reserve, created when shares are "
             "bought back.", gap=0.2),
        Sfx("pop"),
        Line("lex2f", "LEX", "Unrealised profits, such as revaluation gains, to the extent "
             "they exceed unrealised losses.", gap=0.2),
        Sfx("pop"),
        Line("lex2g", "LEX", "And any other reserve the law or the articles say cannot be "
             "distributed.", gap=0.4),
        Line("nia2", "NIA", "So only true, realised profits can ever go out as dividends."),
        Pause("hold", 1.4),
    ], spec={"tpl": "stack", "bg": "studio_teal", "heading": "The capital buffer",
             "syl": "E3(a)",
             "tiers": [{"at": "lex2c", "label": "Share capital", "color": "#0f8b8d"},
                       {"at": "lex2d", "label": "Share premium account", "color": "#2b86c5"},
                       {"at": "lex2e", "label": "Capital redemption reserve",
                        "color": "#7768ae"},
                       {"at": "lex2f", "label": "Net unrealised profits",
                        "sub": "e.g. revaluation surplus", "color": "#f2a541"},
                       {"at": "lex2g", "label": "Other undistributable reserves",
                        "color": "#e4572e"}],
             "top": 200, "bottom": 800,
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia2"}],
             "pops": [{"kind": "chip", "at": "lex2a", "until": "lex2c", "x": 1190, "y": 940,
                       "text": "Trevor v Whitworth (1887)", "color": "#1f3a5f", "size": 34}]}),

    Scene("s3", "Reducing capital", "", [
        Pause("open", 1.0),
        Line("lex3a", "LEX", "A company can still reduce its capital, under strict "
             "control, and only if its articles don't forbid it.", gap=0.3),
        Line("lex3b", "LEX", "Typical reasons: capital lost through trading losses, "
             "cancelling unpaid liability on shares, or returning surplus capital to "
             "members.", gap=0.4),
        Line("lex3c", "LEX", "A private company can pass a special resolution, backed by a "
             "solvency statement. Every director states the company can pay its debts for "
             "the next twelve months.", gap=0.3),
        Line("lex3d", "LEX", "A false statement is a criminal offence.", gap=0.4),
        Line("lex3e", "LEX", "Any company, and every public company, can instead pass a "
             "special resolution confirmed by the court. The court protects creditors, who "
             "may object.", gap=0.3),
        Line("lex3f", "LEX", "And if a public company's capital drops below fifty thousand "
             "pounds, it must re-register as private, unless the court allows otherwise."),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio", "heading": "Capital reduction",
             "syl": "E3(a)", "ts": 32,
             "cols": [{"title": "Solvency statement", "icon": "pen", "color": "#0f8b8d",
                       "at": "lex3c",
                       "items": [{"at": ["lex3c", 0.3], "text": "Private companies only"},
                                 {"at": ["lex3c", 1.5], "text": "Special resolution"},
                                 {"at": ["lex3c", 4.5], "text": "All directors: debts paid "
                                                               "for 12 months"},
                                 {"at": "lex3d", "text": "False statement = crime",
                                  "bad": True}]},
                      {"title": "Court route", "icon": "court", "color": "#7768ae",
                       "at": "lex3e",
                       "items": [{"at": ["lex3e", 0.3], "text": "Any company; required "
                                                               "for plc"},
                                 {"at": ["lex3e", 3.0], "text": "Special resolution + court "
                                                               "confirmation"},
                                 {"at": ["lex3e", 6.0], "text": "Creditors may object"},
                                 {"at": "lex3f", "text": "plc below £50,000: re-register "
                                                         "private"}]}],
             "vs": True,
             "cast": [{"who": "LEX", "x": 250}],
             "pops": [{"kind": "card", "at": "lex3b", "until": "lex3c", "x": 1180, "y": 470,
                       "w": 960, "h": 280, "title": "Why reduce?",
                       "body": "Write off lost capital · cancel unpaid liability · return "
                               "surplus capital", "color": "#f2a541", "dim": True,
                       "bs": 38}]}),

    Scene("s4", "Other safeguards", "", [
        Pause("open", 1.0),
        Line("lex4a", "LEX", "Capital maintenance has other guards too.", gap=0.3),
        Sfx("pop"),
        Line("lex4b", "LEX", "A company buying back or redeeming its own shares must "
             "generally use distributable profits, or a fresh share issue, and keep the "
             "buffer up through the capital redemption reserve.", gap=0.25),
        Sfx("pop"),
        Line("lex4c", "LEX", "A public company may not give financial assistance for "
             "someone to buy its own shares, such as lending them the money.", gap=0.25),
        Sfx("pop"),
        Line("lex4d", "LEX", "And if a public company's net assets fall to half or less of "
             "its called-up share capital, the directors must call a general meeting within "
             "twenty-eight days.", gap=0.4),
        Line("aud4", "AUDITOR", "That last one is called a serious loss of capital."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "heading": "More capital guards",
             "syl": "E3(a)", "row": 150, "ts": 40,
             "items": [{"at": "lex4b", "text": "Buy-backs from distributable profits",
                        "sub": "Or a fresh issue · capital redemption reserve",
                        "icon": "coin", "color": "#0f8b8d"},
                       {"at": "lex4c", "text": "No financial assistance (plc)",
                        "sub": "To buy the company's own shares", "icon": "cross",
                        "color": "#e4572e"},
                       {"at": "lex4d", "text": "Serious loss of capital (plc)",
                        "sub": "Net assets ≤ half called-up capital: meeting in 28 days",
                        "icon": "warning", "color": "#f2a541"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "AUDITOR", "x": 1810, "s": 0.55, "y": 1120, "enter": "aud4",
                       "pose": "clipboard"}]}),

    Scene("s5", "Profits available for dividends", "", [
        Pause("open", 1.0),
        Line("lex5a", "LEX", "Dividends can only be paid from profits available for the "
             "purpose.", gap=0.3),
        Line("lex5b", "LEX", "For any company, that means accumulated realised profits, "
             "less accumulated realised losses. Past years count, and there is no difference "
             "between capital and revenue profits.", gap=0.4),
        Line("lex5c", "LEX", "A public company must also pass a net assets test. After the "
             "dividend, its net assets must not fall below its called-up share capital plus "
             "undistributable reserves.", gap=0.4),
        Line("lex5d", "LEX", "So unrealised losses, which a private company can ignore, can "
             "still block a public company's dividend.", gap=0.4),
        Line("nia5", "NIA", "Safari Solar's realised profits are two hundred thousand, and "
             "last year's realised loss was eighty thousand. So we can pay up to one hundred "
             "and twenty thousand."),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio_purple", "heading": "Distributable profits",
             "syl": "E3(b)", "ts": 32,
             "cols": [{"title": "Private company", "icon": "house", "color": "#0f8b8d",
                       "at": "lex5b",
                       "items": [{"at": ["lex5b", 0.5], "text": "Accumulated realised "
                                                               "profits"},
                                 {"at": ["lex5b", 3.0], "text": "less accumulated realised "
                                                               "losses"},
                                 {"at": ["lex5b", 6.0], "text": "Capital or revenue: no "
                                                               "difference"}]},
                      {"title": "Public company", "icon": "company", "color": "#7768ae",
                       "at": "lex5c",
                       "items": [{"at": ["lex5c", 0.3], "text": "Same profits test, plus…"},
                                 {"at": ["lex5c", 3.0], "text": "Net assets at least called-up "
                                                               "capital + undistributable "
                                                               "reserves"},
                                 {"at": "lex5d", "text": "Unrealised losses count"}]}],
             "vs": True,
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia5"}],
             "pops": [{"kind": "card", "at": "nia5", "x": 1180, "y": 470, "w": 900, "h": 280,
                       "title": "Safari Solar Ltd",
                       "body": "$200,000 realised profit − $80,000 realised loss = "
                               "$120,000 available", "color": "#3bb273", "dim": True,
                       "bs": 38}]}),

    Scene("s6", "Declaring and getting it wrong", "", [
        Pause("open", 1.0),
        Line("lex6a", "LEX", "Under the model articles, members declare a final dividend by "
             "ordinary resolution, but never more than the directors recommend. Directors "
             "may pay interim dividends.", gap=0.3),
        Line("lex6b", "LEX", "Once declared, a dividend becomes a debt owed to the member.",
             gap=0.4),
        Line("lex6c", "LEX", "If a dividend is unlawful, a member who knew, or had "
             "reasonable grounds to believe, it was unlawful must repay it.", gap=0.3),
        Line("lex6d", "LEX", "And directors who authorised it can be personally liable to "
             "repay the company, as in Flitcroft's case.", gap=0.4),
        Line("kito6", "KITO", "Then we'll pay a modest, lawful dividend, and keep the bank "
             "happy."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "white", "heading": "Paying dividends",
             "syl": "E3(b)", "row": 130, "ts": 40,
             "items": [{"at": "lex6a", "text": "Declared by members (ordinary resolution)",
                        "sub": "Never above the directors' recommendation",
                        "icon": "ballot", "color": "#0f8b8d"},
                       {"at": "lex6b", "text": "Declared = a debt to members", "icon": "receipt",
                        "color": "#3bb273"},
                       {"at": "lex6c", "text": "Unlawful? Knowing members repay",
                        "icon": "warning", "color": "#f2a541"},
                       {"at": "lex6d", "text": "Directors personally liable",
                        "sub": "Re Exchange Banking Co (Flitcroft's case, 1882)",
                        "icon": "gavel", "color": "#e4572e"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "KITO", "x": 1810, "s": 0.55, "y": 1120, "enter": "kito6"}]}),

    quiz_scene("s7", "Quick check",
               "A private company may pay dividends out of…",
               ["Its share premium account", "Accumulated realised profits less accumulated "
                "realised losses", "This year's revaluation surplus", "Any cash in the bank"],
               1,
               "Quick check. A private company may pay dividends out of what?",
               "Accumulated realised profits, less accumulated realised losses.",
               syl="E3(b)"),

    quiz_scene("s8", "Quick check",
               "How can a private company reduce its share capital without going to court?",
               ["Ordinary resolution alone", "Special resolution supported by a solvency "
                "statement", "Board resolution", "It cannot"], 1,
               "And how can a private company reduce its capital without going to court?",
               "By special resolution, supported by a solvency statement.",
               think=4.0, syl="E3(a)"),

    recap_scene("s9", [
        ("Capital is the creditors' buffer.", "Capital = creditors' buffer"),
        ("Undistributable reserves stay put.", "Undistributable reserves"),
        ("Reduction: solvency statement or court.", "Reduce: solvency statement / court"),
        ("Dividends from net realised profits.", "Dividends: net realised profits"),
        ("Public companies: net assets test too.", "plc: net assets test"),
    ], [
        Line("lex9", "LEX", "Next time, we meet the people who run the company: its "
             "directors.", gap=0.3),
        Line("nia9", "NIA", "Kito, are you sure you're ready to be a director?", gap=0.3),
        Line("kito9", "KITO", "How hard can it be?", gap=0.6),
    ], next_ep=21, next_title="The Boardroom", next_icon="people"),
]
