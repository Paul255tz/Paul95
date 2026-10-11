"""Episode 10 - Risk on the Water.

Syllabus B2(c)(v)-(vi) and B2(d): effects of avoidance (Arts 81-84),
preservation of the goods (Arts 85-88) and the passing of risk (Arts 66-70).
Setting: a storm in the Indian Ocean damages a container on its way from
Hamburg to Dar es Salaam.
"""
from ._kit import (DISPLAY_NAMES, SERIES, VOICES, Line, Pause, Scene, Sfx,  # noqa: F401
                   quiz_scene, recap_scene, title_scene)

EPISODE = "Episode 10"
EPISODE_TITLE = "Risk on the Water"
SLUG = "episode10_risk_on_the_water"

SCENES = [
    title_scene(10, EPISODE_TITLE, "Syllabus B2(c)–(d)", ("ship", "umbrella")),

    Scene("s1", "Storm at sea", "", [
        Pause("open", 1.2),
        Sfx("horn"),
        Line("cargo1", "CARGO", "Mayday! A storm off the coast, and three crates of parts "
             "are soaked!", gap=0.4),
        Line("kito1", "KITO", "Then Hans pays. They were his parts until they reached us!",
             gap=0.4),
        Line("lex1", "LEX", "Not necessarily. The question is when risk passed. Once risk "
             "has passed to the buyer, loss or damage does not stop the buyer having to pay "
             "the price.", gap=0.3),
        Line("lex1b", "LEX", "Unless the loss was caused by an act or omission of the "
             "seller."),
        Pause("hold", 1.2),
    ], spec={"tpl": "talk", "bg": "port", "syl": "B2(d)",
             "cast": [{"who": "CARGO", "x": 1500, "y": 980, "s": 0.9, "mood": "worried"},
                      {"who": "KITO", "x": 360, "y": 1060, "s": 0.85, "mood": "angry",
                       "talk_pose": "demand"},
                      {"who": "LEX", "x": 700, "y": 1060, "s": 0.85, "enter": "lex1",
                       "from": "left"}],
             "pops": [{"kind": "card", "at": "lex1", "x": 1180, "y": 260, "w": 900, "h": 240,
                       "title": "Article 66",
                       "body": "Loss after risk passes: buyer still pays, unless the seller "
                               "caused it", "color": "#1f3a5f", "bs": 38}]}),

    Scene("s2", "When risk passes", "", [
        Pause("open", 1.4),
        Line("lex2a", "LEX", "If the contract involves carriage, and the seller need not "
             "hand the goods over at a particular place, risk passes when they are handed to "
             "the first carrier.", gap=0.6),
        Line("lex2b", "LEX", "If the seller must hand them to a carrier at a particular "
             "place, such as the port of Hamburg, risk passes there.", gap=0.6),
        Line("lex2c", "LEX", "If goods are sold while already in transit, risk generally "
             "passes when the contract is made. Unless the seller already knew they were "
             "lost or damaged, and kept quiet.", gap=0.6),
        Line("lex2d", "LEX", "In other cases, risk passes when the buyer takes over the "
             "goods. Or, if the buyer delays, when they are placed at its disposal.",
             gap=0.6),
        Line("nia2", "NIA", "And keeping the documents, like the bill of lading, doesn't "
             "stop risk passing. But the goods must be clearly identified to the contract."),
        Pause("hold", 1.6),
    ], spec={"tpl": "route", "heading": "Passing of risk (Arts 67–69)", "syl": "B2(d)",
             "terms": [{"at": "lex2a", "code": "Art 67", "name": "Carriage involved",
                        "note": "Risk passes to the first carrier", "risk": 1, "cost": 1,
                        "color": "#0f8b8d"},
                       {"at": "lex2b", "code": "Art 67", "name": "Carrier at a named place",
                        "note": "Risk passes at that place (e.g. the port)", "risk": 2,
                        "cost": 2, "color": "#0f8b8d"},
                       {"at": "lex2c", "code": "Art 68", "name": "Goods sold in transit",
                        "note": "Risk passes when the contract is made", "risk": 3.5,
                        "cost": 3.5, "color": "#7768ae"},
                       {"at": "lex2d", "code": "Art 69", "name": "Other cases",
                        "note": "When the buyer takes over the goods", "risk": 5,
                        "cost": 5, "color": "#e4572e"}],
             "pops": [{"kind": "chip", "at": "nia2", "x": 960, "y": 200,
                       "text": "Goods must be clearly identified to the contract",
                       "color": "#1f3a5f", "size": 34}]}),

    Scene("s3", "Risk and fundamental breach", "", [
        Pause("open", 1.0),
        Line("lex3a", "LEX", "One more rule. If the seller has committed a fundamental "
             "breach, the passing of risk does not take away the buyer's remedies.",
             gap=0.3),
        Line("lex3b", "LEX", "So if the parts were also the wrong specification, SafariTech "
             "could still avoid the contract, even though risk had passed.", gap=0.4),
        Line("kito3", "KITO", "So for the soaked crates: risk passed to us in Hamburg. That's "
             "a claim on our insurance, not on Hans.", gap=0.3),
        Line("lex3c", "LEX", "Exactly. And that is why the insurance in the Incoterm "
             "matters."),
        Pause("hold", 1.2),
    ], spec={"tpl": "talk", "bg": "harbour", "syl": "B2(d)",
             "cast": [{"who": "LEX", "x": 420, "y": 1030, "s": 0.9},
                      {"who": "KITO", "x": 1100, "y": 1030, "s": 0.92, "mood": "thinking"},
                      {"who": "NIA", "x": 1550, "y": 1030, "s": 0.88}],
             "pops": [{"kind": "card", "at": "lex3a", "until": "kito3", "x": 1100, "y": 280,
                       "w": 900, "h": 240, "title": "Article 70",
                       "body": "Fundamental breach by the seller: buyer keeps its remedies, "
                               "even after risk passes", "color": "#e4572e", "bs": 36},
                      {"kind": "icon", "icon": "umbrella", "x": 1100, "y": 300, "s": 1.4,
                       "at": "kito3", "color": "#3bb273", "label": "Insurance claim"}]}),

    Scene("s4", "After avoidance", "", [
        Pause("open", 1.0),
        Line("lex4a", "LEX", "When a contract is avoided, both parties are released from "
             "their obligations.", gap=0.3),
        Sfx("pop"),
        Line("lex4b", "LEX", "But damages for the breach survive, and so does any dispute "
             "resolution clause, like an arbitration clause.", gap=0.25),
        Sfx("pop"),
        Line("lex4c", "LEX", "A party that has performed can claim back what it supplied or "
             "paid. Both sides make restitution at the same time.", gap=0.25),
        Sfx("pop"),
        Line("lex4d", "LEX", "A seller refunding the price must pay interest on it. A buyer "
             "returning goods must account for any benefit it got from them.", gap=0.25),
        Sfx("pop"),
        Line("lex4e", "LEX", "And a buyer who cannot return the goods in substantially the "
             "condition received generally loses the right to avoid, or to demand "
             "substitutes.", gap=0.4),
        Line("nia4", "NIA", "Unless that's not the buyer's fault, or the goods were used or "
             "sold normally before the defect was found."),
        Pause("hold", 1.4),
    ], spec={"tpl": "flow", "bg": "studio_teal", "heading": "Effects of avoidance (Arts 81–84)",
             "syl": "B2(c)(v)",
             "nodes": [{"id": "av", "x": 1150, "y": 250, "label": "Contract avoided",
                        "icon": "scissors", "color": "#e4572e", "at": "lex4a", "w": 320},
                       {"id": "rel", "x": 640, "y": 560, "label": "Both released from "
                                                                 "obligations",
                        "icon": "door", "color": "#0f8b8d", "at": ["lex4a", 1.5], "w": 300},
                       {"id": "sur", "x": 1000, "y": 620, "label": "Damages + dispute "
                                                                  "clause survive",
                        "icon": "shield", "color": "#7768ae", "at": "lex4b", "w": 300},
                       {"id": "res", "x": 1340, "y": 620, "label": "Mutual restitution",
                        "icon": "handshake", "color": "#3bb273", "at": "lex4c", "w": 300},
                       {"id": "int", "x": 1680, "y": 560, "label": "Interest on refunds · "
                                                                  "account for benefits",
                        "icon": "percent", "color": "#f2a541", "at": "lex4d", "w": 300}],
             "edges": [{"from": "av", "to": "rel", "at": ["lex4a", 1.4], "bend": -30},
                       {"from": "av", "to": "sur", "at": "lex4b"},
                       {"from": "av", "to": "res", "at": "lex4c"},
                       {"from": "av", "to": "int", "at": "lex4d", "bend": 30}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia4"}],
             "pops": [{"kind": "chip", "at": "lex4e", "x": 1180, "y": 900,
                       "text": "Can't return goods in substantially the same condition? "
                               "Usually no avoidance", "color": "#1f3a5f", "size": 28}]}),

    Scene("s5", "Preserving the goods", "", [
        Pause("open", 1.0),
        Line("lex5a", "LEX", "Whoever holds the goods must look after them, even when the "
             "other side is at fault.", gap=0.3),
        Line("lex5b", "LEX", "If the buyer delays taking delivery, or fails to pay when "
             "payment and delivery are due together, the seller must take reasonable steps "
             "to preserve the goods. It can keep them until its expenses are repaid.",
             gap=0.4),
        Line("lex5c", "LEX", "If the buyer has received the goods and intends to reject "
             "them, the buyer must preserve them. The same applies to goods put at its "
             "disposal at the destination, if it can take them without paying and without "
             "unreasonable inconvenience.", gap=0.4),
        Line("lex5d", "LEX", "Either party may store the goods in a third party's "
             "warehouse, at the other side's expense, if the cost is reasonable.", gap=0.3),
        Line("lex5e", "LEX", "If the other side delays unreasonably, the goods may be sold, "
             "with reasonable notice. And perishable goods, or goods that are expensive to "
             "keep, must be sold. The seller keeps its reasonable costs, and accounts for "
             "the balance.", gap=0.4),
        Line("cargo5", "CARGO", "So nobody gets to leave me rotting on the quay!"),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "port", "heading": "Preservation of goods (Arts 85–88)",
             "syl": "B2(c)(vi)", "ts": 32, "top": 150,
             "cols": [{"title": "Seller preserves", "icon": "factory", "color": "#0f8b8d",
                       "at": "lex5b",
                       "items": [{"at": ["lex5b", 0.5], "text": "Buyer delays taking delivery"},
                                 {"at": ["lex5b", 3.0], "text": "Or doesn't pay when due "
                                                               "with delivery"},
                                 {"at": ["lex5b", 8.5], "text": "May keep goods until costs "
                                                               "repaid"}]},
                      {"title": "Buyer preserves", "icon": "warehouse", "color": "#7768ae",
                       "at": "lex5c",
                       "items": [{"at": ["lex5c", 0.5], "text": "Received goods and means to "
                                                               "reject"},
                                 {"at": ["lex5c", 5.0], "text": "Goods at its disposal at "
                                                               "destination (if no payment "
                                                               "or undue hassle)"}]},
                      {"title": "Either may", "icon": "box", "color": "#e4572e",
                       "at": "lex5d",
                       "items": [{"at": ["lex5d", 0.4], "text": "Store with a third party, "
                                                               "at the other's expense"},
                                 {"at": ["lex5e", 0.4], "text": "Sell after unreasonable "
                                                               "delay, with notice"},
                                 {"at": ["lex5e", 4.0], "text": "MUST sell perishables"},
                                 {"at": ["lex5e", 9.0], "text": "Keep costs, account for "
                                                               "balance"}]}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "CARGO", "x": 1800, "y": 1060, "s": 0.5, "enter": "cargo5"}]}),

    quiz_scene("s6", "Quick check",
               "Goods are sold while already at sea. No special terms apply, and the seller "
               "did not know of any damage. When does risk generally pass?",
               ["When the goods were first loaded", "When the contract is made",
                "When the ship docks", "When the buyer inspects the goods"], 1,
               "Quick check. Goods are sold while already at sea. When does risk generally "
               "pass?",
               "When the contract is made.",
               why=("Article 68, unless circumstances show it passed on handover to the "
                    "carrier", "That's Article 68. Sometimes the circumstances show it "
                                "passed earlier, on handover to the carrier."),
               syl="B2(d)"),

    quiz_scene("s7", "Quick check",
               "A buyer rightly rejects a shipment of fresh fish in Dar es Salaam. The "
               "seller is in Mombasa and cannot be reached. What must the buyer do?",
               ["Leave the fish on the quay", "Destroy the fish immediately",
                "Take reasonable steps to sell them", "Ship them back at once"], 2,
               "And this one. A buyer rightly rejects fresh fish, and the seller cannot be "
               "reached. What must the buyer do?",
               "Take reasonable steps to sell them.",
               why="Article 88: perishable goods must be sold; keep costs, account for the rest",
               think=4.0, syl="B2(c)(vi)"),

    recap_scene("s8", [
        ("Risk passed? Buyer still pays.", "Risk passed → buyer still pays"),
        ("Carriage: first carrier, or the named place.", "First carrier / named place"),
        ("In transit: when the contract is made.", "In transit: at the contract"),
        ("Avoidance: release and restitution.", "Avoidance: release · restitution"),
        ("Preserve the goods; sell perishables.", "Preserve · sell perishables"),
    ], [
        Line("lex8", "LEX", "That completes the Sales Convention. Next time, the paperwork "
             "that moves goods and money around the world: bills of lading, and bills of "
             "exchange.", gap=0.3),
        Line("cargo8", "CARGO", "My favourite piece of paper is the bill of lading!", gap=0.6),
    ], next_ep=11, next_title="Paper That Moves the World", next_icon="bill"),
]
