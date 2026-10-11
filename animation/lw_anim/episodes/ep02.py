"""Episode 2 - Three Families of Law.

Syllabus A1(a), A1(d), A2(a)-(b): economic, political and legal systems;
common law, civil law and Sharia law; conflict of laws and why international
rules are needed. Setting: SafariTech, Dar es Salaam, plans to buy from Germany
and sell into Kenya and the UAE.
"""
from ._kit import (DISPLAY_NAMES, SERIES, VOICES, Line, Pause, Scene, Sfx,  # noqa: F401
                   quiz_scene, recap_scene, title_scene)

EPISODE = "Episode 2"
EPISODE_TITLE = "Three Families of Law"
SLUG = "episode02_three_families_of_law"

SCENES = [
    title_scene(2, EPISODE_TITLE, "Syllabus A1 · A2", ("globe", "book")),

    Scene("s1", "SafariTech, Dar es Salaam", "", [
        Pause("open", 1.0),
        Line("kito1", "KITO", "Big news! We're buying machines from Hamburg, and selling "
             "our kits in Nairobi and Dubai.", gap=0.4),
        Line("nia1", "NIA", "Three countries, Kito. Do the same rules apply in all of them?",
             gap=0.4),
        Sfx("pop"),
        Line("lex1", "LEX", "No, and that is today's lesson. Every country's law grows out "
             "of its politics and its economy.", gap=0.4),
        Line("lex1b", "LEX", "So before we compare legal systems, let's look at how an "
             "economy decides who owns what."),
        Pause("hold", 1.2),
    ], spec={"tpl": "talk", "bg": "harbour", "syl": "A1(a)",
             "cast": [{"who": "NIA", "x": 700, "s": 0.92, "y": 1020},
                      {"who": "KITO", "x": 1180, "s": 0.95, "y": 1020, "enter": 0.6,
                       "poses": [[0, "cheer"], ["kito1$", "hips"]], "mood": "excited"},
                      {"who": "LEX", "x": 1620, "s": 0.9, "y": 1020, "enter": "lex1"}],
             "pops": [{"kind": "icon", "icon": "factory", "x": 380, "y": 260, "s": 1.1,
                       "at": ["kito1", 1.4], "label": "Hamburg", "color": "#3d405b",
                       "until": "lex1"},
                      {"kind": "icon", "icon": "company", "x": 640, "y": 260, "s": 1.1,
                       "at": ["kito1", 2.8], "label": "Nairobi", "color": "#3bb273",
                       "until": "lex1"},
                      {"kind": "icon", "icon": "globe", "x": 900, "y": 260, "s": 1.1,
                       "at": ["kito1", 3.6], "label": "Dubai", "color": "#f2a541",
                       "until": "lex1"}]}),

    Scene("s2", "Market, planned and mixed", "", [
        Pause("open", 1.0),
        Line("lex2a", "LEX", "In a market economy, supply and demand set prices, and most "
             "wealth is held privately.", gap=0.4),
        Line("lex2b", "LEX", "In a planned economy, the state allocates resources and fixes "
             "prices.", gap=0.3),
        Line("lex2c", "LEX", "Tanzania tried this after the Arusha Declaration of 1967, "
             "with the Ujamaa policy of state ownership.",
             say="Tanzania tried this after the Arusha Declaration of 1967, with the "
                 "Oo-jah-mah policy of state ownership.", gap=0.4),
        Line("lex2d", "LEX", "A mixed economy combines both. Markets set most prices, but "
             "government steps in with taxes, subsidies and regulation.", gap=0.3),
        Line("lex2e", "LEX", "Since the reforms of the 1980s and 90s, Tanzania and Kenya "
             "are both mixed economies.", gap=0.5),
        Line("nia2", "NIA", "And the law has to fit whichever system a country chooses.",
             gap=0.3),
        Line("lex2f", "LEX", "Exactly. Politics decides who makes the law. The law then "
             "protects property and enforces contracts, which is what investors look for."),
        Pause("hold", 1.6),
    ], spec={"tpl": "compare", "bg": "studio_teal", "heading": "How an economy allocates resources",
             "syl": "A1(a)", "ts": 36,
             "cols": [{"title": "Market", "icon": "chart", "color": "#0f8b8d", "at": "lex2a",
                       "items": [{"at": ["lex2a", 1.5], "text": "Supply and demand set prices"},
                                 {"at": ["lex2a", 3.5], "text": "Wealth held privately"}]},
                      {"title": "Planned", "icon": "parliament", "color": "#7768ae",
                       "at": "lex2b",
                       "items": [{"at": ["lex2b", 1.5], "text": "State allocates resources"},
                                 {"at": ["lex2b", 2.8], "text": "Prices fixed centrally"},
                                 {"at": "lex2c", "text": "Tanzania: Ujamaa after the "
                                                         "1967 Arusha Declaration"}]},
                      {"title": "Mixed", "icon": "scales", "color": "#e4572e", "at": "lex2d",
                       "items": [{"at": ["lex2d", 1.5], "text": "Markets set most prices"},
                                 {"at": ["lex2d", 3.2], "text": "Taxes, subsidies, regulation"},
                                 {"at": "lex2e", "text": "Tanzania and Kenya today"}]}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1780, "s": 0.6, "y": 1110, "enter": "nia2"}]}),

    Scene("s3", "The common law family", "", [
        Pause("open", 1.0),
        Line("lex3a", "LEX", "First family: common law. It began in England after 1066, "
             "when the king's judges made local customs common to the whole country.",
             gap=0.4),
        Sfx("pop"),
        Line("lex3b", "LEX", "Its cornerstone is judicial precedent. Judges follow the "
             "reasoning of earlier, higher courts.", gap=0.4),
        Sfx("pop"),
        Line("lex3c", "LEX", "When money damages were not enough, equity grew up beside it, "
             "with remedies like injunctions and specific performance.", gap=0.4),
        Sfx("pop"),
        Line("lex3d", "LEX", "The Judicature Acts of the 1870s merged the courts. Where "
             "common law and equity conflict, equity prevails.", gap=0.4),
        Sfx("pop"),
        Line("lex3e", "LEX", "Through colonial history, the common law was received into "
             "East Africa. Tanzania and Kenya still use it today, alongside their own "
             "statutes and customary law.", gap=0.4),
        Line("kito3", "KITO", "So our judges in Dar es Salaam follow precedent too!"),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "heading": "Common law", "syl": "A1(d)(i)",
             "items": [{"at": "lex3a", "text": "Born in England after 1066",
                        "sub": "King's judges unify local customs", "icon": "crown"},
                       {"at": "lex3b", "text": "Judicial precedent",
                        "sub": "Follow the reasoning of higher courts", "icon": "ladder"},
                       {"at": "lex3c", "text": "Equity fills the gaps",
                        "sub": "Injunctions, specific performance, rescission",
                        "icon": "scales"},
                       {"at": "lex3d", "text": "Judicature Acts 1873–75",
                        "sub": "Courts merged · equity prevails in a conflict",
                        "icon": "court"},
                       {"at": "lex3e", "text": "Received in Tanzania and Kenya",
                        "sub": "Common law + local statutes + customary law",
                        "icon": "globe"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "KITO", "x": 1760, "s": 0.62, "y": 1110, "enter": "kito3",
                       "mood": "excited"}]}),

    Scene("s4", "How precedent binds", "", [
        Pause("open", 1.0),
        Line("lex4a", "LEX", "A precedent binds a later court only when four things are "
             "true.", gap=0.3),
        Sfx("pop"),
        Line("lex4b", "LEX", "It is a point of law, not a point of fact.", gap=0.25),
        Sfx("pop"),
        Line("lex4c", "LEX", "It is part of the ratio decidendi, the reason for the decision.",
             say="It is part of the ratio, dee-sy-dendy, the reason for the decision.",
             gap=0.25),
        Sfx("pop"),
        Line("lex4d", "LEX", "The material facts are sufficiently similar.", gap=0.25),
        Sfx("pop"),
        Line("lex4e", "LEX", "And the earlier court was higher in the court hierarchy.",
             gap=0.5),
        Line("nia4", "NIA", "And when can a judge avoid it?", gap=0.3),
        Line("lex4f", "LEX", "By distinguishing the facts, or if the earlier ruling was made "
             "per incuriam, meaning carelessly, or was too wide or too obscure, or has since "
             "been overruled.",
             say="By distinguishing the facts, or if the earlier ruling was made per "
                 "in-cure-ee-am, meaning carelessly, or was too wide or too obscure, or has "
                 "since been overruled."),
        Pause("hold", 1.6),
    ], spec={"tpl": "compare", "bg": "studio", "heading": "Judicial precedent", "syl": "A1(d)",
             "ts": 36,
             "cols": [{"title": "Binding when…", "icon": "check", "color": "#3bb273",
                       "at": "lex4a",
                       "items": [{"at": "lex4b", "text": "It is a point of law", "good": True},
                                 {"at": "lex4c", "text": "It is part of the ratio decidendi "
                                                         "(obiter is only persuasive)",
                                  "good": True},
                                 {"at": "lex4d", "text": "Material facts are similar",
                                  "good": True},
                                 {"at": "lex4e", "text": "It comes from a higher court",
                                  "good": True}]},
                      {"title": "Avoided when…", "icon": "cross", "color": "#e4572e",
                       "at": "nia4",
                       "items": [{"at": ["lex4f", 0.2], "text": "Facts are distinguished",
                                  "bad": True},
                                 {"at": ["lex4f", 2.4], "text": "Made per incuriam "
                                                                "(without care)", "bad": True},
                                 {"at": ["lex4f", 5.2], "text": "Too wide or too obscure",
                                  "bad": True},
                                 {"at": ["lex4f", 7.0], "text": "Since overruled",
                                  "bad": True}]}],
             "vs": True,
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1790, "s": 0.58, "y": 1120, "enter": "nia4"}]}),

    Scene("s5", "The civil law family", "", [
        Pause("open", 1.0),
        Sfx("whoosh"),
        Pause("hans_in", 0.6),
        Line("hans5", "HANS", "Guten Tag! In Germany, our judges start with the code, not "
             "with old cases.", gap=0.4),
        Line("lex5a", "LEX", "That is the second family: civil law. It grew from Roman law, "
             "and today it is written down in comprehensive codes.", gap=0.3),
        Line("lex5b", "LEX", "France's Civil Code of 1804, and Germany's Civil Code of 1900, "
             "are the famous examples.", gap=0.4),
        Line("lex5c", "LEX", "Judges apply the code to the facts. Earlier decisions guide "
             "them, but they are not strictly binding.", gap=0.3),
        Line("lex5d", "LEX", "Trials tend to be inquisitorial, with the judge leading the "
             "questioning, and legal scholars' writings carry real weight.", gap=0.4),
        Line("nia5", "NIA", "So in common law the judge is more like a referee, but in civil "
             "law more like an investigator."),
        Pause("hold", 1.6),
    ], spec={"tpl": "compare", "bg": "studio_purple", "heading": "Common law vs civil law",
             "syl": "A1(d)(ii)", "ts": 36, "x0": 480, "x1": 1520,
             "cols": [{"title": "Common law", "icon": "court", "color": "#0f8b8d",
                       "at": "lex5a",
                       "items": [{"at": ["lex5a", 0.4], "text": "Built case by case"},
                                 {"at": ["lex5c", 0.2], "text": "Precedent binds"},
                                 {"at": ["lex5d", 0.2], "text": "Adversarial trial"},
                                 {"at": "nia5", "text": "Judge as referee"}]},
                      {"title": "Civil law", "icon": "book", "color": "#7768ae", "at": "lex5a",
                       "items": [{"at": ["lex5a", 2.5], "text": "Roman roots, written codes"},
                                 {"at": "lex5b", "text": "France 1804 · Germany 1900"},
                                 {"at": ["lex5c", 2.0], "text": "Cases guide, don't bind"},
                                 {"at": ["lex5d", 0.8], "text": "Inquisitorial trial"},
                                 {"at": ["nia5", 2.5], "text": "Judge as investigator"}]}],
             "vs": True,
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "HANS", "x": 1720, "s": 0.8, "y": 1060, "enter": "hans_in",
                       "pose": "idle", "talk_pose": "present"}]}),

    Scene("s6", "The Sharia law family", "", [
        Pause("open", 1.0),
        Line("lex6a", "LEX", "The third family is Sharia law. The word means the path to a "
             "watering place.", say="The third family is Sharee-ah law. The word means "
             "the path to a watering place.", gap=0.4),
        Sfx("pop"),
        Line("lex6b", "LEX", "Its primary source is the Quran.", say="Its primary source is "
             "the Koran.", gap=0.25),
        Sfx("pop"),
        Line("lex6c", "LEX", "Next comes the Sunnah, the accepted practice of the Prophet.",
             say="Next comes the Sunnah, the accepted practice of the Prophet.", gap=0.4),
        Sfx("pop"),
        Line("lex6d", "LEX", "Where these are silent, scholars use ijtihad, independent "
             "reasoning. Ijma is the consensus of scholars.",
             say="Where these are silent, scholars use ij-tee-had, independent reasoning. "
                 "Ij-mah is the consensus of scholars.", gap=0.25),
        Sfx("pop"),
        Line("lex6e", "LEX", "And qiyas is reasoning by analogy. It is the nearest thing to "
             "judicial precedent.", say="And kee-yas is reasoning by analogy. It is the "
             "nearest thing to judicial precedent.", gap=0.4),
        Sfx("pop"),
        Line("lex6f", "LEX", "The schools of law, such as Hanafi, Maliki, Shafi'i and "
             "Hanbali, add detailed interpretation.",
             say="The schools of law, such as Hanafi, Maliki, Shafi-ee and Hanbali, add "
                 "detailed interpretation.", gap=0.4),
        Line("lex6g", "LEX", "Closer to home, Kadhi's courts in Kenya and Zanzibar apply "
             "Islamic law to personal matters such as marriage and inheritance.",
             say="Closer to home, Kaadi's courts in Kenya and Zanzibar apply Islamic law to "
                 "personal matters such as marriage and inheritance.", gap=0.4),
        Line("kito6", "KITO", "And in business, interest is forbidden, right? That matters "
             "for our Dubai customers.", gap=0.3),
        Line("lex6h", "LEX", "Right. Riba, or interest, is prohibited, so Islamic finance "
             "shares profit instead.", say="Right. Ree-ba, or interest, is prohibited, so "
             "Islamic finance shares profit instead."),
        Pause("hold", 1.6),
    ], spec={"tpl": "board", "style": "white", "heading": "Sharia law", "syl": "A1(d)(iii)",
             "row": 112, "ts": 38,
             "items": [{"at": "lex6b", "text": "Quran", "sub": "The primary source",
                        "icon": "book", "color": "#3bb273"},
                       {"at": "lex6c", "text": "Sunnah", "sub": "Accepted practice of the "
                                                               "Prophet", "icon": "scroll",
                        "color": "#0f8b8d"},
                       {"at": "lex6d", "text": "Ijtihad and ijma",
                        "sub": "Independent reasoning · consensus of scholars",
                        "icon": "people", "color": "#7768ae"},
                       {"at": "lex6e", "text": "Qiyas", "sub": "Analogy: the nearest thing "
                                                              "to precedent",
                        "icon": "signpost", "color": "#e4572e"},
                       {"at": "lex6f", "text": "Schools of law",
                        "sub": "Hanafi · Maliki · Shafi'i · Hanbali (and Shia)",
                        "icon": "brain", "color": "#f2a541"},
                       {"at": "lex6g", "text": "Kadhi's courts: Kenya, Zanzibar",
                        "sub": "Muslim personal law: marriage, inheritance",
                        "icon": "court", "color": "#2b86c5"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "KITO", "x": 1790, "s": 0.55, "y": 1120, "enter": "kito6",
                       "mood": "thinking"}],
             "pops": [{"kind": "card", "at": "lex6h", "x": 1190, "y": 470, "w": 760,
                       "h": 220, "title": "Riba is prohibited",
                       "body": "Islamic finance shares profit and risk instead of charging "
                               "interest", "color": "#e4572e", "dim": True}]}),

    Scene("s7", "When laws collide", "", [
        Pause("open", 1.0),
        Line("nia7a", "NIA", "So if our German machine is faulty, whose law decides?",
             gap=0.4),
        Line("lex7a", "LEX", "That is the conflict of laws. In any cross-border dispute, "
             "ask three questions.", gap=0.3),
        Sfx("pop"),
        Line("lex7b", "LEX", "Which country's courts have jurisdiction?", gap=0.25),
        Sfx("pop"),
        Line("lex7c", "LEX", "Which country's law applies to the contract?", gap=0.25),
        Sfx("pop"),
        Line("lex7d", "LEX", "And will a judgment from one country be enforced in the other?",
             gap=0.5),
        Line("lex7e", "LEX", "The simplest protection is a clause in the contract choosing "
             "the law, and the court or arbitration forum.", gap=0.4),
        Line("lex7f", "LEX", "The bigger answer is international harmonisation: shared "
             "rules, so traders face fewer surprises."),
        Pause("hold", 1.4),
    ], spec={"tpl": "flow", "bg": "studio_teal", "heading": "Conflict of laws: three questions",
             "syl": "A2(a)",
             "nodes": [{"id": "tz", "x": 700, "y": 330, "label": "SafariTech (Tanzania)",
                        "icon": "company", "color": "#0f8b8d", "at": "nia7a", "w": 290},
                       {"id": "de", "x": 1600, "y": 330, "label": "Hans GmbH (Germany)",
                        "icon": "factory", "color": "#3d405b", "at": "nia7a", "w": 290},
                       {"id": "q1", "x": 760, "y": 690, "label": "Which court?",
                        "icon": "court", "color": "#7768ae", "at": "lex7b"},
                       {"id": "q2", "x": 1150, "y": 690, "label": "Which law?",
                        "icon": "book", "color": "#e4572e", "at": "lex7c"},
                       {"id": "q3", "x": 1540, "y": 690, "label": "Enforced abroad?",
                        "icon": "gavel", "color": "#f2a541", "at": "lex7d"}],
             "edges": [{"from": "tz", "to": "de", "at": ["nia7a", 0.8], "label": "Faulty machine?",
                        "color": "#e4572e", "dashed": True}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1780, "s": 0.6, "y": 1110}],
             "pops": [{"kind": "card", "at": "lex7e", "until": "lex7f", "x": 1150, "y": 500,
                       "w": 820, "h": 220, "title": "Choice-of-law clause",
                       "body": "“This contract is governed by … and disputes go to …”",
                       "color": "#0f8b8d", "dim": True},
                      {"kind": "card", "at": "lex7f", "x": 1150, "y": 500, "w": 820, "h": 220,
                       "title": "Harmonisation", "body": "Shared international rules mean "
                                                         "fewer surprises", "color": "#3bb273",
                       "dim": True}]}),

    Scene("s8", "Treaties, conventions and model laws", "", [
        Pause("open", 1.0),
        Line("lex8a", "LEX", "Harmonisation comes in different strengths.", gap=0.3),
        Sfx("pop"),
        Line("lex8b", "LEX", "A treaty or convention binds the states that ratify it, like "
             "the UN Sales Convention, which we'll meet in Episode 5.", gap=0.3),
        Sfx("pop"),
        Line("lex8c", "LEX", "A model law is a template. Each state decides whether to adopt "
             "it, and can adapt it, like the UNCITRAL Model Law on arbitration.",
             say="A model law is a template. Each state decides whether to adopt it, and can "
                 "adapt it, like the Uncitral Model Law on arbitration.", gap=0.3),
        Sfx("pop"),
        Line("lex8d", "LEX", "Model codes and principles, like the UNIDROIT Principles, guide "
             "parties and lawmakers without binding anyone.",
             say="Model codes and principles, like the Unee-droit Principles, guide parties "
                 "and lawmakers without binding anyone.", gap=0.3),
        Sfx("pop"),
        Line("lex8e", "LEX", "And uniform trade terms like Incoterms bind only because the "
             "parties write them into their contract.",
             say="And uniform trade terms like Inco-terms bind only because the parties "
                 "write them into their contract.", gap=0.5),
        Line("nia8", "NIA", "So a treaty binds states, but a model law only binds a country "
             "that chooses to adopt it."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "white", "layout": "grid", "cols": 2,
             "heading": "Tools of harmonisation", "syl": "A2(b)", "cell_h": 320, "ts": 34,
             "items": [{"at": "lex8b", "text": "Treaty / convention",
                        "sub": "Binds states that ratify · e.g. CISG", "icon": "seal",
                        "color": "#0f8b8d"},
                       {"at": "lex8c", "text": "Model law",
                        "sub": "Template states may adopt · e.g. arbitration", "icon": "doc",
                        "color": "#7768ae"},
                       {"at": "lex8d", "text": "Model code / principles",
                        "sub": "Guidance only · e.g. UNIDROIT Principles", "icon": "bulb",
                        "color": "#f2a541"},
                       {"at": "lex8e", "text": "Uniform contract terms",
                        "sub": "Bind by agreement · e.g. Incoterms", "icon": "contract",
                        "color": "#e4572e"}],
             "cast": [{"who": "LEX", "x": 250}]}),

    quiz_scene("s9", "Quick check",
               "In Sharia law, which method is the nearest equivalent to judicial precedent?",
               ["Ijma", "Qiyas", "Taqlid", "Sunnah"], 1,
               "Quick check. In Sharia law, which method is the nearest equivalent to "
               "judicial precedent?",
               "Qiyas: reasoning by analogy.",
               why=("Qiyas applies an accepted ruling to a similar new situation",
                    "Qiyas applies an accepted ruling to a new situation that is similar. "
                    "Ijma is consensus, not analogy."),
               syl="A1(d)"),

    recap_scene("s10", [
        ("Market, planned and mixed economies.", "Market · planned · mixed"),
        ("Common law: precedent, plus equity.", "Common law + equity"),
        ("Civil law: written codes.", "Civil law = codes"),
        ("Sharia: Quran, Sunnah, ijma and qiyas.", "Sharia: Quran · Sunnah · ijma · qiyas",
         "Sharee-ah: Koran, Sunnah, ij-mah and kee-yas."),
        ("Conflict of laws, and treaties versus model laws.",
         "Conflict of laws · treaty vs model law"),
    ], [
        Line("lex10", "LEX", "Well done. Next time, we meet the global rule-makers: the UN, "
             "the WTO, the ICC and their friends.", gap=0.3),
        Line("kito10", "KITO", "Rule-makers? I just want to sell my kits!", gap=0.6),
    ], next_ep=3, next_title="The Global Rule-Makers", next_icon="globe"),
]
