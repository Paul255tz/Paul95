"""Episode 8 - The Buyer's Side.

Syllabus B2(b): the buyer's obligations under the CISG: payment of the price
(Arts 53-59), taking delivery (Art 60), and the seller's remedies for the
buyer's breach (Arts 61-65). Also retention-of-title ("Romalpa") clauses.
Setting: Hans has not been paid; Kito wants to hold back the whole price.
"""
from ._kit import (DISPLAY_NAMES, SERIES, VOICES, Line, Pause, Scene, Sfx,  # noqa: F401
                   quiz_scene, recap_scene, title_scene)

EPISODE = "Episode 8"
EPISODE_TITLE = "The Buyer's Side"
SLUG = "episode08_the_buyers_side"

SCENES = [
    title_scene(8, EPISODE_TITLE, "Syllabus B2(b)", ("moneybag", "handshake")),

    Scene("s1", "The unpaid invoice", "", [
        Pause("open", 1.0),
        Line("hans1", "HANS", "Kito, my invoice is thirty days overdue. Two hundred thousand "
             "euros!", gap=0.4),
        Line("kito1", "KITO", "Not until every machine works. I'm holding back the whole "
             "price!", gap=0.4),
        Line("lex1", "LEX", "Careful, Kito. The buyer has duties too, and refusing to pay "
             "for good machines could put SafariTech in breach.", gap=0.3),
        Line("lex1b", "LEX", "Under the CISG, the buyer has two core obligations: pay the "
             "price, and take delivery of the goods."),
        Pause("hold", 1.2),
    ], spec={"tpl": "talk", "bg": "office", "syl": "B2(b)",
             "cast": [{"who": "HANS", "x": 1550, "y": 1030, "s": 0.92, "talk_pose": "demand",
                       "mood": "angry"},
                      {"who": "KITO", "x": 1000, "y": 1030, "s": 0.95, "talk_pose": "hips"},
                      {"who": "LEX", "x": 420, "y": 1030, "s": 0.9, "enter": "lex1",
                       "from": "left"}],
             "pops": [{"kind": "icon", "icon": "receipt", "x": 1300, "y": 280, "s": 1.2,
                       "at": ["hans1", 0.5], "until": "lex1", "float": True,
                       "color": "#e4572e", "label": "€200,000 overdue"},
                      {"kind": "card", "at": "lex1b", "x": 1180, "y": 300, "w": 820, "h": 220,
                       "title": "Article 53: the buyer must…",
                       "body": "pay the price · take delivery of the goods",
                       "color": "#7768ae", "bs": 40}]}),

    Scene("s2", "Paying the price", "", [
        Pause("open", 1.0),
        Line("lex2a", "LEX", "Paying includes the steps needed to make payment possible, "
             "like opening a letter of credit, or getting a bank guarantee.", gap=0.3),
        Sfx("pop"),
        Line("lex2b", "LEX", "If no price was fixed, it is the price generally charged for "
             "such goods when the contract was made.", gap=0.25),
        Sfx("pop"),
        Line("lex2c", "LEX", "If the price depends on weight, use the net weight.", gap=0.25),
        Sfx("pop"),
        Line("lex2d", "LEX", "Place: the seller's place of business, or, if payment is "
             "against goods or documents, wherever they are handed over.", gap=0.25),
        Sfx("pop"),
        Line("lex2e", "LEX", "Time: when the seller places the goods or documents at the "
             "buyer's disposal. The seller can make payment a condition of handing them "
             "over.", gap=0.25),
        Sfx("pop"),
        Line("lex2f", "LEX", "The buyer may examine the goods before paying, unless the "
             "agreed payment method rules that out.", gap=0.25),
        Sfx("pop"),
        Line("lex2g", "LEX", "And the buyer must pay on the due date, without any request "
             "from the seller.", gap=0.4),
        Line("amara2", "AMARA", "That's why our bank asks importers to set up payment terms "
             "before the goods ship."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "white", "heading": "Payment rules (Arts 54–59)",
             "syl": "B2(b)(i)", "row": 100, "ts": 36,
             "items": [{"at": "lex2b", "text": "No price fixed?", "sub": "Price generally "
                                                                          "charged at the "
                                                                          "time of contract",
                        "icon": "tag", "color": "#0f8b8d"},
                       {"at": "lex2c", "text": "Priced by weight?", "sub": "Net weight",
                        "icon": "box", "color": "#7768ae"},
                       {"at": "lex2d", "text": "Where?", "sub": "Seller's place, or where "
                                                                 "goods / documents are "
                                                                 "handed over",
                        "icon": "flag", "color": "#e4572e"},
                       {"at": "lex2e", "text": "When?", "sub": "When goods or documents "
                                                                "are at the buyer's disposal",
                        "icon": "calendar", "color": "#f2a541"},
                       {"at": "lex2f", "text": "Examine first", "sub": "Unless the payment "
                                                                       "method rules it out",
                        "icon": "magnifier", "color": "#3bb273"},
                       {"at": "lex2g", "text": "No reminder needed", "sub": "Pay on the due "
                                                                           "date",
                        "icon": "clock", "color": "#2b86c5"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "AMARA", "x": 1810, "s": 0.55, "y": 1120, "enter": "amara2"}],
             "pops": [{"kind": "card", "at": "lex2a", "until": "lex2b", "x": 1190, "y": 470,
                       "w": 900, "h": 260, "title": "Art 54: steps to enable payment",
                       "body": "e.g. open a letter of credit, obtain a bank guarantee",
                       "color": "#1f3a5f", "bs": 40}]}),

    Scene("s3", "Taking delivery", "", [
        Pause("open", 1.0),
        Line("lex3a", "LEX", "Taking delivery has two parts.", gap=0.3),
        Line("lex3b", "LEX", "First, doing everything that can reasonably be expected so the "
             "seller can deliver. For example, sending a ship under FOB, or giving "
             "specifications.", say="First, doing everything that can reasonably be "
             "expected so the seller can deliver. For example, sending a ship under F.O.B., "
             "or giving specifications.", gap=0.3),
        Line("lex3c", "LEX", "Second, actually taking over the goods.", gap=0.4),
        Line("cargo3", "CARGO", "So if nobody collects me at the port, that's the buyer's "
             "breach!", gap=0.3),
        Line("lex3d", "LEX", "Exactly. And even a buyer who rejects goods must look after "
             "them. We'll see that duty in the next episode."),
        Pause("hold", 1.4),
    ], spec={"tpl": "flow", "bg": "port", "heading": "Taking delivery (Art 60)",
             "syl": "B2(b)(ii)",
             "nodes": [{"id": "a", "x": 860, "y": 330, "label": "Do what is reasonably "
                                                                "expected so seller can "
                                                                "deliver",
                        "icon": "handshake", "color": "#0f8b8d", "at": "lex3b", "w": 380,
                        "h": 220},
                       {"id": "b", "x": 1460, "y": 330, "label": "Take over the goods",
                        "icon": "box", "color": "#7768ae", "at": "lex3c", "w": 320}],
             "edges": [{"from": "a", "to": "b", "at": "lex3c", "label": "then"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "CARGO", "x": 1500, "y": 980, "s": 0.8}]}),

    Scene("s4", "The seller's remedies", "", [
        Pause("open", 1.0),
        Line("lex4a", "LEX", "If the buyer breaches, the seller's toolkit mirrors the "
             "buyer's.", gap=0.3),
        Sfx("pop"),
        Line("lex4b", "LEX", "Require the buyer to pay, take delivery, or perform its other "
             "obligations, unless the seller has chosen an inconsistent remedy.", gap=0.25),
        Sfx("pop"),
        Line("lex4c", "LEX", "Fix an additional period of reasonable length for the buyer "
             "to perform.", gap=0.25),
        Sfx("pop"),
        Line("lex4d", "LEX", "Avoid the contract, for a fundamental breach, or if the buyer "
             "does not pay or take delivery within the additional period.", gap=0.25),
        Sfx("pop"),
        Line("lex4e", "LEX", "If the buyer fails to give specifications, the seller may "
             "supply them itself.", gap=0.25),
        Sfx("pop"),
        Line("lex4f", "LEX", "And claim damages, alongside any other remedy.", gap=0.5),
        Line("lex4g", "LEX", "One limit: once the buyer has paid, the seller generally loses "
             "the right to avoid, unless it acts quickly about late performance or another "
             "breach.", gap=0.3),
        Line("hans4", "HANS", "So I could fix a deadline, and then avoid the contract if "
             "SafariTech still doesn't pay."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "heading": "Seller's remedies (Arts 61–65)",
             "syl": "B2(b)(iii)", "row": 116, "ts": 40,
             "items": [{"at": "lex4b", "text": "Require payment or performance",
                        "icon": "moneybag", "color": "#3bb273"},
                       {"at": "lex4c", "text": "Fix an additional period", "icon": "calendar",
                        "color": "#2b86c5"},
                       {"at": "lex4d", "text": "Avoid the contract", "sub": "Fundamental "
                                                                          "breach or deadline "
                                                                          "missed",
                        "icon": "scissors", "color": "#e4572e"},
                       {"at": "lex4e", "text": "Make the missing specification",
                        "icon": "pen", "color": "#f2a541"},
                       {"at": "lex4f", "text": "Damages", "sub": "Alongside other remedies",
                        "icon": "coin", "color": "#7768ae"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "HANS", "x": 1810, "s": 0.55, "y": 1120, "enter": "hans4"}],
             "pops": [{"kind": "chip", "at": "lex4g", "until": "hans4", "x": 1190, "y": 960,
                       "text": "Buyer has paid? Seller's right to avoid is limited",
                       "color": "#1f3a5f", "size": 32}]}),

    Scene("s5", "Retention of title", "", [
        Pause("open", 1.0),
        Line("hans5", "HANS", "Next time, I'll keep ownership of my machines until I'm "
             "paid.", gap=0.4),
        Line("lex5a", "LEX", "That is a retention of title clause, often called a Romalpa "
             "clause, after a famous English case.", gap=0.3),
        Line("lex5b", "LEX", "A Dutch supplier sold aluminium foil to an English company, "
             "with a clause keeping ownership until payment. The buyer became insolvent.",
             gap=0.3),
        Line("lex5c", "LEX", "The court held the supplier could recover its unsold foil, and "
             "the proceeds of resales held for it, ahead of the other creditors.", gap=0.4),
        Sfx("sparkle"),
        Pause("stamp", 1.2),
        Line("lex5d", "LEX", "But remember: the CISG does not deal with ownership. Whether "
             "such a clause works depends on the national law that applies."),
        Pause("hold", 1.4),
    ], spec={"tpl": "case", "bg": "office", "name": "Aluminium Industrie Vaassen v "
                                                     "Romalpa Aluminium",
             "year": "Court of Appeal, England · 1976", "syl": "B2(b)",
             "rows": [{"at": "lex5b", "label": "Facts", "text": "Foil sold with title kept "
                                                                "until payment · buyer "
                                                                "became insolvent",
                       "color": "#7768ae"},
                      {"at": "lex5c", "label": "Held", "text": "Seller recovered unsold foil "
                                                               "and resale proceeds held for "
                                                               "it",
                       "color": "#3bb273"},
                      {"at": "lex5d", "label": "CISG", "text": "Ownership is outside the "
                                                               "Convention (Art 4): national "
                                                               "law decides",
                       "color": "#e4572e"}],
             "stamp": {"at": "stamp", "text": "TITLE RETAINED", "color": "#3bb273"},
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "HANS", "x": 1810, "s": 0.55, "y": 1120}]}),

    Scene("s6", "Sorting out SafariTech", "", [
        Pause("open", 1.0),
        Line("nia6", "NIA", "So what should we do, Professor?", gap=0.3),
        Line("lex6a", "LEX", "Pay for the three machines that conform. Holding back the "
             "whole price could itself be a fundamental breach.", gap=0.3),
        Line("lex6b", "LEX", "For machine two, demand repair, or reduce the price. For "
             "machine five, ask for a substitute, and keep your damages claim.", gap=0.4),
        Line("kito6", "KITO", "Fine. Pay for what works, and fight for the rest. Hans, the "
             "money's on its way.", gap=0.3),
        Line("hans6", "HANS", "Danke! And I'll send a technician for machine two."),
        Pause("hold", 1.4),
    ], spec={"tpl": "talk", "bg": "harbour", "syl": "B2(a)–(b)",
             "cast": [{"who": "NIA", "x": 700, "y": 1030, "s": 0.9},
                      {"who": "LEX", "x": 300, "y": 1030, "s": 0.9},
                      {"who": "KITO", "x": 1100, "y": 1030, "s": 0.92, "mood": "happy"},
                      {"who": "HANS", "x": 1550, "y": 1030, "s": 0.9, "mood": "happy",
                       "pose": "idle", "talk_pose": "wave"}],
             "pops": [{"kind": "chip", "at": ["lex6a", 0.2], "x": 960, "y": 160,
                       "text": "3 conforming machines → pay", "color": "#3bb273", "size": 38},
                      {"kind": "chip", "at": ["lex6b", 0.2], "x": 960, "y": 250,
                       "text": "Machine 2 → repair or price reduction", "color": "#f2a541",
                       "size": 38},
                      {"kind": "chip", "at": ["lex6b", 3.0], "x": 960, "y": 340,
                       "text": "Machine 5 → substitute + damages", "color": "#e4572e",
                       "size": 38}]}),

    quiz_scene("s7", "Quick check",
               "The contract does not fix a price. Under the CISG, what price is payable?",
               ["Whatever the seller now asks", "The price generally charged for such goods "
                "when the contract was made", "The lowest market price at delivery",
                "There is no contract without a price"], 1,
               "Quick check. If the contract does not fix a price, what price is payable?",
               "The price generally charged for such goods when the contract was made.",
               syl="B2(b)(i)"),

    quiz_scene("s8", "Quick check",
               "What is the effect of a Romalpa clause?",
               ["The buyer may delay payment", "The seller keeps ownership until paid",
                "Risk stays with the seller", "The price is fixed in euros"], 1,
               "And what is the effect of a Romalpa clause?",
               "The seller keeps ownership until it is paid.",
               why=("Whether it works depends on the applicable national law",
                    "Whether it works depends on the applicable national law."),
               think=4.0, syl="B2(b)"),

    recap_scene("s9", [
        ("Pay the price and take delivery.", "Pay the price · take delivery"),
        ("Payment includes steps like a letter of credit.", "Art 54: steps like an L/C"),
        ("No price fixed? The general price at contract.", "No price? General price at "
                                                           "contract"),
        ("Seller's remedies mirror the buyer's.", "Perform · extra time · avoid · damages"),
        ("Romalpa keeps title until payment.", "Romalpa: title until paid"),
    ], [
        Line("lex9", "LEX", "Next time, things go really wrong: anticipatory breach, instalments, "
             "damages, and events beyond anyone's control.", gap=0.3),
        Line("cargo9", "CARGO", "Uh oh. I hope nobody drops me in the ocean!", gap=0.6),
    ], next_ep=9, next_title="When Deals Break", next_icon="warning"),
]
