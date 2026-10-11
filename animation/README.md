# THE LAW BEHIND THE DEAL: ACCA LW-GLO animated series

A 29-episode 2D cartoon course covering the **whole ACCA Corporate and Business
Law – Global (LW-GLO) syllabus, September 2026 to June 2027**. Natural neural
voices are generated locally with Kokoro-82M. Examples are set in **Tanzania
and Kenya**: SafariTech in Dar es Salaam, a bank in Nairobi, an agent in
Kampala, and a supplier in Hamburg.

Each episode has a **"Quick check"** interactive pause. The Auditor asks a
question, a countdown runs, and then the answer and the reason are revealed.
Pause the video before the countdown ends and answer it yourself.

- **Videos:** [`output/`](output/) (MP4 at 1280×720, 24 fps, with a built-in
  subtitle track and a separate `.srt` file)
- **Screenplays:** [`scripts/`](scripts/) (exported with
  `python animation/tools/export_scripts.py`)
- **Study notes with sources:** [`../study-notes/`](../study-notes/README.md)

## Episodes

| # | Title | Syllabus | Status |
|---|---|---|---|
| 1 | Who Makes the Rules? | A1, A2(c), A3(a) | ✅ rendered |
| 2 | Three Families of Law | A1(a), A1(d), A2(a)–(b) | ✅ rendered |
| 3 | The Global Rule-Makers | A2(c) | ✅ rendered |
| 4 | The Arbitration Room | A3 | ✅ rendered |
| 5 | The Contract Across the Ocean | B1(a)–(b) | ✅ rendered |
| 6 | Incoterms: Who Pays, Who Risks | B1(c) | ✅ rendered |
| 7 | The Seller's Promise | B2(a) | 🟡 draft render (re-render pending) |
| 8 | The Buyer's Side | B2(b) | 🟡 draft render |
| 9 | When Deals Break | B2(c)(i)–(iv) | 🟡 draft render |
| 10 | Risk on the Water | B2(c)(v)–(vi), B2(d) | 🟡 draft render |
| 11 | Paper That Moves the World | C1(a), C1(d) | 📝 script ready |
| 12 | Following the Money | C1(b), (c), (e) | 📝 script ready |
| 13 | The Agent's Authority | D1 | 📝 script ready |
| 14 | Partners in Business | D2 | 📝 script ready |
| 15 | Behind the Corporate Veil | D3 | 📝 script ready |
| 16 | Birth of a Company | D4(a)–(d) | 📝 script ready |
| 17 | The Company's Rulebook | D4(e)–(h) | 📝 script ready |
| 18 | Share Capital | E1 | 📝 script ready |
| 19 | Borrowing Power | E2 | 📝 script ready |
| 20 | Keeping the Capital | E3 | 📝 script ready |
| 21 | The Boardroom | F1(a)–(c) | 📝 script ready |
| 22 | Directors' Duties | F1(d) | 📝 script ready |
| 23 | Secretary and Auditor | F2 | 📝 script ready |
| 24 | Meetings and Resolutions | F3 | 📝 script ready |
| 25 | Winding Up | G1(a)–(c) | 📝 script ready |
| 26 | Administration: The Rescue | G1(d)–(e) | 📝 script ready |
| 27 | Insiders and Market Abuse | H1(a)–(b) | 📝 script ready |
| 28 | Dirty Money | H1(c) | 📝 script ready |
| 29 | Bribes, Fraud and the Final Bell | H1(d)–(f) + exam format | 📝 script ready |

**Cast and voices** (Kokoro-82M):

| Character | Role | Voice |
|---|---|---|
| Nia | Junior finance analyst, SafariTech | `af_heart` |
| Kito | Founder of SafariTech | `am_puck` |
| Professor Lex | Legal mentor | `bm_george` |
| The Auditor | Quiz master and compliance voice | `bf_emma` |
| Captain Cargo | Talking shipping container | `am_fenrir` |
| Hans | Supplier, Hamburg | `am_michael` |
| Amara | Trade-finance banker, Nairobi | `bf_isabella` |
| Narrator | | `af_bella` |

## Build

```bash
pip install -r animation/requirements.txt
apt-get install -y libegl1                # needed by skia-python on Linux
./animation/fetch_models.sh               # ~350 MB Kokoro model
python animation/build.py --episode 7     # one episode
python animation/build.py --episode 7,8,9 # several
python animation/build.py --episode all   # everything
python animation/build.py --episode 12 --preview 30 90 150   # still frames only
python animation/tools/export_scripts.py  # screenplays into animation/scripts/
```

On a 4-core machine, one 6–7 minute episode takes about 2 minutes of speech
synthesis (first run only, then it is cached) and about 2–3 minutes to render.

## How it works

```
animation/
  build.py                 TTS -> voice-driven timeline -> audio mix -> parallel render -> mux
  lw_anim/
    beats.py               Line / Pause / Sfx / Scene, voice cast
    episodes/epNN.py       episodes 2-29: dialogue + a visual "spec" per scene
    episodes/_kit.py       helpers for title, quiz and recap scenes
    templates.py           data-driven scene templates (talk, board, compare, flow,
                           stack, route, case, timeline, quiz, recap, title)
    icons.py               ~70 flat icons used by the templates
    script_ep1.py, scenes.py   Episode 1 (hand-animated pilot)
    voice.py, audio.py, gfx.py, characters.py, props.py
  tools/export_scripts.py  screenplay export
```

Every visual element is tied to a **cue**: the id of a spoken line, its end
(`"id$"`), or an offset (`["id", 1.5]`). So the pictures always stay in sync
with the voices, even after a line is edited and re-synthesised. To change a
line, edit its text in the episode file and rebuild. Only changed lines are
re-voiced. If the speech engine mispronounces something, add a `say=` spelling.

## Notes

- This is a **learning aid**. The characters, companies and facts are
  fictional. Company and insolvency law follows the UK model that ACCA LW-GLO
  uses. The Tanzania and Kenya "local lens" points are context, not exam
  content. Have a subject-matter reviewer check the content against current
  ACCA materials before publishing.
- The `animation3d/` folder holds an earlier experimental 3D version of
  Episode 1.
