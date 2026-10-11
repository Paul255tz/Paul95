"""Episode 12 - Following the Money.

Syllabus C1(b), C1(c), C1(e): bank transfers, the UNCITRAL Model Law on
International Credit Transfers (1992), letters of credit (ICC UCP 600) and
letters of comfort. Setting: Amara's bank in Nairobi helps SafariTech get paid
safely by a new buyer in Dubai.
"""
from ._kit import (DISPLAY_NAMES, SERIES, VOICES, Line, Pause, Scene, Sfx,  # noqa: F401
                   quiz_scene, recap_scene, title_scene)

EPISODE = "Episode 12"
EPISODE_TITLE = "Following the Money"
SLUG = "episode12_following_the_money"

SCENES = [
    title_scene(12, EPISODE_TITLE, "Syllabus C1(b), (c), (e)", ("bank", "coin")),

    Scene("s1", "Trust, across borders", "", [
        Pause("open", 1.0),
        Line("kito1", "KITO", "A new buyer in Dubai wants five hundred kits. I've never met "
             "them. What if they never pay?", gap=0.4),
        Line("amara1", "AMARA", "And they're worried you'll take the money and never ship. "
             "Banks exist to solve exactly that problem.", gap=0.4),
        Line("lex1", "LEX", "Today: how money moves between banks, how a letter of credit "
             "builds trust, and why a letter of comfort may give less comfort than it "
             "sounds."),
        Pause("hold", 1.2),
    ], spec={"tpl": "talk", "bg": "bank", "syl": "C1",
             "cast": [{"who": "KITO", "x": 1450, "y": 1040, "s": 0.92, "mood": "worried",
                       "talk_pose": "shrug"},
                      {"who": "AMARA", "x": 960, "y": 1040, "s": 0.92},
                      {"who": "LEX", "x": 420, "y": 1040, "s": 0.88, "enter": "lex1",
                       "from": "left"}]}),

    Scene("s2", "How a bank transfer travels", "", [
        Pause("open", 1.0),
        Line("amara2a", "AMARA", "A cross-border transfer is a chain of payment orders.",
             gap=0.3),
        Line("amara2b", "AMARA", "The buyer, called the originator, instructs its own bank.",
             gap=0.25),
        Line("amara2c", "AMARA", "That bank sends a payment order, usually by a secure "
             "message network like SWIFT, often through an intermediary bank.",
             say="That bank sends a payment order, usually by a secure message network like "
                 "Swift, often through an intermediary bank.", gap=0.25),
        Line("amara2d", "AMARA", "Finally, the beneficiary's bank credits SafariTech, the "
             "beneficiary.", gap=0.4),
        Line("amara2e", "AMARA", "Within Africa, regional systems help too, like the East "
             "African Payment System, and the Pan-African Payment and Settlement System.",
             gap=0.3),
        Line("nia2", "NIA", "So each link in the chain is a separate payment order, from a "
             "sender to a receiving bank."),
        Pause("hold", 1.4),
    ], spec={"tpl": "flow", "bg": "studio_teal", "heading": "A credit transfer", "syl": "C1(b)",
             "nodes": [{"id": "o", "x": 620, "y": 330, "label": "Originator (Dubai buyer)",
                        "icon": "person", "color": "#7768ae", "at": "amara2b", "w": 260},
                       {"id": "ob", "x": 960, "y": 600, "label": "Originator's bank",
                        "icon": "bank", "color": "#7768ae", "at": ["amara2b", 1.6],
                        "w": 260},
                       {"id": "ib", "x": 1300, "y": 330, "label": "Intermediary bank",
                        "icon": "bank", "color": "#5b6670", "at": "amara2c", "w": 260},
                       {"id": "bb", "x": 1640, "y": 600, "label": "Beneficiary's bank",
                        "icon": "bank", "color": "#0f8b8d", "at": "amara2d", "w": 260},
                       {"id": "b", "x": 1640, "y": 880, "label": "Beneficiary (SafariTech)",
                        "icon": "company", "color": "#0f8b8d", "at": ["amara2d", 1.5],
                        "w": 280, "h": 170}],
             "edges": [{"from": "o", "to": "ob", "at": ["amara2b", 1.4], "token": "envelope",
                        "label": "instruction"},
                       {"from": "ob", "to": "ib", "at": ["amara2c", 1.0], "token": "envelope",
                        "label": "payment order"},
                       {"from": "ib", "to": "bb", "at": ["amara2c", 3.0], "token": "envelope"},
                       {"from": "bb", "to": "b", "at": ["amara2d", 1.4], "token": "coin",
                        "tcolor": "#ffb627", "label": "credit"}],
             "cast": [{"who": "AMARA", "x": 250, "talk_pose": "present"},
                      {"who": "NIA", "x": 1840, "s": 0.5, "y": 1130, "enter": "nia2"}],
             "pops": [{"kind": "card", "at": "amara2e", "until": "nia2", "x": 1100, "y": 470,
                       "w": 900, "h": 260, "title": "Local lens: African payment rails",
                       "body": "EAPS links East African central banks · PAPSS settles "
                               "payments across Africa", "color": "#f2a541", "dim": True,
                       "bs": 38}]}),

    Scene("s3", "The Model Law on credit transfers", "", [
        Pause("open", 1.0),
        Line("lex3a", "LEX", "UNCITRAL's Model Law on International Credit Transfers, from "
             "1992, applies where a sending bank and its receiving bank are in different "
             "states.",
             say="Uncitral's Model Law on International Credit Transfers, from 1992, applies "
                 "where a sending bank and its receiving bank are in different states.",
             gap=0.3),
        Sfx("pop"),
        Line("lex3b", "LEX", "A sender must pay the receiving bank once that bank accepts "
             "its payment order.", gap=0.25),
        Sfx("pop"),
        Line("lex3c", "LEX", "A receiving bank that accepts must execute the order, "
             "normally on the day it is received.", gap=0.25),
        Sfx("pop"),
        Line("lex3d", "LEX", "If the transfer is not completed, there is a money-back "
             "guarantee. The originator's bank must refund the originator, with interest.",
             gap=0.25),
        Sfx("pop"),
        Line("lex3e", "LEX", "A bank that delays must pay interest for the delay.", gap=0.25),
        Sfx("pop"),
        Line("lex3f", "LEX", "And the transfer is completed when the beneficiary's bank "
             "accepts the payment order for the beneficiary. That is when the debt is paid.",
             gap=0.4),
        Line("kito3", "KITO", "So once my bank in Dar accepts the order, the buyer has "
             "paid me, even before I see the money!"),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "heading": "Model Law on Credit Transfers "
                                                          "(1992)",
             "syl": "C1(c)", "row": 112, "ts": 38,
             "items": [{"at": "lex3b", "text": "Sender pays on acceptance",
                        "icon": "handshake", "color": "#0f8b8d"},
                       {"at": "lex3c", "text": "Execute, normally the same day",
                        "icon": "clock", "color": "#2b86c5"},
                       {"at": "lex3d", "text": "Money-back guarantee, with interest",
                        "icon": "shield", "color": "#3bb273"},
                       {"at": "lex3e", "text": "Interest for delay", "icon": "percent",
                        "color": "#f2a541"},
                       {"at": "lex3f", "text": "Complete when beneficiary's bank accepts",
                        "icon": "check", "color": "#e4572e"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "KITO", "x": 1810, "s": 0.55, "y": 1120, "enter": "kito3",
                       "mood": "excited"}],
             "pops": [{"kind": "chip", "at": "lex3a", "until": "lex3b", "x": 1190, "y": 930,
                       "text": "Sending and receiving banks in different states",
                       "color": "#1f3a5f", "size": 34}]}),

    Scene("s4", "A letter of credit, step by step", "", [
        Pause("open", 1.0),
        Line("amara4a", "AMARA", "For a new buyer, a documentary letter of credit is the "
             "classic answer. The seller gets paid promptly, and the buyer can still get "
             "credit.", gap=0.3),
        Line("amara4b", "AMARA", "One. The buyer asks its bank, the issuing bank, to open a "
             "credit in favour of SafariTech.", gap=0.25),
        Line("amara4c", "AMARA", "Two. The issuing bank undertakes to pay against the "
             "stated documents, and asks a bank in the seller's country, the advising bank, "
             "to notify the seller.", gap=0.25),
        Line("amara4d", "AMARA", "Three. SafariTech ships, and presents the documents, like "
             "the bill of lading and invoice, to the advising bank.", gap=0.25),
        Line("amara4e", "AMARA", "Four. The advising bank checks the documents, pays "
             "SafariTech, and sends them on to the issuing bank.", gap=0.25),
        Line("amara4f", "AMARA", "Five. The issuing bank checks them, reimburses the "
             "advising bank, debits the buyer, and releases the documents, so the buyer can "
             "collect the goods.", gap=0.4),
        Line("nia4", "NIA", "So nobody hands over goods or money until the paperwork is "
             "right."),
        Pause("hold", 1.4),
    ], spec={"tpl": "flow", "bg": "studio", "heading": "Documentary letter of credit",
             "syl": "C1(e)",
             "nodes": [{"id": "B", "x": 650, "y": 300, "label": "Buyer (applicant)",
                        "icon": "person", "color": "#7768ae", "at": "amara4b", "w": 270},
                       {"id": "IB", "x": 650, "y": 720, "label": "Issuing bank (Dubai)",
                        "icon": "bank", "color": "#7768ae", "at": ["amara4b", 1.5],
                        "w": 270},
                       {"id": "AB", "x": 1650, "y": 720, "label": "Advising bank (Nairobi)",
                        "icon": "bank", "color": "#0f8b8d", "at": "amara4c", "w": 290},
                       {"id": "S", "x": 1650, "y": 300, "label": "Seller (beneficiary)",
                        "icon": "company", "color": "#0f8b8d", "at": ["amara4c", 3.0],
                        "w": 270}],
             "edges": [{"from": "B", "to": "IB", "at": ["amara4b", 1.5], "label": "1 apply",
                        "bend": -40},
                       {"from": "IB", "to": "AB", "at": "amara4c", "label": "2 credit opened",
                        "token": "doc", "bend": -50},
                       {"from": "AB", "to": "S", "at": ["amara4c", 3.0], "label": "advise",
                        "bend": -40},
                       {"from": "S", "to": "AB", "at": "amara4d", "label": "3 documents",
                        "token": "bill", "bend": -40},
                       {"from": "AB", "to": "IB", "at": "amara4e", "label": "4 documents",
                        "token": "bill", "bend": -50},
                       {"from": "IB", "to": "B", "at": "amara4f", "label": "5 documents",
                        "token": "bill", "bend": -40, "color": "#3bb273"}],
             "cast": [{"who": "AMARA", "x": 250, "talk_pose": "present"},
                      {"who": "NIA", "x": 1840, "s": 0.5, "y": 1130, "enter": "nia4"}],
             "pops": [{"kind": "chip", "at": ["amara4e", 1.5], "x": 1150, "y": 500,
                       "text": "Seller paid", "color": "#3bb273", "size": 34},
                      {"kind": "icon", "icon": "ship", "x": 1150, "y": 250, "s": 0.9,
                       "at": "amara4d", "label": "Goods shipped"}]}),

    Scene("s5", "Rules of the letter of credit", "", [
        Pause("open", 1.0),
        Line("lex5a", "LEX", "Most letters of credit follow the ICC's Uniform Customs and "
             "Practice, UCP 600.", say="Most letters of credit follow the I.C.C.'s Uniform "
             "Customs and Practice, U.C.P. 600.", gap=0.3),
        Sfx("pop"),
        Line("lex5b", "LEX", "Autonomy. The credit is separate from the sale contract. Banks "
             "deal in documents, not goods.", gap=0.25),
        Sfx("pop"),
        Line("lex5c", "LEX", "Strict compliance. The documents must match the credit's "
             "terms on their face. A small mismatch can mean no payment.", gap=0.25),
        Sfx("pop"),
        Line("lex5d", "LEX", "Irrevocable. The buyer cannot change or cancel the credit "
             "without the seller's agreement. Under UCP 600, every credit is irrevocable.",
             say="Irrevocable. The buyer cannot change or cancel the credit without the "
                 "seller's agreement. Under U.C.P. 600, every credit is irrevocable.",
             gap=0.25),
        Sfx("pop"),
        Line("lex5e", "LEX", "Confirmed. If the advising bank adds its own promise to pay, "
             "the seller has two banks behind it. Unconfirmed, it relies on the issuing bank "
             "alone.", gap=0.25),
        Sfx("pop"),
        Line("lex5f", "LEX", "And there is a narrow fraud exception. A bank need not pay a "
             "beneficiary who presents documents it knows are fraudulent.", gap=0.4),
        Line("amara5", "AMARA", "For an unknown buyer, I'd always advise a confirmed credit."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "white", "heading": "Letter of credit principles",
             "syl": "C1(e)", "row": 116, "ts": 38,
             "items": [{"at": "lex5b", "text": "Autonomy", "sub": "Separate from the sale · "
                                                                  "documents, not goods",
                        "icon": "scissors", "color": "#0f8b8d"},
                       {"at": "lex5c", "text": "Strict compliance", "sub": "Documents must "
                                                                           "match exactly",
                        "icon": "magnifier", "color": "#e4572e"},
                       {"at": "lex5d", "text": "Irrevocable", "sub": "No change without the "
                                                                     "seller's consent",
                        "icon": "lock", "color": "#7768ae"},
                       {"at": "lex5e", "text": "Confirmed vs unconfirmed",
                        "sub": "Second bank's promise, or issuing bank only",
                        "icon": "shield", "color": "#3bb273"},
                       {"at": "lex5f", "text": "Fraud exception", "sub": "Known fraud: bank "
                                                                         "need not pay",
                        "icon": "mask", "color": "#f2a541"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "AMARA", "x": 1810, "s": 0.55, "y": 1120, "enter": "amara5"}],
             "pops": [{"kind": "chip", "at": "lex5a", "until": "lex5b", "x": 1190, "y": 930,
                       "text": "ICC Uniform Customs and Practice: UCP 600", "color": "#1f3a5f",
                       "size": 34}]}),

    Scene("s6", "Letters of comfort", "", [
        Pause("open", 1.0),
        Line("amara6", "AMARA", "Sometimes a lender to a subsidiary only gets a letter of "
             "comfort from the parent company.", gap=0.3),
        Line("lex6a", "LEX", "A letter of comfort usually says the parent intends to support "
             "its subsidiary. But it is normally a statement of present policy, not a "
             "binding promise.", gap=0.3),
        Line("lex6b", "LEX", "In Kleinwort Benson against Malaysia Mining Corporation, the "
             "parent wrote that its policy was to ensure its subsidiary was always in a "
             "position to meet its liabilities.", gap=0.3),
        Line("lex6c", "LEX", "When the subsidiary collapsed, the bank sued the parent. The "
             "Court of Appeal held the letter was only a statement of policy, not a "
             "contractual promise. The bank lost.", gap=0.4),
        Sfx("sparkle"),
        Pause("stamp", 1.2),
        Line("lex6d", "LEX", "So if you need the parent to be liable, ask for a guarantee, "
             "not comfort."),
        Pause("hold", 1.4),
    ], spec={"tpl": "case", "bg": "bank", "name": "Kleinwort Benson v Malaysia Mining Corp",
             "year": "Court of Appeal, England · 1989", "syl": "C1(e)",
             "rows": [{"at": "lex6b", "label": "Facts", "text": "Parent's letter: our policy "
                                                                "is to keep the subsidiary "
                                                                "able to pay",
                       "color": "#7768ae"},
                      {"at": "lex6c", "label": "Held", "text": "A statement of present "
                                                               "policy, not a contractual "
                                                               "promise",
                       "color": "#e4572e"},
                      {"at": "lex6d", "label": "Lesson", "text": "Want liability? Take a "
                                                                 "guarantee",
                       "color": "#3bb273"}],
             "stamp": {"at": "stamp", "text": "NOT BINDING", "color": "#e4572e"},
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "AMARA", "x": 1810, "s": 0.55, "y": 1120}]}),

    quiz_scene("s7", "Quick check",
               "Under the Model Law on International Credit Transfers, when is a credit "
               "transfer completed?",
               ["When the originator gives the instruction",
                "When the intermediary bank receives the order",
                "When the beneficiary's bank accepts the payment order",
                "When the beneficiary withdraws the cash"], 2,
               "Quick check. Under the Model Law, when is a credit transfer completed?",
               "When the beneficiary's bank accepts the payment order.",
               syl="C1(c)"),

    quiz_scene("s8", "Quick check",
               "What makes a letter of credit “confirmed”?",
               ["The buyer signs it", "A second bank, usually the advising bank, adds its "
                "own undertaking to pay", "The goods have been inspected",
                "It can be revoked at any time"], 1,
               "And what makes a letter of credit confirmed?",
               "A second bank adds its own undertaking to pay.",
               think=4.0, syl="C1(e)"),

    recap_scene("s9", [
        ("Transfers are a chain of payment orders.", "Chain of payment orders"),
        ("Model Law: execute, refund, interest.", "Execute · refund · interest"),
        ("Completed when the beneficiary's bank accepts.", "Complete: beneficiary's bank "
                                                           "accepts"),
        ("Letters of credit: autonomy, strict compliance.", "L/C: autonomy · strict "
                                                             "compliance"),
        ("Letters of comfort rarely bind.", "Comfort letter: not a guarantee"),
    ], [
        Line("lex9", "LEX", "That finishes international trade. Next, we look at the people "
             "who act for a business: agents.", gap=0.3),
        Line("kito9", "KITO", "Good, because I want an agent to sell my kits in Kampala!",
             gap=0.6),
    ], next_ep=13, next_title="The Agent's Authority", next_icon="handshake"),
]
