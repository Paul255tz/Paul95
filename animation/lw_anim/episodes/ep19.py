"""Episode 19 - Borrowing Power.

Syllabus E2(a)-(e): companies' borrowing powers; loan capital and debentures;
loan capital compared with share capital; fixed and floating charges; and
registering charges. UK Companies Act 2006 / Insolvency Act 1986 model.
Setting: Amara's bank lends Safari Solar Limited money for its factory.
"""
from ._kit import (DISPLAY_NAMES, SERIES, VOICES, Line, Pause, Scene, Sfx,  # noqa: F401
                   quiz_scene, recap_scene, title_scene)

EPISODE = "Episode 19"
EPISODE_TITLE = "Borrowing Power"
SLUG = "episode19_borrowing_power"

SCENES = [
    title_scene(19, EPISODE_TITLE, "Syllabus E2", ("chain", "bank")),

    Scene("s1", "A loan offer", "", [
        Pause("open", 1.0),
        Line("amara1", "AMARA", "Our bank will lend Safari Solar five hundred thousand "
             "dollars. But we want security: a fixed charge over the factory, and a floating "
             "charge over your stock.", gap=0.4),
        Line("kito1", "KITO", "Fixed, floating... it sounds like boats!", gap=0.4),
        Line("lex1", "LEX", "They're charges, and they decide who gets paid first if things "
             "go wrong. First, can a company borrow at all?"),
        Pause("hold", 1.2),
    ], spec={"tpl": "talk", "bg": "bank", "syl": "E2",
             "cast": [{"who": "AMARA", "x": 1450, "y": 1040, "s": 0.92},
                      {"who": "KITO", "x": 960, "y": 1040, "s": 0.92, "mood": "thinking"},
                      {"who": "LEX", "x": 420, "y": 1040, "s": 0.88, "enter": "lex1",
                       "from": "left"}],
             "pops": [{"kind": "icon", "icon": "factory", "x": 1100, "y": 260, "s": 1.0,
                       "at": ["amara1", 5.5], "label": "Fixed charge", "until": "lex1"},
                      {"kind": "icon", "icon": "box", "x": 1450, "y": 260, "s": 1.0,
                       "at": ["amara1", 8.0], "label": "Floating charge", "until": "lex1",
                       "color": "#7768ae"}]}),

    Scene("s2", "Borrowing powers and debentures", "", [
        Pause("open", 1.0),
        Line("lex2a", "LEX", "A trading company has an implied power to borrow for its "
             "business. And with unrestricted objects, a modern company can borrow unless "
             "its articles restrict it. The directors exercise the power.", gap=0.3),
        Line("lex2b", "LEX", "A public company cannot borrow until it has its trading "
             "certificate.", gap=0.4),
        Sfx("pop"),
        Line("lex2c", "LEX", "Loan capital is money borrowed long term. The document "
             "acknowledging the debt is called a debenture.", gap=0.25),
        Sfx("pop"),
        Line("lex2d", "LEX", "It can be a single debenture, to one lender like a bank.",
             gap=0.25),
        Sfx("pop"),
        Line("lex2e", "LEX", "A series of debentures, issued to many lenders, ranking "
             "equally, pari passu.", say="A series of debentures, issued to many lenders, "
             "ranking equally, pah-ree pass-oo.", gap=0.25),
        Sfx("pop"),
        Line("lex2f", "LEX", "Or debenture stock, held through a trustee under a trust deed "
             "for the benefit of all the holders.", gap=0.4),
        Line("amara2", "AMARA", "And it can be secured by a charge over assets, or "
             "unsecured."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "white", "heading": "Debentures", "syl": "E2(a)–(b)",
             "row": 130, "ts": 40,
             "items": [{"at": "lex2d", "text": "Single debenture", "sub": "One lender, e.g. "
                                                                         "a bank",
                        "icon": "bank", "color": "#0f8b8d"},
                       {"at": "lex2e", "text": "Series of debentures", "sub": "Many lenders, "
                                                                             "rank pari passu",
                        "icon": "people", "color": "#7768ae"},
                       {"at": "lex2f", "text": "Debenture stock", "sub": "Held via a trustee "
                                                                        "and trust deed",
                        "icon": "shield", "color": "#f2a541"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "AMARA", "x": 1810, "s": 0.55, "y": 1120, "enter": "amara2"}],
             "pops": [{"kind": "card", "at": "lex2a", "until": "lex2c", "x": 1190, "y": 470,
                       "w": 960, "h": 300, "title": "Power to borrow",
                       "body": "Implied for trading companies · exercised by directors · "
                               "plc needs its trading certificate first",
                       "color": "#1f3a5f", "bs": 36}]}),

    Scene("s3", "Shares or loans?", "", [
        Pause("open", 1.0),
        Line("lex3a", "LEX", "Debenture holders and shareholders are very different.",
             gap=0.3),
        Line("lex3b", "LEX", "Shareholders are members, who own the company. Debenture "
             "holders are creditors, who are owed money by it.", gap=0.3),
        Line("lex3c", "LEX", "Interest on debentures must be paid, even with no profits. "
             "Dividends can only come from distributable profits.", gap=0.3),
        Line("lex3d", "LEX", "Debenture holders usually have no vote. On a winding up, they "
             "are repaid before any shareholder, and secured ones can enforce their "
             "security.", gap=0.3),
        Line("lex3e", "LEX", "And debentures may be issued at a discount, and bought back "
             "freely. Shares may not be issued at a discount, and buy-backs are tightly "
             "controlled.", gap=0.4),
        Line("nia3", "NIA", "So shares are riskier for the investor, but debt is riskier "
             "for the company."),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio", "heading": "Share capital vs loan capital",
             "syl": "E2(c)", "ts": 32,
             "cols": [{"title": "Shareholder", "icon": "pie", "color": "#7768ae",
                       "at": "lex3b",
                       "items": [{"at": ["lex3b", 0.3], "text": "A member: owns the company"},
                                 {"at": ["lex3c", 4.0], "text": "Dividend only from "
                                                               "distributable profits"},
                                 {"at": "lex3d", "text": "Usually votes"},
                                 {"at": ["lex3d", 3.5], "text": "Repaid last on winding up"},
                                 {"at": "lex3e", "text": "No discount · buy-backs "
                                                         "controlled"}]},
                      {"title": "Debenture holder", "icon": "bank", "color": "#0f8b8d",
                       "at": ["lex3b", 2.5],
                       "items": [{"at": ["lex3b", 3.0], "text": "A creditor: owed money"},
                                 {"at": "lex3c", "text": "Interest due, profits or not"},
                                 {"at": ["lex3d", 1.5], "text": "Usually no vote"},
                                 {"at": ["lex3d", 4.5], "text": "Repaid before members; can "
                                                               "enforce security"},
                                 {"at": ["lex3e", 1.0], "text": "May issue at discount · "
                                                               "buy back freely"}]}],
             "vs": True,
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia3"}]}),

    Scene("s4", "Fixed and floating charges", "", [
        Pause("open", 1.0),
        Line("lex4a", "LEX", "A charge gives a lender rights over company assets if the "
             "loan is not repaid.", gap=0.3),
        Line("lex4b", "LEX", "A fixed charge attaches to specific, identified assets, like "
             "land, buildings or major machinery. The company cannot sell or deal with them "
             "without the lender's consent.", gap=0.4),
        Line("lex4c", "LEX", "A floating charge, as described in Re Yorkshire Woolcombers, "
             "is a charge over a class of assets, present and future, that changes in the "
             "ordinary course of business.", gap=0.3),
        Line("lex4d", "LEX", "Until it crystallises, the company can deal with those assets "
             "freely. Think inventory and receivables.", gap=0.4),
        Line("lex4e", "LEX", "The label the parties use doesn't decide it. In Re Spectrum "
             "Plus, a so-called fixed charge over book debts was really floating, because "
             "the company could freely use the money it collected.", gap=0.4),
        Line("amara4", "AMARA", "Which is why banks prefer fixed charges wherever they can."),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio_teal", "heading": "Fixed vs floating",
             "syl": "E2(d)", "ts": 32,
             "cols": [{"title": "Fixed charge", "icon": "lock", "color": "#0f8b8d",
                       "at": "lex4b",
                       "items": [{"at": ["lex4b", 0.5], "text": "Specific, identified assets"},
                                 {"at": ["lex4b", 3.0], "text": "Land, buildings, machinery"},
                                 {"at": ["lex4b", 6.0], "text": "Can't sell without consent"},
                                 {"at": "amara4", "text": "Ranks ahead of floating charges",
                                  "good": True}]},
                      {"title": "Floating charge", "icon": "box", "color": "#7768ae",
                       "at": "lex4c",
                       "items": [{"at": ["lex4c", 3.0], "text": "A class of assets, present "
                                                               "and future"},
                                 {"at": ["lex4c", 6.0], "text": "Changes in ordinary "
                                                               "business"},
                                 {"at": "lex4d", "text": "Company deals freely until "
                                                         "crystallisation"},
                                 {"at": ["lex4d", 4.0], "text": "Stock, receivables"}]}],
             "vs": True,
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "AMARA", "x": 1810, "s": 0.55, "y": 1120, "enter": "amara4"}],
             "pops": [{"kind": "chip", "at": "lex4e", "until": "amara4", "x": 1180, "y": 950,
                       "text": "Re Spectrum Plus (2005): substance beats the label",
                       "color": "#e4572e", "size": 32}]}),

    Scene("s5", "Crystallisation and weak spots", "", [
        Pause("open", 1.0),
        Line("lex5a", "LEX", "A floating charge crystallises, becoming fixed on the assets "
             "held at that moment, when certain events happen.", gap=0.3),
        Sfx("pop"),
        Line("lex5b", "LEX", "The company goes into liquidation.", gap=0.2),
        Sfx("pop"),
        Line("lex5c", "LEX", "It stops trading.", gap=0.2),
        Sfx("pop"),
        Line("lex5d", "LEX", "A receiver or administrator is appointed.", gap=0.2),
        Sfx("pop"),
        Line("lex5e", "LEX", "Or an event named in the charge itself occurs.", gap=0.4),
        Line("lex5f", "LEX", "Floating charges have weak spots. They rank behind fixed "
             "charges, liquidation expenses and preferential creditors, and part of their "
             "assets is set aside for unsecured creditors.", gap=0.3),
        Line("lex5g", "LEX", "A floating charge created in the twelve months before "
             "insolvency, or two years for a connected person, may be invalid, except to the "
             "extent of new money given. And a negative pledge clause can stop the company "
             "giving later charges priority, if the later lender knows of it."),
        Pause("hold", 1.4),
    ], spec={"tpl": "timeline", "bg": "studio", "heading": "When a floating charge "
                                                           "crystallises",
             "syl": "E2(d)", "cw": 290,
             "events": [{"at": "lex5b", "label": "Liquidation", "icon": "fire",
                         "color": "#e4572e"},
                        {"at": "lex5c", "label": "Stops trading", "icon": "door",
                         "color": "#f2a541"},
                        {"at": "lex5d", "label": "Receiver or administrator",
                         "icon": "person", "color": "#7768ae"},
                        {"at": "lex5e", "label": "Event named in the charge",
                         "icon": "contract", "color": "#0f8b8d"}],
             "cast": [{"who": "LEX", "x": 250}],
             "pops": [{"kind": "card", "at": "lex5f", "until": "lex5g", "x": 1190, "y": 470,
                       "w": 980, "h": 300, "title": "Weak spots",
                       "body": "Behind fixed charges, expenses and preferential creditors · "
                               "prescribed part for unsecured", "color": "#e4572e",
                       "dim": True, "bs": 36},
                      {"kind": "card", "at": "lex5g", "x": 1190, "y": 470, "w": 980,
                       "h": 300, "title": "Timing and negative pledges",
                       "body": "Created within 12 months (2 years connected) may be invalid, "
                               "except new money · negative pledge binds if known",
                       "color": "#1f3a5f", "dim": True, "bs": 34}]}),

    Scene("s6", "Registering charges", "", [
        Pause("open", 1.0),
        Line("lex6a", "LEX", "Most charges must be registered at Companies House within "
             "twenty-one days, beginning the day after the charge is created.", gap=0.3),
        Line("lex6b", "LEX", "The registrar issues a certificate, which is conclusive "
             "evidence that the charge was properly registered.", gap=0.3),
        Line("lex6c", "LEX", "If it isn't registered in time, the charge is void against a "
             "liquidator, an administrator and other creditors. The debt survives, but it "
             "becomes unsecured, and immediately repayable.", gap=0.3),
        Line("lex6d", "LEX", "A court can allow late registration, without harming rights "
             "already acquired. And the company keeps copies of its charge documents for "
             "inspection.", gap=0.4),
        Line("amara6", "AMARA", "Our lawyers register every charge on day one. In Tanzania "
             "and Kenya too, charges must be registered with the companies registry, within "
             "a set time."),
        Pause("hold", 1.4),
    ], spec={"tpl": "timeline", "bg": "studio_teal", "heading": "Registration of charges",
             "syl": "E2(e)", "cw": 300,
             "events": [{"at": "lex6a", "label": "Charge created", "sub": "Clock starts next "
                                                                         "day",
                         "icon": "chain", "color": "#0f8b8d"},
                        {"at": ["lex6a", 3.0], "label": "21 days to register",
                         "icon": "hourglass", "color": "#f2a541"},
                        {"at": "lex6b", "label": "Certificate", "sub": "Conclusive evidence",
                         "icon": "seal", "color": "#3bb273"},
                        {"at": "lex6c", "label": "Missed it?", "sub": "Void vs liquidator, "
                                                                     "administrator, "
                                                                     "creditors",
                         "icon": "warning", "color": "#e4572e"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "AMARA", "x": 1810, "s": 0.55, "y": 1120, "enter": "amara6"}],
             "pops": [{"kind": "chip", "at": "lex6d", "until": "amara6", "x": 1200, "y": 980,
                       "text": "Court may allow late registration", "color": "#1f3a5f",
                       "size": 32}]}),

    Scene("s7", "Who ranks first?", "", [
        Pause("open", 1.0),
        Line("lex7a", "LEX", "When two charges cover the same asset, the rules on priority "
             "decide.", gap=0.3),
        Sfx("pop"),
        Line("lex7b", "LEX", "A fixed charge ranks ahead of a floating charge, even one "
             "created earlier.", gap=0.25),
        Sfx("pop"),
        Line("lex7c", "LEX", "Unless the floating charge has a negative pledge clause, and "
             "the later fixed chargee knew about it.", gap=0.25),
        Sfx("pop"),
        Line("lex7d", "LEX", "Between charges of the same type, the earlier one created ranks "
             "first, provided each was registered on time.", gap=0.25),
        Sfx("pop"),
        Line("lex7e", "LEX", "And the parties can always change the order by a priority "
             "agreement.", gap=0.4),
        Line("kito7", "KITO", "So the bank's fixed charge on the factory beats everyone else "
             "on that building."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "heading": "Priority of charges",
             "syl": "E2(d)", "row": 130, "ts": 40,
             "items": [{"at": "lex7b", "text": "Fixed beats floating", "icon": "lock",
                        "color": "#0f8b8d"},
                       {"at": "lex7c", "text": "Unless a negative pledge is known",
                        "icon": "eye", "color": "#e4572e"},
                       {"at": "lex7d", "text": "Same type: first created, if registered",
                        "icon": "calendar", "color": "#7768ae"},
                       {"at": "lex7e", "text": "Or by priority agreement", "icon": "handshake",
                        "color": "#3bb273"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "KITO", "x": 1810, "s": 0.55, "y": 1120, "enter": "kito7"}]}),

    quiz_scene("s8", "Quick check",
               "Which feature marks a charge as floating rather than fixed?",
               ["It is over land", "The company can deal with the assets in the ordinary "
                "course of business", "It is registered late", "It secures a large loan"], 1,
               "Quick check. Which feature marks a charge as floating, rather than fixed?",
               "The company can deal with the assets in the ordinary course of business.",
               syl="E2(d)"),

    quiz_scene("s9", "Quick check",
               "A charge is not registered within 21 days. What is the effect?",
               ["The loan is cancelled", "The charge is void against a liquidator and "
                "creditors; the debt is unsecured", "The directors go to prison",
                "Nothing, registration is optional"], 1,
               "And if a charge is not registered within twenty-one days, what happens?",
               "The charge is void against a liquidator and creditors. The debt becomes "
               "unsecured.",
               think=4.0, syl="E2(e)"),

    recap_scene("s10", [
        ("Companies can borrow; directors exercise it.", "Power to borrow"),
        ("Debentures: creditors, not members.", "Debenture holders = creditors"),
        ("Fixed: specific assets. Floating: a changing class.", "Fixed vs floating"),
        ("Crystallisation fixes a floating charge.", "Crystallisation"),
        ("Register within twenty-one days.", "Register within 21 days"),
    ], [
        Line("lex10", "LEX", "Next time: the capital maintenance rules that protect "
             "creditors, and when a company may pay dividends.", gap=0.3),
        Line("kito10", "KITO", "Dividends! My favourite word!", gap=0.6),
    ], next_ep=20, next_title="Keeping the Capital", next_icon="shield"),
]
