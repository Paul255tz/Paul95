"""Pilot Episode 1 - "Who Makes the Rules?"

Dialogue follows the screenplay in the ACCA LW-GLO Deep Learning and 2D
Animation Script (2026-27). Long speeches are split into shorter lines so the
visuals can sync to each idea. `say=` holds a pronunciation-friendly version
for the speech engine when it differs from the subtitle text.
"""
from .beats import DISPLAY_NAMES, VOICES, Line, Pause, Scene, Sfx  # noqa: F401

SERIES = "THE LAW BEHIND THE DEAL"
SLUG = "episode1_who_makes_the_rules"
EPISODE = "Episode 1"
EPISODE_TITLE = "Who Makes the Rules?"
NEXT_TITLE = "Three Families of Law"

SCENES = [
    Scene("title", "Title", "", [
        Sfx("jingle"),
        Pause("logo", 2.6),
        Line("n1", "NARRATOR", "The Law Behind the Deal.", gap=0.25),
        Line("n2", "NARRATOR", "Episode one. Who makes the rules?"),
        Pause("hold", 1.4),
    ]),
    Scene("s1", "SafariTech office, morning", "00:00", [
        Pause("open", 1.2),
        Sfx("paper"),
        Pause("invoice", 1.4),
        Sfx("whoosh"),
        Pause("kito_in", 1.0),
        Line("kito1", "KITO", "The supplier broke our deal! I want them punished, "
             "and I want our money back!", gap=0.5),
        Line("nia1", "NIA", "Hmm. Those might be two different legal questions.", gap=0.3),
        Sfx("pop"),
        Pause("book", 0.9),
        Line("lex1", "LEX", "Exactly. First, identify the type of problem.", gap=0.4),
        Sfx("pop"),
        Line("lex1b", "LEX", "A civil dispute is about a remedy for a private wrong. "
             "A criminal case is a prosecution for an offence."),
        Pause("hold", 2.0),
    ]),
    Scene("s2", "Two doors", "01:00", [
        Pause("open", 1.4),
        Sfx("door"),
        Line("lex2a", "LEX", "A civil claim commonly seeks compensation or another remedy. "
             "The usual standard is the balance of probabilities.", gap=0.6),
        Sfx("door"),
        Line("lex2b", "LEX", "A criminal prosecution concerns an offence, and uses the "
             "higher standard: beyond reasonable doubt.", gap=0.6),
        Line("nia2", "NIA", "So a broken contract does not automatically mean someone "
             "goes to prison."),
        Line("lex2c", "LEX", "Correct. Always classify the facts before choosing the rule."),
        Pause("hold", 1.6),
    ]),
    Scene("s3", "The three branches", "02:15", [
        Pause("open", 1.2),
        Sfx("rise"),
        Line("lex3a", "LEX", "The legislature makes laws.", gap=0.3),
        Sfx("rise"),
        Line("lex3b", "LEX", "The executive puts them into action.", gap=0.3),
        Sfx("rise"),
        Line("lex3c", "LEX", "And the judiciary resolves disputes, and interprets the law.",
             gap=0.5),
        Line("kito3", "KITO", "So the judge does not usually write every new law from "
             "scratch?"),
        Line("lex3d", "LEX", "Right. But judicial decisions can shape legal principles, "
             "especially in common-law systems."),
        Sfx("pop"),
        Pause("summary", 3.2),
    ]),
    Scene("s4", "Precedent in action", "03:15", [
        Pause("open", 1.0),
        Sfx("sparkle"),
        Pause("card", 1.0),
        Line("lex4a", "LEX", "The ratio decidendi is the legal reason necessary for the "
             "earlier decision.",
             say="The ratio, dee-sy-dendy, is the legal reason necessary for the earlier "
                 "decision."),
        Line("lex4b", "LEX", "Obiter dicta are additional observations.",
             say="Obbiter dicta are additional observations.", gap=0.5),
        Line("lex4c", "LEX", "A precedent may bind a later court when it comes from a "
             "superior court, and the material facts are sufficiently similar.", gap=0.6),
        Sfx("whoosh"),
        Pause("panels", 0.8),
        Sfx("pop"),
        Line("lex4d", "LEX", "Reverse: the same case goes up on appeal.", gap=0.3),
        Sfx("pop"),
        Line("lex4e", "LEX", "Overrule: a later case changes the earlier legal rule.",
             gap=0.3),
        Sfx("pop"),
        Line("lex4f", "LEX", "Distinguish: the important facts differ.", gap=0.6),
        Line("lex4g", "LEX", "Do not mix these up. Read the facts, identify the court "
             "hierarchy, and ask what part of the earlier judgment was necessary."),
        Pause("hold", 1.4),
    ]),
    Scene("s5", "When money is not enough", "04:45", [
        Pause("open", 1.0),
        Line("kito5", "KITO", "They never delivered our custom machine. Fine, just pay us "
             "cash!", gap=0.4),
        Line("nia5a", "NIA", "But Kito, that machine is one of a kind. Cash can't buy "
             "another one.", gap=0.5),
        Line("lex5a", "LEX", "Equitable remedies developed because damages are not always "
             "adequate.", gap=0.5),
        Sfx("pop"),
        Line("lex5b", "LEX", "Specific performance.", gap=0.25),
        Sfx("pop"),
        Line("lex5c", "LEX", "An injunction.", gap=0.25),
        Sfx("pop"),
        Line("lex5d", "LEX", "Rescission.", say="Re-sizh-un.", gap=0.25),
        Sfx("pop"),
        Line("lex5e", "LEX", "Rectification.", gap=0.5),
        Line("lex5f", "LEX", "These remedies are discretionary, and depend on the legal "
             "conditions.", gap=0.4),
        Line("nia5b", "NIA", "So I must not assume every claimant automatically gets the "
             "remedy they request."),
        Pause("hold", 1.4),
    ]),
    Scene("s6", "The world of trade", "05:45", [
        Pause("open", 1.6),
        Line("lex6a", "LEX", "International trade needs cooperation, because different "
             "countries may have different laws.", gap=0.4),
        Line("lex6b", "LEX", "Treaties and conventions can create shared rules. "
             "Model laws offer a template for countries to adopt.", gap=0.4),
        Sfx("pop"),
        Line("lex6c", "LEX", "UNCITRAL develops harmonised commercial-law texts.", gap=0.3),
        Sfx("pop"),
        Line("lex6d", "LEX", "The WTO provides a framework for trade cooperation.", gap=0.3),
        Sfx("pop"),
        Line("lex6e", "LEX", "And the ICC develops commercial rules, including Incoterms, "
             "and supports commercial dispute resolution.",
             say="And the I.C.C. develops commercial rules, including Inco-terms, "
                 "and supports commercial dispute resolution.", gap=0.4),
        Sfx("whoosh"),
        Pause("cargo_in", 0.9),
        Line("cargo6", "CARGO", "Ahoy! And who decides whether our case goes to court, "
             "or arbitration?"),
        Line("lex6f", "LEX", "That depends on the agreement, and the applicable law."),
        Pause("hold", 1.4),
    ]),
    Scene("s7", "Court or arbitration?", "07:15", [
        Pause("open", 1.2),
        Line("lex7a", "LEX", "Court adjudication is formal, and usually public.", gap=0.5),
        Line("lex7b", "LEX", "Arbitration may offer privacy, flexibility and specialist "
             "expertise. But it can still be expensive, and its award can only be "
             "challenged on limited grounds.", gap=0.5),
        Line("nia7", "NIA", "And mediation?", gap=0.4),
        Sfx("pop"),
        Line("lex7c", "LEX", "A neutral mediator helps the parties negotiate. The mediator "
             "does not normally impose a decision.", gap=0.6),
        Sfx("whoosh"),
        Pause("aud_in", 0.8),
        Line("aud1", "AUDITOR", "Quick check. Which mechanism usually has a third party "
             "impose a binding decision, under the parties' agreement?", gap=0.3),
        Sfx("tick"), Sfx("tick", 1.0), Sfx("tick", 2.0), Sfx("tick", 3.0),
        Pause("think", 4.0),
        Sfx("ding"),
        Line("aud2", "AUDITOR", "Arbitration.", gap=0.4),
        Pause("hold", 1.6),
    ]),
    Scene("s8", "Episode recap", "08:45", [
        Pause("open", 1.0),
        Sfx("pin"),
        Line("nia8a", "NIA", "Civil versus criminal.", gap=0.3),
        Sfx("pin"),
        Line("nia8b", "NIA", "Legislature, executive, judiciary.", gap=0.3),
        Sfx("pin"),
        Line("nia8c", "NIA", "Ratio versus obiter.", say="Ratio versus obbiter.", gap=0.3),
        Sfx("pin"),
        Line("nia8d", "NIA", "Damages versus equitable remedies.", gap=0.3),
        Sfx("pin"),
        Line("nia8e", "NIA", "Court versus ADR.", say="Court versus A. D. R.", gap=0.5),
        Line("lex8", "LEX", "Excellent. Next time, we tour the world's great legal families: "
             "common law, civil law and Sharia law, and how the world's economies shape "
             "them.", gap=0.3),
        Sfx("horn"),
        Pause("ship", 0.8),
        Line("cargo8", "CARGO", "I've docked in countries from every one of those families!",
             gap=0.8),
        Sfx("jingle"),
        Line("n3", "NARRATOR", "Next time: Episode two. Three Families of Law.",
             gap=0.6),
        Pause("end", 3.6),
    ]),
]
