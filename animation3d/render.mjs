#!/usr/bin/env node
// Render THE LAW BEHIND THE DEAL - Episode 1 in 3D (three.js in headless Chromium).
//
//   node render.mjs                     full render -> output/episode1_who_makes_the_rules_3d.mp4
//   node render.mjs --preview 12 40.5   still JPEGs at those global times into build/
//
// The voice track, timeline and subtitles come from the 2D pipeline
// (python ../animation/build.py --audio-only), so both versions share one voice cast.
import { chromium } from 'playwright';
import { spawn, spawnSync } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { serve } from './serve.mjs';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const ANIM = path.join(HERE, '../animation');
const BUILD = path.join(HERE, 'build');
const OUT = path.join(HERE, 'output');

const args = process.argv.slice(2);
const opt = (name, def) => { const i = args.indexOf(name); return i >= 0 ? args[i + 1] : def; };
const width = Number(opt('--width', 1280)), height = Math.round(width * 9 / 16);
const fps = Number(opt('--fps', 24));
const jobs = Number(opt('--jobs', Math.max(1, Math.min(4, os.cpus().length))));
const pi = args.indexOf('--preview');
const preview = pi >= 0 ? args.slice(pi + 1).filter((a) => !a.startsWith('--')).map(Number) : null;
const only = opt('--scenes', null);

fs.mkdirSync(BUILD, { recursive: true });
fs.mkdirSync(OUT, { recursive: true });

const tlPath = path.join(ANIM, 'build/timeline.json');
const wav = path.join(ANIM, 'build/mix.wav');
const srt = path.join(ANIM, 'output/episode1_who_makes_the_rules.srt');
if (!fs.existsSync(tlPath) || !fs.existsSync(wav) || !fs.existsSync(srt)) {
  console.log('voice track missing - running the audio stage of ../animation/build.py');
  const r = spawnSync('python3', [path.join(ANIM, 'build.py'), '--audio-only'], { stdio: 'inherit' });
  if (r.status !== 0) process.exit(r.status || 1);
}
const TL = JSON.parse(fs.readFileSync(tlPath, 'utf8'));

const server = await serve(0);
const url = `http://127.0.0.1:${server.address().port}/index.html`;
const browser = await chromium.launch({
  args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--disable-gpu-vsync'],
});

async function newPage() {
  const page = await browser.newPage({ viewport: { width, height } });
  page.on('pageerror', (e) => console.error('page error:', e.message));
  page.on('console', (m) => { if (m.type() === 'error') console.error('console:', m.text()); });
  await page.goto(url);
  await page.waitForFunction(() => window.ready === true);
  await page.evaluate(([tl, w, h]) => window.init(tl, w, h), [TL, width, height]);
  return page;
}

const jpeg = (dataUrl) => Buffer.from(dataUrl.slice(dataUrl.indexOf(',') + 1), 'base64');

if (preview) {
  const page = await newPage();
  for (const gt of preview) {
    let idx = 0;
    TL.scenes.forEach((s, i) => { if (s.start <= gt) idx = i; });
    const d = await page.evaluate(([i, t]) => window.frame(i, t, 0.9), [idx, gt - TL.scenes[idx].start]);
    const p = path.join(BUILD, `preview3d_${gt.toFixed(2).padStart(7, '0')}.jpg`);
    fs.writeFileSync(p, jpeg(d));
    console.log('wrote', p);
  }
  await browser.close(); server.close();
  process.exit(0);
}

async function renderScene(page, idx) {
  const sc = TL.scenes[idx];
  const first = Math.round(sc.start * fps);
  const n = Math.round((sc.start + sc.dur) * fps) - first;
  const out = path.join(BUILD, `seg3d_${String(idx).padStart(2, '0')}.mp4`);
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-c:v', 'mjpeg', '-framerate', String(fps), '-i', '-',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', '-pix_fmt', 'yuv420p', '-r', String(fps), out], { stdio: ['pipe', 'inherit', 'inherit'] });
  const done = new Promise((res, rej) => ff.on('close', (c) => (c === 0 ? res() : rej(new Error('ffmpeg ' + c)))));
  const t0 = Date.now();
  for (let i = 0; i < n; i++) {
    const t = (first + i) / fps - sc.start;
    const d = await page.evaluate(([k, tt]) => window.frame(k, tt, 0.93), [idx, t]);
    if (!ff.stdin.write(jpeg(d))) await new Promise((r) => ff.stdin.once('drain', r));
    if (i % 120 === 0) console.log(`  ${sc.key}: frame ${i}/${n}`);
  }
  ff.stdin.end();
  await done;
  console.log(`  rendered ${sc.key} (${n} frames, ${((Date.now() - t0) / 1000).toFixed(0)}s)`);
}

const order = TL.scenes.map((_, i) => i).filter((i) => !only || only.split(',').includes(TL.scenes[i].key))
  .sort((a, b) => TL.scenes[b].dur - TL.scenes[a].dur);
const queue = [...order];
await Promise.all(Array.from({ length: Math.min(jobs, queue.length) }, async () => {
  const page = await newPage();
  while (queue.length) await renderScene(page, queue.shift());
  await page.close();
}));
await browser.close(); server.close();

if (only) process.exit(0);
const list = path.join(BUILD, 'segments3d.txt');
fs.writeFileSync(list, TL.scenes.map((_, i) => `file '${path.join(BUILD, `seg3d_${String(i).padStart(2, '0')}.mp4`)}'`).join('\n') + '\n');
const out = path.join(OUT, 'episode1_who_makes_the_rules_3d.mp4');
const r = spawnSync('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', list, '-i', wav, '-i', srt,
  '-map', '0:v', '-map', '1:a', '-map', '2:s', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '160k', '-c:s', 'mov_text',
  '-metadata:s:s:0', 'language=eng', '-metadata', 'title=THE LAW BEHIND THE DEAL (3D) - Episode 1: Who Makes the Rules?',
  '-movflags', '+faststart', '-t', String(TL.total), out], { stdio: 'inherit' });
if (r.status !== 0) process.exit(r.status || 1);
console.log('wrote', out);
