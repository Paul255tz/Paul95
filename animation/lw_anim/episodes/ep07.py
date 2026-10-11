"""Episode 7 - The Seller's Promise.

Syllabus B2(a): the seller's obligations under the CISG: delivery and
documents (Arts 30-34), conformity and third-party claims (Arts 35-44), and the
buyer's remedies for the seller's breach (Arts 45-52). Setting: the machines
arrive at SafariTech in Dar es Salaam; one keeps failing and one is the wrong
model.
"""
from ._kit import (DISPLAY_NAMES, SERIES, VOICES, Line, Pause, Scene, Sfx,  # noqa: F401
                   quiz_scene, recap_scene, title_scene)

EPISODE = "Episode 7"
EPISODE_TITLE = "The Seller's Promise"
SLUG = "episode07_the_sellers_promise"

SCENES = [
    title_scene(7, EPISODE_TITLE, "Syllabus B2(a)", ("box", "check")),

    Scene("s1", "Unboxing day", "", [
        Pause("open", 1.0),
        Sfx("whoosh"),
        Line("kito1", "KITO", "Five machines arrived. Machine two keeps jamming, and machine "
             "five is the wrong model!", gap=0.4),
        Line("nia1", "NIA", "Before we shout at Hans, let's check what the CISG says the "
             "seller actually promised.", gap=0.3),
        Line("lex1", "LEX", "Good instinct. The seller has three core duties: deliver the "
             "goods, hand over any documents, and transfer the property in the goods, all "
             "as the contract requires."),
        Pause("hold", 1.2),
    ], spec={"tpl": "talk", "bg": "office", "syl": "B2(a)",
             "cast": [{"who": "KITO", "x": 1460, "y": 1030, "s": 0.95, "mood": "angry",
                       "talk_pose": "demand"},
                      {"who": "NIA", "x": 960, "y": 1030, "s": 0.92},
                      {"who": "LEX", "x": 420, "y": 1030, "s": 0.9, "enter": "lex1",
                       "from": "left"}],
             "pops": [{"kind": "icon", "icon": "box", "x": 1020, "y": 300, "s": 1.0,
                       "at": ["kito1", 0.3], "until": "lex1", "label": "Machine 2: jams"},
                      {"kind": "icon", "icon": "box", "x": 1520, "y": 300, "s": 1.0,
                       "at": ["kito1", 2.3], "until": "lex1", "label": "Machine 5: wrong "
                                                                       "model",
                       "color": "#e4572e"},
                      {"kind": "card", "at": ["lex1", 2.0], "x": 1190, "y": 300, "w": 860,
                       "h": 220, "title": "Article 30: the seller must…",
                       "body": "deliver the goods · hand over documents · transfer the "
                               "property", "color": "#0f8b8d", "bs": 38}]}),

    Scene("s2", "Where is delivery?", "", [
        Pause("open", 1.0),
        Line("lex2a", "LEX", "If the contract names a place of delivery, deliver there. If "
             "not, the Convention fills the gap.", gap=0.3),
        Sfx("pop"),
        Line("lex2b", "LEX", "If the contract involves carriage, the seller delivers by "
             "handing the goods to the first carrier.", gap=0.25),
        Sfx("pop"),
        Line("lex2c", "LEX", "If the goods are specific, or come from a known stock or "
             "factory, the seller places them at the buyer's disposal at that place.",
             gap=0.25),
        Sfx("pop"),
        Line("lex2d", "LEX", "Otherwise, at the seller's own place of business.", gap=0.5),
        Line("lex2e", "LEX", "If unidentified goods are shipped, the seller must notify the "
             "buyer which goods are his, and arrange appropriate carriage. Perishable goods "
             "need a suitable carrier.", gap=0.4),
        Line("lex2f", "LEX", "Timing: on the date fixed, within any agreed period, or else "
             "within a reasonable time after the contract. And documents must be handed "
             "over at the time, place and in the form agreed."),
        Pause("hold", 1.4),
    ], spec={"tpl": "flow", "bg": "studio_teal", "heading": "Place of delivery (Art 31)",
             "syl": "B2(a)(i)",
             "nodes": [{"id": "q", "x": 1150, "y": 260, "label": "No place agreed?",
                        "icon": "question", "color": "#1f3a5f", "at": "lex2a", "w": 300},
                       {"id": "a", "x": 680, "y": 640, "label": "Carriage involved → hand to "
                                                               "first carrier",
                        "icon": "truck", "color": "#0f8b8d", "at": "lex2b", "w": 330,
                        "h": 220},
                       {"id": "b", "x": 1150, "y": 640, "label": "Specific / known stock → "
                                                                "at buyer's disposal there",
                        "icon": "warehouse", "color": "#7768ae", "at": "lex2c", "w": 330,
                        "h": 220},
                       {"id": "c", "x": 1620, "y": 640, "label": "Otherwise → seller's place "
                                                                "of business",
                        "icon": "factory", "color": "#e4572e", "at": "lex2d", "w": 330,
                        "h": 220}],
             "edges": [{"from": "q", "to": "a", "at": "lex2b"},
                       {"from": "q", "to": "b", "at": "lex2c"},
                       {"from": "q", "to": "c", "at": "lex2d"}],
             "cast": [{"who": "LEX", "x": 250}],
             "pops": [{"kind": "card", "at": "lex2e", "until": "lex2f", "x": 1150, "y": 470,
                       "w": 900, "h": 270, "title": "Arts 32: shipping duties",
                       "body": "Notify the consignment · appropriate carriage · suitable "
                               "carrier for perishables", "color": "#2b86c5", "dim": True,
                       "bs": 38},
                      {"kind": "card", "at": "lex2f", "x": 1150, "y": 470, "w": 900, "h": 270,
                       "title": "Arts 33–34: time and documents",
                       "body": "Fixed date · agreed period · or reasonable time. Documents as "
                               "agreed.", "color": "#f2a541", "dim": True, "bs": 38}]}),

    Scene("s3", "Conforming goods", "", [
        Pause("open", 1.0),
        Line("lex3a", "LEX", "The goods must match the contract in quantity, quality and "
             "description, and be packaged as the contract requires.", gap=0.3),
        Line("lex3b", "LEX", "Unless agreed otherwise, they must also meet four implied "
             "standards.", gap=0.3),
        Sfx("pop"),
        Line("lex3c", "LEX", "Fit for the purposes such goods are ordinarily used for.",
             gap=0.25),
        Sfx("pop"),
        Line("lex3d", "LEX", "Fit for any particular purpose the buyer made known, unless "
             "the buyer did not rely on the seller's skill.", gap=0.25),
        Sfx("pop"),
        Line("lex3e", "LEX", "Match any sample or model the seller showed.", gap=0.25),
        Sfx("pop"),
        Line("lex3f", "LEX", "And be packed in the usual way, or adequately to protect them.",
             gap=0.5),
        Line("lex3g", "LEX", "The seller is not liable if the buyer knew of the defect when "
             "contracting. But the seller is liable for any defect that existed when risk "
             "passed, even if it only shows up later.", gap=0.4),
        Line("nia3", "NIA", "So machine five, the wrong model, fails the description test."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "white", "layout": "grid", "cols": 2,
             "heading": "Conformity (Arts 35–36)", "syl": "B2(a)(ii)", "cell_h": 300,
             "ts": 38,
             "items": [{"at": "lex3c", "text": "Fit for ordinary purposes", "icon": "check",
                        "color": "#3bb273"},
                       {"at": "lex3d", "text": "Fit for a particular purpose made known",
                        "icon": "bulb", "color": "#f2a541"},
                       {"at": "lex3e", "text": "Matches sample or model", "icon": "magnifier",
                        "color": "#7768ae"},
                       {"at": "lex3f", "text": "Usual or adequate packaging", "icon": "box",
                        "color": "#2b86c5"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia3"}],
             "pops": [{"kind": "card", "at": "lex3a", "until": "lex3b", "x": 1190, "y": 470,
                       "w": 900, "h": 260, "title": "Express terms first",
                       "body": "Quantity · quality · description · packaging as the contract "
                               "requires", "color": "#0f8b8d", "bs": 40},
                      {"kind": "card", "at": "lex3g", "until": "nia3", "x": 1190, "y": 470,
                       "w": 940, "h": 300, "title": "Timing of the defect",
                       "body": "Seller liable if the defect existed when risk passed, even if "
                               "it appears later. Not if the buyer knew at the start.",
                       "color": "#e4572e", "dim": True, "bs": 36}]}),

    Scene("s4", "Examine and notify", "", [
        Pause("open", 1.0),
        Line("lex4a", "LEX", "Now the buyer's homework. Miss it, and the remedies vanish.",
             gap=0.3),
        Sfx("pop"),
        Line("lex4b", "LEX", "On delivery, the buyer must examine the goods within as short "
             "a period as is practicable. If the goods are sent straight on, examination can "
             "wait until they reach the new destination.", gap=0.25),
        Sfx("pop"),
        Line("lex4c", "LEX", "Then give the seller notice of the defect, specifying its "
             "nature, within a reasonable time of discovering it, or when it ought to have "
             "been discovered.", gap=0.25),
        Sfx("pop"),
        Line("lex4d", "LEX", "And there is a long stop. No notice within two years of "
             "delivery means the right is lost, unless a longer guarantee applies.", gap=0.4),
        Line("lex4e", "LEX", "One exception: if the seller knew of the defect and kept "
             "quiet, the seller cannot rely on late notice.", gap=0.4),
        Line("kito4", "KITO", "Nia, email Hans today, and describe exactly how machine two "
             "jams!"),
        Pause("hold", 1.4),
    ], spec={"tpl": "timeline", "bg": "studio", "heading": "The buyer's clock (Arts 38–40)",
             "syl": "B2(a)(ii)", "cw": 330,
             "events": [{"at": "lex4a", "label": "Delivery", "icon": "truck",
                         "color": "#0f8b8d"},
                        {"at": "lex4b", "label": "Examine", "sub": "As soon as practicable",
                         "icon": "magnifier", "color": "#7768ae"},
                        {"at": "lex4c", "label": "Notify seller", "sub": "Reasonable time, "
                                                                       "specify the defect",
                         "icon": "envelope", "color": "#f2a541"},
                        {"at": "lex4d", "label": "2-year long stop",
                         "sub": "Unless a longer guarantee", "icon": "hourglass",
                         "color": "#e4572e"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "KITO", "x": 1810, "s": 0.55, "y": 1120, "enter": "kito4"}],
             "pops": [{"kind": "chip", "at": "lex4e", "x": 1200, "y": 960,
                       "text": "Seller knew and stayed silent? Can't rely on late notice",
                       "color": "#1f3a5f", "size": 32}]}),

    Scene("s5", "Free from third-party claims", "", [
        Pause("open", 1.0),
        Sfx("whoosh"),
        Pause("amara_in", 0.6),
        Line("amara5", "AMARA", "One more check from the bank's side. Does anyone else claim "
             "these machines, or the technology inside them?", gap=0.4),
        Line("lex5a", "LEX", "Good question. The seller must deliver goods free from any "
             "right or claim of a third party, unless the buyer agreed to take them subject "
             "to it.", gap=0.3),
        Line("lex5b", "LEX", "For intellectual property, such as patents, trade marks and "
             "copyright, the seller is liable for rights it knew of, or could not have been "
             "unaware of.", gap=0.3),
        Line("lex5c", "LEX", "That means rights under the law of the country where the goods "
             "will be resold or used, if both parties contemplated it, or otherwise the "
             "buyer's own country.", gap=0.3),
        Line("lex5d", "LEX", "But not if the buyer already knew of the right, or if the "
             "problem came from the buyer's own designs or specifications.", gap=0.3),
        Line("amara5b", "AMARA", "And the buyer must notify any claim within a reasonable "
             "time."),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "bank", "heading": "Third-party claims (Arts 41–43)",
             "syl": "B2(a)(ii)", "ts": 34,
             "cols": [{"title": "Seller liable", "icon": "check", "color": "#0f8b8d",
                       "at": "lex5a",
                       "items": [{"at": ["lex5a", 0.4], "text": "Goods free of third-party "
                                                               "rights and claims"},
                                 {"at": "lex5b", "text": "IP rights the seller knew or "
                                                         "could not be unaware of"},
                                 {"at": "lex5c", "text": "Under the law of the resale or "
                                                         "use country, else the buyer's"}]},
                      {"title": "Seller not liable", "icon": "cross", "color": "#e4572e",
                       "at": "lex5d",
                       "items": [{"at": ["lex5a", 4.0], "text": "Buyer agreed to take the "
                                                               "goods subject to the claim",
                                  "bad": True},
                                 {"at": ["lex5d", 0.4], "text": "Buyer already knew of the "
                                                               "IP right", "bad": True},
                                 {"at": ["lex5d", 2.6], "text": "Caused by the buyer's own "
                                                               "designs or specifications",
                                  "bad": True}]}],
             "vs": True,
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "AMARA", "x": 1810, "s": 0.6, "y": 1120, "enter": "amara_in"}]}),

    Scene("s6", "The buyer's remedies", "", [
        Pause("open", 1.0),
        Line("lex6a", "LEX", "If the seller breaches, the buyer has a toolkit.", gap=0.3),
        Sfx("pop"),
        Line("lex6b", "LEX", "Require performance. Substitute goods only if the defect is a "
             "fundamental breach, and repair if that is reasonable.", gap=0.25),
        Sfx("pop"),
        Line("lex6c", "LEX", "Fix an additional period of reasonable length for the seller "
             "to perform.", gap=0.25),
        Sfx("pop"),
        Line("lex6d", "LEX", "Avoid the contract, by notice, for a fundamental breach, or "
             "for non-delivery within the additional period.", gap=0.25),
        Sfx("pop"),
        Line("lex6e", "LEX", "Reduce the price in proportion to the defect.", gap=0.25),
        Sfx("pop"),
        Line("lex6f", "LEX", "And claim damages, which can be added to any other remedy.",
             gap=0.5),
        Line("lex6g", "LEX", "A breach is fundamental if it substantially deprives the other "
             "party of what it was entitled to expect. And the seller may still cure, "
             "without unreasonable delay or inconvenience, even after the delivery date.",
             gap=0.4),
        Line("nia6", "NIA", "So for machine two, we ask for repair. For machine five, a "
             "replacement, if the wrong model is a fundamental breach."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "heading": "Buyer's remedies (Arts 45–52)",
             "syl": "B2(a)(iii)", "row": 118, "ts": 40,
             "items": [{"at": "lex6b", "text": "Require performance",
                        "sub": "Substitute only if fundamental · repair if reasonable",
                        "icon": "check", "color": "#3bb273"},
                       {"at": "lex6c", "text": "Fix an additional period",
                        "sub": "Reasonable length", "icon": "calendar", "color": "#2b86c5"},
                       {"at": "lex6d", "text": "Avoid the contract",
                        "sub": "Fundamental breach, by notice", "icon": "scissors",
                        "color": "#e4572e"},
                       {"at": "lex6e", "text": "Reduce the price",
                        "sub": "In proportion to the defect", "icon": "percent",
                        "color": "#f2a541"},
                       {"at": "lex6f", "text": "Damages", "sub": "On top of any other remedy",
                        "icon": "moneybag", "color": "#7768ae"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia6"}],
             "pops": [{"kind": "card", "at": "lex6g", "until": "nia6", "x": 1190, "y": 470,
                       "w": 940, "h": 300, "title": "Fundamental breach (Art 25)",
                       "body": "Substantially deprives the other party of what it was "
                               "entitled to expect. Seller may still cure (Art 48).",
                       "color": "#1f3a5f", "dim": True, "bs": 36}]}),

    Scene("s7", "Too early, too much", "", [
        Pause("open", 1.0),
        Line("lex7a", "LEX", "Two more situations come up in exams.", gap=0.3),
        Line("lex7b", "LEX", "If the seller delivers before the date, the buyer may take "
             "delivery, or refuse it. And if goods are short, the seller may make up the "
             "shortfall up to the delivery date, if that causes no unreasonable "
             "inconvenience. The buyer keeps any right to damages.", gap=0.4),
        Line("lex7c", "LEX", "If the seller delivers more than agreed, the buyer may refuse "
             "the excess, or keep some or all of it, paying for it at the contract rate.",
             gap=0.4),
        Line("kito7", "KITO", "So if Hans sends six machines, I can keep the sixth, but I "
             "pay the contract price for it."),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio_purple", "heading": "Early and excess delivery "
                                                                  "(Arts 37, 52)",
             "syl": "B2(a)", "ts": 34,
             "cols": [{"title": "Early delivery", "icon": "clock", "color": "#2b86c5",
                       "at": "lex7b",
                       "items": [{"at": ["lex7b", 0.6], "text": "Buyer may accept or refuse"},
                                 {"at": ["lex7b", 4.0], "text": "Seller may cure a shortfall "
                                                               "up to the date"},
                                 {"at": ["lex7b", 9.0], "text": "Buyer keeps any damages "
                                                               "claim"}]},
                      {"title": "Excess quantity", "icon": "box", "color": "#f2a541",
                       "at": "lex7c",
                       "items": [{"at": ["lex7c", 0.6], "text": "Refuse the excess"},
                                 {"at": ["lex7c", 3.0], "text": "Or keep some or all of it"},
                                 {"at": ["lex7c", 5.0], "text": "Pay for it at the contract "
                                                               "rate"}]}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "KITO", "x": 1810, "s": 0.55, "y": 1120, "enter": "kito7"}]}),

    quiz_scene("s8", "Quick check",
               "A buyer first notices a hidden defect 30 months after delivery. There is no "
               "guarantee, and the seller did not know of the defect. What is the position?",
               ["The buyer can still claim, as the defect was hidden",
                "The buyer has lost the right to rely on the lack of conformity",
                "The buyer can only reduce the price", "The contract is automatically void"],
               1,
               "Quick check. A buyer first notices a hidden defect thirty months after "
               "delivery. No guarantee, and the seller did not know. What is the position?",
               "The buyer has lost the right to rely on it.",
               why=("Article 39: notice must be given within two years of delivery at most",
                    "Article 39 sets a two-year long stop for giving notice."),
               syl="B2(a)(ii)"),

    quiz_scene("s9", "Quick check",
               "When can the buyer demand substitute goods?",
               ["Whenever any defect appears", "Only if the defect is a fundamental breach",
                "Only if the seller agrees", "Never; only damages are available"], 1,
               "And when can the buyer demand substitute goods?",
               "Only if the defect amounts to a fundamental breach.",
               why="Otherwise the buyer can ask for repair, reduce the price or claim damages",
               think=4.0, syl="B2(a)(iii)"),

    recap_scene("s10", [
        ("Deliver, hand over documents, transfer property.", "Deliver · documents · property"),
        ("Place of delivery: carrier, disposal, or seller's place.",
         "Delivery: first carrier · disposal · seller's place"),
        ("Conformity: fit, sample, packaging.", "Conformity: fit · sample · packaging"),
        ("Examine, notify, two-year long stop.", "Examine · notify · 2-year long stop"),
        ("Remedies: perform, extra time, avoid, reduce, damages.",
         "Perform · extra time · avoid · reduce · damages"),
    ], [
        Line("lex10", "LEX", "Next time, we switch sides. What does the buyer owe, and what "
             "can Hans do if SafariTech doesn't pay?", gap=0.3),
        Line("hans10", "HANS", "Finally, my side of the story!", gap=0.6),
    ], next_ep=8, next_title="The Buyer's Side", next_icon="moneybag"),
]
