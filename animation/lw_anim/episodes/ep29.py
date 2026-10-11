"""Episode 29 - Bribes, Fraud and the Final Bell (series finale).

Syllabus H1(d)-(f): bribery (UK Bribery Act 2010), criminal activity in the
operation, management and liquidation of companies, the failure to prevent the
facilitation of tax evasion (Criminal Finances Act 2017, "relevant body"), the
failure to prevent fraud (Economic Crime and Corporate Transparency Act 2023,
in force 1 September 2025), and fraudulent and wrongful trading. Tanzania's
Prevention and Combating of Corruption Act and Kenya's Bribery Act 2016 are
shown as local comparisons. Ends with the LW-GLO exam format.
"""
from ._kit import (DISPLAY_NAMES, SERIES, VOICES, Line, Pause, Scene, Sfx,  # noqa: F401
                   quiz_scene, recap_scene, title_scene)

EPISODE = "Episode 29"
EPISODE_TITLE = "Bribes, Fraud and the Final Bell"
SLUG = "episode29_bribes_fraud_and_the_final_bell"

SCENES = [
    title_scene(29, EPISODE_TITLE, "Syllabus H1(d)–(f) · Finale", ("gift", "handcuffs")),

    Scene("s1", "A small gift", "", [
        Pause("open", 1.0),
        Line("kito1", "KITO", "Our import licence is stuck. An official says a small gift "
             "would speed things up. Five hundred dollars. Everyone does it!", gap=0.4),
        Line("nia1", "NIA", "Kito, that's a bribe.", gap=0.3),
        Line("lex1", "LEX", "And a crime, almost everywhere. In the UK model, the Bribery Act "
             "2010. In Tanzania, the Prevention and Combating of Corruption Act. In Kenya, the "
             "Bribery Act of 2016."),
        Pause("hold", 1.2),
    ], spec={"tpl": "talk", "bg": "office", "syl": "H1(d)",
             "cast": [{"who": "KITO", "x": 1450, "y": 1030, "s": 0.95, "talk_pose": "shrug"},
                      {"who": "NIA", "x": 960, "y": 1030, "s": 0.9, "mood": "worried"},
                      {"who": "LEX", "x": 420, "y": 1030, "s": 0.88, "enter": "lex1",
                       "from": "left"}],
             "pops": [{"kind": "icon", "icon": "gift", "x": 1200, "y": 280, "s": 1.1,
                       "at": ["kito1", 2.5], "until": "lex1", "label": "$500 \"gift\"",
                       "color": "#e4572e"},
                      {"kind": "stamp", "at": "nia1", "until": "lex1", "x": 1200, "y": 300,
                       "text": "BRIBE", "color": "#e4572e", "size": 64}]}),

    Scene("s2", "Four bribery offences", "", [
        Pause("open", 1.0),
        Line("lex2a", "LEX", "The Bribery Act has four offences.", gap=0.3),
        Sfx("pop"),
        Line("lex2b", "LEX", "Bribing: offering, promising or giving a financial or other "
             "advantage, to induce or reward improper performance of a function.", gap=0.2),
        Sfx("pop"),
        Line("lex2c", "LEX", "Being bribed: requesting, agreeing to receive, or accepting "
             "such an advantage.", gap=0.2),
        Sfx("pop"),
        Line("lex2d", "LEX", "Bribing a foreign public official, to obtain or keep "
             "business.", gap=0.2),
        Sfx("pop"),
        Line("lex2e", "LEX", "And a corporate offence: a commercial organisation fails to "
             "prevent bribery by an associated person, such as an employee, agent or "
             "subsidiary, acting for its benefit.", gap=0.4),
        Line("lex2f", "LEX", "Individuals face up to ten years in prison. Companies face "
             "unlimited fines. Facilitation payments, like Kito's gift, are not exempt. "
             "Reasonable, proportionate hospitality is fine."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "heading": "Bribery Act 2010",
             "syl": "H1(d)", "row": 128, "ts": 40,
             "items": [{"at": "lex2b", "text": "Bribing another person", "sub": "Offer, "
                                                                               "promise, give",
                        "icon": "gift", "color": "#e4572e"},
                       {"at": "lex2c", "text": "Being bribed", "sub": "Request, agree, "
                                                                      "accept",
                        "icon": "moneybag", "color": "#f2a541"},
                       {"at": "lex2d", "text": "Bribing a foreign public official",
                        "icon": "flag", "color": "#7768ae"},
                       {"at": "lex2e", "text": "Failure to prevent bribery",
                        "sub": "Commercial organisations · associated persons",
                        "icon": "company", "color": "#0f8b8d"}],
             "cast": [{"who": "LEX", "x": 250}],
             "pops": [{"kind": "chip", "at": "lex2f", "x": 1190, "y": 960,
                       "text": "Up to 10 years · unlimited fines · no facilitation payments",
                       "color": "#e4572e", "size": 30}]}),

    Scene("s3", "Adequate procedures", "", [
        Pause("open", 1.0),
        Line("aud3a", "AUDITOR", "The failure to prevent offence is strict. The company's "
             "only defence is that it had adequate procedures, built on six principles.",
             gap=0.3),
        Sfx("pop"),
        Line("aud3b", "AUDITOR", "Proportionate procedures, matching the risks and the "
             "company's size.", gap=0.2),
        Sfx("pop"),
        Line("aud3c", "AUDITOR", "Top-level commitment, from the board down.", gap=0.2),
        Sfx("pop"),
        Line("aud3d", "AUDITOR", "Risk assessment, regular and documented.", gap=0.2),
        Sfx("pop"),
        Line("aud3e", "AUDITOR", "Due diligence on the people who act for the company.",
             gap=0.2),
        Sfx("pop"),
        Line("aud3f", "AUDITOR", "Communication, including training.", gap=0.2),
        Sfx("pop"),
        Line("aud3g", "AUDITOR", "And monitoring and review.", gap=0.4),
        Line("nia3", "NIA", "Kenya's Bribery Act even requires private businesses to put "
             "prevention procedures in place."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "white", "layout": "grid", "cols": 3,
             "heading": "Six principles", "syl": "H1(d)", "cell_h": 290, "ts": 34,
             "items": [{"at": "aud3b", "text": "Proportionate procedures", "icon": "scales",
                        "color": "#0f8b8d"},
                       {"at": "aud3c", "text": "Top-level commitment", "icon": "crown",
                        "color": "#7768ae"},
                       {"at": "aud3d", "text": "Risk assessment", "icon": "warning",
                        "color": "#f2a541"},
                       {"at": "aud3e", "text": "Due diligence", "icon": "magnifier",
                        "color": "#2b86c5"},
                       {"at": "aud3f", "text": "Communication and training",
                        "icon": "megaphone", "color": "#3bb273"},
                       {"at": "aud3g", "text": "Monitoring and review", "icon": "eye",
                        "color": "#e4572e"}],
             "cast": [{"who": "AUDITOR", "x": 250, "pose": "clipboard",
                       "talk_pose": "present"},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia3"}]}),

    Scene("s4", "Failure to prevent tax evasion", "", [
        Pause("open", 1.0),
        Line("lex4a", "LEX", "The Criminal Finances Act 2017 made a relevant body, meaning a "
             "company or a partnership, liable for failing to prevent the criminal "
             "facilitation of tax evasion.", gap=0.3),
        Line("lex4b", "LEX", "It works in three stages.", gap=0.25),
        Sfx("pop"),
        Line("lex4c", "LEX", "One: a taxpayer criminally evades tax.", gap=0.2),
        Sfx("pop"),
        Line("lex4d", "LEX", "Two: a person associated with the body, like an employee or "
             "agent, criminally facilitates that evasion, while acting for the body.",
             gap=0.2),
        Sfx("pop"),
        Line("lex4e", "LEX", "Three: the body failed to prevent it.", gap=0.4),
        Line("lex4f", "LEX", "It covers UK tax, and foreign tax where there's a UK "
             "connection. The defence is reasonable prevention procedures. The penalty, an "
             "unlimited fine.", gap=0.3),
        Line("aud4", "AUDITOR", "This one matters for accountancy firms. One staff member "
             "helping a client hide income could make the whole firm liable."),
        Pause("hold", 1.4),
    ], spec={"tpl": "flow", "bg": "studio_purple", "heading": "Failure to prevent "
                                                              "facilitation of tax evasion",
             "syl": "H1(e)",
             "nodes": [{"id": "t", "x": 650, "y": 380, "label": "1. Taxpayer evades tax",
                        "icon": "receipt", "color": "#e4572e", "at": "lex4c", "w": 300},
                       {"id": "a", "x": 1150, "y": 380, "label": "2. Associated person "
                                                                "facilitates",
                        "icon": "person", "color": "#f2a541", "at": "lex4d", "w": 320},
                       {"id": "b", "x": 1650, "y": 380, "label": "3. Body failed to prevent",
                        "icon": "company", "color": "#7768ae", "at": "lex4e", "w": 300}],
             "edges": [{"from": "t", "to": "a", "at": "lex4d"},
                       {"from": "a", "to": "b", "at": "lex4e"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "AUDITOR", "x": 1810, "s": 0.55, "y": 1120, "enter": "aud4",
                       "pose": "clipboard"}],
             "pops": [{"kind": "card", "at": "lex4f", "x": 1150, "y": 720, "w": 980,
                       "h": 240, "title": "Defence: reasonable prevention procedures",
                       "body": "UK and foreign tax · relevant body = company or partnership "
                               "· unlimited fine", "color": "#0f8b8d", "bs": 34}]}),

    Scene("s5", "Failure to prevent fraud", "", [
        Pause("open", 1.0),
        Line("lex5a", "LEX", "The newest offence came into force on the first of September "
             "2025, under the Economic Crime and Corporate Transparency Act.", gap=0.3),
        Sfx("pop"),
        Line("lex5b", "LEX", "It applies to large organisations, meeting two of three tests: "
             "more than two hundred and fifty employees, turnover over thirty-six million "
             "pounds, or assets over eighteen million.", gap=0.2),
        Sfx("pop"),
        Line("lex5c", "LEX", "The organisation is liable if an associated person commits a "
             "fraud offence, such as false representation or false accounting, intending to "
             "benefit the organisation.", gap=0.2),
        Sfx("pop"),
        Line("lex5d", "LEX", "The defence: reasonable fraud prevention procedures. The "
             "penalty: an unlimited fine.", gap=0.4),
        Line("lex5e", "LEX", "The same Act also makes it easier to convict companies, by "
             "attributing the economic crimes of senior managers to the company."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "heading": "Failure to prevent fraud (2025)",
             "syl": "H1(e)", "row": 140, "ts": 40,
             "items": [{"at": "lex5b", "text": "Large organisations only",
                        "sub": "2 of: 250+ staff · £36m turnover · £18m assets",
                        "icon": "company", "color": "#0f8b8d"},
                       {"at": "lex5c", "text": "Associated person commits fraud",
                        "sub": "Intending to benefit the organisation", "icon": "mask",
                        "color": "#e4572e"},
                       {"at": "lex5d", "text": "Defence: reasonable procedures",
                        "sub": "Penalty: unlimited fine", "icon": "shield",
                        "color": "#3bb273"}],
             "cast": [{"who": "LEX", "x": 250}],
             "pops": [{"kind": "chip", "at": "lex5a", "until": "lex5b", "x": 1190, "y": 960,
                       "text": "In force 1 September 2025 (ECCTA 2023)", "color": "#1f3a5f",
                       "size": 34},
                      {"kind": "chip", "at": "lex5e", "x": 1190, "y": 960,
                       "text": "Senior managers' crimes attributed to the company",
                       "color": "#7768ae", "size": 32}]}),

    Scene("s6", "Fraudulent or wrongful trading?", "", [
        Pause("open", 1.0),
        Line("lex6a", "LEX", "Two more ways directors can be made to pay.", gap=0.3),
        Line("lex6b", "LEX", "Fraudulent trading: carrying on business with intent to "
             "defraud creditors, or for any fraudulent purpose. It needs real dishonesty.",
             gap=0.25),
        Line("lex6c", "LEX", "It is a crime under the Companies Act, whether or not the "
             "company is wound up, with up to ten years in prison. And in a liquidation, the "
             "court can order anyone knowingly involved, not just directors, to contribute "
             "to the assets.", gap=0.4),
        Line("lex6d", "LEX", "Wrongful trading needs no dishonesty. A director is liable if "
             "they knew, or ought to have concluded, that there was no reasonable prospect "
             "of avoiding insolvent liquidation or administration, and carried on.", gap=0.25),
        Line("lex6e", "LEX", "It is civil only. The court can order the director to "
             "contribute. The defence: they took every step to minimise the loss to "
             "creditors.", gap=0.4),
        Line("aud6", "AUDITOR", "The essential difference is intent to defraud."),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio_red", "heading": "Fraudulent vs wrongful trading",
             "syl": "H1(f)", "ts": 31,
             "cols": [{"title": "Fraudulent", "icon": "mask", "color": "#e4572e",
                       "at": "lex6b",
                       "items": [{"at": ["lex6b", 0.5], "text": "Intent to defraud"},
                                 {"at": ["lex6b", 6.0], "text": "Real dishonesty"},
                                 {"at": "lex6c", "text": "Crime (Companies Act): up to 10 "
                                                         "years"},
                                 {"at": ["lex6c", 7.0], "text": "Civil in liquidation: "
                                                               "anyone knowingly party"}]},
                      {"title": "Wrongful", "icon": "warning", "color": "#f2a541",
                       "at": "lex6d",
                       "items": [{"at": ["lex6d", 0.5], "text": "No dishonesty needed"},
                                 {"at": ["lex6d", 3.0], "text": "Knew or ought to have "
                                                               "concluded: no way out"},
                                 {"at": "lex6e", "text": "Civil only: directors contribute"},
                                 {"at": ["lex6e", 5.0], "text": "Defence: every step to "
                                                               "minimise loss"}]}],
             "vs": True,
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "AUDITOR", "x": 1810, "s": 0.55, "y": 1120, "enter": "aud6",
                       "pose": "clipboard"}]}),

    Scene("s7", "Wrongful trading in court", "", [
        Pause("open", 1.0),
        Line("lex7a", "LEX", "In Re Produce Marketing Consortium, two directors kept a fruit "
             "importing company trading for over a year after they should have seen that "
             "insolvent liquidation was inevitable.", gap=0.3),
        Line("lex7b", "LEX", "They were ordered to contribute to the company's assets. The "
             "court judged them by what a reasonably diligent director, with their own "
             "knowledge and experience, would have concluded.", gap=0.4),
        Sfx("sparkle"),
        Pause("stamp", 1.2),
        Line("lex7c", "LEX", "Other crimes around company life include fraud by false "
             "representation, false accounting, concealing assets before a winding up, and "
             "reusing a failed company's name. And of course, disqualification."),
        Pause("hold", 1.4),
    ], spec={"tpl": "case", "bg": "court", "name": "Re Produce Marketing Consortium Ltd",
             "year": "High Court, England · 1989", "syl": "H1(e)–(f)",
             "rows": [{"at": "lex7a", "label": "Facts", "text": "Directors kept trading long "
                                                                "after insolvency was clear",
                       "color": "#7768ae"},
                      {"at": "lex7b", "label": "Held", "text": "Liable to contribute · "
                                                               "objective + subjective test",
                       "color": "#e4572e"},
                      {"at": "lex7c", "label": "Also", "text": "False representation · false "
                                                               "accounting · phoenix names",
                       "color": "#0f8b8d"}],
             "stamp": {"at": "stamp", "text": "DIRECTORS PAY", "color": "#e4572e"},
             "cast": [{"who": "LEX", "x": 250}]}),

    quiz_scene("s8", "Quick check",
               "What is the defence to the corporate offence of failing to prevent bribery?",
               ["The bribe was small", "Adequate procedures to prevent bribery",
                "The bribe was paid abroad", "The directors didn't know"], 1,
               "Quick check. What is the defence to failing to prevent bribery?",
               "Adequate procedures to prevent bribery.",
               syl="H1(d)"),

    quiz_scene("s9", "Quick check",
               "What is the essential difference between fraudulent and wrongful trading?",
               ["Only wrongful trading is civil", "Fraudulent trading requires intent to "
                "defraud", "Wrongful trading applies to shareholders",
                "There is no difference"], 1,
               "And what is the essential difference between fraudulent and wrongful "
               "trading?",
               "Fraudulent trading requires an intent to defraud.",
               think=4.0, syl="H1(f)"),

    Scene("s10", "Your exam", "", [
        Pause("open", 1.0),
        Line("aud10a", "AUDITOR", "Before we go, let's talk about your exam.", gap=0.3),
        Line("aud10b", "AUDITOR", "Corporate and Business Law Global is a two-hour "
             "computer-based exam. Every question is compulsory, and the pass mark is fifty "
             "percent.", gap=0.3),
        Sfx("pop"),
        Line("aud10c", "AUDITOR", "Section A: twenty-five two-mark questions, and twenty "
             "one-mark questions. Seventy percent of the marks.", gap=0.25),
        Sfx("pop"),
        Line("aud10d", "AUDITOR", "Section B: five multi-task questions, worth six marks "
             "each. Thirty percent.", gap=0.4),
        Line("lex10", "LEX", "So study every area, because the exam covers the whole "
             "syllabus. Practise questions under time pressure, and always ask: what are "
             "the facts, which rule applies, and what is the outcome?"),
        Pause("hold", 1.6),
    ], spec={"tpl": "compare", "bg": "studio_teal", "heading": "LW-GLO: the exam",
             "syl": "2 hours · pass 50%", "ts": 34,
             "cols": [{"title": "Section A · 70%", "icon": "check", "color": "#0f8b8d",
                       "at": "aud10c",
                       "items": [{"at": ["aud10c", 0.5], "text": "25 × 2-mark objective "
                                                               "questions"},
                                 {"at": ["aud10c", 3.0], "text": "20 × 1-mark objective "
                                                               "questions"},
                                 {"at": ["aud10c", 5.0], "text": "Covers the whole syllabus"}]},
                      {"title": "Section B · 30%", "icon": "doc", "color": "#7768ae",
                       "at": "aud10d",
                       "items": [{"at": ["aud10d", 0.5], "text": "5 multi-task questions"},
                                 {"at": ["aud10d", 2.5], "text": "6 marks each"},
                                 {"at": "lex10", "text": "Facts → rule → outcome"}]}],
             "cast": [{"who": "AUDITOR", "x": 250, "pose": "clipboard",
                       "talk_pose": "present"},
                      {"who": "LEX", "x": 1810, "s": 0.55, "y": 1120, "enter": "lex10"}]}),

    recap_scene("s11", [
        ("Bribery: four offences, six principles.", "Bribery Act: 4 offences, 6 principles"),
        ("Failure to prevent tax evasion: three stages.", "Tax evasion: 3 stages"),
        ("Failure to prevent fraud: large organisations.", "ECCTA: failure to prevent "
                                                           "fraud"),
        ("Fraudulent needs intent, wrongful doesn't.", "Fraudulent vs wrongful"),
        ("Two hours, pass mark fifty percent.", "Exam: 2 hours · 50%"),
    ], [
        Line("lex11", "LEX", "And that's the whole syllabus, from who makes the rules, to "
             "the crimes that break them. I'm proud of you all.", gap=0.3),
        Line("kito11", "KITO", "And no bribes for SafariTech. Ever.", gap=0.3),
        Line("cargo11", "CARGO", "Fair winds, and good luck in your exam!", gap=0.6),
    ], next_title="You're exam ready!",
        final_sub="THE LAW BEHIND THE DEAL · ACCA LW-GLO · 29 episodes", next_icon="star"),
]
