"""Episode 25 - Winding Up.

Syllabus G1(a)-(c): members' and creditors' voluntary liquidation; grounds for
and procedure in compulsory liquidation; and the order in which debts are paid
on liquidation (UK Insolvency Act 1986 model, current priority rules including
HMRC's secondary preferential status and the prescribed part). Setting:
Kilimanjaro Retail Ltd owes SafariTech $40,000 and stops paying.
"""
from ._kit import (DISPLAY_NAMES, SERIES, VOICES, Line, Pause, Scene, Sfx,  # noqa: F401
                   quiz_scene, recap_scene, title_scene)

EPISODE = "Episode 25"
EPISODE_TITLE = "Winding Up"
SLUG = "episode25_winding_up"

SCENES = [
    title_scene(25, EPISODE_TITLE, "Syllabus G1(a)–(c)", ("fire", "gavel")),

    Scene("s1", "A customer stops paying", "", [
        Pause("open", 1.0),
        Line("kito1", "KITO", "Kilimanjaro Retail owes us forty thousand dollars, and they've "
             "stopped answering my calls!", gap=0.4),
        Line("nia1", "NIA", "I hear they're insolvent. Can we force them into liquidation?",
             gap=0.4),
        Line("lex1", "LEX", "Possibly. Liquidation, or winding up, ends a company's life. "
             "A liquidator collects and sells its assets, pays its debts in a set order, "
             "and the company is then dissolved. There are three routes."),
        Pause("hold", 1.2),
    ], spec={"tpl": "talk", "bg": "office", "syl": "G1",
             "cast": [{"who": "KITO", "x": 1450, "y": 1030, "s": 0.95, "mood": "angry",
                       "talk_pose": "demand"},
                      {"who": "NIA", "x": 960, "y": 1030, "s": 0.9, "mood": "worried"},
                      {"who": "LEX", "x": 420, "y": 1030, "s": 0.88, "enter": "lex1",
                       "from": "left"}],
             "pops": [{"kind": "icon", "icon": "receipt", "x": 1200, "y": 280, "s": 1.1,
                       "at": ["kito1", 0.6], "until": "lex1", "label": "$40,000 unpaid",
                       "color": "#e4572e"}]}),

    Scene("s2", "Three routes to liquidation", "", [
        Pause("open", 1.0),
        Line("lex2a", "LEX", "A members' voluntary liquidation is for a solvent company. "
             "The members decide to close it down, and every creditor will be paid in full.",
             gap=0.4),
        Line("lex2b", "LEX", "A creditors' voluntary liquidation is for an insolvent "
             "company. The members start it, but the creditors take control.", gap=0.4),
        Line("lex2c", "LEX", "And a compulsory liquidation is ordered by the court, usually "
             "on a creditor's petition.", gap=0.4),
        Line("nia2", "NIA", "So the key question for a voluntary liquidation is: is the "
             "company solvent?"),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio", "heading": "Types of liquidation",
             "syl": "G1(a)–(b)", "ts": 31,
             "cols": [{"title": "Members' voluntary", "icon": "check", "color": "#3bb273",
                       "at": "lex2a",
                       "items": [{"at": ["lex2a", 0.5], "text": "Solvent company"},
                                 {"at": ["lex2a", 3.0], "text": "Members decide"},
                                 {"at": ["lex2a", 5.5], "text": "Creditors paid in full"}]},
                      {"title": "Creditors' voluntary", "icon": "warning",
                       "color": "#f2a541", "at": "lex2b",
                       "items": [{"at": ["lex2b", 0.5], "text": "Insolvent company"},
                                 {"at": ["lex2b", 3.0], "text": "Members start it"},
                                 {"at": ["lex2b", 5.0], "text": "Creditors take control"}]},
                      {"title": "Compulsory", "icon": "court", "color": "#e4572e",
                       "at": "lex2c",
                       "items": [{"at": ["lex2c", 0.5], "text": "Court order"},
                                 {"at": ["lex2c", 3.0], "text": "Usually a creditor's "
                                                               "petition"}]}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia2"}]}),

    Scene("s3", "Voluntary liquidation step by step", "", [
        Pause("open", 1.0),
        Line("lex3a", "LEX", "In a members' voluntary liquidation, the directors first make "
             "a declaration of solvency.", gap=0.25),
        Line("lex3b", "LEX", "After full inquiry, they declare the company will pay its "
             "debts in full, with interest, within a stated period of no more than twelve "
             "months. It must be made within the five weeks before the resolution.",
             gap=0.25),
        Line("lex3c", "LEX", "Making it without reasonable grounds is a crime.", gap=0.3),
        Line("lex3d", "LEX", "The members then pass a special resolution to wind up, and "
             "appoint a liquidator. If the liquidator finds the company is insolvent after "
             "all, it becomes a creditors' liquidation.", gap=0.4),
        Line("lex3e", "LEX", "In a creditors' voluntary liquidation, there's no declaration. "
             "The members pass a special resolution, and within fourteen days the creditors "
             "decide, usually by a virtual meeting or deemed consent, who the liquidator "
             "will be. The directors provide a statement of affairs.", gap=0.4),
        Line("nia3", "NIA", "And if members and creditors nominate different liquidators, "
             "the creditors' choice wins."),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio_teal", "heading": "MVL vs CVL",
             "syl": "G1(a)", "ts": 31,
             "cols": [{"title": "MVL (solvent)", "icon": "check", "color": "#3bb273",
                       "at": "lex3a",
                       "items": [{"at": ["lex3a", 2.0], "text": "Directors' declaration of "
                                                               "solvency"},
                                 {"at": ["lex3b", 4.0], "text": "Debts paid within 12 "
                                                               "months"},
                                 {"at": ["lex3b", 9.0], "text": "Made within 5 weeks before "
                                                               "the resolution"},
                                 {"at": "lex3c", "text": "No reasonable grounds = crime",
                                  "bad": True},
                                 {"at": "lex3d", "text": "Special resolution · members "
                                                         "appoint liquidator"}]},
                      {"title": "CVL (insolvent)", "icon": "warning", "color": "#f2a541",
                       "at": "lex3e",
                       "items": [{"at": ["lex3e", 0.5], "text": "No declaration"},
                                 {"at": ["lex3e", 2.0], "text": "Special resolution"},
                                 {"at": ["lex3e", 5.5], "text": "Creditors decide within "
                                                               "14 days"},
                                 {"at": ["lex3e", 12.0], "text": "Statement of affairs"},
                                 {"at": "nia3", "text": "Creditors' liquidator prevails"}]}],
             "vs": True,
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia3"}]}),

    Scene("s4", "Grounds for compulsory liquidation", "", [
        Pause("open", 1.0),
        Line("lex4a", "LEX", "A court may order winding up on several grounds. The most "
             "important are these.", gap=0.3),
        Sfx("pop"),
        Line("lex4b", "LEX", "The company has resolved, by special resolution, to be wound "
             "up by the court.", gap=0.2),
        Sfx("pop"),
        Line("lex4c", "LEX", "A public company has had no trading certificate for over a "
             "year.", gap=0.2),
        Sfx("pop"),
        Line("lex4d", "LEX", "It hasn't started business within a year, or has suspended it "
             "for a whole year.", gap=0.2),
        Sfx("pop"),
        Line("lex4e", "LEX", "It is unable to pay its debts. For example, a creditor owed "
             "more than seven hundred and fifty pounds serves a statutory demand, which is "
             "unpaid after three weeks.", gap=0.2),
        Sfx("pop"),
        Line("lex4f", "LEX", "Or it is just and equitable. Deadlock, in Re Yenidje Tobacco. "
             "A member shut out of a quasi-partnership, in Ebrahimi against Westbourne "
             "Galleries. Or the company's main purpose has failed.", gap=0.4),
        Line("kito4", "KITO", "Kilimanjaro owes us forty thousand dollars, undisputed. We "
             "serve a statutory demand, and if it's unpaid in three weeks, we petition!"),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "heading": "Compulsory winding up: grounds",
             "syl": "G1(b)", "row": 112, "ts": 38,
             "items": [{"at": "lex4b", "text": "Special resolution for court winding up",
                        "icon": "ballot", "color": "#7768ae"},
                       {"at": "lex4c", "text": "plc: no trading certificate after 1 year",
                        "icon": "company", "color": "#2b86c5"},
                       {"at": "lex4d", "text": "No business started, or suspended, for a "
                                               "year", "icon": "clock", "color": "#f2a541"},
                       {"at": "lex4e", "text": "Unable to pay debts",
                        "sub": "e.g. statutory demand over £750 unpaid for 3 weeks",
                        "icon": "receipt", "color": "#e4572e"},
                       {"at": "lex4f", "text": "Just and equitable",
                        "sub": "Yenidje (deadlock) · Ebrahimi (quasi-partnership)",
                        "icon": "scales", "color": "#3bb273"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "KITO", "x": 1810, "s": 0.55, "y": 1120, "enter": "kito4"}]}),

    Scene("s5", "After the winding-up order", "", [
        Pause("open", 1.0),
        Line("lex5a", "LEX", "A petition can be presented by the company, its directors, "
             "creditors, contributories, or the government.", gap=0.3),
        Line("lex5b", "LEX", "Once the court orders winding up, the official receiver "
             "becomes liquidator, until an insolvency practitioner is appointed.", gap=0.3),
        Sfx("pop"),
        Line("lex5c", "LEX", "The liquidation is treated as starting when the petition was "
             "presented, so later dispositions of property are void unless the court "
             "approves them.", gap=0.25),
        Sfx("pop"),
        Line("lex5d", "LEX", "Legal actions against the company are halted.", gap=0.25),
        Sfx("pop"),
        Line("lex5e", "LEX", "The directors' powers end, and employees are dismissed.",
             gap=0.25),
        Sfx("pop"),
        Line("lex5f", "LEX", "And the liquidator can challenge earlier deals: transactions "
             "at an undervalue, preferences to favoured creditors, and late floating "
             "charges, and pursue directors for fraudulent or wrongful trading.", gap=0.4),
        Line("nia5", "NIA", "So the liquidator steps into the directors' shoes, and looks "
             "backwards too."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "white", "heading": "Effects of a winding-up order",
             "syl": "G1(b)", "row": 120, "ts": 38,
             "items": [{"at": "lex5b", "text": "Official receiver becomes liquidator",
                        "icon": "person", "color": "#1f3a5f"},
                       {"at": "lex5c", "text": "Starts from the petition",
                        "sub": "Later dispositions void unless court approves",
                        "icon": "calendar", "color": "#e4572e"},
                       {"at": "lex5d", "text": "Legal actions halted", "icon": "shield", "color": "#7768ae"},
                       {"at": "lex5e", "text": "Directors' powers end · staff dismissed",
                        "icon": "door", "color": "#f2a541"},
                       {"at": "lex5f", "text": "Challenge past transactions",
                        "sub": "Undervalue · preference · late floating charge",
                        "icon": "magnifier", "color": "#0f8b8d"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia5"}]}),

    Scene("s6", "Who gets paid first?", "", [
        Pause("open", 1.0),
        Line("lex6a", "LEX", "Now the order of payment. Learn it carefully.", gap=0.3),
        Sfx("pop"),
        Line("lex6b", "LEX", "One. Fixed charge holders, from the assets they hold charges "
             "over.", gap=0.2),
        Sfx("pop"),
        Line("lex6c", "LEX", "Two. The costs and expenses of the liquidation.", gap=0.2),
        Sfx("pop"),
        Line("lex6d", "LEX", "Three. Preferential creditors: employees' unpaid wages, up to "
             "four months and eight hundred pounds each, plus holiday pay and pension "
             "contributions.", gap=0.2),
        Sfx("pop"),
        Line("lex6e", "LEX", "Four. Secondary preferential creditors: the tax authority, for "
             "taxes like VAT and PAYE that the company collected for it.",
             say="Four. Secondary preferential creditors: the tax authority, for taxes like "
                 "V.A.T. and pay-as-you-earn that the company collected for it.", gap=0.2),
        Sfx("pop"),
        Line("lex6f", "LEX", "Five. The prescribed part: a slice of floating charge assets "
             "ring-fenced for unsecured creditors.", gap=0.2),
        Sfx("pop"),
        Line("lex6g", "LEX", "Six. Floating charge holders.", gap=0.2),
        Sfx("pop"),
        Line("lex6h", "LEX", "Seven. Unsecured creditors, including any excess wages.",
             gap=0.2),
        Sfx("pop"),
        Line("lex6i", "LEX", "Eight. Deferred debts, such as dividends declared but unpaid.",
             gap=0.2),
        Sfx("pop"),
        Line("lex6j", "LEX", "And nine. Members, preference shareholders first, if their "
             "terms say so.", gap=0.4),
        Line("lex6k", "LEX", "Watch the money pour down. Each class is paid in full before "
             "the next gets anything. If there's not enough, that class shares rateably.",
             gap=0.3),
        Sfx("sparkle"),
        Pause("pour", 10.5),
    ], spec={"tpl": "stack", "bg": "studio_teal", "heading": "Order of distribution",
             "syl": "G1(c)", "top": 160, "bottom": 1010, "ts": 30, "x0": 520,
             "tiers": [{"at": "lex6b", "label": "Fixed charge holders",
                        "color": "#1f3a5f"},
                       {"at": "lex6c", "label": "Liquidation expenses", "color": "#5b6670"},
                       {"at": "lex6d", "label": "Preferential: employees (4 months, £800), "
                                                "pensions", "color": "#0f8b8d"},
                       {"at": "lex6e", "label": "Secondary preferential: HMRC (VAT, PAYE)",
                        "color": "#2b86c5"},
                       {"at": "lex6f", "label": "Prescribed part (for unsecured)",
                        "color": "#3bb273"},
                       {"at": "lex6g", "label": "Floating charge holders",
                        "color": "#7768ae"},
                       {"at": "lex6h", "label": "Unsecured creditors", "color": "#f2a541"},
                       {"at": "lex6i", "label": "Deferred debts", "color": "#d64f8a"},
                       {"at": "lex6j", "label": "Members", "color": "#e4572e"}],
             "pour": {"at": "pour", "fills": [1, 1, 1, 1, 1, 0.6, 0, 0, 0], "dur": 1.1,
                      "label": "Assets realised"},
             "cast": [{"who": "LEX", "x": 250}]}),

    Scene("s7", "The prescribed part", "", [
        Pause("open", 1.0),
        Line("lex7a", "LEX", "The prescribed part protects unsecured creditors from "
             "floating charge holders taking everything.", gap=0.3),
        Line("lex7b", "LEX", "It is fifty percent of the first ten thousand pounds of "
             "floating charge assets, plus twenty percent of the rest, up to a maximum of "
             "eight hundred thousand pounds.", gap=0.4),
        Line("lex7c", "LEX", "So if floating charge assets are a hundred thousand pounds, "
             "the prescribed part is five thousand, plus eighteen thousand. Twenty-three "
             "thousand pounds for the unsecured creditors.", gap=0.4),
        Line("kito7", "KITO", "So as an unsecured creditor of Kilimanjaro, we'd share in "
             "that. Better than nothing!"),
        Pause("hold", 1.4),
    ], spec={"tpl": "talk", "bg": "studio_purple", "syl": "G1(c)",
             "cast": [{"who": "LEX", "x": 300, "y": 1060, "s": 0.85},
                      {"who": "KITO", "x": 1650, "y": 1060, "s": 0.85, "enter": "kito7"}],
             "pops": [{"kind": "card", "at": "lex7b", "x": 960, "y": 280, "w": 1000,
                       "h": 230, "title": "Prescribed part",
                       "body": "50% of the first £10,000 + 20% of the rest · cap £800,000",
                       "color": "#3bb273", "bs": 40},
                      {"kind": "card", "at": "lex7c", "x": 960, "y": 590, "w": 1000,
                       "h": 230, "title": "Example: £100,000 of floating charge assets",
                       "body": "£5,000 + 20% × £90,000 (£18,000) = £23,000 for unsecured",
                       "color": "#1f3a5f", "bs": 38}]}),

    quiz_scene("s8", "Quick check",
               "Who ranks higher on liquidation?",
               ["Floating charge holders", "Preferential creditors such as employees' "
                "wages", "Unsecured trade creditors", "Ordinary shareholders"], 1,
               "Quick check. Which of these ranks highest on a liquidation?",
               "Preferential creditors, such as employees' wages.",
               why="Preferential debts are paid before floating charge holders",
               syl="G1(c)"),

    quiz_scene("s9", "Quick check",
               "In a members' voluntary liquidation, what must the directors make?",
               ["A statement of affairs only", "A declaration of solvency",
                "A statutory demand", "A petition to court"], 1,
               "And in a members' voluntary liquidation, what must the directors make?",
               "A declaration of solvency.",
               think=4.0, syl="G1(a)"),

    recap_scene("s10", [
        ("MVL solvent, CVL insolvent.", "MVL solvent · CVL insolvent"),
        ("Declaration of solvency: twelve months.", "Declaration of solvency"),
        ("Compulsory: unable to pay, or just and equitable.", "Compulsory grounds"),
        ("Liquidation starts from the petition.", "Starts at petition"),
        ("Fixed, expenses, preferential, floating, unsecured.", "Priority order"),
    ], [
        Line("lex10", "LEX", "Next time: administration, the rescue route that can save a "
             "company instead of killing it.", gap=0.3),
        Line("nia10", "NIA", "I prefer rescue stories.", gap=0.6),
    ], next_ep=26, next_title="Administration: The Rescue", next_icon="umbrella"),
]
