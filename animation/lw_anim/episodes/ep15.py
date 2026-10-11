"""Episode 15 - Behind the Corporate Veil.

Syllabus D3(a)-(e): sole traders, partnerships and companies; limited
liability; types of company (private and public); separate legal personality;
lifting the veil. Company law follows the UK Companies Act 2006 model used by
ACCA LW-GLO, with comparisons to French, German, EU, Kenyan and Tanzanian
forms. Setting: Nia and Kito turn Safari Solar into a company.
"""
from ._kit import (DISPLAY_NAMES, SERIES, VOICES, Line, Pause, Scene, Sfx,  # noqa: F401
                   quiz_scene, recap_scene, title_scene)

EPISODE = "Episode 15"
EPISODE_TITLE = "Behind the Corporate Veil"
SLUG = "episode15_behind_the_corporate_veil"

SCENES = [
    title_scene(15, EPISODE_TITLE, "Syllabus D3", ("veil", "company")),

    Scene("s1", "Time to incorporate?", "", [
        Pause("open", 1.0),
        Line("nia1", "NIA", "Safari Solar is growing fast. But if a lamp starts a fire, "
             "could they take my house?", gap=0.4),
        Line("kito1", "KITO", "As partners, yes! Our liability is unlimited.", gap=0.4),
        Line("lex1", "LEX", "Which is why most growing businesses become companies. Let's "
             "compare the three main ways to run a business."),
        Pause("hold", 1.2),
    ], spec={"tpl": "talk", "bg": "harbour", "syl": "D3(a)",
             "cast": [{"who": "NIA", "x": 960, "y": 1030, "s": 0.92, "mood": "worried"},
                      {"who": "KITO", "x": 1450, "y": 1030, "s": 0.95, "mood": "surprised",
                       "talk_pose": "shrug"},
                      {"who": "LEX", "x": 420, "y": 1030, "s": 0.88, "enter": "lex1",
                       "from": "left"}],
             "pops": [{"kind": "icon", "icon": "house", "x": 1200, "y": 280, "s": 1.1,
                       "at": ["nia1", 2.5], "until": "lex1", "color": "#e4572e",
                       "label": "At risk?"}]}),

    Scene("s2", "Sole trader, partnership, company", "", [
        Pause("open", 1.0),
        Line("lex2a", "LEX", "A sole trader is one person in business alone. No formality, "
             "full control, but unlimited personal liability.", gap=0.4),
        Line("lex2b", "LEX", "A partnership shares the work and the profits. Still little "
             "formality, and, in an ordinary partnership, still unlimited liability.",
             gap=0.4),
        Line("lex2c", "LEX", "A company is a separate legal person. It owns its property, "
             "makes its own contracts, and lives on when members change. Members usually "
             "have limited liability.", gap=0.3),
        Line("lex2d", "LEX", "In exchange: formal registration, publicity, filing accounts, "
             "and more regulation.", gap=0.4),
        Line("nia2", "NIA", "And a company can raise money more easily. It can give lenders "
             "a floating charge, which partners generally cannot."),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio", "heading": "Three ways to do business",
             "syl": "D3(a)", "ts": 31,
             "cols": [{"title": "Sole trader", "icon": "person", "color": "#f2a541",
                       "at": "lex2a",
                       "items": [{"at": ["lex2a", 1.5], "text": "No formality", "good": True},
                                 {"at": ["lex2a", 3.0], "text": "Full control", "good": True},
                                 {"at": ["lex2a", 4.5], "text": "Unlimited liability",
                                  "bad": True}]},
                      {"title": "Partnership", "icon": "people", "color": "#7768ae",
                       "at": "lex2b",
                       "items": [{"at": ["lex2b", 1.0], "text": "Shared work and profit",
                                  "good": True},
                                 {"at": ["lex2b", 3.0], "text": "Little formality",
                                  "good": True},
                                 {"at": ["lex2b", 5.5], "text": "Usually unlimited "
                                                               "liability", "bad": True}]},
                      {"title": "Company", "icon": "company", "color": "#0f8b8d",
                       "at": "lex2c",
                       "items": [{"at": ["lex2c", 1.0], "text": "Separate legal person",
                                  "good": True},
                                 {"at": ["lex2c", 4.5], "text": "Perpetual succession",
                                  "good": True},
                                 {"at": ["lex2c", 7.0], "text": "Limited liability",
                                  "good": True},
                                 {"at": "nia2", "text": "Can grant floating charges",
                                  "good": True},
                                 {"at": "lex2d", "text": "Formality, publicity, regulation",
                                  "bad": True}]}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia2"}]}),

    Scene("s3", "Corporations and limited liability", "", [
        Pause("open", 1.0),
        Line("lex3a", "LEX", "A corporation is an artificial legal person.", gap=0.3),
        Sfx("pop"),
        Line("lex3b", "LEX", "A corporation sole is a single office holder, like a mayor or "
             "a bishop. The office continues when the person changes.", gap=0.25),
        Sfx("pop"),
        Line("lex3c", "LEX", "A corporation aggregate is a group of people forming one "
             "legal person, like a company.", gap=0.25),
        Sfx("pop"),
        Line("lex3d", "LEX", "Corporations can be created by royal charter, by a special "
             "statute, or, far more commonly, by registration under the Companies Act.",
             gap=0.4),
        Line("lex3e", "LEX", "Limited liability means a member's liability is limited to "
             "any amount unpaid on their shares, or, in a guarantee company, the amount "
             "they guaranteed. The company itself is still fully liable for its own debts.",
             gap=0.3),
        Line("kito3", "KITO", "So Safari Solar Limited could go bust, but our houses would "
             "be safe!"),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "heading": "Corporations", "syl": "D3(b)",
             "row": 130, "ts": 40,
             "items": [{"at": "lex3b", "text": "Corporation sole", "sub": "One office holder, "
                                                                         "e.g. a mayor",
                        "icon": "crown", "color": "#f2a541"},
                       {"at": "lex3c", "text": "Corporation aggregate", "sub": "Many members "
                                                                              "= one person",
                        "icon": "people", "color": "#0f8b8d"},
                       {"at": "lex3d", "text": "Charter · statute · registration",
                        "sub": "Registration is by far the most common", "icon": "stamp",
                        "color": "#7768ae"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "KITO", "x": 1810, "s": 0.55, "y": 1120, "enter": "kito3",
                       "mood": "excited"}],
             "pops": [{"kind": "card", "at": "lex3e", "x": 1190, "y": 760, "w": 980, "h": 230,
                       "title": "Limited liability",
                       "body": "Members lose at most their unpaid share capital (or "
                               "guarantee). The company pays its own debts.",
                       "color": "#3bb273", "bs": 34}]}),

    Scene("s4", "Private and public companies", "", [
        Pause("open", 1.0),
        Line("lex4a", "LEX", "Companies may be limited by shares, limited by guarantee, or "
             "even unlimited. Most are private companies limited by shares.", gap=0.4),
        Line("lex4b", "LEX", "A public company must be limited by shares, say it is public "
             "in its constitution, and end its name with p l c.",
             say="A public company must be limited by shares, say it is public in its "
                 "constitution, and end its name with P.L.C.", gap=0.3),
        Line("lex4c", "LEX", "It needs allotted share capital of at least fifty thousand "
             "pounds, at least a quarter paid up, plus any premium. And it cannot trade "
             "until it receives a trading certificate.", gap=0.3),
        Line("lex4d", "LEX", "It needs at least two directors, and a qualified company "
             "secretary. And only a public company may offer its shares to the public.",
             gap=0.4),
        Line("lex4e", "LEX", "A private company needs just one director, no secretary, and "
             "no minimum capital.", gap=0.4),
        Line("nia4", "NIA", "And in Kenya and Tanzania, a private company can have at most "
             "fifty members."),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio_teal", "heading": "Private vs public",
             "syl": "D3(c)", "ts": 33,
             "cols": [{"title": "Private (Ltd)", "icon": "house", "color": "#0f8b8d",
                       "at": "lex4e",
                       "items": [{"at": ["lex4e", 0.5], "text": "1 director minimum"},
                                 {"at": ["lex4e", 1.8], "text": "Secretary optional"},
                                 {"at": ["lex4e", 2.8], "text": "No minimum capital"},
                                 {"at": ["lex4e", 3.5], "text": "Cannot offer shares to the "
                                                               "public"},
                                 {"at": "nia4", "text": "Kenya and Tanzania: max 50 members"}]},
                      {"title": "Public (plc)", "icon": "company", "color": "#7768ae",
                       "at": "lex4b",
                       "items": [{"at": ["lex4b", 1.0], "text": "Limited by shares, named "
                                                               "plc"},
                                 {"at": "lex4c", "text": "£50,000 allotted · ¼ paid up"},
                                 {"at": ["lex4c", 7.0], "text": "Trading certificate before "
                                                               "trading"},
                                 {"at": "lex4d", "text": "2+ directors · qualified "
                                                         "secretary"},
                                 {"at": ["lex4d", 5.0], "text": "May offer shares to the "
                                                               "public"}]}],
             "vs": True,
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia4"}]}),

    Scene("s5", "Companies around the world", "", [
        Pause("open", 1.0),
        Line("lex5a", "LEX", "Most countries have the same two-way split.", gap=0.3),
        Sfx("pop"),
        Line("lex5b", "LEX", "In France, the société anonyme, or S A, is like a public "
             "company.", say="In France, the soe-see-ay-tay ah-noh-neem, or S.A., is like a "
             "public company.", gap=0.25),
        Sfx("pop"),
        Line("lex5c", "LEX", "And the S A R L is like a private company. Its capital is "
             "divided into parts that cannot be sold to the public.",
             say="And the S.A.R.L. is like a private company. Its capital is divided into "
                 "parts that cannot be sold to the public.", gap=0.25),
        Sfx("pop"),
        Line("lex5d", "LEX", "In Germany, the A G is like a public company, and the G m b H "
             "like a private one.", say="In Germany, the A.G. is like a public company, and "
             "the G.M.B.H. like a private one.", gap=0.25),
        Sfx("pop"),
        Line("lex5e", "LEX", "The European Company, the S E, is a public company for groups "
             "operating across the EU, with minimum capital of a hundred and twenty "
             "thousand euros.", say="The European Company, the S.E., is a public company for "
             "groups operating across the E.U., with minimum capital of a hundred and "
             "twenty thousand euros.", gap=0.25),
        Sfx("pop"),
        Line("lex5f", "LEX", "And in Islamic law, there is no separate corporate form of "
             "its own, although partnership forms are recognised.", gap=0.4),
        Line("hans5", "HANS", "My company is a G m b H. Now you know it's private!",
             say="My company is a G.M.B.H. Now you know it's private!"),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "white", "layout": "grid", "cols": 3,
             "heading": "Company forms abroad", "syl": "D3(c)", "cell_h": 300, "ts": 34,
             "items": [{"at": "lex5b", "text": "SA (France)", "sub": "Like a public company",
                        "icon": "flag", "color": "#2b86c5"},
                       {"at": "lex5c", "text": "SARL (France)", "sub": "Like a private company",
                        "icon": "flag", "color": "#2b86c5"},
                       {"at": "lex5d", "text": "AG (Germany)", "sub": "Like a public company",
                        "icon": "flag", "color": "#1d2b3a"},
                       {"at": ["lex5d", 2.5], "text": "GmbH (Germany)", "sub": "Like a private "
                                                                               "company",
                        "icon": "flag", "color": "#1d2b3a"},
                       {"at": "lex5e", "text": "SE (EU)", "sub": "European public company · "
                                                                  "€120,000",
                        "icon": "globe", "color": "#7768ae"},
                       {"at": "lex5f", "text": "Islamic law", "sub": "No separate corporate "
                                                                     "form",
                        "icon": "book", "color": "#3bb273"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "HANS", "x": 1810, "s": 0.55, "y": 1120, "enter": "hans5"}]}),

    Scene("s6", "Salomon's case", "", [
        Pause("open", 1.0),
        Line("lex6a", "LEX", "The leading case is Salomon against Salomon and Company, "
             "decided by the House of Lords in 1897.", gap=0.3),
        Line("lex6b", "LEX", "Mr Salomon sold his boot business to a company he formed. He "
             "held almost all the shares, and was also a secured creditor, through "
             "debentures.", gap=0.3),
        Line("lex6c", "LEX", "When the company failed, the liquidator argued the company was "
             "just Salomon in disguise.", gap=0.3),
        Line("lex6d", "LEX", "The Lords disagreed. The company was a separate person, "
             "properly formed. Salomon, as a secured creditor, was paid first.", gap=0.4),
        Sfx("sparkle"),
        Pause("stamp", 1.2),
        Line("lex6e", "LEX", "Other cases follow the same logic. In Macaura, a shareholder "
             "could not insure the company's timber, because it was not his. And in Lee "
             "against Lee's Air Farming, a director could also be his company's employee."),
        Pause("hold", 1.4),
    ], spec={"tpl": "case", "bg": "court", "name": "Salomon v A Salomon & Co Ltd",
             "year": "House of Lords · 1897", "syl": "D3(d)",
             "rows": [{"at": "lex6b", "label": "Facts", "text": "Sole trader incorporated, "
                                                                "kept most shares and "
                                                                "secured debentures",
                       "color": "#7768ae"},
                      {"at": "lex6c", "label": "Claim", "text": "Liquidator: the company is "
                                                                "just Salomon",
                       "color": "#f2a541"},
                      {"at": "lex6d", "label": "Held", "text": "Separate legal person · "
                                                               "Salomon paid as secured "
                                                               "creditor",
                       "color": "#3bb273"},
                      {"at": "lex6e", "label": "See also", "text": "Macaura (1925) · Lee v "
                                                                   "Lee's Air Farming (1961)",
                       "color": "#0f8b8d"}],
             "stamp": {"at": "stamp", "text": "SEPARATE PERSON", "color": "#3bb273"},
             "cast": [{"who": "LEX", "x": 250}]}),

    Scene("s7", "Lifting the veil", "", [
        Pause("open", 1.0),
        Line("lex7a", "LEX", "Separate personality is a veil between a company and its "
             "members. Occasionally the courts look behind it.", gap=0.3),
        Sfx("pop"),
        Line("lex7b", "LEX", "Where a company is a sham, used to evade a legal obligation. "
             "In Gilford Motor against Horne, a former employee set up a company to dodge "
             "his non-compete promise. And in Jones against Lipman, a seller transferred a "
             "house to his company to avoid selling it.", gap=0.25),
        Sfx("pop"),
        Line("lex7c", "LEX", "In wartime, to find a company's enemy character, as in "
             "Daimler against Continental Tyre.", gap=0.25),
        Sfx("pop"),
        Line("lex7d", "LEX", "Under statute: fraudulent and wrongful trading, a plc trading "
             "without its certificate, reusing a failed company's name, and group "
             "accounts.", gap=0.4),
        Line("lex7e", "LEX", "But courts are reluctant. In Adams against Cape Industries, "
             "they refused to treat a group as one entity. And Prest against Petrodel "
             "confirmed the veil is lifted only to stop evasion of an existing obligation.",
             gap=0.3),
        Line("aud7", "AUDITOR", "Exam tip: Salomon is the rule. Lifting the veil is the "
             "exception."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "heading": "Lifting the veil", "syl": "D3(e)",
             "row": 132, "ts": 38,
             "items": [{"at": "lex7b", "text": "Sham to evade an obligation",
                        "sub": "Gilford Motor v Horne · Jones v Lipman", "icon": "mask",
                        "color": "#e4572e"},
                       {"at": "lex7c", "text": "Enemy character in wartime",
                        "sub": "Daimler v Continental Tyre", "icon": "flag",
                        "color": "#7768ae"},
                       {"at": "lex7d", "text": "Statute", "sub": "Fraudulent / wrongful "
                                                                 "trading · no trading "
                                                                 "certificate · phoenix "
                                                                 "names · group accounts",
                        "icon": "book", "color": "#2b86c5"},
                       {"at": "lex7e", "text": "But rarely!", "sub": "Adams v Cape · "
                                                                     "Prest v Petrodel",
                        "icon": "warning", "color": "#f2a541"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "AUDITOR", "x": 1810, "s": 0.55, "y": 1120, "enter": "aud7",
                       "pose": "clipboard"}]}),

    quiz_scene("s8", "Quick check",
               "What did Salomon v Salomon & Co establish?",
               ["Directors are personally liable for company debts",
                "A properly formed company is a person separate from its members",
                "One-person companies are invalid", "Shareholders own the company's assets"],
               1,
               "Quick check. What did Salomon against Salomon establish?",
               "A properly formed company is a person, separate from its members.",
               syl="D3(d)"),

    quiz_scene("s9", "Quick check",
               "What is the minimum allotted share capital of a UK public company?",
               ["£1", "£12,500", "£50,000", "£120,000"], 2,
               "And what is the minimum allotted share capital of a public company?",
               "Fifty thousand pounds, at least a quarter paid up.",
               think=4.0, syl="D3(c)"),

    recap_scene("s10", [
        ("Company: a separate legal person.", "Separate legal person"),
        ("Limited liability protects members.", "Limited liability"),
        ("Public companies: plc, fifty thousand, certificate.", "plc: £50k · certificate"),
        ("Salomon is the rule.", "Salomon (1897)"),
        ("Lifting the veil is the exception.", "Veil lifted: sham · statute"),
    ], [
        Line("lex10", "LEX", "Next time, we form Safari Solar Limited, step by step: "
             "promoters, pre-incorporation contracts, and registration.", gap=0.3),
        Line("kito10", "KITO", "I'll be the promoter! What could go wrong?", gap=0.6),
    ], next_ep=16, next_title="Birth of a Company", next_icon="stamp"),
]
