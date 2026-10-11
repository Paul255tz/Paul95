"""Episode 4 - The Arbitration Room.

Syllabus A3(a)-(e): court adjudication and ADR; the ICC International Court of
Arbitration; the UNCITRAL Model Law on International Commercial Arbitration;
the arbitral tribunal; arbitral awards. Setting: Hans's machine arrives in Dar
es Salaam faulty, and the contract says disputes go to arbitration in Nairobi.
"""
from ._kit import (DISPLAY_NAMES, SERIES, VOICES, Line, Pause, Scene, Sfx,  # noqa: F401
                   quiz_scene, recap_scene, title_scene)

EPISODE = "Episode 4"
EPISODE_TITLE = "The Arbitration Room"
SLUG = "episode04_the_arbitration_room"

SCENES = [
    title_scene(4, EPISODE_TITLE, "Syllabus A3", ("gavel", "handshake")),

    Scene("s1", "A dispute arrives", "", [
        Pause("open", 1.0),
        Line("kito1", "KITO", "Hans's machine keeps breaking down! I'm taking him to the "
             "High Court in Dar es Salaam!", gap=0.4),
        Sfx("paper"),
        Line("nia1", "NIA", "Wait. Clause twenty says any dispute goes to arbitration, "
             "seated in Nairobi.", gap=0.4),
        Line("lex1", "LEX", "Then the court will usually send you to arbitration. Under the "
             "Model Law, a court must refer the parties to arbitration when there is a valid "
             "arbitration agreement.", gap=0.3),
        Line("kito1b", "KITO", "So what's the difference between a court and an arbitration?"),
        Pause("hold", 1.2),
    ], spec={"tpl": "talk", "bg": "office", "syl": "A3(a)",
             "cast": [{"who": "KITO", "x": 1450, "y": 1030, "s": 0.95, "mood": "angry",
                       "talk_pose": "demand", "moods": [["lex1", "thinking"]]},
                      {"who": "NIA", "x": 900, "y": 1030, "s": 0.92},
                      {"who": "LEX", "x": 420, "y": 1030, "s": 0.9, "enter": "lex1",
                       "from": "left"}],
             "pops": [{"kind": "card", "at": ["nia1", 0.4], "until": "kito1b", "x": 1180,
                       "y": 300, "w": 820, "h": 220, "title": "Clause 20: Arbitration",
                       "body": "Any dispute shall be finally resolved by arbitration. "
                               "Seat: Nairobi.", "color": "#7768ae"}]}),

    Scene("s2", "Court or arbitration?", "", [
        Pause("open", 1.0),
        Line("lex2a", "LEX", "Court adjudication has real strengths.", gap=0.3),
        Line("lex2b", "LEX", "Judges are legal experts. Decisions follow precedent, so "
             "outcomes are predictable, and there are rights of appeal.", gap=0.3),
        Line("lex2c", "LEX", "But courts can be slow, formal and expensive, and hearings are "
             "usually public.", gap=0.5),
        Line("lex2d", "LEX", "Arbitration is private. The parties choose an expert "
             "arbitrator, and a flexible procedure, which is often quicker and less "
             "stressful.", gap=0.3),
        Line("lex2e", "LEX", "But an arbitrator may not be a legal expert, awards create no "
             "precedent, and the grounds to challenge an award are very narrow.", gap=0.4),
        Line("nia2", "NIA", "And it isn't always cheaper. The parties pay the arbitrators "
             "and the venue."),
        Pause("hold", 1.6),
    ], spec={"tpl": "compare", "bg": "studio", "heading": "Court vs arbitration", "syl": "A3(a)",
             "ts": 34,
             "cols": [{"title": "Court", "icon": "court", "color": "#1f3a5f", "at": "lex2a",
                       "items": [{"at": ["lex2b", 0.1], "text": "Judges are legal experts",
                                  "good": True},
                                 {"at": ["lex2b", 2.2], "text": "Precedent: predictable",
                                  "good": True},
                                 {"at": ["lex2b", 5.0], "text": "Rights of appeal",
                                  "good": True},
                                 {"at": ["lex2c", 0.6], "text": "Slow, formal, costly",
                                  "bad": True},
                                 {"at": ["lex2c", 3.6], "text": "Usually public", "bad": True}]},
                      {"title": "Arbitration", "icon": "handshake", "color": "#0f8b8d",
                       "at": "lex2d",
                       "items": [{"at": ["lex2d", 0.3], "text": "Private and confidential",
                                  "good": True},
                                 {"at": ["lex2d", 1.6], "text": "Expert arbitrator, chosen "
                                                                "by the parties",
                                  "good": True},
                                 {"at": ["lex2d", 4.0], "text": "Flexible, often quicker",
                                  "good": True},
                                 {"at": ["lex2e", 0.3], "text": "Arbitrator may lack legal "
                                                                "expertise", "bad": True},
                                 {"at": ["lex2e", 3.2], "text": "No precedent", "bad": True},
                                 {"at": ["lex2e", 4.6], "text": "Narrow grounds to challenge",
                                  "bad": True},
                                 {"at": "nia2", "text": "Not always cheaper", "bad": True}]}],
             "vs": True,
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1800, "s": 0.55, "y": 1120, "enter": "nia2"}]}),

    Scene("s3", "The ADR spectrum", "", [
        Pause("open", 1.0),
        Line("lex3a", "LEX", "Arbitration is one of several ways to resolve a dispute "
             "outside court. Think of a spectrum.", gap=0.3),
        Sfx("pop"),
        Line("lex3b", "LEX", "In negotiation, the parties talk directly.", gap=0.25),
        Sfx("pop"),
        Line("lex3c", "LEX", "In mediation, a neutral mediator helps them reach their own "
             "agreement, but imposes nothing.", gap=0.25),
        Sfx("pop"),
        Line("lex3d", "LEX", "In conciliation, the neutral goes further, and proposes terms "
             "for settlement.", gap=0.25),
        Sfx("pop"),
        Line("lex3e", "LEX", "In arbitration, a tribunal makes a binding award.", gap=0.25),
        Sfx("pop"),
        Line("lex3f", "LEX", "And in litigation, a court gives a binding judgment.", gap=0.5),
        Line("nia3", "NIA", "So moving along the line, the parties hand over more control."),
        Pause("hold", 1.4),
    ], spec={"tpl": "timeline", "bg": "studio_teal", "heading": "From talking to judging",
             "syl": "A3(a)", "cw": 290,
             "events": [{"at": "lex3b", "label": "Negotiation", "sub": "Parties talk directly",
                         "icon": "handshake"},
                        {"at": "lex3c", "label": "Mediation", "sub": "Neutral helps, imposes "
                                                                    "nothing",
                         "icon": "people"},
                        {"at": "lex3d", "label": "Conciliation", "sub": "Neutral proposes "
                                                                       "terms",
                         "icon": "bulb"},
                        {"at": "lex3e", "label": "Arbitration", "sub": "Binding award",
                         "icon": "gavel"},
                        {"at": "lex3f", "label": "Litigation", "sub": "Court judgment",
                         "icon": "court"}],
             "cast": [{"who": "LEX", "x": 250}],
             "pops": [{"kind": "chip", "at": "nia3", "x": 1200, "y": 960,
                       "text": "More control handed to a third party →", "color": "#e4572e",
                       "size": 34}]}),

    Scene("s4", "The ICC International Court of Arbitration", "", [
        Pause("open", 1.0),
        Line("lex4a", "LEX", "One famous institution is the ICC's International Court of "
             "Arbitration in Paris, created in 1923.",
             say="One famous institution is the I.C.C.'s International Court of Arbitration "
                 "in Paris, created in 1923.", gap=0.3),
        Line("lex4b", "LEX", "Despite its name, it does not decide disputes itself. It "
             "administers and supervises ICC arbitrations.",
             say="Despite its name, it does not decide disputes itself. It administers and "
                 "supervises I.C.C. arbitrations.", gap=0.4),
        Sfx("pop"),
        Line("lex4c", "LEX", "It confirms or appoints the arbitrators.", gap=0.25),
        Sfx("pop"),
        Line("lex4d", "LEX", "It decides challenges against arbitrators.", gap=0.25),
        Sfx("pop"),
        Line("lex4e", "LEX", "It scrutinises and approves draft awards, before they are "
             "signed.", gap=0.25),
        Sfx("pop"),
        Line("lex4f", "LEX", "And it fixes the arbitrators' fees and expenses.", gap=0.5),
        Line("nia4", "NIA", "So the court is the referee's supervisor, not the referee."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "heading": "ICC Court of Arbitration (1923)",
             "syl": "A3(b)", "row": 120, "ts": 42,
             "items": [{"at": "lex4b", "text": "Administers; does not decide disputes",
                        "icon": "cross", "color": "#e4572e"},
                       {"at": "lex4c", "text": "Confirms or appoints arbitrators",
                        "icon": "people", "color": "#0f8b8d"},
                       {"at": "lex4d", "text": "Decides challenges to arbitrators",
                        "icon": "warning", "color": "#f2a541"},
                       {"at": "lex4e", "text": "Scrutinises and approves draft awards",
                        "icon": "magnifier", "color": "#7768ae"},
                       {"at": "lex4f", "text": "Fixes fees and expenses",
                        "icon": "coin", "color": "#3bb273"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1800, "s": 0.55, "y": 1120, "enter": "nia4"}]}),

    Scene("s5", "The UNCITRAL Model Law", "", [
        Pause("open", 1.0),
        Line("lex5a", "LEX", "Many countries base their arbitration law on the UNCITRAL "
             "Model Law on International Commercial Arbitration. Kenya's Arbitration Act of "
             "1995 follows it closely.",
             say="Many countries base their arbitration law on the Uncitral Model Law on "
                 "International Commercial Arbitration. Kenya's Arbitration Act of 1995 "
                 "follows it closely.", gap=0.4),
        Sfx("pop"),
        Line("lex5b", "LEX", "First, the arbitration agreement must be in writing. A signed "
             "contract, an exchange of letters or emails, or a reference to a document "
             "containing the clause, will all do.", gap=0.3),
        Sfx("pop"),
        Line("lex5c", "LEX", "Second, a court must refer the parties to arbitration, unless "
             "the agreement is void or cannot be performed.", gap=0.3),
        Sfx("pop"),
        Line("lex5d", "LEX", "Third, the tribunal can rule on its own jurisdiction. And the "
             "arbitration clause is treated as separate from the main contract, so it "
             "survives even if the contract is void.", gap=0.3),
        Sfx("pop"),
        Line("lex5e", "LEX", "Fourth, the tribunal may order interim measures, such as "
             "preserving goods or evidence.", gap=0.3),
        Sfx("pop"),
        Line("lex5f", "LEX", "And fifth, the parties must be treated equally, and each given "
             "a full opportunity to present its case.", gap=0.4),
        Line("nia5", "NIA", "And Tanzania?", gap=0.3),
        Line("lex5g", "LEX", "Tanzania's Arbitration Act of 2020 draws more on the English "
             "Arbitration Act, but shares the same core ideas."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "white", "heading": "Model Law: the key rules",
             "syl": "A3(c)", "row": 120, "ts": 40,
             "items": [{"at": "lex5b", "text": "Agreement must be in writing",
                        "sub": "Signed document · letters or emails · reference to a clause",
                        "icon": "contract"},
                       {"at": "lex5c", "text": "Courts refer parties to arbitration",
                        "sub": "Unless the agreement is void or incapable of performance",
                        "icon": "court"},
                       {"at": "lex5d", "text": "Tribunal rules on its own jurisdiction",
                        "sub": "The clause is separable from the main contract",
                        "icon": "scissors"},
                       {"at": "lex5e", "text": "Interim measures",
                        "sub": "e.g. preserve goods or evidence", "icon": "lock"},
                       {"at": "lex5f", "text": "Equal treatment, full opportunity",
                        "sub": "Each party can present its case", "icon": "scales"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1800, "s": 0.55, "y": 1120, "enter": "nia5"}],
             "pops": [{"kind": "card", "at": "lex5g", "x": 1190, "y": 480, "w": 860,
                       "h": 240, "title": "Local lens: East Africa",
                       "body": "Kenya: Arbitration Act 1995 (Model Law) · Tanzania: "
                               "Arbitration Act 2020 (English-style)", "color": "#f2a541",
                       "dim": True, "bs": 36}]}),

    Scene("s6", "Building the tribunal", "", [
        Pause("open", 1.0),
        Line("lex6a", "LEX", "The parties can agree on the number of arbitrators. If they "
             "agree on one, they must also agree who it is, or a court or appointing "
             "authority will choose.", gap=0.4),
        Line("lex6b", "LEX", "If they have not agreed the number, the Model Law says three.",
             gap=0.3),
        Sfx("pop"),
        Line("lex6c", "LEX", "Each party appoints one arbitrator.", gap=0.25),
        Sfx("pop"),
        Line("lex6d", "LEX", "And those two appoint the third, who presides.", gap=0.5),
        Line("lex6e", "LEX", "Nationality alone cannot bar anyone. But every arbitrator must "
             "be impartial and independent, and must disclose anything that could raise "
             "justifiable doubts.", gap=0.3),
        Line("lex6f", "LEX", "A party may challenge an arbitrator on those grounds, or for "
             "lacking the agreed qualifications. If an arbitrator cannot act, they withdraw, "
             "or the parties end the mandate, and a substitute is appointed.", gap=0.4),
        Line("hans6", "HANS", "Then I appoint an engineer, and Kito appoints a lawyer.",
             gap=0.3),
        Line("kito6", "KITO", "Deal. And they pick the chair together."),
        Pause("hold", 1.4),
    ], spec={"tpl": "flow", "bg": "studio_teal", "heading": "Default tribunal: three arbitrators",
             "syl": "A3(d)",
             "nodes": [{"id": "k", "x": 660, "y": 380, "label": "SafariTech (claimant)",
                        "icon": "company", "color": "#0f8b8d", "at": "lex6c", "w": 290},
                       {"id": "h", "x": 1640, "y": 380, "label": "Hans GmbH (respondent)",
                        "icon": "factory", "color": "#3d405b", "at": "lex6c", "w": 290},
                       {"id": "a1", "x": 760, "y": 720, "label": "Arbitrator 1",
                        "icon": "person", "color": "#0f8b8d", "at": ["lex6c", 0.8]},
                       {"id": "a2", "x": 1540, "y": 720, "label": "Arbitrator 2",
                        "icon": "person", "color": "#3d405b", "at": ["lex6c", 1.2]},
                       {"id": "a3", "x": 1150, "y": 520, "label": "Presiding arbitrator",
                        "icon": "gavel", "color": "#e4572e", "at": "lex6d", "w": 290}],
             "edges": [{"from": "k", "to": "a1", "at": ["lex6c", 0.6], "label": "appoints"},
                       {"from": "h", "to": "a2", "at": ["lex6c", 1.0], "label": "appoints"},
                       {"from": "a1", "to": "a3", "at": ["lex6d", 0.5], "color": "#e4572e"},
                       {"from": "a2", "to": "a3", "at": ["lex6d", 0.5], "color": "#e4572e"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "HANS", "x": 1830, "s": 0.55, "y": 1120, "enter": "hans6"},
                      {"who": "KITO", "x": 1660, "s": 0.55, "y": 1120, "enter": "kito6"}],
             "pops": [{"kind": "card", "at": "lex6e", "until": "hans6", "x": 1150, "y": 470,
                       "w": 900, "h": 300, "title": "Impartial and independent",
                       "body": "Disclose anything raising justifiable doubts. Challenge for "
                               "doubts or missing agreed qualifications.",
                       "color": "#7768ae", "dim": True, "bs": 38}]}),

    Scene("s7", "The award", "", [
        Pause("open", 1.0),
        Line("lex7a", "LEX", "With three arbitrators, decisions are made by a majority. If "
             "the parties settle, the tribunal can record it as a consent award.", gap=0.4),
        Line("lex7b", "LEX", "An award must be in writing and signed. It must give reasons, "
             "unless the parties agree otherwise, and state its date and the place of "
             "arbitration.", gap=0.4),
        Line("lex7c", "LEX", "Within thirty days, a party may ask the tribunal to correct "
             "typing or calculation errors.", gap=0.4),
        Line("lex7d", "LEX", "An award is binding, and can be enforced in any country, "
             "including through the New York Convention of 1958, which Tanzania and Kenya "
             "have both joined.", gap=0.3),
        Sfx("sparkle"),
        Pause("stamp", 1.4),
        Line("nia7", "NIA", "So the award is final. Can it ever be cancelled?"),
        Pause("hold", 1.0),
    ], spec={"tpl": "case", "bg": "arbitration", "name": "Final Award",
             "year": "SafariTech Ltd v Hans GmbH · Seat: Nairobi", "syl": "A3(e)",
             "rows": [{"at": "lex7a", "label": "Decision", "text": "By majority of the "
                                                                   "tribunal (or a consent "
                                                                   "award if they settle)",
                       "color": "#0f8b8d"},
                      {"at": "lex7b", "label": "Form", "text": "In writing · signed · reasons "
                                                               "· date and place",
                       "color": "#7768ae"},
                      {"at": "lex7c", "label": "Fix-ups", "text": "Correction of clerical or "
                                                                  "calculation errors within "
                                                                  "30 days",
                       "color": "#f2a541"},
                      {"at": "lex7d", "label": "Effect", "text": "Binding and enforceable "
                                                                 "abroad · New York "
                                                                 "Convention 1958",
                       "color": "#3bb273"}],
             "stamp": {"at": "stamp", "text": "BINDING", "color": "#3bb273"},
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1800, "s": 0.55, "y": 1120, "enter": "nia7"}]}),

    Scene("s8", "Setting an award aside", "", [
        Pause("open", 1.0),
        Line("lex8a", "LEX", "Only rarely. The only route is an application to the court at "
             "the seat, made within three months of receiving the award.", gap=0.3),
        Line("lex8b", "LEX", "The court does not re-hear the merits. A wrong decision on the "
             "facts or the law is not enough. The grounds are listed.", gap=0.4),
        Sfx("pop"),
        Line("lex8c", "LEX", "A party lacked capacity, or the arbitration agreement was "
             "invalid.", gap=0.25),
        Sfx("pop"),
        Line("lex8d", "LEX", "A party was not given proper notice, or could not present its "
             "case.", gap=0.25),
        Sfx("pop"),
        Line("lex8e", "LEX", "The award deals with matters outside what was submitted.",
             gap=0.25),
        Sfx("pop"),
        Line("lex8f", "LEX", "The tribunal or procedure did not follow the agreement.",
             gap=0.25),
        Sfx("pop"),
        Line("lex8g", "LEX", "Or the court itself finds the subject cannot be arbitrated, or "
             "the award conflicts with public policy.", gap=0.4),
        Line("lex8h", "LEX", "Almost the same grounds allow a court elsewhere to refuse "
             "recognition and enforcement."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "heading": "Setting aside: the only grounds",
             "syl": "A3(e)", "row": 116, "ts": 38,
             "items": [{"at": "lex8c", "text": "Incapacity or invalid agreement",
                        "icon": "contract", "color": "#e4572e"},
                       {"at": "lex8d", "text": "No proper notice / could not present case",
                        "icon": "envelope", "color": "#f2a541"},
                       {"at": "lex8e", "text": "Outside the scope of the submission",
                        "icon": "warning", "color": "#7768ae"},
                       {"at": "lex8f", "text": "Tribunal or procedure not as agreed",
                        "icon": "people", "color": "#0f8b8d"},
                       {"at": "lex8g", "text": "Not arbitrable · against public policy",
                        "icon": "shield", "color": "#3bb273"}],
             "cast": [{"who": "LEX", "x": 250}],
             "pops": [{"kind": "chip", "at": "lex8a", "until": "lex8c", "x": 1190, "y": 960,
                       "text": "Court at the seat · within 3 months", "color": "#1f3a5f",
                       "size": 36},
                      {"kind": "stamp", "at": ["lex8b", 1.8], "until": "lex8c", "x": 1190,
                       "y": 500, "text": "NO RE-HEARING OF THE MERITS", "color": "#e4572e",
                       "size": 48}]}),

    quiz_scene("s9", "Quick check",
               "Under the Model Law, if the parties have not agreed the number of "
               "arbitrators, how many will there be?",
               ["One", "Two", "Three", "Five"], 2,
               "Quick check. If the parties have not agreed how many arbitrators, how many "
               "does the Model Law provide?",
               "Three.",
               why=("Each party appoints one, and those two appoint the presiding arbitrator",
                    "Each party appoints one, and those two appoint the presiding "
                    "arbitrator."),
               syl="A3(d)"),

    quiz_scene("s10", "Quick check",
               "Which of these is NOT a ground for setting aside an award?",
               ["A party lacked capacity", "The award conflicts with public policy",
                "The tribunal reached the wrong decision on the facts",
                "The award covers matters outside the submission"], 2,
               "And which of these is not a ground for setting aside an award?",
               "The wrong decision on the facts.",
               why=("Courts do not re-hear the merits; the grounds are procedural",
                    "Courts do not re-hear the merits. The grounds are about procedure, "
                    "jurisdiction and public policy."),
               think=5.0, syl="A3(e)"),

    recap_scene("s11", [
        ("Court versus arbitration.", "Court vs arbitration"),
        ("The ADR spectrum.", "Negotiation → mediation → conciliation → arbitration"),
        ("The ICC Court supervises, it doesn't decide.", "ICC Court: supervises",
         "The I.C.C. Court supervises, it doesn't decide."),
        ("Model Law: written agreement, three arbitrators by default.",
         "Written agreement · 3 arbitrators"),
        ("Awards are binding, and only set aside on narrow grounds.",
         "Award: binding · narrow set-aside"),
    ], [
        Line("lex11", "LEX", "Next time, we go back to the start: how SafariTech and Hans "
             "formed their contract in the first place, under the UN Sales Convention.",
             gap=0.3),
        Line("cargo11", "CARGO", "A contract across the ocean? That's my kind of story!",
             gap=0.6),
    ], next_ep=5, next_title="The Contract Across the Ocean", next_icon="ship"),
]
