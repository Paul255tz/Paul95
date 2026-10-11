"""Episode 22 - Directors' Duties.

Syllabus F1(d): the general duties directors owe their company (Companies Act
2006 ss.171-177) and the statutory controls over dealings between directors and
their companies, including loans. Kenya's Companies Act 2015 codifies the same
general duties. Setting: Kito's three "great ideas" alarm the board.
"""
from ._kit import (DISPLAY_NAMES, SERIES, VOICES, Line, Pause, Scene, Sfx,  # noqa: F401
                   quiz_scene, recap_scene, title_scene)

EPISODE = "Episode 22"
EPISODE_TITLE = "Directors' Duties"
SLUG = "episode22_directors_duties"

SCENES = [
    title_scene(22, EPISODE_TITLE, "Syllabus F1(d)", ("shield", "scales")),

    Scene("s1", "Kito's three great ideas", "", [
        Pause("open", 1.0),
        Line("kito1", "KITO", "Three great ideas! The company buys my car for a hundred and "
             "twenty thousand dollars. It lends me thirty thousand. And that hotel's solar "
             "contract? I'll take it myself, on the side.", gap=0.4),
        Line("amara1", "AMARA", "As a director of this board, I have to object. Three "
             "times.", gap=0.4),
        Line("lex1", "LEX", "Amara is right. Directors owe duties to the company, and the "
             "Companies Act sets out seven general duties. Let's take them one by one."),
        Pause("hold", 1.2),
    ], spec={"tpl": "talk", "bg": "boardroom", "syl": "F1(d)",
             "cast": [{"who": "KITO", "x": 960, "y": 1000, "s": 0.88, "mood": "excited",
                       "talk_pose": "cheer"},
                      {"who": "AMARA", "x": 1350, "y": 1000, "s": 0.85, "mood": "worried",
                       "talk_pose": "hips"},
                      {"who": "NIA", "x": 640, "y": 1000, "s": 0.85, "mood": "worried"},
                      {"who": "LEX", "x": 230, "y": 1040, "s": 0.85, "enter": "lex1",
                       "from": "left"}],
             "pops": [{"kind": "chip", "at": ["kito1", 1.5], "until": "lex1", "x": 960,
                       "y": 140, "text": "1. Company buys my car", "color": "#e4572e",
                       "size": 34},
                      {"kind": "chip", "at": ["kito1", 6.0], "until": "lex1", "x": 960,
                       "y": 230, "text": "2. Company lends me $30,000", "color": "#e4572e",
                       "size": 34},
                      {"kind": "chip", "at": ["kito1", 9.0], "until": "lex1", "x": 960,
                       "y": 320, "text": "3. I take the hotel contract", "color": "#e4572e",
                       "size": 34}]}),

    Scene("s2", "The seven general duties", "", [
        Pause("open", 1.0),
        Sfx("pop"),
        Line("lex2a", "LEX", "One. Act within your powers, under the constitution, and use "
             "powers only for their proper purpose.", gap=0.2),
        Sfx("pop"),
        Line("lex2b", "LEX", "Two. Promote the success of the company, for the benefit of "
             "its members as a whole.", gap=0.2),
        Sfx("pop"),
        Line("lex2c", "LEX", "Three. Exercise independent judgement.", gap=0.2),
        Sfx("pop"),
        Line("lex2d", "LEX", "Four. Exercise reasonable care, skill and diligence.", gap=0.2),
        Sfx("pop"),
        Line("lex2e", "LEX", "Five. Avoid conflicts of interest.", gap=0.2),
        Sfx("pop"),
        Line("lex2f", "LEX", "Six. Do not accept benefits from third parties because you "
             "are a director.", gap=0.2),
        Sfx("pop"),
        Line("lex2g", "LEX", "Seven. Declare any interest in a proposed transaction with the "
             "company.", gap=0.4),
        Line("nia2", "NIA", "And Kenya's Companies Act of 2015 sets out the same duties, "
             "almost word for word."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "heading": "General duties (ss 171–177)",
             "syl": "F1(d)", "row": 92, "ts": 34,
             "items": [{"at": "lex2a", "text": "Act within powers · proper purpose",
                        "color": "#0f8b8d"},
                       {"at": "lex2b", "text": "Promote the success of the company",
                        "color": "#2b86c5"},
                       {"at": "lex2c", "text": "Independent judgement", "color": "#7768ae"},
                       {"at": "lex2d", "text": "Reasonable care, skill and diligence",
                        "color": "#3bb273"},
                       {"at": "lex2e", "text": "Avoid conflicts of interest",
                        "color": "#e4572e"},
                       {"at": "lex2f", "text": "No benefits from third parties",
                        "color": "#f2a541"},
                       {"at": "lex2g", "text": "Declare interest in proposed deals",
                        "color": "#d64f8a"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia2"}]}),

    Scene("s3", "Promoting success", "", [
        Pause("open", 1.0),
        Line("lex3a", "LEX", "When promoting the company's success, directors must have "
             "regard to a list of factors.", gap=0.3),
        Sfx("pop"),
        Line("lex3b", "LEX", "The long-term consequences of their decisions.", gap=0.2),
        Sfx("pop"),
        Line("lex3c", "LEX", "The interests of employees.", gap=0.2),
        Sfx("pop"),
        Line("lex3d", "LEX", "Relationships with suppliers, customers and others.", gap=0.2),
        Sfx("pop"),
        Line("lex3e", "LEX", "The impact on the community and the environment.", gap=0.2),
        Sfx("pop"),
        Line("lex3f", "LEX", "A reputation for high standards of business conduct.", gap=0.2),
        Sfx("pop"),
        Line("lex3g", "LEX", "And acting fairly between members.", gap=0.4),
        Line("lex3h", "LEX", "When a company is insolvent, or close to it, directors must "
             "also consider the interests of its creditors."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "white", "layout": "grid", "cols": 3,
             "heading": "Section 172 factors", "syl": "F1(d)", "cell_h": 290, "ts": 34,
             "items": [{"at": "lex3b", "text": "Long-term consequences", "icon": "hourglass",
                        "color": "#0f8b8d"},
                       {"at": "lex3c", "text": "Employees", "icon": "people",
                        "color": "#2b86c5"},
                       {"at": "lex3d", "text": "Suppliers and customers", "icon": "handshake",
                        "color": "#7768ae"},
                       {"at": "lex3e", "text": "Community and environment", "icon": "globe",
                        "color": "#3bb273"},
                       {"at": "lex3f", "text": "High standards", "icon": "star",
                        "color": "#f2a541"},
                       {"at": "lex3g", "text": "Fairness between members", "icon": "scales",
                        "color": "#e4572e"}],
             "cast": [{"who": "LEX", "x": 250}],
             "pops": [{"kind": "chip", "at": "lex3h", "x": 1190, "y": 960,
                       "text": "Near insolvency: creditors' interests count too",
                       "color": "#1f3a5f", "size": 32}]}),

    Scene("s4", "Care, skill and diligence", "", [
        Pause("open", 1.0),
        Line("lex4a", "LEX", "The standard of care has two parts.", gap=0.3),
        Line("lex4b", "LEX", "An objective minimum: the knowledge, skill and experience "
             "reasonably expected of anyone doing that director's job.", gap=0.3),
        Line("lex4c", "LEX", "Plus a subjective top-up: the director's own knowledge, skill "
             "and experience. So a qualified accountant like Nia is judged as an accountant.",
             gap=0.4),
        Line("lex4d", "LEX", "In Re D'Jan of London, a director signed an insurance form "
             "without reading it, and was negligent. And in Dorchester Finance against "
             "Stebbing, non-executives who signed blank cheques were liable too.", gap=0.4),
        Line("amara4", "AMARA", "So non-executives can't just sit back. I must read every "
             "board paper."),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio", "heading": "Section 174: the dual test",
             "syl": "F1(d)", "ts": 33,
             "cols": [{"title": "Objective minimum", "icon": "people", "color": "#0f8b8d",
                       "at": "lex4b",
                       "items": [{"at": ["lex4b", 1.0], "text": "What anyone in that role "
                                                               "should know and do"},
                                 {"at": "lex4d", "text": "Re D'Jan of London (1993)"}]},
                      {"title": "Subjective top-up", "icon": "brain", "color": "#7768ae",
                       "at": "lex4c",
                       "items": [{"at": ["lex4c", 0.5], "text": "The director's own "
                                                               "knowledge and skill"},
                                 {"at": ["lex4c", 4.5], "text": "Experts held to a higher "
                                                               "standard"},
                                 {"at": ["lex4d", 6.0], "text": "Dorchester Finance v "
                                                               "Stebbing (1989)"}]}],
             "vs": True,
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "AMARA", "x": 1810, "s": 0.55, "y": 1120, "enter": "amara4"}]}),

    Scene("s5", "Conflicts: Kito's hotel deal", "", [
        Pause("open", 1.0),
        Line("lex5a", "LEX", "Now Kito's hotel contract. A director must avoid situations "
             "where his interests conflict with the company's, especially exploiting "
             "property, information or opportunities.", gap=0.3),
        Line("lex5b", "LEX", "In Regal Hastings against Gulliver, directors bought shares "
             "personally, in an opportunity that came to them as directors. They acted "
             "honestly, and the company could not have afforded the shares anyway.",
             gap=0.3),
        Line("lex5c", "LEX", "They still had to hand over their profit to the company.",
             gap=0.4),
        Sfx("sparkle"),
        Pause("stamp", 1.2),
        Line("lex5d", "LEX", "In IDC against Cooley, a director secretly took a contract "
             "offered to him personally, but which he should have obtained for his company. "
             "He too had to account for his profit.", gap=0.3),
        Line("kito5", "KITO", "Unless the independent directors authorise it. Fine, the hotel "
             "deal goes to Safari Solar."),
        Pause("hold", 1.4),
    ], spec={"tpl": "case", "bg": "boardroom", "name": "Regal (Hastings) Ltd v Gulliver",
             "year": "House of Lords · 1942", "syl": "F1(d)",
             "rows": [{"at": "lex5b", "label": "Facts", "text": "Directors used an "
                                                                "opportunity that came via "
                                                                "the company",
                       "color": "#7768ae"},
                      {"at": "lex5c", "label": "Held", "text": "Liable to account, even "
                                                               "though honest",
                       "color": "#e4572e"},
                      {"at": "lex5d", "label": "Also", "text": "IDC v Cooley (1972): "
                                                               "diverted contract",
                       "color": "#0f8b8d"}],
             "stamp": {"at": "stamp", "text": "ACCOUNT FOR PROFIT", "color": "#e4572e"},
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "KITO", "x": 1810, "s": 0.55, "y": 1120, "enter": "kito5"}]}),

    Scene("s6", "Proper purpose and remedies", "", [
        Pause("open", 1.0),
        Line("lex6a", "LEX", "Powers must be used for proper purposes. In Howard Smith "
             "against Ampol Petroleum, directors issued shares to defeat a takeover. That was "
             "an improper purpose, so the issue was set aside.", gap=0.4),
        Line("lex6b", "LEX", "Breach of duty has serious consequences.", gap=0.25),
        Sfx("pop"),
        Line("lex6c", "LEX", "Account for any profit made.", gap=0.2),
        Sfx("pop"),
        Line("lex6d", "LEX", "Compensate the company for its loss.", gap=0.2),
        Sfx("pop"),
        Line("lex6e", "LEX", "Rescission of the contract, or an injunction.", gap=0.4),
        Line("lex6f", "LEX", "Members can ratify some breaches by ordinary resolution, "
             "without the votes of the director concerned. And a court may relieve a "
             "director who acted honestly and reasonably."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "heading": "Breach of duty: remedies",
             "syl": "F1(d)", "row": 130, "ts": 40,
             "items": [{"at": "lex6c", "text": "Account for profits", "icon": "moneybag",
                        "color": "#f2a541"},
                       {"at": "lex6d", "text": "Compensation for loss", "icon": "coin",
                        "color": "#0f8b8d"},
                       {"at": "lex6e", "text": "Rescission or injunction", "icon": "scissors",
                        "color": "#e4572e"},
                       {"at": "lex6f", "text": "Ratification · court relief",
                        "sub": "Interested director can't vote · honest and reasonable",
                        "icon": "ballot", "color": "#7768ae"}],
             "cast": [{"who": "LEX", "x": 250}],
             "pops": [{"kind": "card", "at": "lex6a", "until": "lex6b", "x": 1190, "y": 470,
                       "w": 960, "h": 280, "title": "Howard Smith v Ampol (1974)",
                       "body": "Shares issued to defeat a takeover = improper purpose",
                       "color": "#1f3a5f", "bs": 38}]}),

    Scene("s7", "Statutory controls", "", [
        Pause("open", 1.0),
        Line("lex7a", "LEX", "On top of the general duties, some dealings need the members' "
             "approval.", gap=0.3),
        Sfx("pop"),
        Line("lex7b", "LEX", "A director's service contract guaranteed for more than two "
             "years.", gap=0.25),
        Sfx("pop"),
        Line("lex7c", "LEX", "A substantial property transaction. Buying or selling a "
             "non-cash asset with a director, worth over a hundred thousand pounds, or over "
             "ten percent of net assets, if that is above five thousand pounds. That's "
             "Kito's car!", gap=0.25),
        Sfx("pop"),
        Line("lex7d", "LEX", "Loans to directors, and guarantees or security for them. "
             "Public companies need approval for quasi-loans and credit transactions too.",
             gap=0.25),
        Sfx("pop"),
        Line("lex7e", "LEX", "And payments for loss of office.", gap=0.4),
        Line("lex7f", "LEX", "There are exceptions, such as small loans up to ten thousand "
             "pounds, and up to fifty thousand to cover expenses of doing the company's "
             "business.", gap=0.3),
        Line("amara7", "AMARA", "So Kito's car and loan both need a members' vote. And I'll "
             "be asking hard questions."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "white", "heading": "Members' approval needed",
             "syl": "F1(d)", "row": 120, "ts": 38,
             "items": [{"at": "lex7b", "text": "Service contracts over 2 years",
                        "icon": "calendar", "color": "#0f8b8d"},
                       {"at": "lex7c", "text": "Substantial property transactions",
                        "sub": "> £100,000, or > 10% of net assets (min £5,000)",
                        "icon": "house", "color": "#7768ae"},
                       {"at": "lex7d", "text": "Loans to directors",
                        "sub": "plc: also quasi-loans and credit transactions",
                        "icon": "coin", "color": "#e4572e"},
                       {"at": "lex7e", "text": "Payments for loss of office",
                        "icon": "door", "color": "#f2a541"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "AMARA", "x": 1810, "s": 0.55, "y": 1120, "enter": "amara7"}],
             "pops": [{"kind": "chip", "at": "lex7f", "until": "amara7", "x": 1190, "y": 950,
                       "text": "Exceptions: loans up to £10,000 · business expenses up to £50,000",
                       "color": "#3bb273", "size": 30}]}),

    quiz_scene("s8", "Quick check",
               "In Regal (Hastings) v Gulliver, the directors acted honestly and the company "
               "could not have bought the shares itself. What happened?",
               ["They kept their profit", "They had to account to the company for their "
                "profit", "They were disqualified", "The company was wound up"], 1,
               "Quick check. In Regal Hastings against Gulliver, the directors acted honestly. "
               "What happened?",
               "They still had to account for their profit.",
               why="Strict rule: no profit from an opportunity that comes via the company",
               syl="F1(d)"),

    quiz_scene("s9", "Quick check",
               "Under section 174, a finance director who is a qualified accountant is "
               "judged by…",
               ["Only what an average director would know", "Only her own skills",
                "The objective minimum, raised by her own higher skills",
                "Nothing; directors cannot be negligent"], 2,
               "And a director who is a qualified accountant is judged by what standard?",
               "The objective minimum, raised by her own higher skills.",
               think=4.0, syl="F1(d)"),

    recap_scene("s10", [
        ("Seven general duties.", "7 general duties"),
        ("Promote success, considering stakeholders.", "s172: stakeholders"),
        ("Care and skill: objective plus subjective.", "s174: dual test"),
        ("No conflicts, no secret profits.", "No conflicts (Regal)"),
        ("Members approve big deals and loans.", "Members approve SPTs, loans"),
    ], [
        Line("lex10", "LEX", "Next time, two more officers: the company secretary, and the "
             "auditor.", gap=0.3),
        Line("aud10", "AUDITOR", "Finally! An episode about me.", gap=0.6),
    ], next_ep=23, next_title="Secretary and Auditor", next_icon="magnifier"),
]
