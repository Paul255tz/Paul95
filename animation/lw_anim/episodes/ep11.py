"""Episode 11 - Paper That Moves the World.

Syllabus C1(a) and C1(d): bills of lading, and the UN Convention on
International Bills of Exchange and International Promissory Notes (New York,
1988). Setting: SafariTech's kits leave Dar es Salaam for a buyer in Dubai,
and Amara's bank in Nairobi handles the documents.
"""
from ._kit import (DISPLAY_NAMES, SERIES, VOICES, Line, Pause, Scene, Sfx,  # noqa: F401
                   quiz_scene, recap_scene, title_scene)

EPISODE = "Episode 11"
EPISODE_TITLE = "Paper That Moves the World"
SLUG = "episode11_paper_that_moves_the_world"

SCENES = [
    title_scene(11, EPISODE_TITLE, "Syllabus C1(a), C1(d)", ("bill", "bank")),

    Scene("s1", "A very important receipt", "", [
        Pause("open", 1.2),
        Sfx("horn"),
        Line("cargo1", "CARGO", "Two hundred SafariTech kits, loaded and sailing for Dubai. "
             "Here's your bill of lading, Kito!", gap=0.4),
        Line("kito1", "KITO", "It's just a receipt, isn't it?", gap=0.4),
        Line("amara1", "AMARA", "Oh, it's much more than that. With the right bill of lading, "
             "whoever holds the paper can claim the goods.", gap=0.3),
        Line("lex1", "LEX", "Let's see why traders, and banks, care so much about it."),
        Pause("hold", 1.2),
    ], spec={"tpl": "talk", "bg": "port", "syl": "C1(a)",
             "cast": [{"who": "CARGO", "x": 1500, "y": 980, "s": 0.9},
                      {"who": "KITO", "x": 320, "y": 1060, "s": 0.85, "pose": "hold_r"},
                      {"who": "AMARA", "x": 640, "y": 1060, "s": 0.85, "enter": "amara1",
                       "from": "left"},
                      {"who": "LEX", "x": 930, "y": 1060, "s": 0.82, "enter": "lex1",
                       "from": "left"}],
             "pops": [{"kind": "icon", "icon": "bill", "x": 1150, "y": 300, "s": 1.4,
                       "at": ["cargo1", 2.0], "float": True, "label": "Bill of lading"}]}),

    Scene("s2", "Three jobs in one document", "", [
        Pause("open", 1.0),
        Line("lex2a", "LEX", "A bill of lading is issued by the carrier, or its agent, to "
             "the shipper. It does three jobs.", gap=0.3),
        Sfx("pop"),
        Line("lex2b", "LEX", "It is a receipt, confirming the carrier has received the "
             "goods, in the quantity and apparent condition stated, and usually that they "
             "are on board a named vessel.", gap=0.25),
        Sfx("pop"),
        Line("lex2c", "LEX", "It is evidence of the contract of carriage between shipper and "
             "carrier.", gap=0.25),
        Sfx("pop"),
        Line("lex2d", "LEX", "And it is a document of title. Transferring a negotiable bill "
             "transfers the right to the goods.", gap=0.4),
        Line("lex2e", "LEX", "It also shows when the goods were handed to the carrier, which "
             "often marks when risk passes, unless the contract says otherwise.", gap=0.4),
        Line("nia2", "NIA", "And a clean bill means no defects were noted. A claused bill "
             "records damage, and banks don't like those."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "heading": "A bill of lading is…",
             "syl": "C1(a)", "row": 140, "ts": 42,
             "items": [{"at": "lex2b", "text": "A receipt for the goods",
                        "sub": "Quantity, apparent condition, on board",
                        "icon": "receipt", "color": "#3bb273"},
                       {"at": "lex2c", "text": "Evidence of the contract of carriage",
                        "sub": "Between shipper and carrier", "icon": "contract",
                        "color": "#2b86c5"},
                       {"at": "lex2d", "text": "A document of title",
                        "sub": "Transfer the bill → transfer the right to the goods",
                        "icon": "key", "color": "#f2a541"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia2"}],
             "pops": [{"kind": "chip", "at": "lex2e", "until": "nia2", "x": 1190, "y": 900,
                       "text": "Shows when goods reached the carrier → often when risk passes",
                       "color": "#1f3a5f", "size": 30},
                      {"kind": "chip", "at": "nia2", "x": 1190, "y": 900,
                       "text": "Clean = no defects noted · Claused = damage recorded",
                       "color": "#e4572e", "size": 32}]}),

    Scene("s3", "Kinds of bill", "", [
        Pause("open", 1.0),
        Line("lex3a", "LEX", "Bills come in several kinds.", gap=0.3),
        Sfx("pop"),
        Line("lex3b", "LEX", "A negotiable bill is made out to order. The holder endorses "
             "and hands it on, and the right to the goods goes with it.", gap=0.25),
        Sfx("pop"),
        Line("lex3c", "LEX", "A non-negotiable, or straight, bill names the consignee. The "
             "carrier delivers only to that person.", gap=0.25),
        Sfx("pop"),
        Line("lex3d", "LEX", "An inland bill covers carriage over land to the port of "
             "departure.", gap=0.25),
        Sfx("pop"),
        Line("lex3e", "LEX", "An ocean bill covers the sea voyage, from port to port.",
             gap=0.25),
        Sfx("pop"),
        Line("lex3f", "LEX", "A through bill combines both, from the factory all the way to "
             "the foreign port.", gap=0.25),
        Sfx("pop"),
        Line("lex3g", "LEX", "And an air waybill covers carriage by air. It is always "
             "non-negotiable, so it is not a document of title.", gap=0.4),
        Line("cargo3", "CARGO", "For Dubai, Kito chose a through bill, from Arusha by rail, "
             "then by sea with me!"),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "white", "layout": "grid", "cols": 3,
             "heading": "Types of bill of lading", "syl": "C1(a)", "cell_h": 300, "ts": 36,
             "items": [{"at": "lex3b", "text": "Negotiable", "sub": "To order · endorse and "
                                                                    "transfer",
                        "icon": "key", "color": "#3bb273"},
                       {"at": "lex3c", "text": "Non-negotiable", "sub": "Straight · named "
                                                                        "consignee only",
                        "icon": "lock", "color": "#e4572e"},
                       {"at": "lex3d", "text": "Inland", "sub": "Overland to the port",
                        "icon": "truck", "color": "#f2a541"},
                       {"at": "lex3e", "text": "Ocean", "sub": "Port to port",
                        "icon": "ship", "color": "#2b86c5"},
                       {"at": "lex3f", "text": "Through", "sub": "Inland + ocean combined",
                        "icon": "globe", "color": "#7768ae"},
                       {"at": "lex3g", "text": "Air waybill", "sub": "Always non-negotiable",
                        "icon": "plane", "color": "#0f8b8d"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "CARGO", "x": 1800, "y": 1080, "s": 0.45, "enter": "cargo3"}]}),

    Scene("s4", "What is a bill of exchange?", "", [
        Pause("open", 1.0),
        Line("amara4", "AMARA", "Now, how does the money move? Often with a bill of "
             "exchange.", gap=0.3),
        Line("lex4a", "LEX", "A bill of exchange is an unconditional order in writing, "
             "addressed by one person, the drawer, to another, the drawee.", gap=0.25),
        Line("lex4b", "LEX", "It is signed by the drawer, and requires the drawee to pay a "
             "sum certain in money, on demand, or at a fixed or determinable future time.",
             gap=0.25),
        Line("lex4c", "LEX", "Payment goes to, or to the order of, a specified person, the "
             "payee, or to the bearer.", gap=0.4),
        Line("lex4d", "LEX", "A promissory note is similar, but it is a promise by the maker "
             "to pay, rather than an order to someone else.", gap=0.4),
        Line("kito4", "KITO", "So the bill says: Dubai buyer, pay SafariTech fifty thousand "
             "dollars in ninety days."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "white", "heading": "Bill of exchange: the elements",
             "syl": "C1(d)", "row": 104, "ts": 38,
             "items": [{"at": "lex4a", "text": "Unconditional order in writing",
                        "icon": "doc", "color": "#0f8b8d"},
                       {"at": ["lex4a", 3.5], "text": "Drawer → addressed to the drawee",
                        "icon": "person", "color": "#7768ae"},
                       {"at": "lex4b", "text": "Signed by the drawer", "icon": "pen",
                        "color": "#2b86c5"},
                       {"at": ["lex4b", 4.0], "text": "Sum certain in money",
                        "icon": "coin", "color": "#f2a541"},
                       {"at": ["lex4b", 6.0], "text": "On demand, or a fixed/determinable "
                                                      "date",
                        "icon": "calendar", "color": "#e4572e"},
                       {"at": "lex4c", "text": "To a payee, to order, or to bearer",
                        "icon": "people", "color": "#3bb273"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "AMARA", "x": 1650, "s": 0.55, "y": 1120},
                      {"who": "KITO", "x": 1820, "s": 0.55, "y": 1120, "enter": "kito4"}],
             "pops": [{"kind": "card", "at": "lex4d", "until": "kito4", "x": 1190, "y": 470,
                       "w": 900, "h": 260, "title": "Promissory note",
                       "body": "A promise by the maker to pay, not an order to someone else",
                       "color": "#1f3a5f", "dim": True, "bs": 38}]}),

    Scene("s5", "When is a bill international?", "", [
        Pause("open", 1.0),
        Line("lex5a", "LEX", "UNCITRAL's Convention on International Bills of Exchange and "
             "International Promissory Notes, of 1988, offers an optional global regime.",
             say="Uncitral's Convention on International Bills of Exchange and International "
                 "Promissory Notes, of 1988, offers an optional global regime.", gap=0.3),
        Sfx("pop"),
        Line("lex5b", "LEX", "The instrument must be headed, and say in its text, "
             "International bill of exchange, UNCITRAL Convention.",
             say="The instrument must be headed, and say in its text, International bill of "
                 "exchange, Uncitral Convention.", gap=0.25),
        Sfx("pop"),
        Line("lex5c", "LEX", "It must name at least two of five places: where it was drawn, "
             "next to the drawer's signature, next to the drawee's name, next to the payee's "
             "name, and the place of payment.", gap=0.25),
        Sfx("pop"),
        Line("lex5d", "LEX", "And at least two of those places must be in different "
             "states.", gap=0.4),
        Line("lex5e", "LEX", "A reality check: it needs ten states to come into force, and "
             "so far only five have joined. In practice, national laws on bills still "
             "govern. But the exam tests the Convention's rules."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "heading": "UN Convention on International "
                                                          "Bills (1988)",
             "syl": "C1(d)", "row": 140, "ts": 40,
             "items": [{"at": "lex5b", "text": "Headed: “International bill of exchange "
                                               "(UNCITRAL Convention)”",
                        "icon": "tag", "color": "#0f8b8d"},
                       {"at": "lex5c", "text": "Names at least 2 of the 5 places",
                        "sub": "Drawn · drawer · drawee · payee · payment",
                        "icon": "flag", "color": "#f2a541"},
                       {"at": "lex5d", "text": "Two of them in different states",
                        "icon": "globe", "color": "#e4572e"}],
             "cast": [{"who": "LEX", "x": 250}],
             "pops": [{"kind": "chip", "at": "lex5e", "x": 1190, "y": 930,
                       "text": "Not yet in force: 5 of 10 required states", "color": "#7768ae",
                       "size": 34}]}),

    Scene("s6", "The life of a bill", "", [
        Pause("open", 1.0),
        Line("lex6a", "LEX", "Follow the bill. SafariTech, as drawer, draws it on the Dubai "
             "buyer's bank, the drawee.", gap=0.3),
        Line("lex6b", "LEX", "The drawee signs it as accepted, and becomes the acceptor, "
             "primarily liable to pay.", gap=0.3),
        Line("lex6c", "LEX", "The bill goes to the payee. If the payee wants cash now, it can "
             "endorse the bill to its own creditor, the indorsee, who can endorse it again.",
             gap=0.3),
        Line("lex6d", "LEX", "An endorsement can name the next holder, or be signed in "
             "blank. A bill endorsed in blank becomes a bearer bill, and passes by simple "
             "delivery.", gap=0.3),
        Line("lex6e", "LEX", "And a guarantor can sign to guarantee payment, usually by the "
             "acceptor.", gap=0.4),
        Line("amara6", "AMARA", "That's how our bank can buy the bill today at a discount, "
             "and collect in full in ninety days."),
        Pause("hold", 1.4),
    ], spec={"tpl": "flow", "bg": "bank", "heading": "Parties to a bill", "syl": "C1(d)",
             "nodes": [{"id": "dr", "x": 650, "y": 300, "label": "Drawer (SafariTech)",
                        "icon": "company", "color": "#0f8b8d", "at": "lex6a", "w": 290},
                       {"id": "de", "x": 1150, "y": 300, "label": "Drawee → Acceptor",
                        "icon": "bank", "color": "#7768ae", "at": ["lex6a", 2.5], "w": 290},
                       {"id": "pa", "x": 1650, "y": 300, "label": "Payee → Indorser",
                        "icon": "person", "color": "#f2a541", "at": "lex6c", "w": 290},
                       {"id": "in", "x": 1650, "y": 700, "label": "Indorsee / Holder",
                        "icon": "people", "color": "#3bb273", "at": ["lex6c", 4.0], "w": 290},
                       {"id": "gu", "x": 1150, "y": 700, "label": "Guarantor",
                        "icon": "shield", "color": "#e4572e", "at": "lex6e", "w": 260}],
             "edges": [{"from": "dr", "to": "de", "at": ["lex6a", 2.6], "label": "draws on",
                        "token": "doc"},
                       {"from": "de", "to": "pa", "at": "lex6b", "label": "accepted",
                        "token": "doc", "move": "lex6c"},
                       {"from": "pa", "to": "in", "at": ["lex6c", 4.0], "label": "endorses",
                        "token": "doc"},
                       {"from": "gu", "to": "de", "at": "lex6e", "label": "guarantees",
                        "dashed": True, "color": "#e4572e"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "AMARA", "x": 1810, "s": 0.55, "y": 1120, "enter": "amara6"}],
             "pops": [{"kind": "chip", "at": "lex6d", "until": "lex6e", "x": 1150, "y": 940,
                       "text": "Endorsed in blank → bearer bill, passes by delivery",
                       "color": "#1f3a5f", "size": 32}]}),

    Scene("s7", "Dishonour", "", [
        Pause("open", 1.0),
        Line("kito7", "KITO", "And if the acceptor refuses to pay?", gap=0.3),
        Line("lex7a", "LEX", "Then the bill is dishonoured. The holder can claim against "
             "everyone who signed before it: the drawer, every indorser, and any guarantor.",
             gap=0.3),
        Line("lex7b", "LEX", "They are jointly and severally liable, so the holder can pick "
             "any of them. Whoever pays can then claim back up the chain.", gap=0.3),
        Line("lex7c", "LEX", "Under the Convention, a protected holder, who took the bill "
             "complete, in good faith, and without notice of any problem, takes it free "
             "from most defences.", gap=0.4),
        Line("nia7", "NIA", "So every signature on the bill is like another promise to pay."),
        Pause("hold", 1.4),
    ], spec={"tpl": "flow", "bg": "studio_red", "heading": "Dishonour: who pays?",
             "syl": "C1(d)",
             "nodes": [{"id": "ac", "x": 760, "y": 300, "label": "Acceptor refuses",
                        "icon": "cross", "color": "#e4572e", "at": "kito7", "w": 280},
                       {"id": "ho", "x": 1500, "y": 300, "label": "Holder", "icon": "person",
                        "color": "#3bb273", "at": "lex7a", "w": 260},
                       {"id": "d1", "x": 900, "y": 680, "label": "Drawer", "icon": "company",
                        "color": "#0f8b8d", "at": ["lex7a", 3.0], "w": 230},
                       {"id": "d2", "x": 1200, "y": 720, "label": "Indorsers",
                        "icon": "people", "color": "#f2a541", "at": ["lex7a", 4.0],
                        "w": 230},
                       {"id": "d3", "x": 1500, "y": 680, "label": "Guarantor",
                        "icon": "shield", "color": "#7768ae", "at": ["lex7a", 5.0],
                        "w": 230}],
             "edges": [{"from": "ho", "to": "ac", "at": ["lex7a", 0.5], "label": "dishonour",
                        "color": "#e4572e", "dashed": True},
                       {"from": "ho", "to": "d1", "at": ["lex7a", 3.0], "color": "#1f3a5f"},
                       {"from": "ho", "to": "d2", "at": ["lex7a", 4.0], "color": "#1f3a5f"},
                       {"from": "ho", "to": "d3", "at": ["lex7a", 5.0], "color": "#1f3a5f"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "KITO", "x": 1650, "s": 0.55, "y": 1120},
                      {"who": "NIA", "x": 1820, "s": 0.55, "y": 1120, "enter": "nia7"}],
             "pops": [{"kind": "chip", "at": "lex7b", "until": "lex7c", "x": 1150, "y": 930,
                       "text": "Jointly and severally liable", "color": "#1f3a5f",
                       "size": 36},
                      {"kind": "chip", "at": "lex7c", "x": 1150, "y": 930,
                       "text": "Protected holder: free from most defences", "color": "#3bb273",
                       "size": 34}]}),

    quiz_scene("s8", "Quick check",
               "Which of these is NOT a function of a bill of lading?",
               ["Receipt for the goods", "Evidence of the contract of carriage",
                "Document of title", "Guarantee that the buyer will pay"], 3,
               "Quick check. Which of these is not a function of a bill of lading?",
               "A guarantee that the buyer will pay.",
               why="Receipt · evidence of carriage contract · document of title",
               syl="C1(a)"),

    quiz_scene("s9", "Quick check",
               "A payee signs the back of a bill without naming anyone. What has it created?",
               ["A special endorsement", "A bearer bill that passes by delivery",
                "A cancelled bill", "A promissory note"], 1,
               "And if a payee endorses a bill without naming anyone, what has it created?",
               "A bearer bill, which passes by delivery.",
               think=4.0, syl="C1(d)"),

    recap_scene("s10", [
        ("Bill of lading: receipt, contract evidence, title.", "B/L: receipt · contract · "
                                                               "title"),
        ("Negotiable or straight; inland, ocean, through, air.",
         "Negotiable · straight · inland · ocean · through · air"),
        ("Bill of exchange: unconditional written order.", "Bill: unconditional order"),
        ("International: two places in different states.", "International: 2 places, "
                                                           "2 states"),
        ("Dishonour: every signer is liable.", "Dishonour: all signers liable"),
    ], [
        Line("lex10", "LEX", "Next time: bank transfers across borders, letters of credit, "
             "and the curious letter of comfort.", gap=0.3),
        Line("amara10", "AMARA", "My favourite episode. It's all about banks!", gap=0.6),
    ], next_ep=12, next_title="Following the Money", next_icon="bank"),
]
