# THE LAW BEHIND THE DEAL: Episode 1, "Who Makes the Rules?"

A 2D cartoon animation with natural neural voices. It is based on the pilot
screenplay in the *ACCA LW-GLO Deep Learning and 2D Animation Script (2026–27)*.

**Watch:** [`output/episode1_who_makes_the_rules.mp4`](output/episode1_who_makes_the_rules.mp4)
(1280×720, 24 fps, about 4 min 46 s). It has a built-in English subtitle track,
and the same subtitles are in a separate
[`.srt`](output/episode1_who_makes_the_rules.srt) file.

## What's in it

| # | Scene | What is taught |
|---|-------|----------------|
| – | Title | Series and episode card |
| 1 | SafariTech office, morning | Civil dispute vs criminal case |
| 2 | Two doors | Civil and criminal standards of proof |
| 3 | The three branches | Legislature, executive and judiciary (separation of powers) |
| 4 | Precedent in action | Ratio vs obiter, binding precedent, reverse / overrule / distinguish |
| 5 | When money is not enough | Equitable remedies: specific performance, injunction, rescission, rectification |
| 6 | The world of trade | UN, UNCITRAL, WTO, ICC, UNIDROIT and OECD; treaties vs model laws |
| 7 | Court or arbitration? | Court, arbitration and mediation, plus the Auditor's quick check |
| 8 | Episode recap | Five recap cards, then a teaser for Episode 2 |

**Cast and voices** (Kokoro-82M neural text-to-speech, all running locally):

| Character | Voice |
|-----------|-------|
| Nia (junior finance analyst) | `af_heart` |
| Kito (founder of SafariTech) | `am_puck` |
| Professor Lex (legal mentor) | `bm_george` (British English) |
| Captain Cargo (talking shipping container) | `am_fenrir` |
| The Auditor | `bf_emma` (British English) |
| Narrator | `af_bella` |

Mouth movement is lip-synced to each line's audio. Speech drives every scene's
timing, so the visuals always line up with the voice. The music bed and the
sound effects are generated in code, so no outside samples are used.

## Rebuild it

```bash
pip install -r animation/requirements.txt
# skia-python needs libEGL on Linux: apt-get install -y libegl1
./animation/fetch_models.sh               # ~350 MB Kokoro model into animation/models
python animation/build.py                 # writes animation/output/*.mp4 and *.srt
```

Useful options:

- `--width 1920` renders at 1080p.
- `--fps 30` sets the frame rate.
- `--no-music` turns off the music bed.
- `--preview 12 40 95` renders still PNGs at those times (in seconds) into
  `animation/build/` so you can check frames quickly.

## Code layout

```
animation/
  build.py              pipeline: TTS -> timeline -> audio mix -> parallel render -> mux
  lw_anim/
    script_ep1.py       dialogue, voice cast and scene beats (edit this to change the script)
    voice.py            Kokoro TTS with caching, lip-sync envelopes, timeline layout
    audio.py            procedural music, sound effects and final mix
    gfx.py              drawing helpers (skia), easing and text
    characters.py       parametric cast: Nia, Kito, Professor Lex, the Auditor, Captain Cargo
    props.py            backgrounds, documents, buildings, globe, ship and icons
    scenes.py           one draw function per scene
  assets/fonts/         Fredoka and Nunito (SIL Open Font License)
```

To change a line, edit its text in `script_ep1.py` and run the build again. Only
the changed lines are re-synthesised, and the animation re-times itself to
match. If the speech engine mispronounces something, add a `say=` spelling
(see "ratio decidendi" and "Incoterm" in the script).

## Notes

- This is a **learning aid**. The characters, the company and the facts are
  fictional. The pilot runs about 4¾ minutes at a natural speaking pace,
  against the screenplay's 9½-minute timing. As the production safeguards
  ask, have a subject-matter reviewer check the legal accuracy against the
  current ACCA documents before you publish.
- A few short bridging lines were added so the pictures make sense with sound
  on. For example, Kito asks for cash in Scene 5, and Professor Lex reads out
  the panel names in Scene 4. Each one restates something the screenplay
  already shows on screen.
