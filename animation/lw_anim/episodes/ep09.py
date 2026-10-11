"""Episode 9 - When Deals Break.

Syllabus B2(c)(i)-(iv): provisions common to seller and buyer under the CISG:
fundamental and anticipatory breach and instalment contracts (Arts 25, 71-73),
damages (Arts 74-77), interest (Art 78) and exemptions (Arts 79-80).
Setting: SafariTech's second order, ten monthly deliveries of spare parts from
Hans, runs into trouble; a flood closes Hans's supplier.
"""
from ._kit import (DISPLAY_NAMES, SERIES, VOICES, Line, Pause, Scene, Sfx,  # noqa: F401
                   quiz_scene, recap_scene, title_scene)

EPISODE = "Episode 9"
EPISODE_TITLE = "When Deals Break"
SLUG = "episode09_when_deals_break"

SCENES = [
    title_scene(9, EPISODE_TITLE, "Syllabus B2(c)", ("warning", "scales")),

    Scene("s1", "Bad news from Hamburg", "", [
        Pause("open", 1.0),
        Line("nia1", "NIA", "Our new contract with Hans: spare parts in ten monthly "
             "instalments.", gap=0.3),
        Sfx("whoosh"),
        Line("hans1", "HANS", "Kito, a flood has closed my steel supplier. And frankly, I hear "
             "SafariTech is short of cash.", gap=0.4),
        Line("kito1", "KITO", "Short of cash? Who told you that?", gap=0.4),
        Line("lex1", "LEX", "This is where the provisions common to both seller and buyer "
             "come in. Let's start with what makes a breach serious."),
        Pause("hold", 1.2),
    ], spec={"tpl": "talk", "bg": "office", "syl": "B2(c)",
             "cast": [{"who": "NIA", "x": 650, "y": 1030, "s": 0.9},
                      {"who": "KITO", "x": 1050, "y": 1030, "s": 0.92,
                       "moods": [["hans1", "surprised"], ["kito1", "angry"]],
                       "talk_pose": "shrug"},
                      {"who": "HANS", "x": 1550, "y": 1030, "s": 0.9, "enter": ["hans1", -0.6],
                       "mood": "worried"},
                      {"who": "LEX", "x": 260, "y": 1030, "s": 0.88, "enter": "lex1",
                       "from": "left"}],
             "pops": [{"kind": "icon", "icon": "calendar", "x": 1250, "y": 280, "s": 1.0,
                       "at": ["nia1", 0.5], "until": "hans1", "label": "10 instalments"},
                      {"kind": "icon", "icon": "warning", "x": 1250, "y": 280, "s": 1.1,
                       "at": ["hans1", 0.4], "until": "lex1", "label": "Flood!",
                       "color": "#e4572e"}]}),

    Scene("s2", "Fundamental breach", "", [
        Pause("open", 1.0),
        Line("lex2a", "LEX", "A breach is fundamental if it causes such detriment that it "
             "substantially deprives the other party of what it was entitled to expect.",
             gap=0.3),
        Line("lex2b", "LEX", "Unless the party in breach did not foresee that result, and a "
             "reasonable person in the same position would not have foreseen it either.",
             gap=0.4),
        Line("lex2c", "LEX", "Why does it matter? Because only a fundamental breach lets the "
             "innocent party avoid the contract straight away. Otherwise, it claims damages, "
             "or first fixes an extra period.", gap=0.4),
        Line("nia2", "NIA", "So a small delay, or a minor defect, won't end the contract on "
             "its own."),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio", "heading": "Article 25: fundamental breach",
             "syl": "B2(c)(i)", "ts": 34,
             "cols": [{"title": "Fundamental", "icon": "fire", "color": "#e4572e",
                       "at": "lex2a",
                       "items": [{"at": ["lex2a", 1.0], "text": "Substantial deprivation of "
                                                               "what was expected"},
                                 {"at": "lex2b", "text": "Result was foreseeable"},
                                 {"at": "lex2c", "text": "Innocent party may avoid at once",
                                  "good": True}]},
                      {"title": "Not fundamental", "icon": "clock", "color": "#2b86c5",
                       "at": ["lex2c", 3.0],
                       "items": [{"at": ["lex2c", 3.5], "text": "Damages, price reduction, "
                                                               "repair"},
                                 {"at": ["lex2c", 5.0], "text": "Fix an extra period first"},
                                 {"at": "nia2", "text": "Small delay or minor defect",
                                  "bad": True}]}],
             "vs": True,
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia2"}]}),

    Scene("s3", "Anticipatory breach", "", [
        Pause("open", 1.0),
        Line("lex3a", "LEX", "Sometimes trouble is visible before performance is even due. "
             "That's anticipatory breach.", gap=0.3),
        Sfx("pop"),
        Line("lex3b", "LEX", "If it becomes apparent that the other side will not perform a "
             "substantial part of its obligations, because of a serious deficiency in its "
             "ability, or its creditworthiness, or its conduct, a party may suspend its own "
             "performance.", gap=0.25),
        Sfx("pop"),
        Line("lex3c", "LEX", "It must give notice of the suspension at once, and must carry "
             "on if the other side gives adequate assurance.", gap=0.25),
        Sfx("pop"),
        Line("lex3d", "LEX", "A seller who has already shipped can stop the goods reaching "
             "the buyer, even if the buyer holds the documents.", gap=0.25),
        Sfx("pop"),
        Line("lex3e", "LEX", "And if it is clear that a fundamental breach will happen, the "
             "party may avoid the contract in advance, giving reasonable notice so the other "
             "side can offer assurance.", gap=0.4),
        Line("hans3", "HANS", "So I may pause shipments, but I must tell Kito, and restart "
             "if his bank guarantees payment.", gap=0.3),
        Line("amara3", "AMARA", "Our bank can issue that guarantee today."),
        Pause("hold", 1.4),
    ], spec={"tpl": "timeline", "bg": "studio_teal", "heading": "Anticipatory breach "
                                                                "(Arts 71–72)",
             "syl": "B2(c)(i)", "cw": 300,
             "events": [{"at": "lex3b", "label": "Warning signs", "sub": "Ability, credit or "
                                                                        "conduct",
                         "icon": "warning", "color": "#f2a541"},
                        {"at": "lex3c", "label": "Suspend + notify", "sub": "Resume if "
                                                                           "adequate "
                                                                           "assurance",
                         "icon": "envelope", "color": "#0f8b8d"},
                        {"at": "lex3d", "label": "Stop in transit", "sub": "Even if buyer "
                                                                          "holds documents",
                         "icon": "ship", "color": "#2b86c5"},
                        {"at": "lex3e", "label": "Avoid in advance", "sub": "Clear "
                                                                            "fundamental "
                                                                            "breach ahead",
                         "icon": "scissors", "color": "#e4572e"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "HANS", "x": 1650, "s": 0.55, "y": 1120, "enter": "hans3"},
                      {"who": "AMARA", "x": 1820, "s": 0.55, "y": 1120, "enter": "amara3"}]}),

    Scene("s4", "Instalment contracts", "", [
        Pause("open", 1.0),
        Line("lex4a", "LEX", "With ten monthly deliveries, each instalment is judged "
             "separately.", gap=0.3),
        Sfx("pop"),
        Line("lex4b", "LEX", "If one instalment is a fundamental breach, the buyer may avoid "
             "the contract for that instalment.", gap=0.25),
        Sfx("pop"),
        Line("lex4c", "LEX", "If it gives good grounds to expect fundamental breaches in "
             "future instalments, the buyer may avoid for the future too, within a "
             "reasonable time.", gap=0.25),
        Sfx("pop"),
        Line("lex4d", "LEX", "And if the deliveries depend on each other, so earlier ones "
             "are useless alone, the buyer may avoid for past ones as well.", gap=0.4),
        Line("nia4", "NIA", "So if the first delivery is badly defective, the whole deal may "
             "go. But if seven are fine and the eighth is faulty, we probably just reject "
             "the eighth, and claim damages."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "white", "heading": "Instalment contracts (Art 73)",
             "syl": "B2(c)(i)", "row": 140, "ts": 40,
             "items": [{"at": "lex4b", "text": "Avoid for that instalment",
                        "sub": "If that instalment is a fundamental breach",
                        "icon": "box", "color": "#f2a541"},
                       {"at": "lex4c", "text": "Avoid for future instalments",
                        "sub": "Good grounds to expect future fundamental breach",
                        "icon": "calendar", "color": "#e4572e"},
                       {"at": "lex4d", "text": "Avoid for past instalments too",
                        "sub": "If deliveries are interdependent", "icon": "chain",
                        "color": "#7768ae"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia4"}]}),

    Scene("s5", "Damages", "", [
        Pause("open", 1.0),
        Line("lex5a", "LEX", "Damages equal the loss, including lost profit, caused by the "
             "breach.", gap=0.3),
        Sfx("pop"),
        Line("lex5b", "LEX", "But only loss the party in breach foresaw, or ought to have "
             "foreseen, as a possible consequence when the contract was made.", gap=0.25),
        Sfx("pop"),
        Line("lex5c", "LEX", "If the contract is avoided and the innocent party makes a "
             "substitute deal, it can claim the difference between the contract price and "
             "the substitute price.", gap=0.25),
        Sfx("pop"),
        Line("lex5d", "LEX", "With no substitute deal, it can claim the difference from the "
             "current market price.", gap=0.25),
        Sfx("pop"),
        Line("lex5e", "LEX", "And it must mitigate. Damages are reduced by any loss it could "
             "reasonably have avoided.", gap=0.4),
        Line("kito5", "KITO", "So if Hans stops supplying, I buy parts elsewhere, at a "
             "sensible price, and claim the extra cost."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "heading": "Damages (Arts 74–77)",
             "syl": "B2(c)(ii)", "row": 120, "ts": 40,
             "items": [{"at": "lex5a", "text": "Loss caused, including lost profit",
                        "icon": "moneybag", "color": "#3bb273"},
                       {"at": "lex5b", "text": "Limited to foreseeable loss",
                        "icon": "eye", "color": "#2b86c5"},
                       {"at": "lex5c", "text": "Substitute deal: price difference",
                        "icon": "handshake", "color": "#7768ae"},
                       {"at": "lex5d", "text": "No substitute: market price difference",
                        "icon": "chart", "color": "#f2a541"},
                       {"at": "lex5e", "text": "Duty to mitigate", "icon": "shield",
                        "color": "#e4572e"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "KITO", "x": 1810, "s": 0.55, "y": 1120, "enter": "kito5"}]}),

    Scene("s6", "Interest", "", [
        Pause("open", 1.0),
        Line("lex6a", "LEX", "If a party fails to pay the price, or any other sum in "
             "arrears, the other party is entitled to interest on it.", gap=0.3),
        Line("lex6b", "LEX", "That is on top of any damages. The Convention does not fix the "
             "rate, so it comes from the contract or the applicable law.", gap=0.4),
        Line("amara6", "AMARA", "That's why our trade contracts always state an interest "
             "rate for late payment."),
        Pause("hold", 1.2),
    ], spec={"tpl": "talk", "bg": "bank", "syl": "B2(c)(iii)",
             "cast": [{"who": "LEX", "x": 420, "y": 1040, "s": 0.88},
                      {"who": "AMARA", "x": 1500, "y": 1040, "s": 0.9}],
             "pops": [{"kind": "card", "at": "lex6a", "x": 960, "y": 300, "w": 900, "h": 240,
                       "title": "Article 78: interest", "body": "On the price or any sum in "
                                                                "arrears, without prejudice "
                                                                "to damages",
                       "color": "#0f8b8d", "bs": 38},
                      {"kind": "chip", "at": "lex6b", "x": 960, "y": 520,
                       "text": "Rate: from the contract or the applicable law",
                       "color": "#f2a541", "size": 34},
                      {"kind": "icon", "icon": "percent", "x": 960, "y": 700, "s": 1.3,
                       "at": ["lex6a", 1.0], "color": "#7768ae", "float": True}]}),

    Scene("s7", "Exemptions: beyond control", "", [
        Pause("open", 1.0),
        Line("lex7a", "LEX", "Now Hans's flood. A party is not liable for a failure if it "
             "proves four things.", gap=0.3),
        Sfx("pop"),
        Line("lex7b", "LEX", "The failure was due to an impediment beyond its control.",
             gap=0.25),
        Sfx("pop"),
        Line("lex7c", "LEX", "It could not reasonably have taken it into account when "
             "contracting.", gap=0.25),
        Sfx("pop"),
        Line("lex7d", "LEX", "It could not reasonably have avoided or overcome it, or its "
             "consequences.", gap=0.25),
        Sfx("pop"),
        Line("lex7e", "LEX", "And it gave notice of the impediment within a reasonable "
             "time.", gap=0.5),
        Line("lex7f", "LEX", "If a third party, like Hans's supplier, caused the failure, "
             "Hans is exempt only if both he and the supplier would be exempt.", gap=0.3),
        Line("lex7g", "LEX", "The exemption lasts only while the impediment lasts. And it "
             "only blocks damages. The other remedies, like avoidance, remain available.",
             gap=0.4),
        Line("hans7", "HANS", "So I can't be sued for damages because of the flood, but Kito "
             "could still end the contract if the delay is fundamental."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "white", "heading": "Exemption (Art 79)",
             "syl": "B2(c)(iv)", "row": 112, "ts": 40,
             "items": [{"at": "lex7b", "text": "Impediment beyond its control",
                        "icon": "fire", "color": "#e4572e"},
                       {"at": "lex7c", "text": "Not reasonably foreseeable at contract",
                        "icon": "eye", "color": "#7768ae"},
                       {"at": "lex7d", "text": "Could not avoid or overcome it",
                        "icon": "shield", "color": "#2b86c5"},
                       {"at": "lex7e", "text": "Notice within a reasonable time",
                        "icon": "envelope", "color": "#f2a541"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "HANS", "x": 1810, "s": 0.55, "y": 1120, "enter": "hans7"}],
             "pops": [{"kind": "card", "at": "lex7f", "until": "lex7g", "x": 1190, "y": 470,
                       "w": 900, "h": 280, "title": "Third party caused it?",
                       "body": "Exempt only if BOTH the party and the third party would be "
                               "exempt", "color": "#1f3a5f", "dim": True, "bs": 38},
                      {"kind": "card", "at": "lex7g", "until": "hans7", "x": 1190, "y": 470,
                       "w": 900, "h": 280, "title": "Limits",
                       "body": "Only while the impediment lasts · blocks damages only · "
                               "other remedies survive", "color": "#e4572e", "dim": True,
                       "bs": 38}]}),

    quiz_scene("s8", "Quick check",
               "A buyer's damages claim is limited to loss that the seller…",
               ["actually caused, whatever its size", "foresaw or ought to have foreseen when "
                "contracting", "agreed to pay after the breach", "could insure against"], 1,
               "Quick check. A buyer's damages are limited to loss that the seller did what?",
               "Foresaw, or ought to have foreseen, when the contract was made.",
               syl="B2(c)(ii)"),

    quiz_scene("s9", "Quick check",
               "Hans proves the flood was an impediment beyond his control. What does that "
               "exemption stop?",
               ["All of the buyer's remedies", "Only a claim for damages",
                "Only avoidance of the contract", "Nothing; floods are foreseeable"], 1,
               "And if Hans proves the flood is a valid impediment, what does the exemption "
               "stop?",
               "Only a claim for damages.",
               why="The buyer may still avoid the contract, or claim interest",
               think=4.0, syl="B2(c)(iv)"),

    recap_scene("s10", [
        ("Fundamental breach allows avoidance.", "Fundamental breach → avoid"),
        ("Anticipatory breach: suspend, notify, assurance.", "Suspend · notify · assurance"),
        ("Instalments are judged one by one.", "Instalments: one by one"),
        ("Damages: foreseeable, and mitigate.", "Damages: foreseeable · mitigate"),
        ("Exemption blocks damages only.", "Art 79: damages only"),
    ], [
        Line("lex10", "LEX", "Next time: what happens after avoidance, who must look after "
             "the goods, and exactly when risk passes to the buyer.", gap=0.3),
        Line("cargo10", "CARGO", "Finally, an episode about me!", gap=0.6),
    ], next_ep=10, next_title="Risk on the Water", next_icon="ship"),
]
