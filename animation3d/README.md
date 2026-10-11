# THE LAW BEHIND THE DEAL: Episode 1 in 3D

This is a 3D version of the pilot episode "Who Makes the Rules?". It uses the
same script, natural neural voices, music and subtitles as the 2D version in
[`../animation`](../animation). The pictures are rebuilt in 3D: modelled and
rigged characters, real-time lighting with soft shadows, and moving cameras.

**Watch:** [`output/episode1_who_makes_the_rules_3d.mp4`](output/episode1_who_makes_the_rules_3d.mp4)
(1280×720, 24 fps, about 4 min 46 s). It has a built-in English subtitle track.

## What's 3D about it

- **Characters.** Nia, Kito, Professor Lex and the Auditor are built from 3D
  shapes and have a simple skeleton: shoulders, elbows and head. They blink,
  breathe, turn to each other, and their 3D mouths are lip-synced to the voice
  audio. Captain Cargo is a talking shipping container with a captain's hat.
- **Sets.** The SafariTech office has a desk and laptop, and a window showing
  the city or the harbour.
  - **Scene 2:** two real doors swing open on their hinges.
  - **Scene 3:** Parliament, a government office and a courthouse rise out of
    the ground.
  - **Scene 4:** the court hierarchy is a 3D staircase.
  - **Scene 5:** the four equitable remedies sit on turning pedestals.
  - **Scene 6:** a spinning globe, with the international organisations
    orbiting it.
  - **Scene 7:** a courtroom next to an arbitration room.
  - **End card:** a container ship on an animated sea.
- **Camera.** Each scene has its own camera moves: push-ins, pans between the
  two rooms, a crane over the three branches and an orbit around the globe.
- **Lighting.** Image-based lighting, a key light and a fill light, and soft
  shadows.

## Rebuild it

```bash
# 1. voice track, timeline and subtitles (shared with the 2D version)
pip install -r ../animation/requirements.txt && ../animation/fetch_models.sh
python ../animation/build.py --audio-only

# 2. 3D render (three.js in headless Chromium, software WebGL, no GPU needed)
npm install            # three + playwright; uses the pre-installed Chromium
node render.mjs        # -> output/episode1_who_makes_the_rules_3d.mp4
```

`render.mjs` runs step 1 by itself if the voice track is missing.

Useful options:

- `--width 1920` renders at 1080p.
- `--jobs 4` sets how many browser pages render in parallel.
- `--scenes s3,s4` re-renders only those scenes.
- `--preview 12 40.5` saves still JPEGs at those times (in seconds) into
  `build/` so you can check frames quickly.

## Code layout

```
animation3d/
  render.mjs      launches Chromium, renders every frame, encodes with ffmpeg and muxes the audio
  serve.mjs       tiny local web server for the page, fonts and three.js
  web/
    index.html    page that loads the renderer
    main.js       renderer setup and the frame() entry point
    core.js       easing, materials, canvas-texture labels and the on-screen text layer
    chars.js      the rigged 3D cast, poses, blinking and lip-sync mouths
    props.js      sets, buildings, the globe, the ship, the sea, icons and lighting
    scenes.js     the title, the 8 scenes and the end card, with camera moves
```

To change a line of dialogue, edit `../animation/lw_anim/script_ep1.py` and run
both steps again. The 3D scenes re-time themselves from the new voice timeline.
