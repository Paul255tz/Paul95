"""Episode 18 - Share Capital.

Syllabus E1(a)-(d): types of capital; classes of shares, treasury shares and
variation of class rights; allotment, pre-emption, rights and bonus issues;
issuing shares at a discount or a premium. UK Companies Act 2006 model.
Setting: Safari Solar Limited raises money for a lamp factory in Arusha.
"""
from ._kit import (DISPLAY_NAMES, SERIES, VOICES, Line, Pause, Scene, Sfx,  # noqa: F401
                   quiz_scene, recap_scene, title_scene)

EPISODE = "Episode 18"
EPISODE_TITLE = "Share Capital"
SLUG = "episode18_share_capital"

SCENES = [
    title_scene(18, EPISODE_TITLE, "Syllabus E1", ("pie", "coin")),

    Scene("s1", "Money for a factory", "", [
        Pause("open", 1.0),
        Line("kito1", "KITO", "We need a factory in Arusha! Let's sell new shares. One "
             "dollar shares at fifty cents each. Investors will love the bargain!", gap=0.4),
        Line("nia1", "NIA", "Is that even allowed?", gap=0.3),
        Line("lex1", "LEX", "No. But before we see why, let's sort out the vocabulary of "
             "share capital."),
        Pause("hold", 1.2),
    ], spec={"tpl": "talk", "bg": "harbour", "syl": "E1",
             "cast": [{"who": "KITO", "x": 1450, "y": 1030, "s": 0.95, "mood": "excited",
                       "talk_pose": "cheer"},
                      {"who": "NIA", "x": 960, "y": 1030, "s": 0.9, "mood": "thinking"},
                      {"who": "LEX", "x": 420, "y": 1030, "s": 0.88, "enter": "lex1",
                       "from": "left"}],
             "pops": [{"kind": "icon", "icon": "factory", "x": 1200, "y": 280, "s": 1.1,
                       "at": ["kito1", 0.4], "until": "nia1", "label": "Arusha factory"},
                      {"kind": "stamp", "at": "lex1", "x": 1200, "y": 300,
                       "text": "50¢ for a $1 share?", "color": "#e4572e", "size": 48}]}),

    Scene("s2", "Types of capital", "", [
        Pause("open", 1.0),
        Line("lex2a", "LEX", "Each share has a nominal, or par, value. Say one dollar.",
             gap=0.25),
        Sfx("pop"),
        Line("lex2b", "LEX", "Issued, or allotted, capital is the nominal value of the "
             "shares actually issued.", gap=0.25),
        Sfx("pop"),
        Line("lex2c", "LEX", "Called-up capital is the part the company has asked "
             "shareholders to pay.", gap=0.25),
        Sfx("pop"),
        Line("lex2d", "LEX", "Paid-up capital is what they have actually paid.", gap=0.25),
        Sfx("pop"),
        Line("lex2e", "LEX", "Uncalled capital is what remains unpaid. Shareholders must pay "
             "it if called, which is the limit of their liability.", gap=0.25),
        Sfx("pop"),
        Line("lex2f", "LEX", "And reserve capital is uncalled capital that, by special "
             "resolution, can only be called if the company is wound up.", gap=0.4),
        Line("lex2g", "LEX", "Authorised capital, an old upper limit, was abolished, though "
             "articles may still set a cap. And market value is simply what a buyer will "
             "pay."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "heading": "Kinds of share capital",
             "syl": "E1(a)", "row": 108, "ts": 38,
             "items": [{"at": "lex2a", "text": "Nominal (par) value", "sub": "e.g. $1 per "
                                                                           "share",
                        "icon": "tag", "color": "#0f8b8d"},
                       {"at": "lex2b", "text": "Issued / allotted", "sub": "Shares actually "
                                                                          "issued",
                        "icon": "pie", "color": "#2b86c5"},
                       {"at": "lex2c", "text": "Called up", "sub": "Amount asked for",
                        "icon": "megaphone", "color": "#7768ae"},
                       {"at": "lex2d", "text": "Paid up", "sub": "Amount actually paid",
                        "icon": "coin", "color": "#3bb273"},
                       {"at": "lex2e", "text": "Uncalled", "sub": "The members' remaining "
                                                                  "liability",
                        "icon": "hourglass", "color": "#f2a541"},
                       {"at": "lex2f", "text": "Reserve capital", "sub": "Callable only on "
                                                                         "winding up",
                        "icon": "lock", "color": "#e4572e"}],
             "cast": [{"who": "LEX", "x": 250}]}),

    Scene("s3", "Classes of shares", "", [
        Pause("open", 1.0),
        Line("lex3a", "LEX", "Companies can issue different classes of share, with "
             "different rights.", gap=0.3),
        Line("lex3b", "LEX", "Ordinary shares are the equity. They usually carry votes, "
             "receive dividends after any preference shares, and share any surplus when the "
             "company is wound up.", gap=0.4),
        Line("lex3c", "LEX", "Preference shares usually get a fixed dividend first. That "
             "dividend is presumed cumulative, so missed payments carry forward.", gap=0.3),
        Line("lex3d", "LEX", "But they usually have no vote, and only get priority for "
             "capital on a winding up if the terms say so.", gap=0.4),
        Line("lex3e", "LEX", "Redeemable shares can be bought back by the company on set "
             "terms. A company can only issue them if it also has non-redeemable shares.",
             gap=0.3),
        Line("amara3", "AMARA", "Our bank's investment arm would want preference shares: a "
             "steady dividend, paid before the ordinary shareholders."),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio", "heading": "Ordinary vs preference",
             "syl": "E1(b)", "ts": 33,
             "cols": [{"title": "Ordinary", "icon": "people", "color": "#0f8b8d",
                       "at": "lex3b",
                       "items": [{"at": ["lex3b", 1.0], "text": "Usually carry votes"},
                                 {"at": ["lex3b", 3.0], "text": "Dividend after "
                                                               "preference shares"},
                                 {"at": ["lex3b", 6.0], "text": "Share the surplus on "
                                                               "winding up"}]},
                      {"title": "Preference", "icon": "star", "color": "#f2a541",
                       "at": "lex3c",
                       "items": [{"at": ["lex3c", 0.5], "text": "Fixed dividend, paid first"},
                                 {"at": ["lex3c", 3.5], "text": "Presumed cumulative"},
                                 {"at": "lex3d", "text": "Usually no vote"},
                                 {"at": ["lex3d", 2.5], "text": "Capital priority only if "
                                                               "stated"}]}],
             "vs": True,
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "AMARA", "x": 1810, "s": 0.55, "y": 1120, "enter": "amara3"}],
             "pops": [{"kind": "chip", "at": "lex3e", "until": "amara3", "x": 1180, "y": 950,
                       "text": "Redeemable shares: only if non-redeemable shares exist too",
                       "color": "#1f3a5f", "size": 30}]}),

    Scene("s4", "Varying class rights", "", [
        Pause("open", 1.0),
        Line("lex4a", "LEX", "Class rights, such as a preference dividend, cannot simply be "
             "changed by the majority of ordinary shareholders.", gap=0.3),
        Line("lex4b", "LEX", "Follow any procedure in the articles. If there is none, you "
             "need the written consent of holders of three-quarters of that class, or a "
             "special resolution at a separate class meeting.", gap=0.3),
        Line("lex4c", "LEX", "Even then, holders of at least fifteen percent of the class "
             "who did not agree can apply to court, within twenty-one days, to cancel the "
             "variation.", gap=0.4),
        Line("lex4d", "LEX", "But not everything that affects a class varies its rights. In "
             "White against Bristol Aeroplane, issuing new shares diluted a class's voting "
             "power, but did not vary its rights."),
        Pause("hold", 1.4),
    ], spec={"tpl": "timeline", "bg": "studio_teal", "heading": "Variation of class rights",
             "syl": "E1(b)", "cw": 310,
             "events": [{"at": "lex4a", "label": "Class rights", "sub": "Majority alone "
                                                                       "can't change them",
                         "icon": "lock", "color": "#7768ae"},
                        {"at": "lex4b", "label": "Articles' procedure", "sub": "If there "
                                                                               "is one",
                         "icon": "book", "color": "#0f8b8d"},
                        {"at": ["lex4b", 3.5], "label": "Or 75% of the class",
                         "sub": "Written consent, or class special resolution",
                         "icon": "ballot", "color": "#2b86c5"},
                        {"at": "lex4c", "label": "15% may object", "sub": "Apply to court "
                                                                          "within 21 days",
                         "icon": "court", "color": "#e4572e"}],
             "cast": [{"who": "LEX", "x": 250}],
             "pops": [{"kind": "chip", "at": "lex4d", "x": 1200, "y": 980,
                       "text": "White v Bristol Aeroplane (1953): dilution is not variation",
                       "color": "#1f3a5f", "size": 30}]}),

    Scene("s5", "Treasury shares", "", [
        Pause("open", 1.0),
        Line("lex5a", "LEX", "A company may buy back its own shares, out of distributable "
             "profits, so creditors' protection is kept.", gap=0.3),
        Line("lex5b", "LEX", "Normally the shares are then cancelled. But qualifying shares "
             "can instead be held in treasury.", gap=0.3),
        Sfx("pop"),
        Line("lex5c", "LEX", "Treasury shares carry no votes, and receive no dividends.",
             gap=0.25),
        Sfx("pop"),
        Line("lex5d", "LEX", "They can later be sold for cash, transferred to an employee "
             "share scheme, or cancelled, without a fresh issue process.", gap=0.25),
        Sfx("pop"),
        Line("lex5e", "LEX", "When they are cancelled, the company files a return, with an "
             "updated statement of capital.", gap=0.4),
        Line("nia5", "NIA", "So the company parks its own shares, like stock in a "
             "warehouse, ready to reissue."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "white", "heading": "Treasury shares", "syl": "E1(b)",
             "row": 130, "ts": 40,
             "items": [{"at": "lex5a", "text": "Bought back from distributable profits",
                        "icon": "coin", "color": "#0f8b8d"},
                       {"at": "lex5c", "text": "No votes · no dividends", "icon": "lock",
                        "color": "#e4572e"},
                       {"at": "lex5d", "text": "Resell · employee scheme · cancel",
                        "icon": "box", "color": "#7768ae"},
                       {"at": "lex5e", "text": "Cancel? File a return and capital statement",
                        "icon": "doc", "color": "#f2a541"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia5"}]}),

    Scene("s6", "Allotting new shares", "", [
        Pause("open", 1.0),
        Line("lex6a", "LEX", "To allot new shares, directors need authority.", gap=0.25),
        Sfx("pop"),
        Line("lex6b", "LEX", "A private company with one class of shares lets directors "
             "allot unless the articles forbid it. Otherwise, authority comes from the "
             "articles, or an ordinary resolution, for up to five years.", gap=0.25),
        Sfx("pop"),
        Line("lex6c", "LEX", "Next, pre-emption rights. New ordinary shares issued for cash "
             "must first be offered to existing ordinary shareholders, in proportion to "
             "their holdings, for at least fourteen days.", gap=0.25),
        Sfx("pop"),
        Line("lex6d", "LEX", "Pre-emption rights can be disapplied by special resolution, "
             "and they do not apply to bonus shares, non-cash issues, or employee schemes.",
             gap=0.25),
        Sfx("pop"),
        Line("lex6e", "LEX", "Finally, a return of allotment goes to the registrar within "
             "one month.", gap=0.4),
        Line("kito6", "KITO", "So Nia and I get first chance to buy any new Safari Solar "
             "shares, so we keep our percentages."),
        Pause("hold", 1.4),
    ], spec={"tpl": "timeline", "bg": "studio", "heading": "Allotment step by step",
             "syl": "E1(c)", "cw": 310,
             "events": [{"at": "lex6a", "label": "Directors' authority",
                         "sub": "Articles or ordinary resolution", "icon": "key",
                         "color": "#0f8b8d"},
                        {"at": "lex6c", "label": "Pre-emption offer",
                         "sub": "Existing holders, pro rata, 14 days", "icon": "people",
                         "color": "#7768ae"},
                        {"at": "lex6d", "label": "Exceptions", "sub": "Disapplied, bonus, "
                                                                      "non-cash, employees",
                         "icon": "scissors", "color": "#f2a541"},
                        {"at": "lex6e", "label": "Return of allotment",
                         "sub": "Registrar within 1 month", "icon": "envelope",
                         "color": "#3bb273"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "KITO", "x": 1810, "s": 0.55, "y": 1120, "enter": "kito6"}]}),

    Scene("s7", "Rights issue or bonus issue?", "", [
        Pause("open", 1.0),
        Line("lex7a", "LEX", "A rights issue offers new shares to existing members, in "
             "proportion to their holdings, usually below market price. It raises new cash. "
             "Members who don't want them can often sell the rights.", gap=0.4),
        Line("lex7b", "LEX", "A bonus issue gives existing members free, fully paid shares, "
             "funded by turning reserves into share capital. No new cash comes in.",
             gap=0.4),
        Line("nia7", "NIA", "So a rights issue fills the bank account, and a bonus issue "
             "just reshuffles the balance sheet."),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio_purple", "heading": "Rights vs bonus issue",
             "syl": "E1(c)", "ts": 33,
             "cols": [{"title": "Rights issue", "icon": "moneybag", "color": "#3bb273",
                       "at": "lex7a",
                       "items": [{"at": ["lex7a", 0.5], "text": "Offered to existing "
                                                               "members, pro rata"},
                                 {"at": ["lex7a", 4.5], "text": "Usually below market "
                                                               "price"},
                                 {"at": ["lex7a", 6.5], "text": "Raises new cash",
                                  "good": True},
                                 {"at": ["lex7a", 8.5], "text": "Rights can often be sold"}]},
                      {"title": "Bonus issue", "icon": "gift", "color": "#7768ae",
                       "at": "lex7b",
                       "items": [{"at": ["lex7b", 0.5], "text": "Free, fully paid shares"},
                                 {"at": ["lex7b", 3.5], "text": "Reserves become share "
                                                               "capital"},
                                 {"at": ["lex7b", 6.5], "text": "No new cash", "bad": True}]}],
             "vs": True,
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia7"}]}),

    Scene("s8", "Discount and premium", "", [
        Pause("open", 1.0),
        Line("lex8a", "LEX", "Back to Kito's bargain. Shares cannot be allotted at a "
             "discount to their nominal value.", gap=0.3),
        Line("lex8b", "LEX", "In Ooregum Gold Mining against Roper, one pound shares issued "
             "for five shillings were invalid. The allottee must pay the discount, plus "
             "interest.", gap=0.4),
        Line("lex8c", "LEX", "Shares can be paid for in money or money's worth. A private "
             "company's directors value non-cash assets honestly. A public company needs an "
             "independent valuation, and cannot accept a promise of future work.", gap=0.4),
        Line("lex8d", "LEX", "Issuing above nominal value is fine. The excess goes to a "
             "share premium account, which is treated like capital.", gap=0.3),
        Line("lex8e", "LEX", "It can only be used to pay up bonus shares, or to write off "
             "the expenses and commission of that share issue.", gap=0.4),
        Line("kito8", "KITO", "Then we'll issue one dollar shares at a dollar fifty, and "
             "credit fifty cents to share premium!"),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio_red", "heading": "Discount vs premium",
             "syl": "E1(d)", "ts": 33,
             "cols": [{"title": "At a discount", "icon": "cross", "color": "#e4572e",
                       "at": "lex8a",
                       "items": [{"at": ["lex8a", 0.5], "text": "Not allowed below nominal",
                                  "bad": True},
                                 {"at": "lex8b", "text": "Ooregum v Roper (1892)"},
                                 {"at": ["lex8b", 4.5], "text": "Allottee pays the discount "
                                                               "+ interest"},
                                 {"at": "lex8c", "text": "plc non-cash: independent "
                                                         "valuation, no future-services "
                                                         "promise"}]},
                      {"title": "At a premium", "icon": "check", "color": "#3bb273",
                       "at": "lex8d",
                       "items": [{"at": ["lex8d", 0.5], "text": "Allowed above nominal",
                                  "good": True},
                                 {"at": ["lex8d", 2.5], "text": "Excess to share premium "
                                                               "account"},
                                 {"at": "lex8e", "text": "Uses: bonus shares · issue "
                                                         "expenses and commission"}]}],
             "vs": True,
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "KITO", "x": 1810, "s": 0.55, "y": 1120, "enter": "kito8",
                       "mood": "excited"}]}),

    quiz_scene("s9", "Quick check",
               "A company issues new ordinary shares for cash. Unless disapplied, who must be "
               "offered them first?",
               ["The directors", "Existing ordinary shareholders, pro rata",
                "Preference shareholders only", "The company's bank"], 1,
               "Quick check. New ordinary shares are issued for cash. Who must be offered them "
               "first?",
               "Existing ordinary shareholders, in proportion to their holdings.",
               syl="E1(c)"),

    quiz_scene("s10", "Quick check",
               "Which statement about a bonus issue is true?",
               ["It raises new cash", "It is funded by capitalising reserves",
                "It must be at a discount", "Only preference shareholders receive it"], 1,
               "And which statement about a bonus issue is true?",
               "It is funded by capitalising reserves.",
               think=4.0, syl="E1(c)"),

    recap_scene("s11", [
        ("Nominal, issued, called, paid, uncalled.", "Nominal · issued · called · paid"),
        ("Ordinary versus preference shares.", "Ordinary vs preference"),
        ("Varying class rights: seventy-five percent of the class.", "Class rights: 75% of "
                                                                     "class"),
        ("Pre-emption, rights issues and bonus issues.", "Pre-emption · rights · bonus"),
        ("No discount. Premium to share premium.", "No discount · share premium"),
    ], [
        Line("lex11", "LEX", "Next time, the other way to raise money: borrowing, "
             "debentures, and charges over the company's assets.", gap=0.3),
        Line("amara11", "AMARA", "That's where I come in!", gap=0.6),
    ], next_ep=19, next_title="Borrowing Power", next_icon="chain"),
]
