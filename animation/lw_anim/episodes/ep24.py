"""Episode 24 - Meetings and Resolutions.

Syllabus F3(a)-(c): general meetings and AGMs; ordinary, special and written
resolutions; calling and conducting meetings (notice, quorum, voting, proxies).
UK Companies Act 2006 model. Setting: Safari Solar Limited's shareholders
(now including Hans) meet for the first time.
"""
from ._kit import (DISPLAY_NAMES, SERIES, VOICES, Line, Pause, Scene, Sfx,  # noqa: F401
                   quiz_scene, recap_scene, title_scene)

EPISODE = "Episode 24"
EPISODE_TITLE = "Meetings and Resolutions"
SLUG = "episode24_meetings_and_resolutions"

SCENES = [
    title_scene(24, EPISODE_TITLE, "Syllabus F3", ("ballot", "mic")),

    Scene("s1", "The members gather", "", [
        Pause("open", 1.0),
        Line("hans1", "HANS", "I bought ten percent of Safari Solar. So when is the annual "
             "general meeting?", gap=0.4),
        Line("kito1", "KITO", "Do private companies even have those?", gap=0.4),
        Line("lex1", "LEX", "Good question. The members make their decisions through "
             "general meetings and resolutions. Let's see the rules."),
        Pause("hold", 1.2),
    ], spec={"tpl": "talk", "bg": "boardroom", "syl": "F3",
             "cast": [{"who": "HANS", "x": 1350, "y": 1000, "s": 0.85},
                      {"who": "KITO", "x": 960, "y": 1000, "s": 0.88, "mood": "thinking",
                       "talk_pose": "shrug"},
                      {"who": "NIA", "x": 640, "y": 1000, "s": 0.85},
                      {"who": "LEX", "x": 230, "y": 1040, "s": 0.85, "enter": "lex1",
                       "from": "left"}]}),

    Scene("s2", "AGMs and general meetings", "", [
        Pause("open", 1.0),
        Line("lex2a", "LEX", "A general meeting is any meeting of the company's members.",
             gap=0.3),
        Line("lex2b", "LEX", "A public company must also hold an annual general meeting, "
             "within six months after its financial year end.", gap=0.3),
        Line("lex2c", "LEX", "Typical AGM business: laying the accounts and reports, "
             "electing directors, appointing the auditor, and declaring a dividend.",
             gap=0.4),
        Line("lex2d", "LEX", "A private company does not need an AGM, unless its articles "
             "require one. It can take most decisions by written resolution instead.",
             gap=0.4),
        Line("hans2", "HANS", "So I may never get a meeting, but I still get a vote on the "
             "resolutions."),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio", "heading": "Meetings of members",
             "syl": "F3(a)", "ts": 33,
             "cols": [{"title": "Public company", "icon": "company", "color": "#7768ae",
                       "at": "lex2b",
                       "items": [{"at": ["lex2b", 0.5], "text": "AGM required"},
                                 {"at": ["lex2b", 3.0], "text": "Within 6 months of "
                                                               "year end"},
                                 {"at": "lex2c", "text": "Accounts · directors · auditor · "
                                                         "dividend"}]},
                      {"title": "Private company", "icon": "house", "color": "#0f8b8d",
                       "at": "lex2d",
                       "items": [{"at": ["lex2d", 0.5], "text": "No AGM needed"},
                                 {"at": ["lex2d", 2.0], "text": "Unless the articles "
                                                               "require one"},
                                 {"at": ["lex2d", 4.5], "text": "Written resolutions "
                                                               "instead"}]}],
             "vs": True,
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "HANS", "x": 1810, "s": 0.55, "y": 1120, "enter": "hans2"}],
             "pops": [{"kind": "chip", "at": "lex2a", "until": "lex2b", "x": 1180, "y": 950,
                       "text": "General meeting = any meeting of members", "color": "#1f3a5f",
                       "size": 34}]}),

    Scene("s3", "Who can call a meeting?", "", [
        Pause("open", 1.0),
        Line("lex3a", "LEX", "Normally, the directors call general meetings.", gap=0.3),
        Line("lex3b", "LEX", "But members holding at least five percent of the paid-up "
             "voting capital can require them to. The directors must call it within "
             "twenty-one days, for a date within twenty-eight days of the notice.", gap=0.3),
        Line("lex3c", "LEX", "If they don't, those members can call it themselves, at the "
             "company's expense.", gap=0.3),
        Line("lex3d", "LEX", "A court can order a meeting where it's impractical to call one, "
             "for example to break a deadlock.", gap=0.3),
        Line("lex3e", "LEX", "And a resigning auditor can require one too.", gap=0.4),
        Line("hans3", "HANS", "Ten percent! So I could force a meeting if I needed to."),
        Pause("hold", 1.4),
    ], spec={"tpl": "flow", "bg": "studio_teal", "heading": "Calling a general meeting",
             "syl": "F3(c)",
             "nodes": [{"id": "gm", "x": 1150, "y": 520, "label": "General meeting",
                        "icon": "mic", "color": "#1f3a5f", "at": "lex3a", "w": 300},
                       {"id": "d", "x": 700, "y": 260, "label": "Directors", "icon": "people",
                        "color": "#0f8b8d", "at": "lex3a", "w": 250},
                       {"id": "m", "x": 1600, "y": 260, "label": "Members with 5%+",
                        "icon": "pie", "color": "#7768ae", "at": "lex3b", "w": 270},
                       {"id": "c", "x": 700, "y": 800, "label": "The court", "icon": "court",
                        "color": "#f2a541", "at": "lex3d", "w": 250},
                       {"id": "a", "x": 1600, "y": 800, "label": "Resigning auditor",
                        "icon": "magnifier", "color": "#e4572e", "at": "lex3e", "w": 280}],
             "edges": [{"from": "d", "to": "gm", "at": ["lex3a", 0.5], "label": "usually"},
                       {"from": "m", "to": "d", "at": ["lex3b", 1.5], "label": "require",
                        "bend": -40},
                       {"from": "m", "to": "gm", "at": "lex3c", "label": "if directors don't",
                        "dashed": True},
                       {"from": "c", "to": "gm", "at": ["lex3d", 0.5]},
                       {"from": "a", "to": "gm", "at": ["lex3e", 0.5]}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "HANS", "x": 1810, "s": 0.55, "y": 1120, "enter": "hans3"}],
             "pops": [{"kind": "chip", "at": ["lex3b", 5.0], "until": "lex3c", "x": 1150,
                       "y": 960, "text": "Call within 21 days · hold within 28 days of "
                                         "notice", "color": "#1f3a5f", "size": 30}]}),

    Scene("s4", "Notice periods", "", [
        Pause("open", 1.0),
        Line("lex4a", "LEX", "Members must get proper notice.", gap=0.25),
        Sfx("pop"),
        Line("lex4b", "LEX", "At least fourteen clear days for a general meeting.", gap=0.2),
        Sfx("pop"),
        Line("lex4c", "LEX", "Twenty-one days for a public company's AGM.", gap=0.2),
        Sfx("pop"),
        Line("lex4d", "LEX", "Short notice is possible, if enough members agree: ninety "
             "percent in a private company, ninety-five in a public one. For a public "
             "company's AGM, every member must agree.", gap=0.2),
        Sfx("pop"),
        Line("lex4e", "LEX", "And special notice, twenty-eight days to the company, for "
             "resolutions to remove a director or an auditor.", gap=0.4),
        Line("lex4f", "LEX", "The notice states the date, time, place, and general nature of "
             "the business, the full text of any special resolution, and members' rights to "
             "appoint proxies."),
        Pause("hold", 1.4),
    ], spec={"tpl": "timeline", "bg": "studio", "heading": "How much notice?",
             "syl": "F3(c)", "cw": 300,
             "events": [{"at": "lex4b", "label": "14 clear days", "sub": "General meeting",
                         "icon": "calendar", "color": "#0f8b8d"},
                        {"at": "lex4c", "label": "21 days", "sub": "Public company AGM",
                         "icon": "company", "color": "#7768ae"},
                        {"at": "lex4d", "label": "Short notice", "sub": "90% private · 95% "
                                                                        "public · plc AGM "
                                                                        "100%",
                         "icon": "clock", "color": "#f2a541"},
                        {"at": "lex4e", "label": "Special notice", "sub": "28 days: remove "
                                                                          "director/auditor",
                         "icon": "warning", "color": "#e4572e"}],
             "cast": [{"who": "LEX", "x": 250}],
             "pops": [{"kind": "chip", "at": "lex4f", "x": 1200, "y": 990,
                       "text": "Notice: when, where, business, special resolution text, "
                               "proxies", "color": "#1f3a5f", "size": 28}]}),

    Scene("s5", "Three kinds of resolution", "", [
        Pause("open", 1.0),
        Line("lex5a", "LEX", "An ordinary resolution needs a simple majority, more than "
             "fifty percent of the votes cast. It is the default, for example to appoint or "
             "remove a director.", gap=0.3),
        Line("lex5b", "LEX", "A special resolution needs at least seventy-five percent. It "
             "is needed to change the articles, change the name, reduce capital, or wind up "
             "voluntarily. Its exact text must be in the notice, and a copy filed within "
             "fifteen days.", gap=0.3),
        Line("lex5c", "LEX", "A written resolution is for private companies only. It is "
             "circulated, and passes when enough of all eligible members sign: a majority "
             "for ordinary, seventy-five percent for special.", gap=0.3),
        Line("lex5d", "LEX", "But a written resolution cannot remove a director or an "
             "auditor, and the auditor must receive a copy.", gap=0.4),
        Line("nia5", "NIA", "So a written resolution counts all the members, not just the "
             "ones who turn up."),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio_purple", "heading": "Resolutions",
             "syl": "F3(b)", "ts": 30,
             "cols": [{"title": "Ordinary", "icon": "ballot", "color": "#0f8b8d",
                       "at": "lex5a",
                       "items": [{"at": ["lex5a", 0.5], "text": "Over 50% of votes cast"},
                                 {"at": ["lex5a", 4.5], "text": "The default"},
                                 {"at": ["lex5a", 6.0], "text": "e.g. appoint or remove "
                                                               "a director"}]},
                      {"title": "Special", "icon": "star", "color": "#7768ae",
                       "at": "lex5b",
                       "items": [{"at": ["lex5b", 0.5], "text": "At least 75%"},
                                 {"at": ["lex5b", 3.0], "text": "Articles · name · capital · "
                                                               "voluntary winding up"},
                                 {"at": ["lex5b", 10.0], "text": "Text in notice · file in "
                                                                "15 days"}]},
                      {"title": "Written", "icon": "pen", "color": "#f2a541", "at": "lex5c",
                       "items": [{"at": ["lex5c", 0.5], "text": "Private companies only"},
                                 {"at": ["lex5c", 4.0], "text": "Majority of ALL eligible "
                                                               "votes"},
                                 {"at": "lex5d", "text": "Not to remove director or "
                                                         "auditor", "bad": True},
                                 {"at": ["lex5d", 3.5], "text": "Copy to the auditor"}]}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "NIA", "x": 1810, "s": 0.55, "y": 1120, "enter": "nia5"}]}),

    Scene("s6", "Quorum and proxies", "", [
        Pause("open", 1.0),
        Line("lex6a", "LEX", "A meeting needs a quorum, the minimum number present for "
             "valid business. Unless the articles say otherwise, it is two qualifying "
             "persons, or one for a single-member company.", gap=0.3),
        Line("lex6b", "LEX", "If there's no quorum, the meeting is adjourned, as the "
             "articles provide.", gap=0.4),
        Line("lex6c", "LEX", "Every member may appoint a proxy, who need not be a member, to "
             "attend, speak and vote for them, on a show of hands and on a poll. A proxy can "
             "also demand a poll.", gap=0.3),
        Line("lex6d", "LEX", "The company cannot require proxy forms more than forty-eight "
             "hours before the meeting. And a corporate member appoints a representative.",
             gap=0.4),
        Line("hans6", "HANS", "Perfect. When I'm in Hamburg, Nia can be my proxy!"),
        Pause("hold", 1.4),
    ], spec={"tpl": "board", "style": "chalk", "heading": "Quorum and proxies",
             "syl": "F3(c)", "row": 130, "ts": 40,
             "items": [{"at": "lex6a", "text": "Quorum: 2 (or 1 for a sole member)",
                        "icon": "people", "color": "#0f8b8d"},
                       {"at": "lex6b", "text": "No quorum? Adjourn", "icon": "clock",
                        "color": "#f2a541"},
                       {"at": "lex6c", "text": "Proxy: attend, speak, vote, demand a poll",
                        "icon": "person", "color": "#7768ae"},
                       {"at": "lex6d", "text": "Forms: no earlier than 48 hours before",
                        "icon": "hourglass", "color": "#e4572e"}],
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "HANS", "x": 1810, "s": 0.55, "y": 1120, "enter": "hans6"}]}),

    Scene("s7", "Hands up, or count the shares?", "", [
        Pause("open", 1.0),
        Line("lex7a", "LEX", "Voting starts with a show of hands: one vote per person "
             "present, whatever their shareholding.", gap=0.3),
        Line("lex7b", "LEX", "A poll counts votes by shares, usually one vote per share. "
             "So big shareholders often demand one.", gap=0.3),
        Line("lex7c", "LEX", "The articles cannot stop a poll being demanded by five or more "
             "members, or by members holding ten percent of the voting rights, or ten "
             "percent of the paid-up capital. The chair can also call one.", gap=0.4),
        Line("lex7d", "LEX", "And abstentions count neither for nor against.", gap=0.3),
        Line("kito7", "KITO", "On a show of hands Hans equals me. On a poll, I win easily!"),
        Pause("hold", 1.4),
    ], spec={"tpl": "compare", "bg": "studio", "heading": "Show of hands vs poll",
             "syl": "F3(c)", "ts": 33,
             "cols": [{"title": "Show of hands", "icon": "people", "color": "#f2a541",
                       "at": "lex7a",
                       "items": [{"at": ["lex7a", 0.5], "text": "One vote per person "
                                                               "present"},
                                 {"at": ["lex7a", 3.5], "text": "Shareholding ignored"}]},
                      {"title": "Poll", "icon": "pie", "color": "#7768ae", "at": "lex7b",
                       "items": [{"at": ["lex7b", 0.5], "text": "Votes counted by shares"},
                                 {"at": "lex7c", "text": "Demand: 5+ members, 10% votes, or "
                                                         "10% capital"},
                                 {"at": ["lex7c", 8.0], "text": "Or the chair"},
                                 {"at": "lex7d", "text": "Abstentions don't count"}]}],
             "vs": True,
             "cast": [{"who": "LEX", "x": 250},
                      {"who": "KITO", "x": 1810, "s": 0.55, "y": 1120, "enter": "kito7",
                       "mood": "excited"}]}),

    quiz_scene("s8", "Quick check",
               "Which of these CANNOT be done by written resolution?",
               ["Change the company's name", "Remove a director",
                "Approve a director's service contract", "Alter the articles"], 1,
               "Quick check. Which of these cannot be done by written resolution?",
               "Removing a director.",
               why="Removal of a director or auditor must be at a meeting, with special notice",
               syl="F3(b)"),

    quiz_scene("s9", "Quick check",
               "What majority does a special resolution need?",
               ["More than 50%", "At least two-thirds", "At least 75%", "100%"], 2,
               "And what majority does a special resolution need?",
               "At least seventy-five percent.",
               think=4.0, syl="F3(b)"),

    recap_scene("s10", [
        ("Public companies hold AGMs within six months.", "plc AGM: within 6 months"),
        ("Members with five percent can force a meeting.", "5% can requisition"),
        ("Fourteen days' notice; twenty-one for a plc AGM.", "14 days · 21 plc AGM"),
        ("Ordinary over fifty, special seventy-five.", "Ordinary >50% · special 75%"),
        ("Proxies, quorum, and polls.", "Proxies · quorum · polls"),
    ], [
        Line("lex10", "LEX", "Next time, the darkest day for any company: insolvency, and "
             "winding up.", gap=0.3),
        Line("kito10", "KITO", "Let's hope Safari Solar never needs that one.", gap=0.6),
    ], next_ep=25, next_title="Winding Up", next_icon="fire"),
]
