"""Episode 17 - The Company's Rulebook.

Syllabus D4(e)-(h): the effect of the constitution (articles as a statutory
contract), contents of the model articles, how articles are changed, objects
and capacity, and controls over company names. UK Companies Act 2006 model.
"""
from ._kit import (DISPLAY_NAMES, SERIES, VOICES, Line, Pause, Scene, Sfx,  # noqa: F401
                   quiz_scene, recap_scene, title_scene)

EPISODE = "Episode 17"
EPISODE_TITLE = "The Company's Rulebook"
SLUG = "episode17_the_companys_rulebook"

SCENES = [
    title_scene(17, EPISODE_TITLE, "Syllabus D4(e)–(h)", ("book", "company")),

    Scene("s1", "What is the constitution?", "", [
        Pause("open", 1.0),
        Line("nia1", "NIA", "Safari Solar Limited exists. So what are its rules?", gap=0.3),
        Line("lex1a", "LEX", "Its constitution. Under the Companies Act, that means the "
             "articles of association, plus certain resolutions and agreements that affect "
             "them, such as special resolutions.", gap=0.3),
        Line("lex1b", "LEX", "The memorandum used to matter a lot. Now it is just a "
             "historical snapshot of who formed the company.", gap=0.3),
        Line("lex1c", "LEX", "And a modern company's objects are unrestricted, unless its "
             "articles restrict them."),
        Pause("hold", 1.2),
    ], spec={"tpl": "flow", "bg": "studio_teal", "heading": "The company's constitution",
             "syl": "D4(e)",
             "nodes": [{"id": "c", "x": 1150, "y": 260, "label": "Constitution",
                        "icon": "book", "color": "#1f3a5f", "at": "lex1a", "w": 300},
                       {"id": "a", "x": 760, "y": 600, "label": "Articles of association",
                        "icon": "scroll", "color": "#0f8b8d", "at": ["lex1a", 3.0], "w": 300},
                       {"id": "r", "x": 1540, "y": 600, "label": "Resolutions and agreements "
                                                               "affecting them",
                        "icon": "ballot", "color": "#7768ae", "at": ["lex1a", 5.5],
                        "w": 320, "h": 210},
                       {"id": "m", "x": 1150, "y": 880, "label": "Memorandum: history only",
                        "icon": "doc", "color": "#8a96a3", "at": "lex1b", "w": 340,
                        "h": 160}],
             "edges": [{"from": "c", "to": "a", "at": ["lex1a", 3.0]},
                       {"from": "c", "to": "r", "at": ["lex1a", 5.5]}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120}],
             "pops": [{"kind": "chip", "at": "lex1c", "x": 1150, "y": 160,
                       "text": "Objects unrestricted unless the articles restrict them",
                       "color": "#e4572e", "size": 32}]}),

    Scene("s2", "The articles as a contract", "", [
        Pause("open", 1.0),
        Line("lex2a", "LEX", "The articles bind the company and its members as if each had "
             "signed them. It is a special statutory contract.", gap=0.3),
        Sfx("pop"),
        Line("lex2b", "LEX", "Members are bound to the company. In Hickman's case, a member "
             "had to take a dispute to arbitration, as the articles required.", gap=0.25),
        Sfx("pop"),
        Line("lex2c", "LEX", "The company is bound to its members. In Pender against "
             "Lushington, a member could enforce his right to vote.", gap=0.25),
        Sfx("pop"),
        Line("lex2d", "LEX", "And members are bound to each other, as in Rayfield against "
             "Hands, where directors had to buy a member's shares.", gap=0.25),
        Sfx("pop"),
        Line("lex2e", "LEX", "But the articles do not bind the company to outsiders, or to "
             "members in another capacity. In Eley's case, a solicitor named in the articles "
             "could not enforce his appointment.", gap=0.4),
        Line("kito2", "KITO", "So writing my job title into the articles doesn't protect it. "
             "I need a separate contract."),
        Pause("hold", 1.4),
    ], spec={"tpl": "flow", "bg": "studio", "heading": "Who can enforce the articles?",
             "syl": "D4(e)",
             "nodes": [{"id": "co", "x": 760, "y": 330, "label": "Company", "icon": "company",
                        "color": "#0f8b8d", "at": "lex2a", "w": 250},
                       {"id": "m1", "x": 1450, "y": 330, "label": "Member", "icon": "person",
                        "color": "#7768ae", "at": "lex2a", "w": 230},
                       {"id": "m2", "x": 1450, "y": 690, "label": "Another member",
                        "icon": "person", "color": "#7768ae", "at": "lex2d", "w": 250},
                       {"id": "out", "x": 760, "y": 690, "label": "Outsider (e.g. solicitor)",
                        "icon": "person", "color": "#e4572e", "at": "lex2e", "w": 300}],
             "edges": [{"from": "m1", "to": "co", "at": "lex2b", "label": "Hickman (1915)",
                        "bend": -40, "ly": -10},
                       {"from": "co", "to": "m1", "at": "lex2c", "label": "Pender (1877)",
                        "bend": -40, "ly": 10},
                       {"from": "m1", "to": "m2", "at": "lex2d", "label": "Rayfield (1960)"},
                       {"from": "out", "to": "co", "at": "lex2e", "label": "Eley (1876): no",
                        "dashed": True, "color": "#e4572e"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "KITO", "x": 1810, "s": 0.55, "y": 1120, "enter": "kito2"}]}),

    Scene("s3", "The model articles", "", [
        Pause("open", 1.0),
        Line("lex3a", "LEX", "If a company does not register its own articles, the model "
             "articles apply automatically, to the extent they are not excluded. There are "
             "versions for private and public companies.", gap=0.3),
        Sfx("pop"),
        Line("lex3b", "LEX", "They give the directors general authority to manage the "
             "business, but members can direct them by special resolution.", gap=0.25),
        Sfx("pop"),
        Line("lex3c", "LEX", "They set out how directors take decisions, and how directors "
             "are appointed: by ordinary resolution, or by the board.", gap=0.25),
        Sfx("pop"),
        Line("lex3d", "LEX", "They deal with shares and distributions. Dividends are declared "
             "by ordinary resolution, but never more than the directors recommend.",
             gap=0.25),
        Sfx("pop"),
        Line("lex3e", "LEX", "They cover members' decisions: general meetings, quorum, "
             "voting, polls and proxies.", gap=0.25),
        Sfx("pop"),
        Line("lex3f", "LEX", "And administrative matters, such as notices, the company seal, "
             "and indemnity and insurance for directors."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "white", "heading": "Inside the model articles",
             "syl": "D4(f)", "row": 116, "ts": 38,
             "items": [{"at": "lex3b", "text": "Directors manage the business",
                        "sub": "Members may direct by special resolution", "icon": "people",
                        "color": "#0f8b8d"},
                       {"at": "lex3c", "text": "Board decisions and appointments",
                        "sub": "Ordinary resolution, or by the directors", "icon": "ballot",
                        "color": "#2b86c5"},
                       {"at": "lex3d", "text": "Shares and dividends",
                        "sub": "Declared by members, capped by the board's recommendation",
                        "icon": "coin", "color": "#f2a541"},
                       {"at": "lex3e", "text": "Members' meetings",
                        "sub": "Quorum · voting · polls · proxies", "icon": "mic",
                        "color": "#7768ae"},
                       {"at": "lex3f", "text": "Administration", "sub": "Notices · seal · "
                                                                        "indemnity, "
                                                                        "insurance",
                        "icon": "stamp", "color": "#3bb273"}],
             "cast": [{"who": "LEX", "x": 250}]}),

    Scene("s4", "Changing the articles", "", [
        Pause("open", 1.0),
        Line("lex4a", "LEX", "Articles can be changed by special resolution, a seventy-five "
             "percent majority. A copy goes to the registrar within fifteen days.", gap=0.3),
        Line("lex4b", "LEX", "Some provisions can be entrenched, needing extra conditions to "
             "change. But nothing can stop the articles ever being changed, if all members "
             "agree.", gap=0.3),
        Line("lex4c", "LEX", "A member cannot be made to take more shares, or pay more, "
             "without written consent.", gap=0.4),
        Line("lex4d", "LEX", "And the change must be made bona fide, for the benefit of the "
             "company as a whole.", gap=0.3),
        Line("lex4e", "LEX", "In Allen against Gold Reefs, a change giving the company a lien "
             "over one member's shares was valid. In Greenhalgh against Arderne Cinemas, the "
             "test was the hypothetical individual member.", gap=0.3),
        Line("lex4f", "LEX", "Expelling a competing member was allowed in Sidebottom. But "
             "forcing out a minority without good reason, in Brown against British Abrasive "
             "Wheel, was not.", gap=0.4),
        Line("aud4", "AUDITOR", "And remember, a valid change can still breach an outside "
             "contract. In Southern Foundries against Shirlaw, the company had to pay "
             "damages."),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio_purple", "heading": "Altering the articles",
             "syl": "D4(g)", "ts": 32,
             "cols": [{"title": "The procedure", "icon": "ballot", "color": "#0f8b8d",
                       "at": "lex4a",
                       "items": [{"at": ["lex4a", 0.5], "text": "Special resolution (75%)"},
                                 {"at": ["lex4a", 4.0], "text": "File within 15 days"},
                                 {"at": "lex4b", "text": "Entrenchment: extra conditions, "
                                                         "never a total bar"},
                                 {"at": "lex4c", "text": "No extra liability without "
                                                         "consent"}]},
                      {"title": "The limits", "icon": "scales", "color": "#e4572e",
                       "at": "lex4d",
                       "items": [{"at": ["lex4d", 0.5], "text": "Bona fide, for the company "
                                                               "as a whole"},
                                 {"at": "lex4e", "text": "Allen v Gold Reefs (1900): valid",
                                  "good": True},
                                 {"at": ["lex4e", 5.5], "text": "Greenhalgh (1951): "
                                                               "hypothetical member"},
                                 {"at": "lex4f", "text": "Sidebottom (1920): expelling a "
                                                         "competitor OK", "good": True},
                                 {"at": ["lex4f", 3.8], "text": "Brown v British Abrasive "
                                                               "Wheel (1919): invalid",
                                  "bad": True}]}],
             "vs": True,
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "AUDITOR", "x": 1810, "s": 0.55, "y": 1120, "enter": "aud4",
                       "pose": "clipboard"}]}),

    Scene("s5", "Objects and capacity", "", [
        Pause("open", 1.0),
        Line("lex5a", "LEX", "In the past, a company acting outside its objects acted ultra "
             "vires, beyond its powers, and the contract was void, as in Ashbury Railway "
             "against Riche.", say="In the past, a company acting outside its objects acted "
             "ultra vye-reez, beyond its powers, and the contract was void, as in Ashbury "
             "Railway against Riche.", gap=0.3),
        Line("lex5b", "LEX", "Today, a company's capacity cannot be challenged because of "
             "anything in its constitution.", gap=0.3),
        Line("lex5c", "LEX", "And for a third party dealing in good faith, the directors' "
             "power to bind the company is free of any limit in the constitution. Good faith "
             "is presumed, and the third party need not check.", gap=0.3),
        Line("lex5d", "LEX", "Inside the company, though, members can still try to stop a "
             "planned act beyond the objects, and directors who exceed their powers may be "
             "liable.", gap=0.4),
        Line("nia5", "NIA", "So outsiders are protected, and insiders are held to the rules."),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio", "heading": "Ultra vires today",
             "syl": "D4(e)", "ts": 33,
             "cols": [{"title": "Outsiders", "icon": "shield", "color": "#3bb273",
                       "at": "lex5b",
                       "items": [{"at": ["lex5b", 0.5], "text": "Capacity can't be "
                                                               "challenged",
                                  "good": True},
                                 {"at": "lex5c", "text": "Directors' power free of "
                                                         "constitutional limits",
                                  "good": True},
                                 {"at": ["lex5c", 6.0], "text": "Good faith presumed · no "
                                                               "duty to check",
                                  "good": True}]},
                      {"title": "Insiders", "icon": "people", "color": "#e4572e",
                       "at": "lex5d",
                       "items": [{"at": ["lex5d", 0.5], "text": "Members can restrain a "
                                                               "planned act"},
                                 {"at": ["lex5d", 4.0], "text": "Directors liable for "
                                                               "exceeding powers"}]}],
             "vs": True,
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia5"}],
             "pops": [{"kind": "chip", "at": "lex5a", "until": "lex5b", "x": 1180, "y": 930,
                       "text": "Old law: Ashbury Railway v Riche (1875)", "color": "#1f3a5f",
                       "size": 32}]}),

    Scene("s6", "What's in a name?", "", [
        Pause("open", 1.0),
        Line("kito6", "KITO", "I want to call us Safari Royal Bank of Solar!", gap=0.4),
        Line("lex6a", "LEX", "Not so fast. A company name has rules.", gap=0.3),
        Sfx("pop"),
        Line("lex6b", "LEX", "It must end with Limited, or p l c, for a public company.",
             say="It must end with Limited, or P.L.C., for a public company.", gap=0.25),
        Sfx("pop"),
        Line("lex6c", "LEX", "It cannot be the same as a name already on the register.",
             gap=0.25),
        Sfx("pop"),
        Line("lex6d", "LEX", "It cannot be offensive, or suggest a criminal purpose. And "
             "sensitive words, like bank or royal, need approval.", gap=0.25),
        Sfx("pop"),
        Line("lex6e", "LEX", "The registrar can order a change within twelve months if the "
             "name is too like an existing one, within five years if misleading information "
             "was given, and at any time if the name misleads the public about its "
             "activities.", gap=0.25),
        Sfx("pop"),
        Line("lex6f", "LEX", "A company names adjudicator hears complaints about names taken "
             "to exploit another's goodwill. And a business can sue for passing off, as in "
             "Ewing against Buttercup Margarine.", gap=0.4),
        Line("lex6g", "LEX", "To change its name, a company normally passes a special "
             "resolution, and receives a new certificate of incorporation.", gap=0.3),
        Line("kito6b", "KITO", "Fine. Safari Solar Limited it is."),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "heading": "Company names", "syl": "D4(h)",
             "row": 112, "ts": 38,
             "items": [{"at": "lex6b", "text": "Ends with Limited or plc", "icon": "tag",
                        "color": "#0f8b8d"},
                       {"at": "lex6c", "text": "Not the same as an existing name",
                        "icon": "cross", "color": "#e4572e"},
                       {"at": "lex6d", "text": "Nothing offensive · sensitive words approved",
                        "icon": "warning", "color": "#f2a541"},
                       {"at": "lex6e", "text": "Ordered change: 12 months · 5 years · any time",
                        "icon": "calendar", "color": "#7768ae"},
                       {"at": "lex6f", "text": "Adjudicator · passing off",
                        "sub": "Ewing v Buttercup Margarine (1917)", "icon": "scales",
                        "color": "#2b86c5"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "KITO", "x": 1810, "s": 0.55, "y": 1120, "mood": "excited"}],
             "pops": [{"kind": "chip", "at": "lex6g", "until": "kito6b", "x": 1190, "y": 950,
                       "text": "Change of name: special resolution → new certificate",
                       "color": "#3bb273", "size": 32}]}),

    quiz_scene("s7", "Quick check",
               "A solicitor's appointment is written into a company's articles. The company "
               "dismisses him. Can he enforce the articles?",
               ["Yes, the articles are a contract with everyone",
                "No, the articles don't bind the company to outsiders",
                "Yes, but only with members' consent", "Only if he holds 25% of the shares"],
               1,
               "Quick check. A solicitor's appointment is in the articles, and he is "
               "dismissed. Can he enforce the articles?",
               "No. The articles do not bind the company to outsiders.",
               why="Eley v Positive Government Security Life Assurance (1876)",
               syl="D4(e)"),

    quiz_scene("s8", "Quick check",
               "What majority is needed to change a company's articles?",
               ["A simple majority", "Two-thirds", "75% (special resolution)",
                "Every member"], 2,
               "And what majority is needed to change the articles?",
               "Seventy-five percent, a special resolution.",
               think=4.0, syl="D4(g)"),

    recap_scene("s9", [
        ("Constitution: articles plus resolutions.", "Constitution = articles + "
                                                      "resolutions"),
        ("Articles bind company and members, not outsiders.", "Articles: not outsiders"),
        ("Model articles fill the gaps.", "Model articles by default"),
        ("Change by special resolution, in good faith.", "Change: 75%, bona fide"),
        ("Names: Ltd or plc, no copies, no tricks.", "Names: Ltd/plc, unique"),
    ], [
        Line("lex9", "LEX", "Next time, we follow the money in: shares, share classes, and "
             "how new shares are issued.", gap=0.3),
        Line("kito9", "KITO", "Shares! Now we're talking!", gap=0.6),
    ], next_ep=18, next_title="Share Capital", next_icon="pie"),
]
