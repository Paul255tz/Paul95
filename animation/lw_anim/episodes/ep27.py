"""Episode 27 - Insiders and Market Abuse.

Syllabus H1(a)-(b): the nature and legal control of insider dealing (UK
Criminal Justice Act 1993, Part V) and of market abuse (UK Market Abuse
Regulation, the FCA's civil regime, and the criminal offences of misleading
statements and impressions). Tanzania's Capital Markets and Securities Act and
Kenya's Capital Markets Act also prohibit insider dealing. Setting: Kito hears
that Kilima Power plc, a listed customer, is about to win a huge contract.
"""
from ._kit import (DISPLAY_NAMES, SERIES, VOICES, Line, Pause, Scene, Sfx,  # noqa: F401
                   quiz_scene, recap_scene, title_scene)

EPISODE = "Episode 27"
EPISODE_TITLE = "Insiders and Market Abuse"
SLUG = "episode27_insiders_and_market_abuse"

SCENES = [
    title_scene(27, EPISODE_TITLE, "Syllabus H1(a)–(b)", ("eye", "chart")),

    Scene("s1", "A hot tip", "", [
        Pause("open", 1.0),
        Line("kito1", "KITO", "Kilima Power's finance director just told me, in confidence: "
             "next week they announce a giant government contract!", gap=0.4),
        Line("hans1", "HANS", "Kilima is listed on the stock exchange. I'll buy their shares "
             "today, before the price jumps!", gap=0.4),
        Sfx("whoosh"),
        Line("aud1", "AUDITOR", "Stop right there. That could be insider dealing, a criminal "
             "offence, for both of you.", gap=0.3),
        Line("lex1", "LEX", "Section H of the syllabus: corporate fraudulent and criminal "
             "behaviour. Let's start with insiders."),
        Pause("hold", 1.2),
    ], spec={"tpl": "talk", "bg": "office", "syl": "H1(a)",
             "cast": [{"who": "KITO", "x": 900, "y": 1030, "s": 0.92, "mood": "excited"},
                      {"who": "HANS", "x": 1300, "y": 1030, "s": 0.9, "mood": "excited",
                       "talk_pose": "cheer"},
                      {"who": "AUDITOR", "x": 1680, "y": 1030, "s": 0.9, "enter": "aud1",
                       "pose": "clipboard", "talk_pose": "demand"},
                      {"who": "LEX", "x": 420, "y": 1030, "s": 0.88, "enter": "lex1",
                       "from": "left"}],
             "pops": [{"kind": "icon", "icon": "chart", "x": 1100, "y": 280, "s": 1.1,
                       "at": ["hans1", 0.5], "until": "aud1", "label": "Kilima Power plc"},
                      {"kind": "stamp", "at": "aud1", "x": 1100, "y": 280,
                       "text": "INSIDER DEALING?", "color": "#e4572e", "size": 52}]}),

    Scene("s2", "Three offences", "", [
        Pause("open", 1.0),
        Line("lex2a", "LEX", "In the UK model, the Criminal Justice Act of 1993 creates "
             "three insider dealing offences.", gap=0.3),
        Sfx("pop"),
        Line("lex2b", "LEX", "Dealing: an insider buys or sells price-affected securities, "
             "on a regulated market or through a professional intermediary.", gap=0.25),
        Sfx("pop"),
        Line("lex2c", "LEX", "Encouraging: an insider encourages someone else to deal, "
             "whether or not they actually do.", gap=0.25),
        Sfx("pop"),
        Line("lex2d", "LEX", "Disclosing: an insider passes on the information, other than "
             "in the proper performance of their job.", gap=0.4),
        Line("aud2", "AUDITOR", "So Kito telling Hans could be disclosing, and Hans buying "
             "could be dealing."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "heading": "Insider dealing offences",
             "syl": "H1(a)", "row": 150, "ts": 42,
             "items": [{"at": "lex2b", "text": "Dealing", "sub": "Buying or selling "
                                                                 "price-affected securities",
                        "icon": "chart", "color": "#e4572e"},
                       {"at": "lex2c", "text": "Encouraging", "sub": "Even if no one deals",
                        "icon": "megaphone", "color": "#f2a541"},
                       {"at": "lex2d", "text": "Disclosing", "sub": "Outside the proper "
                                                                    "course of a job",
                        "icon": "envelope", "color": "#7768ae"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "AUDITOR", "x": 1810, "s": 0.55, "y": 1120, "enter": "aud2",
                       "pose": "clipboard"}]}),

    Scene("s3", "What is inside information?", "", [
        Pause("open", 1.0),
        Line("lex3a", "LEX", "Inside information has four features.", gap=0.3),
        Sfx("pop"),
        Line("lex3b", "LEX", "It relates to particular securities, or particular issuers.",
             gap=0.2),
        Sfx("pop"),
        Line("lex3c", "LEX", "It is specific or precise, not just a vague rumour.", gap=0.2),
        Sfx("pop"),
        Line("lex3d", "LEX", "It has not been made public.", gap=0.2),
        Sfx("pop"),
        Line("lex3e", "LEX", "And if it were made public, it would be likely to have a "
             "significant effect on the price.", gap=0.4),
        Line("nia3", "NIA", "A confirmed government contract, not yet announced, that will "
             "move the share price. That ticks all four boxes."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "white", "layout": "grid", "cols": 2,
             "heading": "Inside information", "syl": "H1(a)", "cell_h": 290, "ts": 40,
             "items": [{"at": "lex3b", "text": "About particular securities or issuers",
                        "icon": "tag", "color": "#0f8b8d"},
                       {"at": "lex3c", "text": "Specific or precise", "icon": "magnifier",
                        "color": "#7768ae"},
                       {"at": "lex3d", "text": "Not made public", "icon": "lock",
                        "color": "#f2a541"},
                       {"at": "lex3e", "text": "Likely to significantly move the price",
                        "icon": "chart", "color": "#e4572e"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia3"}]}),

    Scene("s4", "Who is an insider?", "", [
        Pause("open", 1.0),
        Line("lex4a", "LEX", "An insider has inside information, and knows it is inside "
             "information from an inside source.", gap=0.3),
        Line("lex4b", "LEX", "Primary insiders get it by being a director, employee or "
             "shareholder of an issuer, or through their job, office or profession, like an "
             "auditor or lawyer.", gap=0.3),
        Line("lex4c", "LEX", "Secondary insiders, sometimes called tippees, get it directly "
             "or indirectly from a primary insider.", gap=0.4),
        Line("aud4", "AUDITOR", "So the finance director is a primary insider, and Kito and "
             "Hans became secondary insiders the moment they heard."),
        Pause("hold", 1.4),
    ], spec={"tpl": "flow", "bg": "studio_red", "heading": "The chain of insiders",
             "syl": "H1(a)",
             "nodes": [{"id": "fd", "x": 700, "y": 330, "label": "Kilima's finance director",
                        "tag": "primary", "icon": "person", "color": "#e4572e",
                        "at": "lex4b", "w": 320},
                       {"id": "k", "x": 1150, "y": 650, "label": "Kito", "tag": "secondary",
                        "icon": "person", "color": "#f2a541", "at": "lex4c", "w": 240},
                       {"id": "h", "x": 1620, "y": 330, "label": "Hans", "tag": "secondary",
                        "icon": "person", "color": "#f2a541", "at": ["lex4c", 2.0],
                        "w": 240}],
             "edges": [{"from": "fd", "to": "k", "at": ["lex4c", 0.3], "label": "tip",
                        "token": "envelope", "tcolor": "#e4572e"},
                       {"from": "k", "to": "h", "at": ["lex4c", 2.0], "label": "tip",
                        "token": "envelope", "tcolor": "#e4572e"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "AUDITOR", "x": 1810, "s": 0.55, "y": 1120, "enter": "aud4",
                       "pose": "clipboard"}]}),

    Scene("s5", "Defences and penalties", "", [
        Pause("open", 1.0),
        Line("lex5a", "LEX", "There are defences. The accused did not expect to profit "
             "because the information was price-sensitive.", gap=0.25),
        Line("lex5b", "LEX", "Or believed, on reasonable grounds, that it had been widely "
             "disclosed.", gap=0.25),
        Line("lex5c", "LEX", "Or would have done the same thing anyway, without the "
             "information. There are also special defences for market makers and price "
             "stabilisation.", gap=0.4),
        Line("lex5d", "LEX", "Insider dealing is a crime, punishable by imprisonment, an "
             "unlimited fine, or both. Oddly, the contract itself is not made void.",
             gap=0.4),
        Line("lex5e", "LEX", "And it's not just a UK idea. Tanzania's Capital Markets and "
             "Securities Act, and Kenya's Capital Markets Act, also ban insider dealing, "
             "policed by their capital markets regulators.", gap=0.3),
        Line("hans5", "HANS", "Then I'll wait for the public announcement. Keine Aktien "
             "heute. No shares today.", say="Then I'll wait for the public announcement. "
             "Kine Ak-tee-en hoy-ter. No shares today."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "heading": "Defences and penalties",
             "syl": "H1(a)", "row": 120, "ts": 38,
             "items": [{"at": "lex5a", "text": "No expected profit from the information",
                        "icon": "shield", "color": "#3bb273"},
                       {"at": "lex5b", "text": "Reasonably believed widely disclosed",
                        "icon": "megaphone", "color": "#2b86c5"},
                       {"at": "lex5c", "text": "Would have dealt anyway",
                        "sub": "+ market maker and stabilisation defences",
                        "icon": "check", "color": "#7768ae"},
                       {"at": "lex5d", "text": "Crime: prison and/or unlimited fine",
                        "sub": "The contract itself is not void", "icon": "handcuffs",
                        "color": "#e4572e"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "HANS", "x": 1810, "s": 0.55, "y": 1120, "enter": "hans5",
                       "mood": "worried"}],
             "pops": [{"kind": "card", "at": "lex5e", "until": "hans5", "x": 1190, "y": 470,
                       "w": 980, "h": 280, "title": "Local lens: East Africa",
                       "body": "Tanzania: Capital Markets and Securities Act · Kenya: Capital "
                               "Markets Act · both ban insider dealing",
                       "color": "#f2a541", "dim": True, "bs": 36}]}),

    Scene("s6", "Market abuse", "", [
        Pause("open", 1.0),
        Line("lex6a", "LEX", "Market abuse is wider, and in the UK it is mainly a civil "
             "regime, under the Market Abuse Regulation, enforced by the Financial Conduct "
             "Authority.", gap=0.3),
        Line("lex6b", "LEX", "It covers three behaviours: insider dealing, unlawful "
             "disclosure of inside information, and market manipulation.", gap=0.3),
        Line("lex6c", "LEX", "Because it's civil, the regulator need only prove it on the "
             "balance of probabilities, and intent isn't always needed. Sanctions include "
             "unlimited fines, public censure, injunctions and restitution.", gap=0.4),
        Line("lex6d", "LEX", "Separately, it is a crime to make misleading statements, or "
             "create a misleading impression, to induce people to invest, or to manipulate "
             "benchmarks.", gap=0.4),
        Line("nia6", "NIA", "So the regulator has two weapons: civil penalties, and criminal "
             "prosecution."),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio", "heading": "Market abuse: civil and criminal",
             "syl": "H1(b)", "ts": 32,
             "cols": [{"title": "Civil regime (UK MAR)", "icon": "scales", "color": "#0f8b8d",
                       "at": "lex6a",
                       "items": [{"at": "lex6b", "text": "Insider dealing"},
                                 {"at": ["lex6b", 2.5], "text": "Unlawful disclosure"},
                                 {"at": ["lex6b", 5.0], "text": "Market manipulation"},
                                 {"at": "lex6c", "text": "Balance of probabilities"},
                                 {"at": ["lex6c", 6.0], "text": "Fines · censure · injunctions "
                                                               "· restitution"}]},
                      {"title": "Criminal offences", "icon": "handcuffs", "color": "#e4572e",
                       "at": "lex6d",
                       "items": [{"at": ["lex6d", 1.0], "text": "Misleading statements"},
                                 {"at": ["lex6d", 3.0], "text": "Misleading impressions"},
                                 {"at": ["lex6d", 6.0], "text": "Benchmark manipulation"},
                                 {"at": ["lex6d", 6.5], "text": "Beyond reasonable doubt"}]}],
             "vs": True,
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia6"}]}),

    Scene("s7", "What manipulation looks like", "", [
        Pause("open", 1.0),
        Line("aud7a", "AUDITOR", "Market manipulation means distorting the market. Watch "
             "for these patterns.", gap=0.3),
        Sfx("pop"),
        Line("aud7b", "AUDITOR", "Trades that give false or misleading signals about supply, "
             "demand or price.", gap=0.2),
        Sfx("pop"),
        Line("aud7c", "AUDITOR", "Wash trades, where someone trades with themselves to fake "
             "activity.", gap=0.2),
        Sfx("pop"),
        Line("aud7d", "AUDITOR", "Pump and dump: spreading hype to push a price up, then "
             "selling.", gap=0.2),
        Sfx("pop"),
        Line("aud7e", "AUDITOR", "Spreading false or misleading information or rumours, "
             "including online.", gap=0.2),
        Sfx("pop"),
        Line("aud7f", "AUDITOR", "And securing an artificial price, for example by cornering "
             "the supply.", gap=0.4),
        Line("kito7", "KITO", "So even a social media post hyping Kilima shares could be "
             "market abuse!"),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "white", "layout": "grid", "cols": 3,
             "heading": "Market manipulation", "syl": "H1(b)", "cell_h": 290, "ts": 34,
             "items": [{"at": "aud7b", "text": "False or misleading signals",
                        "icon": "warning", "color": "#e4572e"},
                       {"at": "aud7c", "text": "Wash trades", "icon": "washer",
                        "color": "#2b86c5"},
                       {"at": "aud7d", "text": "Pump and dump", "icon": "chart",
                        "color": "#f2a541"},
                       {"at": "aud7e", "text": "False rumours", "icon": "megaphone",
                        "color": "#7768ae"},
                       {"at": "aud7f", "text": "Artificial price", "icon": "tag",
                        "color": "#0f8b8d"},
                       {"at": "kito7", "text": "Online hype counts too", "icon": "laptop",
                        "color": "#d64f8a"}],
             "cast": [{"who": "AUDITOR", "x": 250, "pose": "clipboard",
                       "talk_pose": "present"},
                      {"who": "KITO", "x": 1810, "s": 0.55, "y": 1120, "enter": "kito7"}]}),

    quiz_scene("s8", "Quick check",
               "Hans hears the unannounced contract news from Kito, who heard it from "
               "Kilima's finance director. What is Hans?",
               ["Not an insider, as he doesn't work for Kilima", "A secondary insider",
                "A market maker", "A primary insider"], 1,
               "Quick check. Hans heard the news from Kito, who heard it from Kilima's "
               "finance director. What is Hans?",
               "A secondary insider.",
               why="Information from an inside source, directly or indirectly",
               syl="H1(a)"),

    quiz_scene("s9", "Quick check",
               "Which is NOT one of the three insider dealing offences?",
               ["Dealing", "Encouraging another to deal", "Disclosing inside information",
                "Failing to buy shares"], 3,
               "And which is not one of the three insider dealing offences?",
               "Failing to buy shares.",
               think=4.0, syl="H1(a)"),

    recap_scene("s10", [
        ("Dealing, encouraging, disclosing.", "Deal · encourage · disclose"),
        ("Inside information: specific, unpublished, price-sensitive.",
         "Specific · not public · price-sensitive"),
        ("Primary and secondary insiders.", "Primary · secondary insiders"),
        ("Market abuse: civil regime plus crimes.", "Market abuse: civil + criminal"),
        ("Manipulation: false signals and rumours.", "Manipulation"),
    ], [
        Line("lex10", "LEX", "Next time: dirty money. How money laundering works, and the "
             "controls every accountant must apply.", gap=0.3),
        Line("aud10", "AUDITOR", "Bring your customer due diligence checklist.", gap=0.6),
    ], next_ep=28, next_title="Dirty Money", next_icon="washer"),
]
