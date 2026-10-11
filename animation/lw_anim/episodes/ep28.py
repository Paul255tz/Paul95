"""Episode 28 - Dirty Money.

Syllabus H1(c)(i)-(v): the nature and legal control of money laundering
(UK Proceeds of Crime Act 2002 and Money Laundering Regulations 2017 model),
including risk management practices, internal controls, customer due
diligence, reliance and record keeping, and the monitoring and internal
communication of policies. Tanzania (Anti-Money Laundering Act, Financial
Intelligence Unit) and Kenya (Proceeds of Crime and Anti-Money Laundering Act,
Financial Reporting Centre) follow the FATF standards too. Setting: a mystery
customer offers SafariTech a large cash prepayment.
"""
from ._kit import (DISPLAY_NAMES, SERIES, VOICES, Line, Pause, Scene, Sfx,  # noqa: F401
                   quiz_scene, recap_scene, title_scene)

EPISODE = "Episode 28"
EPISODE_TITLE = "Dirty Money"
SLUG = "episode28_dirty_money"

SCENES = [
    title_scene(28, EPISODE_TITLE, "Syllabus H1(c)", ("washer", "magnifier")),

    Scene("s1", "Too good to be true", "", [
        Pause("open", 1.0),
        Line("kito1", "KITO", "A new customer wants to prepay two hundred thousand dollars, "
             "in cash, for kits. Then he'll probably cancel, and wants the refund sent to an "
             "offshore account. Easy money!", gap=0.4),
        Line("nia1", "NIA", "Cash in, refund out, to a different country? That's a classic "
             "warning sign.", gap=0.4),
        Line("lex1", "LEX", "Nia is right. This could be money laundering: turning the "
             "proceeds of crime into money that looks legitimate."),
        Pause("hold", 1.2),
    ], spec={"tpl": "talk", "bg": "office", "syl": "H1(c)",
             "cast": [{"who": "KITO", "x": 1450, "y": 1030, "s": 0.95, "mood": "excited",
                       "talk_pose": "cheer"},
                      {"who": "NIA", "x": 960, "y": 1030, "s": 0.9, "mood": "worried"},
                      {"who": "LEX", "x": 420, "y": 1030, "s": 0.88, "enter": "lex1",
                       "from": "left"}],
             "pops": [{"kind": "icon", "icon": "cash", "x": 1100, "y": 280, "s": 1.1,
                       "at": ["kito1", 1.5], "until": "lex1", "label": "$200,000 cash"},
                      {"kind": "icon", "icon": "globe", "x": 1450, "y": 280, "s": 1.0,
                       "at": ["kito1", 7.0], "until": "lex1", "label": "Offshore refund",
                       "color": "#e4572e"},
                      {"kind": "icon", "icon": "washer", "x": 1250, "y": 300, "s": 1.3,
                       "at": "lex1", "float": True}]}),

    Scene("s2", "Three stages of laundering", "", [
        Pause("open", 1.0),
        Line("lex2a", "LEX", "Laundering usually has three stages.", gap=0.3),
        Line("lex2b", "LEX", "Placement: dirty cash enters the financial system, for example "
             "as deposits, or a business's takings.", gap=0.3),
        Line("lex2c", "LEX", "Layering: it moves through many transactions, accounts and "
             "countries, to hide where it came from.", gap=0.3),
        Line("lex2d", "LEX", "Integration: it comes back looking clean, as profits, loans or "
             "property.", gap=0.4),
        Line("aud2", "AUDITOR", "And remember: criminal property includes the proceeds of "
             "any crime. Theft, fraud, and tax evasion too."),
        Pause("hold", 1.4),
    ], spec={"tpl": "flow", "bg": "studio_red", "heading": "Placement · layering · "
                                                           "integration",
             "syl": "H1(c)",
             "nodes": [{"id": "p", "x": 650, "y": 420, "label": "Placement",
                        "icon": "cash", "color": "#e4572e", "at": "lex2b", "w": 260},
                       {"id": "l", "x": 1150, "y": 420, "label": "Layering", "icon": "globe",
                        "color": "#f2a541", "at": "lex2c", "w": 260},
                       {"id": "i", "x": 1650, "y": 420, "label": "Integration",
                        "icon": "house", "color": "#3bb273", "at": "lex2d", "w": 260}],
             "edges": [{"from": "p", "to": "l", "at": "lex2c", "token": "coin",
                        "tcolor": "#ffb627"},
                       {"from": "l", "to": "i", "at": "lex2d", "token": "coin",
                        "tcolor": "#ffb627"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "AUDITOR", "x": 1810, "s": 0.55, "y": 1120, "enter": "aud2",
                       "pose": "clipboard"}],
             "pops": [{"kind": "chip", "at": "aud2", "x": 1150, "y": 760,
                       "text": "Criminal property: proceeds of ANY crime, incl. tax evasion",
                       "color": "#1f3a5f", "size": 32}]}),

    Scene("s3", "The offences", "", [
        Pause("open", 1.0),
        Line("lex3a", "LEX", "In the UK model, the Proceeds of Crime Act creates three "
             "groups of offence.", gap=0.3),
        Sfx("pop"),
        Line("lex3b", "LEX", "Laundering itself: concealing, converting or transferring "
             "criminal property, arranging to help someone else do it, or acquiring, using or "
             "possessing it. Up to fourteen years in prison.", gap=0.25),
        Sfx("pop"),
        Line("lex3c", "LEX", "Failure to disclose: in the regulated sector, like "
             "accountancy, not reporting knowledge or suspicion of laundering, or where "
             "there are reasonable grounds to suspect it.", gap=0.25),
        Sfx("pop"),
        Line("lex3d", "LEX", "And tipping off: telling a suspect that a report has been "
             "made, in a way likely to prejudice an investigation.", gap=0.4),
        Line("lex3e", "LEX", "The key defence is reporting. Make a report to your firm's "
             "money laundering reporting officer, who decides whether to report to the "
             "authorities."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "heading": "Money laundering offences",
             "syl": "H1(c)", "row": 150, "ts": 40,
             "items": [{"at": "lex3b", "text": "Laundering", "sub": "Conceal · arrange · "
                                                                    "acquire · up to 14 "
                                                                    "years",
                        "icon": "washer", "color": "#e4572e"},
                       {"at": "lex3c", "text": "Failure to disclose",
                        "sub": "Regulated sector: knowledge, suspicion or reasonable grounds",
                        "icon": "envelope", "color": "#f2a541"},
                       {"at": "lex3d", "text": "Tipping off", "sub": "Warning the suspect",
                        "icon": "megaphone", "color": "#7768ae"}],
             "cast": [{"who": "LEX", "x": 250}],
             "pops": [{"kind": "chip", "at": "lex3e", "x": 1190, "y": 950,
                       "text": "Defence: report to the MLRO", "color": "#3bb273",
                       "size": 36}]}),

    Scene("s4", "Risk management and internal controls", "", [
        Pause("open", 1.0),
        Line("aud4a", "AUDITOR", "Firms in the regulated sector must have policies, controls "
             "and procedures. The syllabus lists five areas.", gap=0.3),
        Line("aud4b", "AUDITOR", "First, risk management. Take a risk-based approach. Assess "
             "the firm's risks, by customer type, country, product, transaction and delivery "
             "channel, and write it down.", gap=0.3),
        Line("aud4c", "AUDITOR", "A small local charity funded by government grants is low "
             "risk. A charity collecting street cash and sending it abroad is much higher.",
             gap=0.4),
        Line("aud4d", "AUDITOR", "Second, internal controls. Appoint a money laundering "
             "reporting officer, give a senior manager responsibility, screen and train "
             "staff, and have the system independently checked.", gap=0.4),
        Line("nia4", "NIA", "So every staff member should know who the MLRO is, and how to "
             "report."),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio", "heading": "(i) Risk management · (ii) "
                                                          "Internal controls",
             "syl": "H1(c)(i)–(ii)", "ts": 32,
             "cols": [{"title": "Risk management", "icon": "chart", "color": "#0f8b8d",
                       "at": "aud4b",
                       "items": [{"at": ["aud4b", 0.5], "text": "Risk-based approach"},
                                 {"at": ["aud4b", 3.0], "text": "Customer · country · "
                                                               "product · transaction · "
                                                               "channel"},
                                 {"at": ["aud4b", 8.0], "text": "Written risk assessment"},
                                 {"at": "aud4c", "text": "Grant charity low · street-cash "
                                                         "charity high"}]},
                      {"title": "Internal controls", "icon": "shield", "color": "#7768ae",
                       "at": "aud4d",
                       "items": [{"at": ["aud4d", 1.0], "text": "Appoint an MLRO"},
                                 {"at": ["aud4d", 3.5], "text": "Senior manager responsible"},
                                 {"at": ["aud4d", 6.0], "text": "Screen and train staff"},
                                 {"at": ["aud4d", 8.0], "text": "Independent review"}]}],
             "vs": False,
             "cast": [{"who": "AUDITOR", "x": 250, "pose": "clipboard",
                       "talk_pose": "present"},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia4"}]}),

    Scene("s5", "Customer due diligence", "", [
        Pause("open", 1.0),
        Line("aud5a", "AUDITOR", "Third, customer due diligence, or know your customer.",
             gap=0.3),
        Line("aud5b", "AUDITOR", "Identify the customer, and verify it with reliable "
             "documents. Identify the beneficial owners, usually anyone owning or "
             "controlling more than twenty-five percent. Understand the purpose of the "
             "relationship. Then keep monitoring it.", gap=0.4),
        Line("aud5c", "AUDITOR", "Simplified due diligence may be allowed for clearly "
             "low-risk customers, such as listed companies or regulated banks.", gap=0.3),
        Line("aud5d", "AUDITOR", "Enhanced due diligence is required for high risk: "
             "politically exposed persons, and their families and close associates, "
             "high-risk countries, and complex or unusually large transactions.", gap=0.3),
        Line("aud5e", "AUDITOR", "And if you can't complete due diligence, you must not "
             "act for that customer.", gap=0.4),
        Line("kito5", "KITO", "Our cash customer won't even give his full name. So, no "
             "deal."),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio_teal", "heading": "(iii) Customer due diligence",
             "syl": "H1(c)(iii)", "ts": 30,
             "cols": [{"title": "Simplified", "icon": "check", "color": "#3bb273",
                       "at": "aud5c",
                       "items": [{"at": ["aud5c", 2.0], "text": "Clearly low risk"},
                                 {"at": ["aud5c", 4.5], "text": "e.g. listed companies, "
                                                               "regulated banks"}]},
                      {"title": "Standard", "icon": "person", "color": "#2b86c5",
                       "at": "aud5b",
                       "items": [{"at": ["aud5b", 0.5], "text": "Identify and verify the "
                                                               "customer"},
                                 {"at": ["aud5b", 4.5], "text": "Beneficial owners (over "
                                                               "25%)"},
                                 {"at": ["aud5b", 9.0], "text": "Purpose of the "
                                                               "relationship"},
                                 {"at": ["aud5b", 11.5], "text": "Ongoing monitoring"}]},
                      {"title": "Enhanced", "icon": "warning", "color": "#e4572e",
                       "at": "aud5d",
                       "items": [{"at": ["aud5d", 3.0], "text": "Politically exposed "
                                                               "persons + family, "
                                                               "associates"},
                                 {"at": ["aud5d", 8.0], "text": "High-risk countries"},
                                 {"at": ["aud5d", 9.5], "text": "Complex or unusually large "
                                                               "deals"}]}],
             "cast": [{"who": "AUDITOR", "x": 250, "pose": "clipboard",
                       "talk_pose": "present"},
                      {"who": "KITO", "x": 1810, "s": 0.55, "y": 1120, "enter": "kito5"}],
             "pops": [{"kind": "chip", "at": "aud5e", "until": "kito5", "x": 1180, "y": 960,
                       "text": "Can't complete CDD? Don't act", "color": "#e4572e",
                       "size": 36}]}),

    Scene("s6", "Records, reliance and compliance", "", [
        Pause("open", 1.0),
        Line("aud6a", "AUDITOR", "Fourth, reliance and record keeping. A firm may rely on "
             "another regulated firm's due diligence, but it stays responsible if that "
             "turns out to be wrong.", gap=0.25),
        Line("aud6b", "AUDITOR", "And it must keep due diligence and transaction records, "
             "generally for five years after the relationship ends.", gap=0.4),
        Line("aud6c", "AUDITOR", "Fifth, monitoring and managing compliance, and "
             "communicating the policies internally. Ask yourself.", gap=0.3),
        Sfx("pop"),
        Line("aud6d", "AUDITOR", "Would every staff member know who the MLRO is, and where "
             "the procedures are?", gap=0.2),
        Sfx("pop"),
        Line("aud6e", "AUDITOR", "Can we prove everyone is trained, and kept up to date?",
             gap=0.2),
        Sfx("pop"),
        Line("aud6f", "AUDITOR", "Would a random client file show a risk assessment and "
             "complete due diligence?", gap=0.2),
        Sfx("pop"),
        Line("aud6g", "AUDITOR", "And do reporting patterns reveal teams that report "
             "unusually little?", gap=0.4),
        Line("lex6", "LEX", "A bought-in manual is not enough. Policies must fit the firm's "
             "actual risks."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "white", "heading": "(iv) Records · (v) Monitoring "
                                                          "compliance",
             "syl": "H1(c)(iv)–(v)", "row": 108, "ts": 36,
             "items": [{"at": "aud6a", "text": "Reliance allowed, responsibility stays",
                        "icon": "handshake", "color": "#0f8b8d"},
                       {"at": "aud6b", "text": "Keep records 5 years after the relationship",
                        "icon": "book", "color": "#2b86c5"},
                       {"at": "aud6d", "text": "Staff know the MLRO and procedures?",
                        "icon": "people", "color": "#7768ae"},
                       {"at": "aud6e", "text": "Training proven and current?",
                        "icon": "brain", "color": "#f2a541"},
                       {"at": "aud6f", "text": "Random file test passes?",
                        "icon": "magnifier", "color": "#3bb273"},
                       {"at": "aud6g", "text": "Reporting patterns reviewed?",
                        "icon": "chart", "color": "#e4572e"}],
             "cast": [{"who": "AUDITOR", "x": 250, "pose": "clipboard",
                       "talk_pose": "present"},
                      {"who": "LEX", "x": 1810, "s": 0.55, "y": 1120, "enter": "lex6"}]}),

    Scene("s7", "What SafariTech does next", "", [
        Pause("open", 1.0),
        Line("nia7", "NIA", "So we decline the cash, and I report my suspicion to our MLRO. "
             "And we say nothing to the customer about the report.", gap=0.3),
        Line("lex7a", "LEX", "Exactly right. Tipping him off could be an offence.", gap=0.4),
        Line("lex7b", "LEX", "East Africa follows the same global standards, set by the "
             "Financial Action Task Force. In Tanzania, reports go to the Financial "
             "Intelligence Unit, under the Anti-Money Laundering Act.", gap=0.3),
        Line("lex7c", "LEX", "In Kenya, to the Financial Reporting Centre, under the Proceeds "
             "of Crime and Anti-Money Laundering Act.", gap=0.4),
        Line("amara7", "AMARA", "Our bank files these reports every week. It's how the "
             "system catches criminals."),
        Pause("hold", 1.4),
    ], spec={"tpl": "talk", "bg": "harbour", "syl": "H1(c)",
             "cast": [{"who": "NIA", "x": 960, "y": 1030, "s": 0.9},
                      {"who": "LEX", "x": 420, "y": 1030, "s": 0.88},
                      {"who": "AMARA", "x": 1450, "y": 1030, "s": 0.9, "enter": "amara7"}],
             "pops": [{"kind": "card", "at": "lex7b", "until": "amara7", "x": 1180, "y": 280,
                       "w": 1000, "h": 260, "title": "Local lens: FATF standards",
                       "body": "Tanzania: Financial Intelligence Unit (AMLA) · Kenya: "
                               "Financial Reporting Centre (POCAMLA)",
                       "color": "#f2a541", "bs": 36}]}),

    quiz_scene("s8", "Quick check",
               "Moving funds through many accounts and countries to hide their origin is "
               "which stage of money laundering?",
               ["Placement", "Layering", "Integration", "Tipping off"], 1,
               "Quick check. Moving funds through many accounts and countries to hide their "
               "origin. Which stage is that?",
               "Layering.",
               syl="H1(c)"),

    quiz_scene("s9", "Quick check",
               "A new client is a politically exposed person. What level of due diligence "
               "applies?",
               ["Simplified", "Standard", "Enhanced", "None"], 2,
               "And if a new client is a politically exposed person, what due diligence "
               "applies?",
               "Enhanced due diligence.",
               think=4.0, syl="H1(c)(iii)"),

    recap_scene("s10", [
        ("Placement, layering, integration.", "Placement · layering · integration"),
        ("Laundering, failure to disclose, tipping off.", "3 offence groups"),
        ("Risk-based approach and an MLRO.", "Risk-based · MLRO"),
        ("Simplified, standard, enhanced due diligence.", "CDD: simplified · standard · "
                                                          "enhanced"),
        ("Records kept five years; monitor compliance.", "Records 5 years · monitor"),
    ], [
        Line("lex10", "LEX", "Next time, our final episode: bribery, failure to prevent "
             "offences, and fraudulent and wrongful trading.", gap=0.3),
        Line("kito10", "KITO", "The final episode? Already?", gap=0.6),
    ], next_ep=29, next_title="Bribes, Fraud and the Final Bell", next_icon="gift"),
]
