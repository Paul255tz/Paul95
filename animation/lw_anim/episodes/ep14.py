"""Episode 14 - Partners in Business.

Syllabus D2(a)-(e): partnership legislation (Partnership Act 1890, Limited
Partnerships Act 1907, Limited Liability Partnerships Act 2000, as used by the
ACCA syllabus), formation, authority of partners, liability for partnership
debts, and termination. Also partnership forms abroad: France, Islamic law and
Kenya. Setting: Nia and Kito start a side business, Safari Solar.
"""
from ._kit import (DISPLAY_NAMES, SERIES, VOICES, Line, Pause, Scene, Sfx,  # noqa: F401
                   quiz_scene, recap_scene, title_scene)

EPISODE = "Episode 14"
EPISODE_TITLE = "Partners in Business"
SLUG = "episode14_partners_in_business"

SCENES = [
    title_scene(14, EPISODE_TITLE, "Syllabus D2", ("people", "handshake")),

    Scene("s1", "Safari Solar", "", [
        Pause("open", 1.0),
        Line("kito1", "KITO", "Nia, let's sell solar lamps in Arusha on weekends. Fifty-fifty. "
             "No paperwork needed!", gap=0.4),
        Line("nia1", "NIA", "No paperwork... but are we a partnership?", gap=0.3),
        Line("lex1", "LEX", "Very likely. A partnership is the relationship between persons "
             "carrying on a business in common, with a view of profit. That is the "
             "definition in the English Partnership Act of 1890, which the exam uses.",
             gap=0.3),
        Line("lex1b", "LEX", "No formality is needed. If your arrangement fits the "
             "definition, the law treats you as partners, whatever you call yourselves."),
        Pause("hold", 1.2),
    ], spec={"tpl": "talk", "bg": "harbour", "syl": "D2(a)–(b)",
             "cast": [{"who": "KITO", "x": 1450, "y": 1030, "s": 0.95, "mood": "excited",
                       "talk_pose": "cheer"},
                      {"who": "NIA", "x": 960, "y": 1030, "s": 0.9, "mood": "thinking"},
                      {"who": "LEX", "x": 420, "y": 1030, "s": 0.88, "enter": "lex1",
                       "from": "left"}],
             "pops": [{"kind": "icon", "icon": "bulb", "x": 1200, "y": 280, "s": 1.1,
                       "at": ["kito1", 0.8], "until": "lex1", "label": "Safari Solar"},
                      {"kind": "card", "at": ["lex1", 1.0], "x": 1180, "y": 300, "w": 900,
                       "h": 240, "title": "Partnership Act 1890, s.1",
                       "body": "Persons carrying on a business in common with a view of "
                               "profit", "color": "#7768ae", "bs": 38}]}),

    Scene("s2", "Is it a partnership?", "", [
        Pause("open", 1.0),
        Line("lex2a", "LEX", "Break the definition down.", gap=0.3),
        Sfx("pop"),
        Line("lex2b", "LEX", "Persons: at least two. They can be individuals, or "
             "companies.", gap=0.25),
        Sfx("pop"),
        Line("lex2c", "LEX", "A business: any trade, occupation or profession.", gap=0.25),
        Sfx("pop"),
        Line("lex2d", "LEX", "Carried on: it should be continuing, not a one-off deal, "
             "although a single venture can sometimes count.", gap=0.25),
        Sfx("pop"),
        Line("lex2e", "LEX", "In common: run for the benefit of all the partners.", gap=0.25),
        Sfx("pop"),
        Line("lex2f", "LEX", "With a view of profit. Sharing profits is strong evidence of a "
             "partnership, but merely sharing gross takings is not.", gap=0.4),
        Line("nia2", "NIA", "And in England, a partnership is not a separate legal person. "
             "The partners are the firm."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "white", "heading": "The definition, piece by piece",
             "syl": "D2(b)", "row": 112, "ts": 38,
             "items": [{"at": "lex2b", "text": "Persons", "sub": "Two or more: people or "
                                                                 "companies",
                        "icon": "people", "color": "#0f8b8d"},
                       {"at": "lex2c", "text": "A business", "sub": "Trade, occupation or "
                                                                    "profession",
                        "icon": "company", "color": "#2b86c5"},
                       {"at": "lex2d", "text": "Carried on", "sub": "Continuing, not usually "
                                                                    "a one-off",
                        "icon": "clock", "color": "#7768ae"},
                       {"at": "lex2e", "text": "In common", "sub": "For all the partners",
                        "icon": "handshake", "color": "#f2a541"},
                       {"at": "lex2f", "text": "With a view of profit", "sub": "Sharing "
                                                                               "profits = "
                                                                               "strong "
                                                                               "evidence",
                        "icon": "chart", "color": "#3bb273"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia2"}]}),

    Scene("s3", "The default rules", "", [
        Pause("open", 1.0),
        Line("lex3a", "LEX", "Partners can agree almost anything. Where they haven't, the "
             "Act fills the gaps.", gap=0.3),
        Sfx("pop"),
        Line("lex3b", "LEX", "Capital and profits are shared equally, and losses too.",
             gap=0.25),
        Sfx("pop"),
        Line("lex3c", "LEX", "No interest on capital, but five percent a year on loans a "
             "partner makes beyond agreed capital.", gap=0.25),
        Sfx("pop"),
        Line("lex3d", "LEX", "Every partner may take part in management, but no partner is "
             "entitled to a salary.", gap=0.25),
        Sfx("pop"),
        Line("lex3e", "LEX", "A partner is indemnified for liabilities properly incurred for "
             "the firm.", gap=0.25),
        Sfx("pop"),
        Line("lex3f", "LEX", "Ordinary matters are decided by majority. But changing the "
             "business, or admitting a new partner, needs everyone's consent.", gap=0.25),
        Sfx("pop"),
        Line("lex3g", "LEX", "The books are open to every partner. No expulsion unless the "
             "agreement allows it. And secret profits, or profits from a competing "
             "business, must be handed over to the firm.", gap=0.4),
        Line("kito3", "KITO", "Fifty-fifty works for me. But no salary? Hmm."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "heading": "Default rules (1890 Act)",
             "syl": "D2(a)", "row": 100, "ts": 36,
             "items": [{"at": "lex3b", "text": "Equal shares of capital and profit",
                        "icon": "pie", "color": "#0f8b8d"},
                       {"at": "lex3c", "text": "5% interest on advances, none on capital",
                        "icon": "percent", "color": "#2b86c5"},
                       {"at": "lex3d", "text": "All manage · no salary", "icon": "people",
                        "color": "#7768ae"},
                       {"at": "lex3e", "text": "Indemnity for firm liabilities",
                        "icon": "shield", "color": "#3bb273"},
                       {"at": "lex3f", "text": "Majority, but unanimity for new partner or "
                                               "business",
                        "icon": "ballot", "color": "#f2a541"},
                       {"at": "lex3g", "text": "Books open · no expulsion · no secret profits",
                        "icon": "book", "color": "#e4572e"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "KITO", "x": 1810, "s": 0.55, "y": 1120, "enter": "kito3",
                       "mood": "thinking"}]}),

    Scene("s4", "A partner's authority", "", [
        Pause("open", 1.0),
        Line("lex4a", "LEX", "Every partner is an agent of the firm, and of the other "
             "partners, for carrying on business of the kind the firm does, in the usual "
             "way.", gap=0.3),
        Line("lex4b", "LEX", "So the firm is bound, unless the partner had no authority, and "
             "the third party knew that, or did not know or believe he was a partner.",
             gap=0.4),
        Line("lex4c", "LEX", "A partner using the firm's credit for private purposes does "
             "not bind the firm, unless the others authorised it.", gap=0.3),
        Line("lex4d", "LEX", "And anyone who lets themselves be held out as a partner is "
             "liable, like a partner, to those who gave credit on that basis.", gap=0.4),
        Line("nia4", "NIA", "So if Kito orders lamps for Safari Solar, I'm bound too, even if "
             "we agreed only I would order."),
        Pause("hold", 1.4),
    ], spec={"tpl": "flow", "bg": "studio_teal", "heading": "Partners as agents (ss 5–8, 14)",
             "syl": "D2(c)",
             "nodes": [{"id": "k", "x": 700, "y": 320, "label": "Kito orders lamps",
                        "icon": "person", "color": "#f2a541", "at": "lex4a", "w": 280},
                       {"id": "f", "x": 1150, "y": 650, "label": "Firm bound (and Nia)",
                        "icon": "people", "color": "#0f8b8d", "at": ["lex4a", 3.0], "w": 300},
                       {"id": "s", "x": 1600, "y": 320, "label": "Supplier", "icon": "factory",
                        "color": "#7768ae", "at": ["lex4a", 1.5], "w": 260}],
             "edges": [{"from": "k", "to": "s", "at": ["lex4a", 1.5], "label": "usual business"},
                       {"from": "s", "to": "f", "at": ["lex4a", 3.0], "label": "can sue",
                        "color": "#e4572e"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia4"}],
             "pops": [{"kind": "card", "at": "lex4b", "until": "lex4c", "x": 1150, "y": 470,
                       "w": 900, "h": 280, "title": "Not bound if…",
                       "body": "No authority AND the third party knew it, or didn't know he "
                               "was a partner", "color": "#e4572e", "dim": True, "bs": 38},
                      {"kind": "chip", "at": "lex4c", "x": 1150, "y": 880,
                       "text": "Private use of the firm's credit: not binding",
                       "color": "#1f3a5f", "size": 32},
                      {"kind": "chip", "at": "lex4d", "x": 1150, "y": 960,
                       "text": "Held out as a partner? Liable as one",
                       "color": "#e4572e", "size": 32}]}),

    Scene("s5", "Liability for the firm's debts", "", [
        Pause("open", 1.0),
        Line("lex5a", "LEX", "In an ordinary partnership, liability is unlimited. Partners "
             "are jointly liable for the firm's debts, and jointly and severally liable for "
             "its wrongs.", gap=0.3),
        Line("lex5b", "LEX", "In practice, a creditor can pursue any partner for the whole "
             "debt, and that partner claims a contribution from the others.", gap=0.4),
        Sfx("pop"),
        Line("lex5c", "LEX", "A new partner is not liable for debts incurred before joining.",
             gap=0.25),
        Sfx("pop"),
        Line("lex5d", "LEX", "A retiring partner stays liable for debts incurred while a "
             "partner.", gap=0.25),
        Sfx("pop"),
        Line("lex5e", "LEX", "And for debts incurred after retiring, unless notice was given: "
             "actual notice to existing customers, and a public notice in the Gazette for "
             "everyone else.", gap=0.25),
        Sfx("pop"),
        Line("lex5f", "LEX", "A retiring partner can be released from old debts by "
             "novation, a new agreement with the creditor."),
        Pause("hold", 1.4),
    ], spec={"tpl": "timeline", "bg": "studio", "heading": "Who is liable, and when?",
             "syl": "D2(d)", "cw": 300,
             "events": [{"at": "lex5a", "label": "Unlimited liability", "sub": "Jointly for "
                                                                             "debts, jointly "
                                                                             "and severally "
                                                                             "for wrongs",
                         "icon": "warning", "color": "#e4572e"},
                        {"at": "lex5c", "label": "Incoming partner", "sub": "Not liable for "
                                                                            "earlier debts",
                         "icon": "door", "color": "#3bb273"},
                        {"at": "lex5d", "label": "Retiring partner", "sub": "Liable for debts "
                                                                            "while a partner",
                         "icon": "person", "color": "#f2a541"},
                        {"at": "lex5e", "label": "Give notice!", "sub": "Customers told · "
                                                                        "Gazette notice",
                         "icon": "megaphone", "color": "#7768ae"},
                        {"at": "lex5f", "label": "Novation", "sub": "Creditor agrees to "
                                                                    "release",
                         "icon": "contract", "color": "#0f8b8d"}],
             "cast": [{"who": "LEX", "x": 250}]}),

    Scene("s6", "Ending a partnership", "", [
        Pause("open", 1.0),
        Line("lex6a", "LEX", "Unless agreed otherwise, a partnership is dissolved "
             "automatically when its fixed term ends, its single venture is complete, a "
             "partner gives notice in a partnership at will, or a partner dies or becomes "
             "bankrupt.", gap=0.3),
        Line("lex6b", "LEX", "Also if the business becomes illegal. And if a partner's share "
             "is charged for a private debt, the others may choose to dissolve.", gap=0.4),
        Line("lex6c", "LEX", "A court may order dissolution for a partner's permanent "
             "incapacity, conduct prejudicial to the business, persistent breach of the "
             "agreement, when the business can only run at a loss, or when it is just and "
             "equitable.", gap=0.4),
        Line("nia6", "NIA", "So the first group happens automatically, but the second group "
             "needs a judge."),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio_purple", "heading": "Dissolution (ss 32–35)",
             "syl": "D2(e)", "ts": 33,
             "cols": [{"title": "Automatic", "icon": "clock", "color": "#0f8b8d",
                       "at": "lex6a",
                       "items": [{"at": ["lex6a", 2.5], "text": "Fixed term expires"},
                                 {"at": ["lex6a", 4.0], "text": "Single venture completed"},
                                 {"at": ["lex6a", 5.6], "text": "Notice (partnership at "
                                                               "will)"},
                                 {"at": ["lex6a", 8.5], "text": "Death or bankruptcy of a "
                                                               "partner"},
                                 {"at": "lex6b", "text": "Business becomes illegal"},
                                 {"at": ["lex6b", 2.5], "text": "Share charged: others may "
                                                               "dissolve"}]},
                      {"title": "By the court", "icon": "court", "color": "#7768ae",
                       "at": "lex6c",
                       "items": [{"at": ["lex6c", 1.5], "text": "Permanent incapacity"},
                                 {"at": ["lex6c", 3.5], "text": "Prejudicial conduct"},
                                 {"at": ["lex6c", 5.5], "text": "Persistent breach"},
                                 {"at": ["lex6c", 7.5], "text": "Business only at a loss"},
                                 {"at": ["lex6c", 9.5], "text": "Just and equitable"}]}],
             "vs": True,
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia6"}]}),

    Scene("s7", "Sharing out after dissolution", "", [
        Pause("open", 1.0),
        Line("lex7a", "LEX", "On dissolution, the partners have authority to wind up the "
             "firm. Then the assets are paid out in this order.", gap=0.3),
        Sfx("pop"),
        Line("lex7b", "LEX", "First, outside creditors.", gap=0.25),
        Sfx("pop"),
        Line("lex7c", "LEX", "Second, partners' loans and advances to the firm.", gap=0.25),
        Sfx("pop"),
        Line("lex7d", "LEX", "Third, each partner's capital.", gap=0.25),
        Sfx("pop"),
        Line("lex7e", "LEX", "Fourth, anything left is shared in the profit-sharing ratio.",
             gap=0.4),
        Line("lex7f", "LEX", "Losses are met from profits, then capital, and then by the "
             "partners personally. If one partner cannot pay a capital deficiency, the "
             "others bear it in proportion to their capital, under Garner against Murray.",
             gap=0.3),
        Sfx("sparkle"),
        Pause("pour", 4.6),
    ], spec={"tpl": "stack", "bg": "studio_teal", "heading": "Order of payment (s 44)",
             "syl": "D2(e)",
             "tiers": [{"at": "lex7b", "label": "Outside creditors", "color": "#e4572e"},
                       {"at": "lex7c", "label": "Partners' loans and advances",
                        "color": "#f2a541"},
                       {"at": "lex7d", "label": "Partners' capital", "color": "#7768ae"},
                       {"at": "lex7e", "label": "Surplus in profit-sharing ratio",
                        "color": "#3bb273"}],
             "pour": {"at": "pour", "fills": [1, 1, 0.55, 0], "label": "Assets realised"},
             "top": 250, "bottom": 760,
             "cast": [{"who": "LEX", "x": 250}],
             "pops": [{"kind": "chip", "at": "lex7f", "x": 1190, "y": 940,
                       "text": "Garner v Murray: deficiency shared by capital ratio",
                       "color": "#1f3a5f", "size": 32}]}),

    Scene("s8", "Limited and LLP", "", [
        Pause("open", 1.0),
        Line("lex8a", "LEX", "Two variations limit liability.", gap=0.3),
        Line("lex8b", "LEX", "A limited partnership, under the 1907 Act, needs at least one "
             "general partner with unlimited liability, and at least one limited partner. "
             "It must be registered.", gap=0.3),
        Line("lex8c", "LEX", "The limited partner's liability is limited to its capital. But "
             "it must not take part in management, or it loses that protection, and it "
             "cannot withdraw its capital.", gap=0.4),
        Line("lex8d", "LEX", "A limited liability partnership, under the 2000 Act, is "
             "different. It is a separate legal person, registered like a company.", gap=0.3),
        Line("lex8e", "LEX", "Members' liability is limited. It must file accounts, usually "
             "audited, and the rules on fraudulent and wrongful trading still apply.",
             gap=0.4),
        Line("kito8", "KITO", "And Kenya has its own Partnerships Act, and a Limited "
             "Liability Partnerships Act, too!"),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio", "heading": "General · limited · LLP",
             "syl": "D2(a)", "ts": 31,
             "cols": [{"title": "General", "icon": "people", "color": "#e4572e",
                       "at": "lex8a",
                       "items": [{"at": ["lex8a", 0.5], "text": "Unlimited liability"},
                                 {"at": ["lex8a", 1.0], "text": "No separate personality "
                                                               "(England)"},
                                 {"at": ["lex8a", 1.5], "text": "No formality needed"}]},
                      {"title": "Limited (1907)", "icon": "shield", "color": "#f2a541",
                       "at": "lex8b",
                       "items": [{"at": ["lex8b", 1.5], "text": "1+ general, 1+ limited "
                                                               "partner"},
                                 {"at": ["lex8b", 7.0], "text": "Must register"},
                                 {"at": "lex8c", "text": "Limited partner: no management"},
                                 {"at": ["lex8c", 6.0], "text": "Can't withdraw capital"}]},
                      {"title": "LLP (2000)", "icon": "company", "color": "#0f8b8d",
                       "at": "lex8d",
                       "items": [{"at": ["lex8d", 1.5], "text": "Separate legal person"},
                                 {"at": ["lex8d", 3.5], "text": "Registered like a company"},
                                 {"at": "lex8e", "text": "Members' liability limited"},
                                 {"at": ["lex8e", 2.5], "text": "Files accounts"},
                                 {"at": ["lex8e", 5.0], "text": "Wrongful / fraudulent "
                                                               "trading apply"}]}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "KITO", "x": 1810, "s": 0.55, "y": 1120, "enter": "kito8"}]}),

    Scene("s9", "Partnerships around the world", "", [
        Pause("open", 1.0),
        Line("lex9a", "LEX", "Other systems have their own versions.", gap=0.3),
        Sfx("pop"),
        Line("lex9b", "LEX", "In France, a société en nom collectif works like a general "
             "partnership.", say="In France, a soe-see-ay-tay on nom koh-lek-teef works "
             "like a general partnership.", gap=0.25),
        Sfx("pop"),
        Line("lex9c", "LEX", "And a société en commandite simple is like a limited "
             "partnership.", say="And a soe-see-ay-tay on koh-mon-deet sampl is like a "
             "limited partnership.", gap=0.25),
        Sfx("pop"),
        Line("lex9d", "LEX", "Islamic law recognises musharakah, where partners pool capital "
             "and share profits, losses and decisions.",
             say="Islamic law recognises moo-shah-rah-kah, where partners pool capital and "
                 "share profits, losses and decisions.", gap=0.25),
        Sfx("pop"),
        Line("lex9e", "LEX", "Mudarabah, where one partner provides capital and the other "
             "manages, sharing profit instead of paying interest.",
             say="Moo-dah-rah-bah, where one partner provides capital and the other manages, "
                 "sharing profit instead of paying interest.", gap=0.25),
        Sfx("pop"),
        Line("lex9f", "LEX", "And shirkah al-inan, where partners invest and share profits, "
             "but are not liable for each other's debts.",
             say="And shir-kah al ee-nan, where partners invest and share profits, but are "
                 "not liable for each other's debts.", gap=0.4),
        Line("nia9", "NIA", "Mudarabah sounds like a limited partnership, but without "
             "interest.", say="Moo-dah-rah-bah sounds like a limited partnership, but "
             "without interest."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "white", "layout": "grid", "cols": 3,
             "heading": "Partnerships abroad", "syl": "D2", "cell_h": 300, "ts": 34,
             "items": [{"at": "lex9b", "text": "Société en nom collectif",
                        "sub": "France · like a general partnership", "icon": "flag",
                        "color": "#2b86c5"},
                       {"at": "lex9c", "text": "Société en commandite simple",
                        "sub": "France · like a limited partnership", "icon": "flag",
                        "color": "#7768ae"},
                       {"at": "lex9d", "text": "Musharakah", "sub": "Pool capital · share "
                                                                    "profit, loss, decisions",
                        "icon": "handshake", "color": "#3bb273"},
                       {"at": "lex9e", "text": "Mudarabah", "sub": "One funds, one manages · "
                                                                   "profit share",
                        "icon": "moneybag", "color": "#f2a541"},
                       {"at": "lex9f", "text": "Shirkah al-inan", "sub": "Invest, share "
                                                                         "profits · no "
                                                                         "liability for "
                                                                         "others",
                        "icon": "people", "color": "#e4572e"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia9"}]}),

    quiz_scene("s10", "Quick check",
               "With no partnership agreement, how are profits shared?",
               ["In proportion to capital", "Equally", "By hours worked",
                "As the senior partner decides"], 1,
               "Quick check. With no partnership agreement, how are profits shared?",
               "Equally.",
               why="And there is no salary, and no interest on capital",
               syl="D2(a)"),

    quiz_scene("s11", "Quick check",
               "A limited partner starts managing the firm's business. What is the risk?",
               ["Nothing changes", "It may lose its limited liability",
                "The firm becomes an LLP", "It must leave the firm"], 1,
               "And if a limited partner starts managing the business, what is the risk?",
               "It may lose its limited liability.",
               think=4.0, syl="D2(a)"),

    recap_scene("s12", [
        ("Business in common with a view of profit.", "Business in common, view of profit"),
        ("Default rules: equal shares, no salary.", "Equal shares · no salary"),
        ("Every partner is an agent of the firm.", "Partner = agent of firm"),
        ("Retiring? Give notice.", "Retiring: give notice"),
        ("Limited partnership versus LLP.", "LP vs LLP"),
    ], [
        Line("lex12", "LEX", "Next time, the biggest idea in company law: a company is a "
             "person, separate from its owners.", gap=0.3),
        Line("kito12", "KITO", "A company is a person? Does it get a birthday?", gap=0.3),
        Line("lex12b", "LEX", "In a way, yes. Its date of incorporation.", gap=0.6),
    ], next_ep=15, next_title="Behind the Corporate Veil", next_icon="veil"),
]
