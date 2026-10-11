"""Episode 16 - Birth of a Company.

Syllabus D4(a)-(d): promoters and their duties; pre-incorporation contracts;
registering private and public companies, including streamlined online
registration; statutory books, records and returns, the confirmation statement
and the register of people with significant control. UK Companies Act 2006
model, with East African comparisons (BRELA in Tanzania, the Business
Registration Service in Kenya).
"""
from ._kit import (DISPLAY_NAMES, SERIES, VOICES, Line, Pause, Scene, Sfx,  # noqa: F401
                   quiz_scene, recap_scene, title_scene)

EPISODE = "Episode 16"
EPISODE_TITLE = "Birth of a Company"
SLUG = "episode16_birth_of_a_company"

SCENES = [
    title_scene(16, EPISODE_TITLE, "Syllabus D4(a)–(d)", ("stamp", "company")),

    Scene("s1", "Kito the promoter", "", [
        Pause("open", 1.0),
        Line("kito1", "KITO", "I'll set up Safari Solar Limited. I've already found a "
             "warehouse, and signed the lease, in the company's name!", gap=0.4),
        Line("nia1", "NIA", "But the company doesn't exist yet.", gap=0.3),
        Line("lex1", "LEX", "Two warning lights at once. Kito is acting as a promoter, and "
             "he's made a pre-incorporation contract."),
        Pause("hold", 1.2),
    ], spec={"tpl": "talk", "bg": "office", "syl": "D4(a)–(b)",
             "cast": [{"who": "KITO", "x": 1450, "y": 1030, "s": 0.95, "mood": "excited",
                       "talk_pose": "cheer"},
                      {"who": "NIA", "x": 960, "y": 1030, "s": 0.9, "mood": "worried"},
                      {"who": "LEX", "x": 420, "y": 1030, "s": 0.88, "enter": "lex1",
                       "from": "left"}],
             "pops": [{"kind": "icon", "icon": "contract", "x": 1200, "y": 280, "s": 1.1,
                       "at": ["kito1", 3.0], "until": "lex1", "label": "Warehouse lease"},
                      {"kind": "icon", "icon": "warning", "x": 1200, "y": 280, "s": 1.1,
                       "at": "lex1", "color": "#e4572e", "float": True}]}),

    Scene("s2", "Promoters and their duties", "", [
        Pause("open", 1.0),
        Line("lex2a", "LEX", "A promoter is someone who undertakes to form a company, and "
             "set it going. Lawyers or accountants acting only in a professional capacity "
             "are not promoters.", gap=0.3),
        Sfx("pop"),
        Line("lex2b", "LEX", "Promoters do the groundwork: choose the name, draft the "
             "constitution, find directors and shareholders, file the documents, and pay "
             "the formation costs.", gap=0.25),
        Sfx("pop"),
        Line("lex2c", "LEX", "They owe fiduciary duties to the company they are forming. "
             "They must act with reasonable skill and care, and not make secret profits.",
             gap=0.25),
        Sfx("pop"),
        Line("lex2d", "LEX", "Any profit or interest must be disclosed, to an independent "
             "board, or to the members.", gap=0.4),
        Line("lex2e", "LEX", "In Erlanger against New Sombrero Phosphate, promoters sold an "
             "island to their own company at a huge hidden profit. The company could "
             "rescind the sale.", gap=0.3),
        Line("lex2f", "LEX", "If rescission is not possible, the company can recover the "
             "secret profit, as in Gluckstein against Barnes, or claim damages for breach of "
             "duty."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "heading": "Promoters", "syl": "D4(a)",
             "row": 130, "ts": 40,
             "items": [{"at": "lex2b", "text": "Do the groundwork",
                        "sub": "Name · constitution · people · filings · costs",
                        "icon": "pen", "color": "#0f8b8d"},
                       {"at": "lex2c", "text": "Fiduciary duties",
                        "sub": "Skill and care · no secret profit", "icon": "shield",
                        "color": "#7768ae"},
                       {"at": "lex2d", "text": "Disclose interests",
                        "sub": "To an independent board or the members", "icon": "eye",
                        "color": "#f2a541"},
                       {"at": "lex2e", "text": "Remedies for breach",
                        "sub": "Rescind · recover secret profit · damages", "icon": "gavel",
                        "color": "#e4572e"}],
             "cast": [{"who": "LEX", "x": 250}],
             "pops": [{"kind": "chip", "at": "lex2e", "until": "lex2f", "x": 1190, "y": 940,
                       "text": "Erlanger v New Sombrero Phosphate (1878): rescission",
                       "color": "#1f3a5f", "size": 30},
                      {"kind": "chip", "at": "lex2f", "x": 1190, "y": 940,
                       "text": "Gluckstein v Barnes (1900): account for secret profit",
                       "color": "#1f3a5f", "size": 30}]}),

    Scene("s3", "Pre-incorporation contracts", "", [
        Pause("open", 1.0),
        Line("lex3a", "LEX", "A company cannot ratify a contract made before it existed. "
             "Remember Kelner against Baxter.", gap=0.3),
        Line("lex3b", "LEX", "And under the Companies Act, a contract made for a company not "
             "yet formed takes effect as a contract with the person who made it. That "
             "person is personally liable, unless the contract says otherwise.", gap=0.3),
        Line("lex3c", "LEX", "In Phonogram against Lane, a promoter signed for a company "
             "that was never formed, and had to pay personally.", gap=0.4),
        Line("kito3", "KITO", "So I'm on the hook for the warehouse lease!", gap=0.3),
        Line("lex3d", "LEX", "Unless you avoid it. Buy a ready-made company off the shelf, "
             "or sign only a draft, to be signed by the company once it exists. Or after "
             "incorporation, the company can make a new contract with the landlord, "
             "replacing yours. That's novation."),
        Pause("hold", 1.4),
    ], spec={"tpl": "flow", "bg": "studio_red", "heading": "Who is bound before incorporation?",
             "syl": "D4(b)",
             "nodes": [{"id": "k", "x": 700, "y": 320, "label": "Kito signs “for Safari "
                                                               "Solar Ltd”",
                        "icon": "pen", "color": "#f2a541", "at": "lex3b", "w": 320},
                       {"id": "l", "x": 1600, "y": 320, "label": "Landlord",
                        "icon": "warehouse", "color": "#7768ae", "at": ["lex3b", 1.0],
                        "w": 260},
                       {"id": "c", "x": 1150, "y": 650, "label": "Company not yet formed",
                        "icon": "question", "color": "#5b6670", "at": "lex3a", "w": 300}],
             "edges": [{"from": "k", "to": "l", "at": ["lex3b", 1.0], "label": "lease"},
                       {"from": "l", "to": "k", "at": ["lex3b", 5.0], "label": "personally "
                                                                           "liable",
                        "color": "#e4572e", "bend": 60, "ly": 40},
                       {"from": "c", "to": "l", "at": ["lex3a", 0.5], "label": "can't "
                                                                             "ratify",
                        "dashed": True, "color": "#5b6670"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "KITO", "x": 1810, "s": 0.55, "y": 1120, "enter": "kito3",
                       "mood": "worried"}],
             "pops": [{"kind": "chip", "at": "lex3c", "until": "lex3d", "x": 1150, "y": 900,
                       "text": "Phonogram v Lane (1982): promoter liable", "color": "#1f3a5f",
                       "size": 32},
                      {"kind": "card", "at": "lex3d", "x": 1150, "y": 470, "w": 960, "h": 300,
                       "title": "How to avoid personal liability",
                       "body": "Buy an off-the-shelf company · sign only a draft · novation "
                               "after incorporation", "color": "#3bb273", "dim": True,
                       "bs": 36}]}),

    Scene("s4", "Registering the company", "", [
        Pause("open", 1.0),
        Line("lex4a", "LEX", "To register, the promoters send the registrar an application "
             "with several documents.", gap=0.3),
        Sfx("pop"),
        Line("lex4b", "LEX", "The memorandum of association: the subscribers wish to form a "
             "company, and agree to become members, taking at least one share each.",
             gap=0.25),
        Sfx("pop"),
        Line("lex4c", "LEX", "The application itself: proposed name, where the registered "
             "office is, whether liability is limited by shares or guarantee, and whether "
             "the company is private or public.", gap=0.25),
        Sfx("pop"),
        Line("lex4d", "LEX", "A statement of capital and initial shareholdings, and a "
             "statement of the proposed officers.", gap=0.25),
        Sfx("pop"),
        Line("lex4e", "LEX", "Articles of association, unless the model articles will "
             "apply. And a statement of initial significant control.", gap=0.25),
        Sfx("pop"),
        Line("lex4f", "LEX", "A statement of compliance, and the fee.", gap=0.4),
        Line("lex4g", "LEX", "If all is in order, the registrar issues a certificate of "
             "incorporation. It is conclusive evidence that the company exists from that "
             "date, as Jubilee Cotton Mills against Lewis shows. A public company also "
             "needs its trading certificate before it trades."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "white", "heading": "The registration pack",
             "syl": "D4(c)", "row": 102, "ts": 36,
             "items": [{"at": "lex4b", "text": "Memorandum of association",
                        "sub": "Subscribers form the company, take a share each",
                        "icon": "scroll", "color": "#0f8b8d"},
                       {"at": "lex4c", "text": "Application for registration",
                        "sub": "Name · office · limited by shares/guarantee · private/public",
                        "icon": "doc", "color": "#2b86c5"},
                       {"at": "lex4d", "text": "Capital and proposed officers",
                        "sub": "Statement of capital · directors (and secretary)",
                        "icon": "people", "color": "#7768ae"},
                       {"at": "lex4e", "text": "Articles · significant control",
                        "sub": "Own articles, or model articles apply", "icon": "book",
                        "color": "#f2a541"},
                       {"at": "lex4f", "text": "Statement of compliance + fee",
                        "icon": "check", "color": "#3bb273"}],
             "cast": [{"who": "LEX", "x": 250}],
             "pops": [{"kind": "card", "at": "lex4g", "x": 1190, "y": 470, "w": 960,
                       "h": 300, "title": "Certificate of incorporation",
                       "body": "Conclusive evidence of incorporation (Jubilee Cotton Mills "
                               "v Lewis). plc: trading certificate too.",
                       "color": "#1f3a5f", "dim": True, "bs": 36}]}),

    Scene("s5", "Streamlined online registration", "", [
        Pause("open", 1.0),
        Line("nia5", "NIA", "Can we just do this online?", gap=0.3),
        Line("lex5a", "LEX", "Yes. Streamlined registration lets a private company be "
             "formed online, often within a day, and registers it for tax at the same time. "
             "One click, several government offices.", gap=0.4),
        Line("lex5b", "LEX", "East Africa works the same way. In Tanzania, BRELA's Online "
             "Registration System handles companies, business names and beneficial "
             "ownership.", say="East Africa works the same way. In Tanzania, Brella's Online "
             "Registration System handles companies, business names and beneficial "
             "ownership.", gap=0.3),
        Line("lex5c", "LEX", "In Kenya, companies are registered online through the "
             "Business Registration Service, on the eCitizen platform.",
             say="In Kenya, companies are registered online through the Business "
                 "Registration Service, on the e-citizen platform.", gap=0.4),
        Line("kito5", "KITO", "Done! Safari Solar Limited is born!"),
        Sfx("sparkle"),
        Pause("hold", 1.6),
    ], spec={"tpl": "flow", "bg": "studio_teal", "heading": "One application, many offices",
             "syl": "D4(c)",
             "nodes": [{"id": "app", "x": 700, "y": 500, "label": "Online application",
                        "icon": "laptop", "color": "#0f8b8d", "at": "lex5a", "w": 290},
                       {"id": "reg", "x": 1450, "y": 260, "label": "Companies registry",
                        "icon": "stamp", "color": "#7768ae", "at": ["lex5a", 2.5], "w": 290},
                       {"id": "tax", "x": 1450, "y": 520, "label": "Tax authority",
                        "icon": "percent", "color": "#f2a541", "at": ["lex5a", 6.0],
                        "w": 290},
                       {"id": "cert", "x": 1450, "y": 780, "label": "Certificate issued",
                        "icon": "seal", "color": "#3bb273", "at": "kito5", "w": 290}],
             "edges": [{"from": "app", "to": "reg", "at": ["lex5a", 2.5], "token": "doc"},
                       {"from": "app", "to": "tax", "at": ["lex5a", 6.0], "token": "doc"},
                       {"from": "app", "to": "cert", "at": "kito5", "color": "#3bb273"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1660, "s": 0.55, "y": 1120},
                      {"who": "KITO", "x": 1820, "s": 0.55, "y": 1120, "enter": "kito5",
                       "mood": "excited"}],
             "pops": [{"kind": "card", "at": "lex5b", "until": "kito5", "x": 1100, "y": 500,
                       "w": 960, "h": 300, "title": "Local lens: East Africa",
                       "body": "Tanzania: BRELA Online Registration System · Kenya: Business "
                               "Registration Service on eCitizen", "color": "#f2a541",
                       "dim": True, "bs": 36}]}),

    Scene("s6", "Statutory books and returns", "", [
        Pause("open", 1.0),
        Line("lex6a", "LEX", "Once formed, a company must keep statutory registers, "
             "usually at its registered office, open to inspection.", gap=0.3),
        Sfx("pop"),
        Line("lex6b", "LEX", "A register of members.", gap=0.2),
        Sfx("pop"),
        Line("lex6c", "LEX", "Registers of directors, and of their residential addresses, "
             "and of secretaries if any.", gap=0.2),
        Sfx("pop"),
        Line("lex6d", "LEX", "Copies of documents creating charges over its assets.",
             gap=0.2),
        Sfx("pop"),
        Line("lex6e", "LEX", "Minutes of meetings, and adequate accounting records.",
             gap=0.2),
        Sfx("pop"),
        Line("lex6f", "LEX", "And a register of people with significant control.", gap=0.4),
        Line("lex6g", "LEX", "Private companies may choose to keep some of this information "
             "on the central public register instead.", gap=0.3),
        Line("lex6h", "LEX", "Each year, the company must also file accounts, and a "
             "confirmation statement, confirming the registrar's information is up to "
             "date. It replaced the old annual return."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "layout": "grid", "cols": 3,
             "heading": "Statutory books", "syl": "D4(d)", "cell_h": 280, "ts": 34,
             "items": [{"at": "lex6b", "text": "Members", "icon": "people",
                        "color": "#0f8b8d"},
                       {"at": "lex6c", "text": "Directors and secretaries",
                        "sub": "Including residential addresses", "icon": "person",
                        "color": "#2b86c5"},
                       {"at": "lex6d", "text": "Charges", "sub": "Copies of instruments",
                        "icon": "chain", "color": "#7768ae"},
                       {"at": "lex6e", "text": "Minutes", "icon": "book",
                        "color": "#f2a541"},
                       {"at": ["lex6e", 1.8], "text": "Accounting records", "icon": "chart",
                        "color": "#3bb273"},
                       {"at": "lex6f", "text": "People with significant control",
                        "icon": "key", "color": "#e4572e"}],
             "cast": [{"who": "LEX", "x": 250}],
             "pops": [{"kind": "card", "at": "lex6h", "x": 1190, "y": 470, "w": 960,
                       "h": 280, "title": "Every year",
                       "body": "Annual accounts · confirmation statement (replaced the "
                               "annual return)", "color": "#1f3a5f", "dim": True, "bs": 38}]}),

    Scene("s7", "Who really controls it?", "", [
        Pause("open", 1.0),
        Line("lex7a", "LEX", "The register of people with significant control, the PSC "
             "register, shows who really stands behind a company.",
             say="The register of people with significant control, the P.S.C. register, "
                 "shows who really stands behind a company.", gap=0.3),
        Sfx("pop"),
        Line("lex7b", "LEX", "A PSC holds more than twenty-five percent of the shares,",
             say="A P.S.C. holds more than twenty-five percent of the shares,", gap=0.2),
        Sfx("pop"),
        Line("lex7c", "LEX", "or more than twenty-five percent of the votes,", gap=0.2),
        Sfx("pop"),
        Line("lex7d", "LEX", "or can appoint or remove a majority of the board,", gap=0.2),
        Sfx("pop"),
        Line("lex7e", "LEX", "or otherwise has the right to exercise, or actually exercises, "
             "significant influence or control, including through a trust or firm.",
             gap=0.4),
        Line("amara7", "AMARA", "Banks check this to fight money laundering. And Tanzania and "
             "Kenya now require companies to file beneficial ownership information too.",
             gap=0.3),
        Line("lex7f", "LEX", "And new UK reforms now require directors and PSCs to verify "
             "their identity with Companies House."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "white", "heading": "Person with significant control",
             "syl": "D4(d)", "row": 120, "ts": 40,
             "items": [{"at": "lex7b", "text": "More than 25% of the shares", "icon": "pie",
                        "color": "#0f8b8d"},
                       {"at": "lex7c", "text": "More than 25% of the votes", "icon": "ballot",
                        "color": "#2b86c5"},
                       {"at": "lex7d", "text": "Can appoint or remove most directors",
                        "icon": "people", "color": "#7768ae"},
                       {"at": "lex7e", "text": "Significant influence or control",
                        "sub": "Directly, or via a trust or firm", "icon": "key",
                        "color": "#e4572e"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "AMARA", "x": 1810, "s": 0.55, "y": 1120, "enter": "amara7"}],
             "pops": [{"kind": "chip", "at": "amara7", "until": "lex7f", "x": 1190, "y": 940,
                       "text": "Tanzania and Kenya: beneficial ownership filing",
                       "color": "#f2a541", "size": 32, "fg": "#1d2b3a"},
                      {"kind": "chip", "at": "lex7f", "x": 1190, "y": 940,
                       "text": "UK: identity verification for directors and PSCs",
                       "color": "#1f3a5f", "size": 32}]}),

    quiz_scene("s8", "Quick check",
               "Kito signs a lease “for Safari Solar Ltd” before the company is incorporated. "
               "Unless agreed otherwise, who is liable on the lease?",
               ["The company, once it is formed", "Kito personally", "Nobody: the contract "
                "is void", "The registrar of companies"], 1,
               "Quick check. Kito signs a lease for a company that does not yet exist. Who is "
               "liable on it?",
               "Kito, personally.",
               why=("The person who acted is liable: Phonogram v Lane",
                    "The person who made the contract is liable, as in Phonogram against "
                    "Lane."),
               syl="D4(b)"),

    quiz_scene("s9", "Quick check",
               "Which of these makes someone a person with significant control?",
               ["Holding 20% of the shares", "Being the company's auditor",
                "Holding more than 25% of the voting rights", "Being a customer"], 2,
               "And which of these makes someone a person with significant control?",
               "Holding more than twenty-five percent of the voting rights.",
               think=4.0, syl="D4(d)"),

    recap_scene("s10", [
        ("Promoters: fiduciaries, disclose profits.", "Promoter: fiduciary, disclose"),
        ("Pre-incorporation: the signer is liable.", "Pre-incorp contract: signer liable"),
        ("Registration pack, then the certificate.", "Register → certificate"),
        ("Statutory books and confirmation statement.", "Registers · confirmation statement"),
        ("PSC: over twenty-five percent, or control.", "PSC: >25% or control",
         "P.S.C.: over twenty-five percent, or control."),
    ], [
        Line("lex10", "LEX", "Next time, we open the company's rulebook: its constitution, "
             "the articles, and the company's name.", gap=0.3),
        Line("nia10", "NIA", "Rules, I like rules.", gap=0.6),
    ], next_ep=17, next_title="The Company's Rulebook", next_icon="book"),
]
