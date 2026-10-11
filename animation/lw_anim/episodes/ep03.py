"""Episode 3 - The Global Rule-Makers.

Syllabus A2(c): the roles of the UN, UNCITRAL, the WTO, the ICC, the OECD,
UNIDROIT and courts in promoting and regulating international trade.
Setting: the port of Dar es Salaam, where SafariTech's first export to Kenya
is held up.
"""
from ._kit import (DISPLAY_NAMES, SERIES, VOICES, Line, Pause, Scene, Sfx,  # noqa: F401
                   quiz_scene, recap_scene, title_scene)

EPISODE = "Episode 3"
EPISODE_TITLE = "The Global Rule-Makers"
SLUG = "episode03_the_global_rule_makers"

SCENES = [
    title_scene(3, EPISODE_TITLE, "Syllabus A2(c)", ("globe", "handshake")),

    Scene("s1", "Port of Dar es Salaam", "", [
        Pause("open", 1.2),
        Sfx("horn"),
        Line("cargo1", "CARGO", "Ahoy! I'm loaded with SafariTech kits for Mombasa, but "
             "I'm stuck in the paperwork queue!", gap=0.4),
        Line("kito1", "KITO", "Customs forms, tariffs, different rules in every country. "
             "Who sorts all this out?", gap=0.4),
        Line("lex1", "LEX", "A whole family of international organisations. None of them "
             "is a world government, but each one pushes trade law in the same direction.",
             gap=0.3),
        Line("nia1", "NIA", "Let's meet them one by one."),
        Pause("hold", 1.2),
    ], spec={"tpl": "talk", "bg": "port", "syl": "A2(c)",
             "cast": [{"who": "CARGO", "x": 1520, "y": 980, "s": 0.9},
                      {"who": "KITO", "x": 330, "y": 1060, "s": 0.85, "mood": "worried",
                       "talk_pose": "shrug"},
                      {"who": "LEX", "x": 640, "y": 1060, "s": 0.85, "enter": "lex1",
                       "from": "left"},
                      {"who": "NIA", "x": 920, "y": 1060, "s": 0.8, "enter": ["lex1", 1.0],
                       "from": "left"}],
             "pops": [{"kind": "icon", "icon": "doc", "x": 1400, "y": 300, "s": 0.8,
                       "at": ["cargo1", 2.0], "until": "lex1", "float": True},
                      {"kind": "icon", "icon": "stamp", "x": 1560, "y": 260, "s": 0.8,
                       "at": ["cargo1", 2.6], "until": "lex1", "float": True,
                       "color": "#e4572e"},
                      {"kind": "icon", "icon": "percent", "x": 1720, "y": 320, "s": 0.8,
                       "at": ["kito1", 1.4], "until": "lex1", "float": True,
                       "color": "#7768ae"}]}),

    Scene("s2", "The UN and UNCITRAL", "", [
        Pause("open", 1.0),
        Line("lex2a", "LEX", "The United Nations, founded in 1945, aims to keep peace and "
             "security, build friendly relations between nations, and promote cooperation "
             "on economic and social problems and human rights.", gap=0.4),
        Line("lex2b", "LEX", "For trade law, its key body is UNCITRAL, the UN Commission on "
             "International Trade Law, set up in 1966.",
             say="For trade law, its key body is Uncitral, the U.N. Commission on "
                 "International Trade Law, set up in 1966.", gap=0.4),
        Sfx("pop"),
        Line("lex2c", "LEX", "UNCITRAL prepares conventions, model laws and legal guides.",
             say="Uncitral prepares conventions, model laws and legal guides.", gap=0.25),
        Sfx("pop"),
        Line("lex2d", "LEX", "It coordinates the work of other organisations, so they do "
             "not duplicate each other.", gap=0.25),
        Sfx("pop"),
        Line("lex2e", "LEX", "It encourages more countries to join existing conventions.",
             gap=0.25),
        Sfx("pop"),
        Line("lex2f", "LEX", "It promotes consistent interpretation, by collecting and "
             "publishing court decisions.", gap=0.25),
        Sfx("pop"),
        Line("lex2g", "LEX", "And it works closely with UNCTAD, the UN trade and development "
             "body.", say="And it works closely with Unk-tad, the U.N. trade and development "
             "body.", gap=0.5),
        Line("nia2", "NIA", "So the Sales Convention, the Hamburg Rules on sea carriage, and "
             "the Model Law on arbitration all came from UNCITRAL.",
             say="So the Sales Convention, the Hamburg Rules on sea carriage, and the Model "
                 "Law on arbitration all came from Uncitral."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "white", "heading": "UNCITRAL: how it harmonises",
             "syl": "A2(c)", "row": 118, "ts": 40,
             "items": [{"at": "lex2c", "text": "Drafts conventions and model laws",
                        "sub": "CISG · Model Law on arbitration · Hamburg Rules",
                        "icon": "doc"},
                       {"at": "lex2d", "text": "Coordinates other organisations",
                        "sub": "Encourages cooperation, avoids duplication",
                        "icon": "people"},
                       {"at": "lex2e", "text": "Promotes wider participation",
                        "sub": "More states joining existing conventions", "icon": "flag"},
                       {"at": "lex2f", "text": "Consistent interpretation",
                        "sub": "Collects and publishes case law (CLOUT)",
                        "icon": "magnifier"},
                       {"at": "lex2g", "text": "Liaises with UNCTAD",
                        "sub": "UN Conference on Trade and Development", "icon": "globe"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1790, "s": 0.58, "y": 1120, "enter": "nia2"}],
             "pops": [{"kind": "card", "at": "lex2a", "until": "lex2b", "x": 1190, "y": 470,
                       "w": 900, "h": 300, "title": "United Nations (1945)",
                       "body": "Peace and security · friendly relations · economic and "
                               "social cooperation · human rights", "color": "#2b86c5",
                       "bs": 40}]}),

    Scene("s3", "The World Trade Organization", "", [
        Pause("open", 1.0),
        Line("lex3a", "LEX", "The WTO was formed in 1995, building on the General Agreement "
             "on Tariffs and Trade, the GATT, from 1947.",
             say="The W.T.O. was formed in 1995, building on the General Agreement on "
                 "Tariffs and Trade, the Gatt, from 1947.", gap=0.4),
        Line("lex3b", "LEX", "It promotes free trade in goods, services and intellectual "
             "property, by removing barriers: tariffs, quotas, import controls and red tape.",
             gap=0.4),
        Sfx("pop"),
        Line("lex3c", "LEX", "It is a forum for negotiating trade agreements, and it "
             "administers them once agreed.", gap=0.25),
        Sfx("pop"),
        Line("lex3d", "LEX", "It reviews each member's trade policies.", gap=0.25),
        Sfx("pop"),
        Line("lex3e", "LEX", "It helps developing countries build their trade capacity.",
             gap=0.25),
        Sfx("pop"),
        Line("lex3f", "LEX", "And it settles trade disputes between member states.", gap=0.5),
        Line("kito3", "KITO", "Are Tanzania and Kenya members?", gap=0.3),
        Line("lex3g", "LEX", "Both have been members since the WTO began in 1995. Regionally, "
             "the East African Community customs union goes even further, with a common "
             "external tariff.",
             say="Both have been members since the W.T.O. began in 1995. Regionally, the "
                 "East African Community customs union goes even further, with a common "
                 "external tariff."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "layout": "grid", "cols": 2,
             "heading": "WTO: what it does", "syl": "A2(c)", "cell_h": 280, "ts": 38,
             "items": [{"at": "lex3c", "text": "Negotiates and administers agreements",
                        "icon": "handshake", "color": "#0f8b8d"},
                       {"at": "lex3d", "text": "Reviews trade policies",
                        "icon": "magnifier", "color": "#7768ae"},
                       {"at": "lex3e", "text": "Helps developing countries",
                        "icon": "chart", "color": "#3bb273"},
                       {"at": "lex3f", "text": "Settles disputes between states",
                        "icon": "scales", "color": "#e4572e"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "KITO", "x": 1790, "s": 0.58, "y": 1120, "enter": "kito3"}],
             "pops": [{"kind": "card", "at": "lex3a", "until": "lex3c", "x": 1190, "y": 470,
                       "w": 900, "h": 300, "title": "WTO · 1995 (from GATT 1947)",
                       "body": "Free trade in goods, services and IP: cut tariffs, quotas, "
                               "import controls and red tape", "color": "#0f8b8d", "bs": 40},
                      {"kind": "card", "at": "lex3g", "x": 1190, "y": 470, "w": 900, "h": 260,
                       "title": "Local lens: East Africa",
                       "body": "Tanzania and Kenya: WTO members since 1995 · EAC customs "
                               "union with a common external tariff", "color": "#f2a541",
                       "dim": True, "bs": 38}]}),

    Scene("s4", "The International Chamber of Commerce", "", [
        Pause("open", 1.0),
        Line("lex4a", "LEX", "The ICC is the world business organisation, founded in 1919. "
             "It speaks for business, not governments.",
             say="The I.C.C. is the world business organisation, founded in 1919. It speaks "
                 "for business, not governments.", gap=0.4),
        Line("lex4b", "LEX", "It promotes trade, investment and open markets, and free and "
             "fair competition.", gap=0.3),
        Line("lex4c", "LEX", "It fights commercial crime, such as fraud and counterfeiting.",
             gap=0.4),
        Line("lex4d", "LEX", "And it writes rules that traders adopt in their contracts: "
             "Incoterms for delivery, and the UCP rules for letters of credit.",
             say="And it writes rules that traders adopt in their contracts: Inco-terms for "
                 "delivery, and the U.C.P. rules for letters of credit.", gap=0.4),
        Line("lex4e", "LEX", "Its International Court of Arbitration, created in 1923, "
             "supervises ICC arbitrations around the world.",
             say="Its International Court of Arbitration, created in 1923, supervises I.C.C. "
                 "arbitrations around the world.", gap=0.4),
        Line("cargo4", "CARGO", "Incoterms! I knew they'd come up!",
             say="Inco-terms! I knew they'd come up!"),
        Pause("hold", 1.4),
    ], spec={"tpl": "flow", "bg": "studio", "heading": "ICC: rules made by business",
             "syl": "A2(c)",
             "nodes": [{"id": "icc", "x": 1150, "y": 300, "label": "ICC (1919)",
                        "icon": "globe", "color": "#1f3a5f", "at": "lex4a", "w": 300},
                       {"id": "trade", "x": 640, "y": 660, "label": "Trade, investment, "
                                                                    "fair competition",
                        "icon": "chart", "color": "#3bb273", "at": "lex4b", "w": 290},
                       {"id": "crime", "x": 960, "y": 720, "label": "Fights commercial crime",
                        "icon": "shield", "color": "#e4572e", "at": "lex4c", "w": 270},
                       {"id": "rules", "x": 1310, "y": 720, "label": "Incoterms · UCP 600",
                        "icon": "contract", "color": "#f2a541", "at": "lex4d", "w": 270},
                       {"id": "court", "x": 1650, "y": 660, "label": "Court of Arbitration "
                                                                     "(1923)",
                        "icon": "gavel", "color": "#7768ae", "at": "lex4e", "w": 290}],
             "edges": [{"from": "icc", "to": "trade", "at": "lex4b", "bend": -30},
                       {"from": "icc", "to": "crime", "at": "lex4c"},
                       {"from": "icc", "to": "rules", "at": "lex4d"},
                       {"from": "icc", "to": "court", "at": "lex4e", "bend": 30}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "CARGO", "x": 1760, "y": 1040, "s": 0.55, "enter": "cargo4"}]}),

    Scene("s5", "The OECD and UNIDROIT", "", [
        Pause("open", 1.0),
        Line("lex5a", "LEX", "The OECD, based in Paris, brings together governments to "
             "share data and agree better economic policies.",
             say="The O.E.C.D., based in Paris, brings together governments to share data "
                 "and agree better economic policies.", gap=0.3),
        Line("lex5b", "LEX", "Its standards reach far beyond its members: guidelines for "
             "multinational enterprises, an anti-bribery convention, and work on "
             "international tax.", gap=0.5),
        Line("lex5c", "LEX", "UNIDROIT, founded in Rome in 1926, is an independent "
             "intergovernmental body. It studies how to modernise and harmonise private "
             "law, especially trade law.",
             say="Unee-droit, founded in Rome in 1926, is an independent intergovernmental "
                 "body. It studies how to modernise and harmonise private law, especially "
                 "trade law.", gap=0.4),
        Line("lex5d", "LEX", "Its best-known work is the UNIDROIT Principles of International "
             "Commercial Contracts. And it has a three-tier structure.",
             say="Its best-known work is the Unee-droit Principles of International "
                 "Commercial Contracts. And it has a three-tier structure.", gap=0.3),
        Sfx("pop"),
        Line("lex5e", "LEX", "The Secretariat runs it day to day.", gap=0.25),
        Sfx("pop"),
        Line("lex5f", "LEX", "The Governing Council sets policy, draws up the work programme, "
             "and supervises the Secretariat.", gap=0.25),
        Sfx("pop"),
        Line("lex5g", "LEX", "And the General Assembly is the ultimate decision-maker. It "
             "approves the budget and the work programme, and elects the Council."),
        Pause("hold", 1.6),
    ], spec={"tpl": "flow", "bg": "studio_purple", "heading": "OECD (Paris) · UNIDROIT (Rome, 1926)",
             "syl": "A2(c)",
             "nodes": [{"id": "oecd", "x": 760, "y": 330, "label": "OECD (Paris)",
                        "icon": "chart", "color": "#2b86c5", "at": "lex5a", "w": 300},
                       {"id": "oecd2", "x": 760, "y": 690, "label": "MNE guidelines · "
                                                                    "anti-bribery · tax",
                        "icon": "shield", "color": "#2b86c5", "at": "lex5b", "w": 300},
                       {"id": "ga", "x": 1500, "y": 270, "label": "General Assembly: decides",
                        "icon": "people", "color": "#e4572e", "at": "lex5g", "w": 380},
                       {"id": "gc", "x": 1500, "y": 560, "label": "Governing Council: policy",
                        "icon": "brain", "color": "#7768ae", "at": "lex5f", "w": 380},
                       {"id": "sec", "x": 1500, "y": 850, "label": "Secretariat: day to day",
                        "icon": "laptop", "color": "#0f8b8d", "at": "lex5e", "w": 380}],
             "edges": [{"from": "oecd", "to": "oecd2", "at": "lex5b"},
                       {"from": "ga", "to": "gc", "at": ["lex5g", 2.0], "label": "elects",
                        "lx": 100},
                       {"from": "gc", "to": "sec", "at": ["lex5f", 2.0],
                        "label": "supervises", "lx": 110}],
             "cast": [{"who": "LEX", "x": 250}]}),

    Scene("s6", "Courts in international trade", "", [
        Pause("open", 1.0),
        Line("nia6", "NIA", "And when trading nations or companies fall out, which courts "
             "step in?", gap=0.4),
        Sfx("pop"),
        Line("lex6a", "LEX", "The International Court of Justice in The Hague hears "
             "disputes between states only. A company cannot sue there.", gap=0.3),
        Sfx("pop"),
        Line("lex6b", "LEX", "Regional courts interpret trade treaties. The East African "
             "Court of Justice sits right here in Arusha.", gap=0.3),
        Sfx("pop"),
        Line("lex6c", "LEX", "WTO panels settle trade disputes between member governments.",
             say="W.T.O. panels settle trade disputes between member governments.", gap=0.3),
        Sfx("pop"),
        Line("lex6d", "LEX", "But most commercial disputes go to national courts, or to "
             "arbitration, often supervised by bodies like the ICC Court, or the Nairobi "
             "Centre for International Arbitration.",
             say="But most commercial disputes go to national courts, or to arbitration, "
                 "often supervised by bodies like the I.C.C. Court, or the Nairobi Centre for "
                 "International Arbitration.", gap=0.4),
        Line("kito6", "KITO", "Arbitration again. I think that's our next stop."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "white", "layout": "grid", "cols": 2,
             "heading": "Who resolves international disputes?", "syl": "A2(c)",
             "cell_h": 300, "ts": 36,
             "items": [{"at": "lex6a", "text": "International Court of Justice",
                        "sub": "The Hague · states only", "icon": "court", "color": "#2b86c5"},
                       {"at": "lex6b", "text": "East African Court of Justice",
                        "sub": "Arusha · interprets the EAC Treaty", "icon": "flag",
                        "color": "#3bb273"},
                       {"at": "lex6c", "text": "WTO dispute settlement",
                        "sub": "Between member governments", "icon": "scales",
                        "color": "#7768ae"},
                       {"at": "lex6d", "text": "National courts and arbitration",
                        "sub": "ICC Court · NCIA Nairobi · TIAC Dar es Salaam",
                        "icon": "gavel", "color": "#e4572e"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1800, "s": 0.55, "y": 1120},
                      {"who": "KITO", "x": 1640, "s": 0.55, "y": 1120, "enter": "kito6"}]}),

    quiz_scene("s7", "Quick check",
               "Which organisation publishes the Incoterms rules?",
               ["The United Nations", "The World Trade Organization",
                "The International Chamber of Commerce", "UNIDROIT"], 2,
               "Quick check. Which organisation publishes the Incoterms rules?",
               "The International Chamber of Commerce.",
               why=("The ICC writes rules that traders adopt by contract: Incoterms, UCP 600",
                    "The I.C.C. writes rules that traders adopt by contract, like Inco-terms "
                    "and the U.C.P. rules."),
               syl="A2(c)"),

    quiz_scene("s8", "Quick check",
               "Within UNIDROIT, which body is the ultimate decision-maker?",
               ["The Secretariat", "The Governing Council", "The General Assembly",
                "The Court of Arbitration"], 2,
               "One more. Within UNIDROIT, which body is the ultimate decision-maker?",
               "The General Assembly.",
               why=("It approves the budget and work programme, and elects the Council",
                    "It approves the budget and the work programme, and elects the "
                    "Governing Council."),
               think=4.0, syl="A2(c)"),

    recap_scene("s9", [
        ("UN and UNCITRAL: conventions and model laws.", "UN + UNCITRAL: conventions, "
         "model laws", "U.N. and Uncitral: conventions and model laws."),
        ("WTO: free trade and disputes between states.", "WTO: free trade, state disputes",
         "W.T.O.: free trade and disputes between states."),
        ("ICC: Incoterms, UCP, and arbitration.", "ICC: Incoterms · UCP · arbitration",
         "I.C.C.: Inco-terms, U.C.P., and arbitration."),
        ("OECD and UNIDROIT.", "OECD · UNIDROIT (3 tiers)",
         "O.E.C.D. and Unee-droit."),
        ("Courts: ICJ for states, plus regional courts.", "ICJ · EACJ · national courts",
         "Courts: the I.C.J. for states, plus regional courts."),
    ], [
        Line("lex9", "LEX", "Next time, we step inside an arbitration, from the clause in "
             "the contract to the final award.", gap=0.3),
        Line("cargo9", "CARGO", "Finally cleared customs! Mombasa, here I come!", gap=0.6),
    ], next_ep=4, next_title="The Arbitration Room", next_icon="gavel"),
]
