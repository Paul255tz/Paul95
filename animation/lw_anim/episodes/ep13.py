"""Episode 13 - The Agent's Authority.

Syllabus D1(a)-(d): the role of the agent (with partners and directors as
examples), formation of agency, the agent's authority, and the liability of
principal and agent. Setting: Kito appoints a sales agent in Kampala,
Uganda. (The case law shown is English, as used
by the ACCA syllabus; East African courts apply the same common-law principles.)
"""
from ._kit import (DISPLAY_NAMES, SERIES, VOICES, Line, Pause, Scene, Sfx,  # noqa: F401
                   quiz_scene, recap_scene, title_scene)

EPISODE = "Episode 13"
EPISODE_TITLE = "The Agent's Authority"
SLUG = "episode13_the_agents_authority"

SCENES = [
    title_scene(13, EPISODE_TITLE, "Syllabus D1", ("handshake", "key")),

    Scene("s1", "An agent in Kampala", "", [
        Pause("open", 1.0),
        Line("kito1", "KITO", "I've hired an agent in Kampala to sign up shops for our kits. "
             "If she signs a deal, am I bound?", gap=0.4),
        Line("lex1", "LEX", "If she acts within her authority, yes. That is the whole point "
             "of agency.", gap=0.3),
        Line("lex1b", "LEX", "An agent's job is to bring the principal into a legal "
             "relationship with a third party. The contract is between the principal and the "
             "third party. The agent usually drops out."),
        Pause("hold", 1.2),
    ], spec={"tpl": "talk", "bg": "office", "syl": "D1(a)",
             "cast": [{"who": "KITO", "x": 1450, "y": 1030, "s": 0.95, "mood": "thinking"},
                      {"who": "NIA", "x": 960, "y": 1030, "s": 0.9},
                      {"who": "LEX", "x": 420, "y": 1030, "s": 0.88, "enter": "lex1",
                       "from": "left"}],
             "pops": [{"kind": "icon", "icon": "flag", "x": 1200, "y": 280, "s": 1.0,
                       "at": ["kito1", 1.0], "until": "lex1b", "label": "Kampala agent",
                       "color": "#f2a541"}]}),

    Scene("s2", "The agency triangle", "", [
        Pause("open", 1.0),
        Line("lex2a", "LEX", "Picture a triangle. The principal appoints the agent.",
             gap=0.3),
        Line("lex2b", "LEX", "The agent deals with the third party.", gap=0.3),
        Line("lex2c", "LEX", "And the resulting contract binds the principal and the third "
             "party directly.", gap=0.4),
        Line("lex2d", "LEX", "Agents are everywhere: employees buying supplies, brokers, "
             "estate agents. Two matter most in this exam.", gap=0.3),
        Sfx("pop"),
        Line("lex2e", "LEX", "Every partner is an agent of the firm and of the other partners, "
             "for the firm's usual business.", gap=0.25),
        Sfx("pop"),
        Line("lex2f", "LEX", "And company directors act as agents of the company."),
        Pause("hold", 1.4),
    ], spec={"tpl": "flow", "bg": "studio_teal", "heading": "Principal · agent · third party",
             "syl": "D1(a)",
             "nodes": [{"id": "p", "x": 760, "y": 300, "label": "Principal (SafariTech)",
                        "icon": "company", "color": "#0f8b8d", "at": "lex2a", "w": 300},
                       {"id": "a", "x": 1150, "y": 700, "label": "Agent (Kampala)",
                        "icon": "person", "color": "#f2a541", "at": ["lex2a", 1.5], "w": 280},
                       {"id": "t", "x": 1540, "y": 300, "label": "Third party (shop)",
                        "icon": "house", "color": "#7768ae", "at": "lex2b", "w": 280}],
             "edges": [{"from": "p", "to": "a", "at": ["lex2a", 1.5], "label": "appoints"},
                       {"from": "a", "to": "t", "at": "lex2b", "label": "negotiates"},
                       {"from": "p", "to": "t", "at": "lex2c", "label": "CONTRACT",
                        "color": "#3bb273", "lcolor": "#3bb273", "ls": 32}],
             "cast": [{"who": "LEX", "x": 250}],
             "pops": [{"kind": "chip", "at": "lex2e", "x": 1150, "y": 920,
                       "text": "Partners: agents of the firm", "color": "#7768ae", "size": 34},
                      {"kind": "chip", "at": "lex2f", "x": 1150, "y": 1000,
                       "text": "Directors: agents of the company", "color": "#1f3a5f",
                       "size": 34}]}),

    Scene("s3", "How agency is created", "", [
        Pause("open", 1.0),
        Line("lex3a", "LEX", "Agency can arise in five ways.", gap=0.3),
        Sfx("pop"),
        Line("lex3b", "LEX", "By express agreement, written or oral. A power of attorney, "
             "giving wide authority, must be made formally in writing.", gap=0.25),
        Sfx("pop"),
        Line("lex3c", "LEX", "By implied agreement, from the parties' conduct or "
             "relationship.", gap=0.25),
        Sfx("pop"),
        Line("lex3d", "LEX", "By ratification, where the principal later adopts a contract "
             "made without authority. It works backwards, as if authorised all along.",
             gap=0.25),
        Sfx("pop"),
        Line("lex3e", "LEX", "By estoppel, where the principal holds someone out as its "
             "agent, and cannot later deny it.", gap=0.25),
        Sfx("pop"),
        Line("lex3f", "LEX", "And by necessity, in a genuine emergency, when the owner of "
             "goods cannot be contacted, and someone acts in good faith to protect them.",
             gap=0.4),
        Line("nia3", "NIA", "Like a carrier selling perishable fruit before it rots, when "
             "the owner can't be reached."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "heading": "Creating agency", "syl": "D1(b)",
             "row": 116, "ts": 40,
             "items": [{"at": "lex3b", "text": "Express agreement", "sub": "Power of "
                                                                          "attorney: formal "
                                                                          "and written",
                        "icon": "contract", "color": "#0f8b8d"},
                       {"at": "lex3c", "text": "Implied agreement", "sub": "From conduct or "
                                                                          "relationship",
                        "icon": "handshake", "color": "#2b86c5"},
                       {"at": "lex3d", "text": "Ratification", "sub": "Adopted later, "
                                                                     "works backwards",
                        "icon": "stamp", "color": "#7768ae"},
                       {"at": "lex3e", "text": "Estoppel", "sub": "Held out as agent",
                        "icon": "megaphone", "color": "#f2a541"},
                       {"at": "lex3f", "text": "Necessity", "sub": "Emergency, owner "
                                                                  "unreachable, good faith",
                        "icon": "warning", "color": "#e4572e"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia3"}]}),

    Scene("s4", "Ratification's limits", "", [
        Pause("open", 1.0),
        Line("lex4a", "LEX", "Ratification has strict conditions.", gap=0.3),
        Line("lex4b", "LEX", "The agent must have claimed to act for that principal. The "
             "principal must have existed, and had capacity, when the contract was made.",
             gap=0.3),
        Line("lex4c", "LEX", "And the principal must ratify the whole contract, within a "
             "reasonable time.", gap=0.4),
        Line("lex4d", "LEX", "In Kelner against Baxter, promoters bought wine for a hotel "
             "company that had not yet been formed. The company later tried to ratify.",
             gap=0.3),
        Line("lex4e", "LEX", "It could not, because it did not exist when the contract was "
             "made. The promoters were personally liable to pay.", gap=0.4),
        Sfx("sparkle"),
        Pause("stamp", 1.2),
        Line("kito4", "KITO", "So I'll register SafariTech Uganda before my agent signs "
             "anything in its name!"),
        Pause("hold", 1.2),
    ], spec={"tpl": "case", "bg": "office", "name": "Kelner v Baxter",
             "year": "England · 1866", "syl": "D1(b)",
             "rows": [{"at": "lex4b", "label": "Rule", "text": "Principal must exist and have "
                                                               "capacity when the contract "
                                                               "is made",
                       "color": "#0f8b8d"},
                      {"at": "lex4d", "label": "Facts", "text": "Promoters bought wine for a "
                                                                "company not yet formed",
                       "color": "#7768ae"},
                      {"at": "lex4e", "label": "Held", "text": "No ratification possible · "
                                                               "promoters personally liable",
                       "color": "#e4572e"}],
             "stamp": {"at": "stamp", "text": "CANNOT RATIFY", "color": "#e4572e"},
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "KITO", "x": 1810, "s": 0.55, "y": 1120, "enter": "kito4"}]}),

    Scene("s5", "Types of authority", "", [
        Pause("open", 1.0),
        Line("lex5a", "LEX", "An agent's authority comes in three kinds.", gap=0.3),
        Sfx("pop"),
        Line("lex5b", "LEX", "Express actual authority: what the principal actually said the "
             "agent may do.", gap=0.25),
        Sfx("pop"),
        Line("lex5c", "LEX", "Implied actual authority: what is incidental to that, or usual "
             "for an agent in that position, unless the principal has forbidden it.",
             gap=0.25),
        Sfx("pop"),
        Line("lex5d", "LEX", "And apparent, or ostensible, authority: what the principal "
             "has led the third party to believe the agent may do, even if it was never "
             "actually given.", gap=0.4),
        Line("lex5e", "LEX", "Apparent authority needs three things. A representation by the "
             "principal, not by the agent. Reliance on it by the third party. And the third "
             "party acting on it.", gap=0.3),
        Line("nia5", "NIA", "So if Kito tells shops that the agent can sign deals of any "
             "size, SafariTech is bound, even if he privately capped her at ten thousand "
             "dollars."),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio", "heading": "Authority of the agent",
             "syl": "D1(c)", "ts": 33,
             "cols": [{"title": "Express", "icon": "contract", "color": "#0f8b8d",
                       "at": "lex5b",
                       "items": [{"at": ["lex5b", 0.5], "text": "What the principal actually "
                                                               "said"},
                                 {"at": ["lex5b", 2.5], "text": "Written or oral"}]},
                      {"title": "Implied", "icon": "bulb", "color": "#7768ae", "at": "lex5c",
                       "items": [{"at": ["lex5c", 0.5], "text": "Incidental to the task"},
                                 {"at": ["lex5c", 2.5], "text": "Usual for that position"},
                                 {"at": ["lex5c", 5.0], "text": "Unless forbidden"}]},
                      {"title": "Apparent", "icon": "eye", "color": "#e4572e", "at": "lex5d",
                       "items": [{"at": ["lex5d", 0.8], "text": "Principal's representation"},
                                 {"at": ["lex5e", 3.0], "text": "Made by the principal, not "
                                                               "the agent"},
                                 {"at": ["lex5e", 5.5], "text": "Third party relied on it"},
                                 {"at": ["lex5e", 7.5], "text": "And acted on it"}]}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia5"}]}),

    Scene("s6", "Apparent authority in action", "", [
        Pause("open", 1.0),
        Line("lex6a", "LEX", "In Freeman and Lockyer against Buckhurst Park Properties, a "
             "director acted as if he were the managing director, and the board knew and let "
             "him.", gap=0.3),
        Line("lex6b", "LEX", "He hired architects for the company. The company refused to "
             "pay, saying he had never been appointed.", gap=0.3),
        Line("lex6c", "LEX", "The court held the company liable. By allowing him to act as "
             "managing director, it represented that he had that authority.", gap=0.4),
        Sfx("sparkle"),
        Pause("stamp", 1.2),
        Line("lex6d", "LEX", "Compare Hely-Hutchinson against Brayhead. A chairman acting as "
             "chief executive had implied actual authority, from the board's acceptance of "
             "his role."),
        Pause("hold", 1.4),
    ], spec={"tpl": "case", "bg": "boardroom",
             "name": "Freeman & Lockyer v Buckhurst Park",
             "year": "Court of Appeal, England · 1964", "syl": "D1(c)",
             "rows": [{"at": "lex6a", "label": "Facts", "text": "Director acted as MD with "
                                                                "the board's knowledge",
                       "color": "#7768ae"},
                      {"at": "lex6b", "label": "Issue", "text": "He hired architects; company "
                                                                "refused to pay",
                       "color": "#f2a541"},
                      {"at": "lex6c", "label": "Held", "text": "Company bound by his apparent "
                                                               "authority",
                       "color": "#3bb273"}],
             "stamp": {"at": "stamp", "text": "COMPANY LIABLE", "color": "#3bb273"},
             "cast": [{"who": "LEX", "x": 250}],
             "pops": [{"kind": "chip", "at": "lex6d", "x": 1200, "y": 990,
                       "text": "Hely-Hutchinson v Brayhead (1968): implied actual authority",
                       "color": "#1f3a5f", "size": 30}]}),

    Scene("s7", "Who is liable?", "", [
        Pause("open", 1.0),
        Line("lex7a", "LEX", "When an agent acts within actual or apparent authority, the "
             "principal is liable on the contract, and the agent usually cannot sue or be "
             "sued on it.", gap=0.4),
        Line("lex7b", "LEX", "But the agent can be personally liable in some cases.",
             gap=0.25),
        Sfx("pop"),
        Line("lex7c", "LEX", "If it acted without authority, it is liable for breach of "
             "warranty of authority, as in Collen against Wright.", gap=0.25),
        Sfx("pop"),
        Line("lex7d", "LEX", "If it hid the principal's existence, the third party may sue "
             "the agent, or the principal once discovered.", gap=0.25),
        Sfx("pop"),
        Line("lex7e", "LEX", "If the principal did not exist, as with pre-incorporation "
             "contracts.", gap=0.25),
        Sfx("pop"),
        Line("lex7f", "LEX", "Or if trade custom, or the form of the contract, makes the "
             "agent liable.", gap=0.4),
        Line("lex7g", "LEX", "And an agency ends by agreement, by revocation, or "
             "automatically on death, insanity, or the principal's bankruptcy. But tell "
             "third parties, or apparent authority may linger."),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio_purple", "heading": "Liability of principal and "
                                                                 "agent",
             "syl": "D1(d)", "ts": 33,
             "cols": [{"title": "Principal liable", "icon": "company", "color": "#0f8b8d",
                       "at": "lex7a",
                       "items": [{"at": ["lex7a", 0.5], "text": "Agent within actual "
                                                               "authority"},
                                 {"at": ["lex7a", 2.5], "text": "Or within apparent "
                                                               "authority"},
                                 {"at": ["lex7a", 5.0], "text": "Agent drops out of the "
                                                               "contract"}]},
                      {"title": "Agent personally liable", "icon": "person",
                       "color": "#e4572e", "at": "lex7b",
                       "items": [{"at": "lex7c", "text": "Breach of warranty of authority "
                                                         "(Collen v Wright)"},
                                 {"at": "lex7d", "text": "Principal undisclosed"},
                                 {"at": "lex7e", "text": "Principal did not exist"},
                                 {"at": "lex7f", "text": "Trade custom or contract form"}]}],
             "vs": True,
             "cast": [{"who": "LEX", "x": 250}],
             "pops": [{"kind": "card", "at": "lex7g", "x": 1180, "y": 470, "w": 960, "h": 300,
                       "title": "Ending an agency",
                       "body": "Agreement · revocation · death · insanity · principal's "
                               "bankruptcy. Notify third parties!", "color": "#1f3a5f",
                       "dim": True, "bs": 36}]}),

    quiz_scene("s8", "Quick check",
               "For apparent authority, who must make the representation that the agent has "
               "authority?",
               ["The agent", "The principal", "The third party", "Any independent witness"],
               1,
               "Quick check. For apparent authority, who must make the representation that "
               "the agent has authority?",
               "The principal.",
               why=("Freeman & Lockyer: the company's conduct created the representation",
                    "In Freeman and Lockyer, it was the company's own conduct that created "
                    "the representation."),
               syl="D1(c)"),

    quiz_scene("s9", "Quick check",
               "Why could the company in Kelner v Baxter not ratify the contract?",
               ["The price was too high", "It did not exist when the contract was made",
                "The agent was a minor", "Wine contracts need to be in writing"], 1,
               "And why could the company in Kelner against Baxter not ratify?",
               "It did not exist when the contract was made.",
               think=4.0, syl="D1(b)"),

    recap_scene("s10", [
        ("Principal, agent, third party.", "Principal · agent · third party"),
        ("Five ways to create agency.", "Express · implied · ratify · estoppel · necessity"),
        ("Ratify only if the principal existed.", "Ratify: principal must exist"),
        ("Express, implied and apparent authority.", "Express · implied · apparent"),
        ("Agent liable for breach of warranty of authority.", "Warranty of authority"),
    ], [
        Line("lex10", "LEX", "Next time: partnerships, where every partner is both a principal "
             "and an agent.", gap=0.3),
        Line("kito10", "KITO", "Nia, how would you like to be my partner?", gap=0.3),
        Line("nia10", "NIA", "Let's watch the next episode first!", gap=0.6),
    ], next_ep=14, next_title="Partners in Business", next_icon="people"),
]
