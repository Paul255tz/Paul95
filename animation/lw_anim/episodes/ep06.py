"""Episode 6 - Incoterms: Who Pays, Who Risks.

Syllabus B1(c): the meaning and effect of the ICC Incoterms rules (Incoterms
2020). Each rule is shown on a route map with two bars: who pays the costs of
carriage, and where risk passes from seller to buyer.
"""
from ._kit import (DISPLAY_NAMES, SERIES, VOICES, Line, Pause, Scene, Sfx,  # noqa: F401
                   quiz_scene, recap_scene, title_scene)

EPISODE = "Episode 6"
EPISODE_TITLE = "Incoterms: Who Pays, Who Risks"
SLUG = "episode06_incoterms_who_pays_who_risks"

ANY = "#0f8b8d"
SEA = "#2b86c5"

SCENES = [
    title_scene(6, EPISODE_TITLE, "Syllabus B1(c)", ("container", "ship"),
                say_title="Inco-terms. Who Pays, Who Risks?"),

    Scene("s1", "Three letters on a quote", "", [
        Pause("open", 1.2),
        Sfx("horn"),
        Line("hans1", "HANS", "My quote says FOB Hamburg, Incoterms 2020.",
             say="My quote says F.O.B. Hamburg, Inco-terms 2020.", gap=0.4),
        Line("kito1", "KITO", "Three letters? What do they actually decide?", gap=0.4),
        Line("lex1", "LEX", "Incoterms are trade terms published by the ICC. The current "
             "version is Incoterms 2020.",
             say="Inco-terms are trade terms published by the I.C.C. The current version is "
                 "Inco-terms 2020.", gap=0.3),
        Sfx("pop"),
        Line("lex1b", "LEX", "Each rule tells you who arranges and pays for carriage, who "
             "handles export and import clearance, and the exact point where risk passes "
             "from seller to buyer.", gap=0.4),
        Sfx("pop"),
        Line("lex1c", "LEX", "But careful. They do not decide when ownership passes, how the "
             "price is paid, or what happens on breach. The contract and the governing law "
             "do that.", gap=0.3),
        Line("cargo1", "CARGO", "And they only apply if the contract says so!"),
        Pause("hold", 1.2),
    ], spec={"tpl": "talk", "bg": "port", "syl": "B1(c)",
             "cast": [{"who": "HANS", "x": 900, "y": 1060, "s": 0.85, "pose": "hold_r"},
                      {"who": "KITO", "x": 620, "y": 1060, "s": 0.85, "mood": "thinking"},
                      {"who": "LEX", "x": 300, "y": 1060, "s": 0.85, "enter": "lex1",
                       "from": "left"},
                      {"who": "CARGO", "x": 1560, "y": 1000, "s": 0.8, "enter": "cargo1",
                       "from": "right"}],
             "pops": [{"kind": "chip", "at": ["hans1", 0.5], "until": "lex1b", "x": 960,
                       "y": 200, "text": "FOB Hamburg · Incoterms® 2020", "color": "#1f3a5f",
                       "size": 46},
                      {"kind": "card", "at": "lex1b", "until": "lex1c", "x": 960, "y": 300,
                       "w": 900, "h": 260, "title": "Incoterms DO decide",
                       "body": "Carriage and its costs · export and import clearance · "
                               "where risk passes", "color": "#3bb273", "bs": 38},
                      {"kind": "card", "at": "lex1c", "x": 960, "y": 300, "w": 900, "h": 260,
                       "title": "Incoterms do NOT decide",
                       "body": "Transfer of ownership · payment terms · remedies for breach",
                       "color": "#e4572e", "bs": 38}]}),

    Scene("s2", "Two families of rules", "", [
        Pause("open", 1.0),
        Line("lex2a", "LEX", "There are eleven rules, in two families.", gap=0.3),
        Line("lex2b", "LEX", "Seven can be used for any mode of transport, or more than one: "
             "EXW, FCA, CPT, CIP, DAP, DPU and DDP.",
             say="Seven can be used for any mode of transport, or more than one: E.X.W., "
                 "F.C.A., C.P.T., C.I.P., D.A.P., D.P.U. and D.D.P.", gap=0.4),
        Line("lex2c", "LEX", "Four are only for sea and inland waterway: FAS, FOB, CFR and "
             "CIF.", say="Four are only for sea and inland waterway: F.A.S., F.O.B., C.F.R. "
             "and C.I.F.", gap=0.4),
        Line("lex2d", "LEX", "Always name the place, and the version. For example, CIP Dar "
             "es Salaam, Incoterms 2020.",
             say="Always name the place, and the version. For example, C.I.P. Dar es Salaam, "
                 "Inco-terms 2020.", gap=0.3),
        Line("nia2", "NIA", "E terms, F terms, C terms and D terms. The seller's job grows "
             "as the letters go up."),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio_teal", "heading": "Incoterms® 2020: eleven rules",
             "syl": "B1(c)", "ts": 36,
             "cols": [{"title": "Any mode (7)", "icon": "truck", "color": ANY, "at": "lex2b",
                       "items": [{"at": ["lex2b", 3.6], "text": "EXW · Ex Works"},
                                 {"at": ["lex2b", 4.4], "text": "FCA · Free Carrier"},
                                 {"at": ["lex2b", 5.2], "text": "CPT · Carriage Paid To"},
                                 {"at": ["lex2b", 6.0], "text": "CIP · Carriage and Insurance "
                                                               "Paid To"},
                                 {"at": ["lex2b", 6.8], "text": "DAP · Delivered at Place"},
                                 {"at": ["lex2b", 7.6], "text": "DPU · Delivered at Place "
                                                               "Unloaded"},
                                 {"at": ["lex2b", 8.6], "text": "DDP · Delivered Duty Paid"}]},
                      {"title": "Sea and waterway (4)", "icon": "ship", "color": SEA,
                       "at": "lex2c",
                       "items": [{"at": ["lex2c", 3.0], "text": "FAS · Free Alongside Ship"},
                                 {"at": ["lex2c", 3.8], "text": "FOB · Free On Board"},
                                 {"at": ["lex2c", 4.6], "text": "CFR · Cost and Freight"},
                                 {"at": ["lex2c", 5.6], "text": "CIF · Cost, Insurance and "
                                                               "Freight"}]}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia2"}],
             "pops": [{"kind": "chip", "at": "lex2d", "x": 1180, "y": 960,
                       "text": "Rule + named place + version", "color": "#e4572e",
                       "size": 36}]}),

    Scene("s3", "Any-mode rules on the map", "", [
        Pause("open", 1.4),
        Line("lex3a", "LEX", "EXW, Ex Works. The seller just makes the goods available at "
             "its own premises. The buyer loads, clears export, and bears all risk from "
             "there.", say="E.X.W., Ex Works. The seller just makes the goods available at "
             "its own premises. The buyer loads, clears export, and bears all risk from "
             "there.", gap=0.6),
        Line("lex3b", "LEX", "FCA, Free Carrier. The seller clears export and hands the "
             "goods to the buyer's carrier. Risk passes on that handover.",
             say="F.C.A., Free Carrier. The seller clears export and hands the goods to the "
                 "buyer's carrier. Risk passes on that handover.", gap=0.6),
        Line("lex3c", "LEX", "CPT, Carriage Paid To. The seller pays the carriage all the way "
             "to the named destination, but risk still passes when the goods reach the "
             "first carrier.", say="C.P.T., Carriage Paid To. The seller pays the carriage "
             "all the way to the named destination, but risk still passes when the goods "
             "reach the first carrier.", gap=0.6),
        Line("lex3d", "LEX", "CIP is the same, plus insurance. Under the 2020 rules, the "
             "seller must buy all-risks cover, for at least the price plus ten percent.",
             say="C.I.P. is the same, plus insurance. Under the 2020 rules, the seller must "
                 "buy all-risks cover, for at least the price plus ten percent.", gap=0.6),
        Line("lex3e", "LEX", "DAP, Delivered at Place. The seller bears the risk until the "
             "goods arrive, ready for unloading, at the named place.",
             say="D.A.P., Delivered at Place. The seller bears the risk until the goods "
                 "arrive, ready for unloading, at the named place.", gap=0.6),
        Line("lex3f", "LEX", "DPU, Delivered at Place Unloaded. The only rule where the "
             "seller must also unload the goods.",
             say="D.P.U., Delivered at Place Unloaded. The only rule where the seller must "
                 "also unload the goods.", gap=0.6),
        Line("lex3g", "LEX", "And DDP, Delivered Duty Paid. Maximum obligation for the "
             "seller, who even clears import and pays the duties.",
             say="And D.D.P., Delivered Duty Paid. Maximum obligation for the seller, who "
                 "even clears import and pays the duties."),
        Pause("hold", 1.8),
    ], spec={"tpl": "route", "heading": "Any mode of transport", "syl": "B1(c)",
             "terms": [{"at": "lex3a", "code": "EXW", "name": "Ex Works",
                        "note": "Buyer does almost everything", "risk": 0, "cost": 0,
                        "color": ANY},
                       {"at": "lex3b", "code": "FCA", "name": "Free Carrier",
                        "note": "Risk passes on handover to the carrier", "risk": 1,
                        "cost": 1, "color": ANY},
                       {"at": "lex3c", "code": "CPT", "name": "Carriage Paid To",
                        "note": "Seller pays carriage, risk passed at first carrier",
                        "risk": 1, "cost": 5, "color": "#7768ae"},
                       {"at": "lex3d", "code": "CIP", "name": "Carriage & Insurance Paid To",
                        "note": "Plus all-risks insurance (ICC A), 110%", "risk": 1,
                        "cost": 5, "color": "#7768ae", "insure": True},
                       {"at": "lex3e", "code": "DAP", "name": "Delivered at Place",
                        "note": "Risk passes on arrival, ready for unloading", "risk": 4.85,
                        "cost": 5, "color": "#e4572e"},
                       {"at": "lex3f", "code": "DPU", "name": "Delivered at Place Unloaded",
                        "note": "Seller unloads too", "risk": 5, "cost": 5,
                        "color": "#e4572e"},
                       {"at": "lex3g", "code": "DDP", "name": "Delivered Duty Paid",
                        "note": "Seller clears import and pays duties", "risk": 5,
                        "cost": 5, "color": "#e4572e"}]}),

    Scene("s4", "Sea-only rules on the map", "", [
        Pause("open", 1.4),
        Line("lex4a", "LEX", "Now the four sea rules. FAS, Free Alongside Ship. Risk passes "
             "when the goods are placed alongside the vessel at the port of shipment.",
             say="Now the four sea rules. F.A.S., Free Alongside Ship. Risk passes when the "
                 "goods are placed alongside the vessel at the port of shipment.", gap=0.6),
        Line("lex4b", "LEX", "FOB, Free On Board. The buyer books the ship. Risk passes once "
             "the goods are on board.",
             say="F.O.B., Free On Board. The buyer books the ship. Risk passes once the "
                 "goods are on board.", gap=0.6),
        Line("lex4c", "LEX", "CFR, Cost and Freight. The seller pays the freight to the "
             "destination port, but risk has already passed on board, at the port of "
             "shipment.", say="C.F.R., Cost and Freight. The seller pays the freight to the "
             "destination port, but risk has already passed on board, at the port of "
             "shipment.", gap=0.6),
        Line("lex4d", "LEX", "CIF adds insurance. But here the minimum is only basic cover, "
             "again for the price plus ten percent.",
             say="C.I.F. adds insurance. But here the minimum is only basic cover, again for "
                 "the price plus ten percent.", gap=0.6),
        Line("nia4", "NIA", "So with every C term, the seller pays further than it carries "
             "the risk. Two critical points!"),
        Pause("hold", 1.8),
    ], spec={"tpl": "route", "heading": "Sea and inland waterway only", "syl": "B1(c)",
             "terms": [{"at": "lex4a", "code": "FAS", "name": "Free Alongside Ship",
                        "note": "Risk passes alongside the vessel", "risk": 2, "cost": 2,
                        "color": SEA},
                       {"at": "lex4b", "code": "FOB", "name": "Free On Board",
                        "note": "Risk passes once on board", "risk": 3, "cost": 3,
                        "color": SEA},
                       {"at": "lex4c", "code": "CFR", "name": "Cost and Freight",
                        "note": "Freight paid to destination port, risk passed on board",
                        "risk": 3, "cost": 4, "color": "#7768ae"},
                       {"at": "lex4d", "code": "CIF", "name": "Cost, Insurance and Freight",
                        "note": "Plus minimum cover (ICC C), 110%", "risk": 3, "cost": 4,
                        "color": "#7768ae", "insure": True}],
             "pops": [{"kind": "chip", "at": "nia4", "x": 960, "y": 200,
                       "text": "C terms: two critical points", "color": "#e4572e",
                       "size": 40}]}),

    Scene("s5", "Exam traps", "", [
        Pause("open", 1.0),
        Line("aud5a", "AUDITOR", "Let me flag the classic exam traps.", gap=0.3),
        Sfx("pop"),
        Line("aud5b", "AUDITOR", "Under C terms, the seller pays to the destination, but risk "
             "passes at shipment.", gap=0.25),
        Sfx("pop"),
        Line("aud5c", "AUDITOR", "CIP needs all-risks insurance. CIF only needs minimum "
             "cover.", say="C.I.P. needs all-risks insurance. C.I.F. only needs minimum "
             "cover.", gap=0.25),
        Sfx("pop"),
        Line("aud5d", "AUDITOR", "Under EXW, the buyer clears export. Under DDP, the seller "
             "clears import.", say="Under E.X.W., the buyer clears export. Under D.D.P., the "
             "seller clears import.", gap=0.25),
        Sfx("pop"),
        Line("aud5e", "AUDITOR", "For goods in containers, FCA, CPT or CIP usually fit better "
             "than FOB, CFR or CIF.",
             say="For goods in containers, F.C.A., C.P.T. or C.I.P. usually fit better than "
                 "F.O.B., C.F.R. or C.I.F.", gap=0.25),
        Sfx("pop"),
        Line("aud5f", "AUDITOR", "And DPU is the only rule that makes the seller unload.",
             say="And D.P.U. is the only rule that makes the seller unload.", gap=0.4),
        Line("kito5", "KITO", "Our machines travel in containers, and I want them insured. "
             "So, CIP Dar es Salaam!",
             say="Our machines travel in containers, and I want them insured. So, C.I.P. "
                 "Dar es Salaam!"),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "heading": "Five classic traps", "syl": "B1(c)",
             "row": 122, "ts": 40,
             "items": [{"at": "aud5b", "text": "C terms: pay far, risk passes early",
                        "icon": "warning", "color": "#e4572e"},
                       {"at": "aud5c", "text": "CIP = all-risks · CIF = minimum cover",
                        "icon": "umbrella", "color": "#3bb273"},
                       {"at": "aud5d", "text": "EXW: buyer exports · DDP: seller imports",
                        "icon": "stamp", "color": "#7768ae"},
                       {"at": "aud5e", "text": "Containers? Prefer FCA, CPT, CIP",
                        "icon": "container", "color": "#2b86c5"},
                       {"at": "aud5f", "text": "DPU: the only rule where seller unloads",
                        "icon": "box", "color": "#f2a541"}],
             "cast": [{"who": "AUDITOR", "x": 250, "pose": "clipboard",
                       "talk_pose": "clipboard"},
                      {"who": "KITO", "x": 1800, "s": 0.55, "y": 1120, "enter": "kito5",
                       "mood": "excited"}]}),

    quiz_scene("s6", "Quick check",
               "Under FOB, when does risk pass from seller to buyer?",
               ["At the seller's premises", "When the goods are on board the vessel",
                "On arrival at the destination port", "When the buyer unloads the goods"], 1,
               "Quick check. Under F.O.B., when does risk pass from seller to buyer?",
               "When the goods are on board the vessel.",
               why=("FOB: the buyer books the ship; risk passes once the goods are on board",
                    "Under F.O.B., the buyer books the ship, and risk passes once the goods "
                    "are on board."),
               syl="B1(c)"),

    quiz_scene("s7", "Quick check",
               "Which rule puts the maximum obligation on the seller, including import "
               "duties?",
               ["EXW", "CIF", "DAP", "DDP"], 3,
               "And which rule puts the maximum obligation on the seller, including import "
               "duties?",
               "D.D.P., Delivered Duty Paid.",
               why="EXW is the opposite: the minimum obligation for the seller",
               think=4.0, syl="B1(c)"),

    recap_scene("s8", [
        ("Incoterms come from the ICC.", "ICC rules · Incoterms® 2020",
         "Inco-terms come from the I.C.C."),
        ("They cover costs, clearance and risk, not ownership.",
         "Costs · clearance · risk (not title)"),
        ("Seven any-mode rules, four sea rules.", "7 any mode · 4 sea"),
        ("C terms have two critical points.", "C terms: 2 critical points"),
        ("CIP all-risks, CIF minimum cover.", "CIP all-risks · CIF minimum",
         "C.I.P. all-risks, C.I.F. minimum cover."),
    ], [
        Line("lex8", "LEX", "Next time, the machines arrive. What exactly must the seller "
             "deliver, and what can the buyer do if they are not right?", gap=0.3),
        Line("hans8", "HANS", "My machines are always perfect!", gap=0.3),
        Line("kito8", "KITO", "We'll see about that.", gap=0.6),
    ], next_ep=7, next_title="The Seller's Promise", next_icon="box"),
]
