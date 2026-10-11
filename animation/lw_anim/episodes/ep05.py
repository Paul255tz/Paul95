"""Episode 5 - The Contract Across the Ocean.

Syllabus B1(a)-(b): sphere of application and general provisions of the UN
Convention on Contracts for the International Sale of Goods (CISG, Vienna 1980),
and the rules for forming a contract (offer and acceptance, Articles 14-24).
Setting: SafariTech (Dar es Salaam) orders machines from Hans GmbH (Hamburg) by
email. Tanzania is not a CISG Contracting State but Germany is.
"""
from ._kit import (DISPLAY_NAMES, SERIES, VOICES, Line, Pause, Scene, Sfx,  # noqa: F401
                   quiz_scene, recap_scene, title_scene)

EPISODE = "Episode 5"
EPISODE_TITLE = "The Contract Across the Ocean"
SLUG = "episode05_the_contract_across_the_ocean"

SCENES = [
    title_scene(5, EPISODE_TITLE, "Syllabus B1(a)–(b)", ("ship", "contract")),

    Scene("s1", "An order by email", "", [
        Pause("open", 1.0),
        Line("kito1", "KITO", "Hans emailed a price for five packing machines. I replied "
             "with a few changes. Do we have a contract yet?", gap=0.4),
        Line("nia1", "NIA", "Hamburg to Dar es Salaam. That's an international sale of "
             "goods.", gap=0.4),
        Line("lex1", "LEX", "Which brings us to the CISG, the UN Convention on Contracts for "
             "the International Sale of Goods, agreed in Vienna in 1980. More than ninety "
             "countries have joined it.",
             say="Which brings us to the C.I.S.G., the U.N. Convention on Contracts for the "
                 "International Sale of Goods, agreed in Vienna in 1980. More than ninety "
                 "countries have joined it.", gap=0.3),
        Line("lex1b", "LEX", "It gives traders one set of rules for forming the contract, "
             "and for the rights and duties of seller and buyer."),
        Pause("hold", 1.2),
    ], spec={"tpl": "talk", "bg": "harbour", "syl": "B1(a)",
             "cast": [{"who": "KITO", "x": 1450, "y": 1030, "s": 0.95, "pose": "hold_r",
                       "mood": "thinking"},
                      {"who": "NIA", "x": 950, "y": 1030, "s": 0.92},
                      {"who": "LEX", "x": 450, "y": 1030, "s": 0.9, "enter": "lex1",
                       "from": "left"}],
             "pops": [{"kind": "icon", "icon": "envelope", "x": 1180, "y": 300, "s": 1.2,
                       "at": ["kito1", 0.6], "until": "nia1", "float": True},
                      {"kind": "card", "at": ["lex1", 2.0], "x": 1180, "y": 300, "w": 760,
                       "h": 220, "title": "CISG · Vienna 1980",
                       "body": "UN Convention on Contracts for the International Sale "
                               "of Goods", "color": "#0f8b8d"}]}),

    Scene("s2", "Does the CISG apply?", "", [
        Pause("open", 1.0),
        Line("lex2a", "LEX", "The Convention applies to contracts for the sale of goods "
             "between parties whose places of business are in different states.", gap=0.3),
        Sfx("pop"),
        Line("lex2b", "LEX", "Route A: both states are Contracting States.", gap=0.25),
        Sfx("pop"),
        Line("lex2c", "LEX", "Route B: the rules of private international law lead to the "
             "law of a Contracting State.", gap=0.5),
        Line("lex2d", "LEX", "Nationality is irrelevant. What matters is where each party "
             "has its place of business.", gap=0.4),
        Line("nia2", "NIA", "But Tanzania hasn't joined the Convention, and Germany has.",
             gap=0.3),
        Line("lex2e", "LEX", "So route A fails. But if the contract chooses German law, "
             "route B applies, and German law includes the CISG.", gap=0.4),
        Line("lex2f", "LEX", "And remember, the parties can also exclude the Convention, or "
             "vary its rules, in their contract."),
        Pause("hold", 1.4),
    ], spec={"tpl": "flow", "bg": "studio_teal", "heading": "Article 1: sphere of application",
             "syl": "B1(a)",
             "nodes": [{"id": "sale", "x": 1150, "y": 250, "label": "Sale of goods · places "
                                                                    "of business in "
                                                                    "different states",
                        "icon": "box", "color": "#1f3a5f", "at": "lex2a", "w": 420, "h": 200},
                       {"id": "a", "x": 760, "y": 580, "label": "A: both are Contracting "
                                                               "States",
                        "icon": "flag", "color": "#0f8b8d", "at": "lex2b", "w": 320},
                       {"id": "b", "x": 1540, "y": 580, "label": "B: conflict rules point "
                                                                "to a Contracting State's "
                                                                "law",
                        "icon": "signpost", "color": "#7768ae", "at": "lex2c", "w": 340,
                        "h": 220},
                       {"id": "cisg", "x": 1150, "y": 860, "label": "CISG applies",
                        "icon": "check", "color": "#3bb273", "at": ["lex2c", 2.0], "w": 300,
                        "h": 170}],
             "edges": [{"from": "sale", "to": "a", "at": "lex2b"},
                       {"from": "sale", "to": "b", "at": "lex2c"},
                       {"from": "a", "to": "cisg", "at": ["lex2c", 1.6], "color": "#3bb273"},
                       {"from": "b", "to": "cisg", "at": ["lex2c", 1.6], "color": "#3bb273"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia2"}],
             "pops": [{"kind": "chip", "at": "lex2d", "until": "nia2", "x": 1150, "y": 400,
                       "text": "Place of business counts, not nationality", "color": "#e4572e",
                       "size": 32},
                      {"kind": "card", "at": "lex2e", "x": 1150, "y": 480, "w": 920, "h": 300,
                       "title": "Local lens: Tanzania × Germany",
                       "body": "Tanzania is not a Contracting State, Germany is. Choose German "
                               "law → CISG applies via route B. Parties may opt out (Art 6).",
                       "color": "#f2a541", "dim": True, "bs": 36}]}),

    Scene("s3", "What the CISG does not cover", "", [
        Pause("open", 1.0),
        Line("lex3a", "LEX", "Some sales are left out completely.", gap=0.3),
        Sfx("pop"),
        Line("lex3b", "LEX", "Consumer sales, for personal, family or household use, unless "
             "the seller neither knew nor ought to have known that.", gap=0.25),
        Sfx("pop"),
        Line("lex3c", "LEX", "Sales by auction, or on execution by legal authority.",
             gap=0.25),
        Sfx("pop"),
        Line("lex3d", "LEX", "Shares, securities, negotiable instruments, and money.",
             gap=0.25),
        Sfx("pop"),
        Line("lex3e", "LEX", "Ships, hovercraft and aircraft.", gap=0.25),
        Sfx("pop"),
        Line("lex3f", "LEX", "And electricity.", gap=0.5),
        Line("lex3g", "LEX", "Goods to be manufactured do count as sales, unless the buyer "
             "supplies a substantial part of the materials. And contracts that are mainly "
             "for labour or services are excluded.", gap=0.4),
        Line("lex3h", "LEX", "Finally, the Convention does not deal with whether the contract "
             "is valid, who owns the goods, or liability for death or personal injury. "
             "National law covers those."),
        Pause("hold", 1.6),
    ], spec={"tpl": "board", "style": "white", "layout": "grid", "cols": 3,
             "heading": "Excluded from the CISG", "syl": "B1(a)", "cell_h": 290, "ts": 36,
             "items": [{"at": "lex3b", "text": "Consumer sales", "sub": "Personal, family, "
                                                                        "household",
                        "icon": "house", "color": "#e4572e"},
                       {"at": "lex3c", "text": "Auctions · execution", "sub": "By legal "
                                                                              "authority",
                        "icon": "gavel", "color": "#7768ae"},
                       {"at": "lex3d", "text": "Shares, securities, money",
                        "sub": "and negotiable instruments", "icon": "chart",
                        "color": "#0f8b8d"},
                       {"at": "lex3e", "text": "Ships, hovercraft, aircraft", "icon": "ship",
                        "color": "#2b86c5"},
                       {"at": "lex3f", "text": "Electricity", "icon": "bulb",
                        "color": "#f2a541"},
                       {"at": "lex3g", "text": "Mainly labour or services",
                        "sub": "or buyer supplies most materials", "icon": "people",
                        "color": "#3bb273"}],
             "cast": [{"who": "LEX", "x": 250}],
             "pops": [{"kind": "card", "at": "lex3h", "x": 1190, "y": 470, "w": 900, "h": 280,
                       "title": "Not covered (Arts 4–5)",
                       "body": "Validity of the contract · ownership (property) of the goods · "
                               "death or personal injury", "color": "#1f3a5f", "dim": True,
                       "bs": 38}]}),

    Scene("s4", "General provisions", "", [
        Pause("open", 1.0),
        Line("lex4a", "LEX", "A few general rules run through the whole Convention.",
             gap=0.3),
        Sfx("pop"),
        Line("lex4b", "LEX", "Interpret it with regard to its international character, the "
             "need for uniformity, and good faith in international trade.", gap=0.25),
        Sfx("pop"),
        Line("lex4c", "LEX", "Gaps are filled by its general principles, and only then by "
             "the applicable national law.", gap=0.25),
        Sfx("pop"),
        Line("lex4d", "LEX", "The parties' statements are read by their intent, if the "
             "other side knew it, or else as a reasonable person would understand them.",
             gap=0.25),
        Sfx("pop"),
        Line("lex4e", "LEX", "Parties are bound by usages they agreed to, and by practices "
             "they have established between themselves.", gap=0.25),
        Sfx("pop"),
        Line("lex4f", "LEX", "And a sales contract need not be in writing. It can be proved "
             "by any means, even by witnesses.", gap=0.4),
        Line("kito4", "KITO", "So even a phone call with Hans could create a contract!"),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "heading": "General provisions (Arts 7–11)",
             "syl": "B1(a)", "row": 120, "ts": 40,
             "items": [{"at": "lex4b", "text": "International, uniform, good faith",
                        "sub": "How to interpret the Convention", "icon": "globe"},
                       {"at": "lex4c", "text": "Gaps: general principles first",
                        "sub": "then the applicable national law", "icon": "book"},
                       {"at": "lex4d", "text": "Intent, or a reasonable person",
                        "sub": "How statements and conduct are read", "icon": "brain"},
                       {"at": "lex4e", "text": "Usages and established practices bind",
                        "sub": "What the parties agreed or have always done",
                        "icon": "handshake"},
                       {"at": "lex4f", "text": "No writing needed",
                        "sub": "Any proof, even witnesses", "icon": "mic"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "KITO", "x": 1800, "s": 0.55, "y": 1120, "enter": "kito4",
                       "mood": "excited"}]}),

    Scene("s5", "Making an offer", "", [
        Pause("open", 1.0),
        Line("lex5a", "LEX", "A contract needs an offer, and an acceptance.", gap=0.3),
        Sfx("pop"),
        Line("lex5b", "LEX", "An offer is a proposal addressed to one or more specific "
             "people. It must be sufficiently definite, naming the goods and fixing the "
             "quantity and the price, and it must show an intention to be bound.", gap=0.4),
        Line("lex5c", "LEX", "Adverts, catalogues and price lists sent to the public are "
             "usually just invitations to make offers.", gap=0.4),
        Sfx("pop"),
        Line("lex5d", "LEX", "An offer takes effect when it reaches the offeree.", gap=0.25),
        Sfx("pop"),
        Line("lex5e", "LEX", "It can be withdrawn if the withdrawal arrives first, or at the "
             "same time.", gap=0.25),
        Sfx("pop"),
        Line("lex5f", "LEX", "It can be revoked until the offeree sends an acceptance. But "
             "not if the offer states a fixed time for acceptance, says it is irrevocable, "
             "or the offeree reasonably relied on it.", gap=0.25),
        Sfx("pop"),
        Line("lex5g", "LEX", "And a rejection ends the offer when it reaches the offeror.",
             gap=0.4),
        Line("hans5", "HANS", "My email offered five machines at forty thousand euros each, "
             "open for fourteen days. So I can't revoke it during that time."),
        Pause("hold", 1.4),
    ], spec={"tpl": "timeline", "bg": "studio", "heading": "The life of an offer (Arts 14–17)",
             "syl": "B1(b)", "cw": 290, "y": 540,
             "events": [{"at": "lex5b", "label": "Offer made", "sub": "Definite: goods, "
                                                                     "quantity, price",
                         "icon": "envelope", "color": "#0f8b8d"},
                        {"at": "lex5d", "label": "Reaches offeree", "sub": "Now effective",
                         "icon": "check", "color": "#3bb273"},
                        {"at": "lex5e", "label": "Withdrawal", "sub": "Must arrive first or "
                                                                     "at the same time",
                         "icon": "door", "color": "#f2a541"},
                        {"at": "lex5f", "label": "Revocation", "sub": "Before acceptance is "
                                                                     "sent · not if "
                                                                     "irrevocable",
                         "icon": "cross", "color": "#e4572e"},
                        {"at": "lex5g", "label": "Rejection", "sub": "Ends the offer",
                         "icon": "stamp", "color": "#7768ae"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "HANS", "x": 1810, "s": 0.55, "y": 1120, "enter": "hans5"}],
             "pops": [{"kind": "chip", "at": "lex5c", "until": "lex5d", "x": 1200, "y": 950,
                       "text": "Adverts and catalogues = invitations", "color": "#1f3a5f",
                       "size": 34}]}),

    Scene("s6", "Accepting, or countering?", "", [
        Pause("open", 1.0),
        Line("lex6a", "LEX", "Acceptance is a statement, or conduct, showing assent. "
             "Silence or inactivity alone is never acceptance.", gap=0.3),
        Line("lex6b", "LEX", "It takes effect when it reaches the offeror, within the time "
             "fixed, or a reasonable time. An oral offer must be accepted immediately, "
             "unless the circumstances show otherwise.", gap=0.3),
        Line("lex6c", "LEX", "The contract is concluded at the moment the acceptance takes "
             "effect.", gap=0.5),
        Line("lex6d", "LEX", "Now the trap. A reply that adds to, or changes, the offer is a "
             "rejection plus a counter-offer.", gap=0.3),
        Line("lex6e", "LEX", "Unless the changes are immaterial. Then it is still an "
             "acceptance, unless the offeror objects without undue delay.", gap=0.3),
        Line("lex6f", "LEX", "Changes to price, payment, quality, quantity, place and time of "
             "delivery, liability, or dispute settlement are always material.", gap=0.4),
        Line("kito6", "KITO", "I replied: we accept, but at thirty-eight thousand euros.",
             gap=0.3),
        Line("nia6", "NIA", "That changes the price. So it's a counter-offer, and there's no "
             "contract until Hans accepts it."),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio_purple",
             "heading": "Acceptance vs counter-offer (Arts 18–19)", "syl": "B1(b)", "ts": 34,
             "cols": [{"title": "Acceptance", "icon": "check", "color": "#3bb273",
                       "at": "lex6a",
                       "items": [{"at": ["lex6a", 0.2], "text": "Statement or conduct "
                                                               "showing assent",
                                  "good": True},
                                 {"at": ["lex6a", 3.4], "text": "Silence alone never counts",
                                  "bad": True},
                                 {"at": "lex6b", "text": "Effective when it reaches the "
                                                         "offeror", "good": True},
                                 {"at": "lex6c", "text": "Contract concluded at that moment",
                                  "good": True},
                                 {"at": "lex6e", "text": "Immaterial changes: still "
                                                         "acceptance unless offeror objects",
                                  "good": True}]},
                      {"title": "Counter-offer", "icon": "cross", "color": "#e4572e",
                       "at": "lex6d",
                       "items": [{"at": ["lex6d", 0.4], "text": "Reply adds or changes "
                                                               "terms",
                                  "bad": True},
                                 {"at": ["lex6d", 2.8], "text": "= rejection + new offer",
                                  "bad": True},
                                 {"at": "lex6f", "text": "Material: price, payment, quality, "
                                                         "quantity, delivery, liability, "
                                                         "disputes", "bad": True},
                                 {"at": "nia6", "text": "Kito's €38,000 reply = counter-offer",
                                  "bad": True}]}],
             "vs": True,
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "KITO", "x": 1660, "s": 0.55, "y": 1120, "enter": "kito6"},
                      {"who": "NIA", "x": 1820, "s": 0.55, "y": 1120, "enter": "nia6"}]}),

    quiz_scene("s7", "Quick check",
               "Kito replies to Hans's offer: “We accept, but the price must be €38,000.” "
               "Under the CISG, this reply is…",
               ["An acceptance", "An acceptance with an immaterial change",
                "A rejection and counter-offer", "A withdrawal of the offer"], 2,
               "Quick check. Kito replies, we accept, but the price must be thirty-eight "
               "thousand euros. What is that reply?",
               "A rejection, and a counter-offer.",
               why=("A change to the price is always a material alteration",
                    "A change to the price is always a material alteration."),
               syl="B1(b)"),

    quiz_scene("s8", "Quick check",
               "Tanzania has not joined the CISG. Can the CISG still govern a sale between a "
               "Tanzanian buyer and a German seller?",
               ["No, never", "Yes, if the conflict rules lead to German law",
                "Only if both parties are German nationals", "Only for consumer sales"], 1,
               "And this one. Can the CISG govern a sale between a Tanzanian buyer and a "
               "German seller?",
               "Yes, if the conflict rules lead to German law.",
               why=("Article 1(1)(b): the law of a Contracting State applies",
                    "That's Article 1, paragraph 1 b. The law of a Contracting State "
                    "applies, and that law includes the Convention."),
               syl="B1(a)"),

    recap_scene("s9", [
        ("Different states, places of business.", "Places of business in different states"),
        ("Two routes: both Contracting States, or conflict rules.", "Art 1: route A or B"),
        ("Exclusions: consumers, auctions, shares, ships, electricity.",
         "Excluded: consumer, auction, shares, ships, power"),
        ("Offer must be definite. Revocation has limits.", "Offer: definite · revocable "
         "until acceptance sent"),
        ("Material change means counter-offer.", "Material change = counter-offer"),
    ], [
        Line("lex9", "LEX", "Next time, Hans and Kito must choose how the machines travel, "
             "who pays for the voyage, and where the risk passes. That means Incoterms.",
             say="Next time, Hans and Kito must choose how the machines travel, who pays for "
                 "the voyage, and where the risk passes. That means Inco-terms.", gap=0.3),
        Line("cargo9", "CARGO", "Eleven little codes, and every one of them matters!",
             gap=0.6),
    ], next_ep=6, next_title="Incoterms: Who Pays, Who Risks", next_icon="container"),
]
