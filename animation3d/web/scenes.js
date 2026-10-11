// The nine 3D scenes of Episode 1. Each scene has setup() (build the set once)
// and draw() (pose everything for scene-local time t, using the voice timeline).
import * as THREE from 'three';
import {
  PAL, Stage, at, box, canvasTex, cardTex, checkTex, chip3, chipTex, clamp, cyl, easeInOut, easeOut,
  easeOutBack, font, lerp, mat, mesh, pop, prog, rbox, rr, setOpacity, sphere, texPlane, textTex, win, wrapLines,
} from './core.js';
import { makeCargo, makeMini, makePerson, poseCargo, posePerson, poseTrack } from './chars.js';
import * as P from './props.js';

// ------------------------------------------------------------- helpers
export class ST {
  constructor(sc) { this.sc = sc; this.ev = sc.events; this.lines = sc.lines; this.dur = sc.dur; }
  at(k) { return this.ev[k][0]; }
  end(k) { return this.ev[k][1]; }
  during(k, t) { return this.at(k) <= t && t <= this.end(k); }
  mouth(who, t) {
    for (const ln of this.lines) {
      if (ln.who === who && ln.t0 <= t && t <= ln.t1) {
        const e = ln.env, i = (t - ln.t0) * 60, i0 = Math.floor(i);
        if (i0 + 1 >= e.length) return e.length ? e[e.length - 1] : 0;
        return e[i0] * (1 - (i - i0)) + e[i0 + 1] * (i - i0);
      }
    }
    return 0;
  }
  talking(who, t) { return this.lines.some((l) => l.who === who && l.t0 <= t && t <= l.t1); }
}

const V = new THREE.Vector3();

function person(stage, st, t, who, x, z, o = {}) {
  const p = stage.get(o.id || who, () => makePerson(who));
  p.position.set(x, o.y || 0, z);
  p.rotation.y = o.ry || 0;
  p.scale.setScalar(o.s || 1);
  const talking = st.talking(who, t);
  let mood = o.mood || 'neutral';
  if (talking && mood === 'neutral') mood = 'smile';
  posePerson(p, { pose: o.pose || 'idle', mouth: st.mouth(who, t), mood, look: o.look || 0, t, talking, bob: o.bob || 0 });
  p.updateMatrixWorld(true);
  return p;
}

function handPos(p, side = 'R') { return p.userData.rig.arms[side].hand.getWorldPosition(V.clone()); }

function cargo(stage, st, t, x, y, z, o = {}) {
  const c = stage.get(o.id || 'cargo', () => makeCargo());
  c.position.set(x, y, z); c.rotation.y = o.ry || 0; c.scale.setScalar(o.s || 1);
  const talking = st.talking('CARGO', t);
  poseCargo(c, { mouth: st.mouth('CARGO', t), mood: o.mood || (talking ? 'smile' : 'happy'), look: o.look || 0, t });
  return c;
}

// camera keyframes: [time, [px,py,pz], [tx,ty,tz], fov]
function camTrack(cam, t, keys) {
  let a = keys[0], b = keys[0];
  for (let i = 0; i < keys.length; i++) {
    if (t >= keys[i][0]) { a = keys[i]; b = keys[i + 1] || keys[i]; }
  }
  const span = b[0] - a[0];
  const k = span > 0 ? easeInOut((t - a[0]) / span) : 0;
  const p = a[1].map((v, i) => lerp(v, b[1][i], k));
  const tg = a[2].map((v, i) => lerp(v, b[2][i], k));
  const fov = lerp(a[3] || 35, b[3] || 35, k);
  cam.position.set(p[0] + Math.sin(t * 0.37) * 0.04, p[1] + Math.sin(t * 0.29) * 0.03, p[2]);
  cam.fov = fov; cam.updateProjectionMatrix();
  cam.lookAt(tg[0], tg[1], tg[2]);
}

// keys where the camera should move: helper to build "arrive at" segments
const K = (t, p, tg, fov = 35) => [t, p, tg, fov];

function bg(scene, top, bottom) {
  const t = canvasTex(`bg|${top}|${bottom}`, 16, 256, (g, w, h) => {
    const gr = g.createLinearGradient(0, 0, 0, h); gr.addColorStop(0, top); gr.addColorStop(1, bottom);
    g.fillStyle = gr; g.fillRect(0, 0, w, h);
  });
  scene.background = t.tex;
}

function studio(scene, top, bottom, floorC) {
  bg(scene, top, bottom);
  scene.add(P.floor(floorC));
  const cyc = mesh(new THREE.CylinderGeometry(14, 14, 14, 64, 1, true, Math.PI * 0.75, Math.PI * 1.5), new THREE.MeshStandardMaterial({ color: bottom, side: THREE.BackSide, roughness: 1 }), { cast: false, receive: true });
  cyc.position.set(0, 7, 4);
  scene.add(cyc);
}

function chipDraw(hud, id, label, x, y, o = {}) { return hud.chip(id, label, x, y, o); }

// ============================================================== TITLE
const title = {
  setup(S, ctx) {
    bg(S.scene, '#13233a', '#24426b');
    P.lights(S.scene, { sky: '#9fc3e6', ground: '#13233a', sun: 2.0 });
    S.scene.add(P.stars(700, 30));
    const disc = mesh(new THREE.CylinderGeometry(6, 6, 0.2, 64), mat('#1f3a5f', { rough: 0.3, metal: 0.3 }), { cast: false, receive: true });
    disc.position.y = -0.1; S.scene.add(disc);
    const ring = mesh(new THREE.TorusGeometry(6, 0.05, 8, 96), new THREE.MeshBasicMaterial({ color: '#0f8b8d', toneMapped: false }));
    ring.rotation.x = Math.PI / 2; S.scene.add(ring);
  },
  draw(S, t, st, cam, hud) {
    const g = S.get('globe', () => P.globe(1.0));
    g.position.set(0, 5.75, -2.0); g.userData.ball.rotation.y = t * 0.5;
    g.scale.setScalar(pop(t, 0.3, 0.7));
    const gv = S.get('gavel', () => P.gavel());
    gv.position.set(1.15, 5.55, -1.5); gv.rotation.set(0.2, -0.4, -0.6 + Math.sin(t * 2) * 0.25);
    gv.scale.setScalar(pop(t, 0.5, 0.7) * 0.9);
    const up = easeOutBack(prog(t, 1.0, 0.9), 1.4);
    const y = (1 - up) * -2.6;
    const cast = [['NIA', -3.4, 'wave', 'happy', 0.35], ['KITO', -1.7, 'cheer', 'excited', 0.15], ['LEX', 1.7, 'present', 'happy', -0.15], ['AUDITOR', 3.4, 'clipboard', 'smile', -0.35]];
    for (const [w, x, pose, mood, ry] of cast) person(S, st, t, w, x, 0.6, { y, pose, mood, ry });
    cargo(S, st, t, 0, y, 0.9, { s: 0.85 });
    camTrack(cam, t, [K(0, [0, 5.9, 6.0], [0, 5.6, -2.0], 32), K(2.5, [0, 3.6, 11.0], [0, 3.55, 0], 36), K(st.dur, [0, 3.6, 12.0], [0, 3.5, 0], 36)]);
    hud.text('t1', 'THE LAW BEHIND THE DEAL', 960, 330, 104, '#ffffff', { outline: '#0b1622', ow: 16 }, pop(t, 0.9, 0.6));
    const bw = 900 * easeOut(prog(t, 1.3, 0.6));
    hud.rect('bar', 960 - bw / 2, 380, bw, 10, PAL.accent, bw > 1 ? 1 : 0);
    hud.text('t2', 'ACCA LW-GLO  ·  Corporate and Business Law – Global  ·  2026–27', 960, 435, 34, '#cfe3f7', { weight: 500, outline: '#0b1622', ow: 8 }, 1, easeInOut(prog(t, 1.6, 0.6)));
    const n2 = st.at('n2');
    chipDraw(hud, 'ep', 'EPISODE 1', 960, 515, { s: pop(t, n2, 0.5) });
    hud.text('t3', 'Who Makes the Rules?', 960, 610, 92, PAL.accent, { outline: '#0b1622', ow: 14 }, pop(t, n2 + 0.5, 0.5));
  },
};

// ============================================================== SCENE 1
const s1 = {
  setup(S) {
    bg(S.scene, '#fbf3e4', '#f1e2c8');
    P.lights(S.scene, { sunPos: [-3, 8, 7] });
    P.office(S.scene, { windowX: 2.4, windowW: 3.2 });
    const d = P.desk(); d.position.set(-0.6, 0, 0.2); S.scene.add(d);
  },
  draw(S, t, st, cam, hud) {
    const tk = st.at('kito_in');
    let look = t < st.at('invoice') + 0.9 ? -0.3 : t < tk ? 0 : 0.5, mood = 'neutral';
    if (tk <= t && t < st.at('kito1') + 0.6) mood = 'surprised';
    if (st.during('nia1', t)) mood = 'thinking';
    if (t >= st.at('lex1')) { look = -0.6; mood = t > st.at('lex1b') ? 'happy' : 'surprised'; }
    const npose = poseTrack(t, [[0, 'idle'], [st.at('nia1'), 'think'], [st.end('nia1'), 'idle']]);
    person(S, st, t, 'NIA', -0.4, -0.55, { pose: npose, mood, look, ry: 0.15 });
    // invoice
    const ti = st.at('invoice');
    const inv = S.get('invoice', () => P.paper('INVOICE', PAL.mistake, 5, 0.42));
    if (t >= ti) {
      const k = easeOut(prog(t, ti, 0.9));
      inv.position.set(lerp(0.9, 0.35, k), lerp(4.5, 1.03, k), lerp(0.6, 0.45, k));
      inv.rotation.set(lerp(0, -Math.PI / 2, k) + (k < 1 ? Math.sin(t * 9) * 0.3 : 0), 0, lerp(1.2, 0.25, k));
    } else inv.visible = false;
    // book + mini Lex
    const tb = st.at('book');
    const book = S.get('book', () => P.legalBook());
    book.position.set(-1.45, 1.02, 0.4); book.rotation.y = 0.3;
    P.setBook(book, easeOut(prog(t, tb, 0.6)));
    if (t >= tb + 0.3) {
      const rise = easeOutBack(prog(t, tb + 0.35, 0.7), 1.2);
      person(S, st, t, 'LEX', -1.45, 0.4, { id: 'minilex', s: 0.3 * rise, y: 1.05, pose: t > st.at('lex1b') ? 'point' : 'wave', mood: 'happy', ry: 0.4 });
      const glow = S.get('glow', () => { const l = new THREE.PointLight('#ffd27a', 0, 3); return l; });
      glow.position.set(-1.45, 1.5, 0.7); glow.intensity = 3 * easeInOut(prog(t, tb, 0.5));
    }
    // Kito
    if (t >= tk - 0.05) {
      const k = easeOut(prog(t, tk, 0.9));
      const x = lerp(6.5, 2.0, k);
      const run = Math.abs(Math.sin(t * 14)) * 0.12 * (1 - k);
      const k1 = st.end('kito1');
      const kpose = poseTrack(t, [[0, 'wave_paper'], [k1 + 0.2, 'hips']]);
      let kmood = t < k1 + 0.3 ? 'angry' : 'thinking';
      if (t > st.at('lex1')) kmood = 'surprised';
      const kito = person(S, st, t, 'KITO', x, 0.5, { pose: kpose, mood: kmood, look: -0.3, ry: -0.5, bob: run });
      const c = S.get('contract', () => P.paper('CONTRACT', PAL.navy, 4, 0.36));
      if (t < k1 + 0.25) {
        const hp = handPos(kito);
        c.position.set(hp.x, hp.y + 0.2, hp.z + 0.05); c.rotation.set(0, -0.3, Math.sin(t * 10) * 0.15);
      } else c.visible = false;
    }
    camTrack(cam, t, [
      K(0, [-0.2, 2.3, 8.8], [0.3, 1.5, 0]),
      K(tk, [0.4, 1.9, 7.6], [0.6, 1.4, 0]),
      K(st.at('nia1'), [0.2, 1.8, 6.6], [0.2, 1.5, 0]),
      K(tb + 0.2, [-1.2, 1.7, 3.6], [-1.3, 1.3, 0.3], 34),
      K(st.at('lex1b'), [-1.1, 1.75, 3.9], [-1.3, 1.35, 0.3], 34),
      K(st.at('lex1b') + 1.2, [0, 2.1, 8.4], [0.2, 1.65, 0]),
      K(st.dur, [0.1, 2.1, 8.2], [0.2, 1.65, 0]),
    ]);
    const tc = st.at('lex1b');
    if (t >= tc) {
      const a = easeInOut(prog(t, tc, 0.4));
      hud.card('c1', 540, 210, 680, 200, { title: 'CIVIL DISPUTE', body: '= remedy for a private wrong', accent: PAL.teal, titleSize: 44, bodySize: 40 }, pop(t, tc, 0.5), a);
      hud.card('c2', 1380, 210, 680, 200, { title: 'CRIMINAL CASE', body: '= prosecution for an offence', accent: PAL.purple, titleSize: 44, bodySize: 40 }, pop(t, tc + 0.25, 0.5), a);
    }
  },
};

// ============================================================== SCENE 2
function fillRoom(room, kind) {
  const isC = kind === 'civil';
  const bench = box(1.0, 0.45, 0.35, isC ? '#8c5a3c' : '#5e3b25'); bench.position.set(0, 0.85, -0.45);
  const judge = makeMini('#1b1b1b', isC ? '#c98b62' : '#e8b48f', { wig: true, scale: 0.7 }); judge.position.set(0, 0.62, -0.62);
  room.add(at(box(1.0, 0.65, 0.3, isC ? '#8c5a3c' : '#5e3b25'), 0, 0.32, -0.45), bench, judge);
  const a = makeMini(isC ? '#e07a5f' : '#1f3a5f', '#8d5a3b', { scale: 0.75 }); a.position.set(-0.5, 0, 0.25); a.rotation.y = 0.6;
  const b = makeMini(isC ? '#3d405b' : '#8a96a3', '#e8b48f', { scale: 0.75 }); b.position.set(0.5, 0, 0.25); b.rotation.y = -0.6;
  room.add(a, b);
  if (isC) {
    room.add(at(P.paper('', PAL.mistake, 3, 0.18), -0.32, 0.55, 0.35, 0.4), at(P.paper('', PAL.mistake, 3, 0.18), 0.32, 0.55, 0.35, -0.4));
  }
}

const s2 = {
  setup(S) {
    studio(S.scene, '#fff4e0', '#ffe2b8', '#f2cf9e');
    P.lights(S.scene, { sunPos: [-4, 9, 7] });
    const dc = P.doorway(PAL.teal, 'CIVIL'); dc.position.set(0.7, 0, -0.6); fillRoom(dc.userData.room, 'civil'); S.scene.add(dc); S.cache.set('dcivil', dc);
    const dk = P.doorway(PAL.purple, 'CRIMINAL', true); dk.position.set(3.1, 0, -0.6); fillRoom(dk.userData.room, 'criminal'); S.scene.add(dk); S.cache.set('dcrim', dk);
  },
  draw(S, t, st, cam, hud) {
    const o1 = easeInOut(prog(t, st.at('lex2a') - 0.1, 0.9)), o2 = easeInOut(prog(t, st.at('lex2b') - 0.1, 0.9));
    const dc = S.get('dcivil'), dk = S.get('dcrim');
    dc.userData.hinge.rotation.y = -1.95 * o1;
    dk.userData.hinge.rotation.y = 1.95 * o2;
    chip3(S, 'lc', 'CIVIL', 0.7, 3.05, -0.4, { bg: PAL.teal, size: 44 });
    chip3(S, 'lk', 'CRIMINAL', 3.1, 3.05, -0.4, { bg: PAL.purple, size: 44 });
    const coin = S.get('coin', () => P.coinStack(1));
    const ph = (t * 0.5) % 1;
    coin.position.set(0.7 + lerp(0.45, -0.45, easeInOut(ph)), 0.9 + Math.sin(Math.PI * ph) * 0.35, -1.25);
    coin.rotation.set(Math.PI / 2, 0, t * 3); coin.scale.setScalar(0.6);
    coin.visible = o1 > 0.3;
    chip3(S, 'q', '?', 3.6, 1.35, -1.2, { bg: '#ffffff', fg: PAL.purple, size: 50, s: (1 + 0.06 * Math.sin(t * 4)) * (o2 > 0.3 ? 1 : 0) });
    for (const [x, key, label, c] of [[0.7, 'lex2a', 'Balance of probabilities', PAL.teal], [3.1, 'lex2b', 'Beyond reasonable doubt', PAL.purple]]) {
      chip3(S, 'std' + key, label, x, 0.35, 0.6, { bg: c, size: 34, s: pop(t, st.at(key) + 2.2, 0.5) });
    }
    const lpose = poseTrack(t, [[0, 'idle'], [st.at('lex2a'), 'point'], [st.end('lex2b'), 'idle'], [st.at('lex2c'), 'present']]);
    person(S, st, t, 'LEX', -1.3, 0.4, { pose: lpose, mood: 'happy', ry: t < st.end('lex2b') ? 0.45 : -0.1, look: t < st.end('lex2b') ? 0.3 : -0.3 });
    const npose = poseTrack(t, [[0, 'idle'], [st.at('nia2'), 'think'], [st.end('nia2'), 'idle']]);
    person(S, st, t, 'NIA', -3.0, 0.6, { pose: npose, mood: st.during('nia2', t) ? 'thinking' : 'neutral', ry: 0.45, look: 0.2 });
    camTrack(cam, t, [
      K(0, [-0.6, 2.4, 10.5], [0.3, 1.4, 0]),
      K(st.at('lex2a'), [-0.2, 2.2, 9.5], [0.4, 1.4, 0]),
      K(st.at('lex2a') + 1.6, [0.9, 1.8, 5.2], [0.7, 1.2, -0.8]),
      K(st.at('lex2b'), [1.0, 1.8, 5.4], [0.8, 1.2, -0.8]),
      K(st.at('lex2b') + 1.4, [2.8, 1.8, 5.2], [3.0, 1.2, -0.8]),
      K(st.at('nia2'), [2.6, 1.8, 5.4], [2.8, 1.2, -0.8]),
      K(st.at('nia2') + 1.2, [-0.4, 2.3, 10.2], [0.2, 1.4, 0]),
      K(st.dur, [-0.3, 2.3, 10.0], [0.2, 1.4, 0]),
    ]);
    if (t >= st.at('lex2c')) chipDraw(hud, 'ban', 'Classify the facts, then choose the rule', 960, 95, { bg: PAL.accent, fg: PAL.ink, size: 44, s: pop(t, st.at('lex2c') + 0.6, 0.5) });
  },
};

// ============================================================== SCENE 3
const s3 = {
  setup(S) {
    bg(S.scene, '#7cc6f5', '#e3f6ff');
    S.scene.fog = new THREE.Fog('#d6efff', 22, 60);
    P.lights(S.scene, { sunPos: [5, 10, 6], sun: 2.6, span: 12 });
    const gt = canvasTex('grass', 512, 512, (g, w, h) => {
      g.fillStyle = '#93c47d'; g.fillRect(0, 0, w, h);
      g.strokeStyle = 'rgba(255,255,255,0.35)'; g.lineWidth = 4;
      for (let i = 0; i <= w; i += 64) { g.beginPath(); g.moveTo(i, 0); g.lineTo(i, h); g.stroke(); g.beginPath(); g.moveTo(0, i); g.lineTo(w, i); g.stroke(); }
    });
    gt.tex.wrapS = gt.tex.wrapT = THREE.RepeatWrapping; gt.tex.repeat.set(12, 12);
    const ground = mesh(new THREE.PlaneGeometry(80, 80), new THREE.MeshStandardMaterial({ map: gt.tex, roughness: 0.95 }), { cast: false, receive: true });
    ground.rotation.x = -Math.PI / 2; S.scene.add(ground);
    const road = mesh(new THREE.PlaneGeometry(80, 1.2), mat('#c9c3b6', { rough: 0.9 }), { cast: false, receive: true });
    road.rotation.x = -Math.PI / 2; road.position.set(0, 0.01, 1.3); S.scene.add(road);
    for (let i = 0; i < 7; i++) { const tr = new THREE.Group(); tr.add(at(cyl(0.08, 0.1, 0.6, '#8c5a3c'), 0, 0.3, 0), at(sphere(0.45, '#3bb273', { rough: 0.8 }), 0, 0.95, 0)); tr.position.set(-9 + i * 3.4, 0, -5 - (i % 2) * 1.5); S.scene.add(tr); }
    for (let i = 0; i < 4; i++) { const cl = new THREE.Group(); [[0, 0, 0.9], [0.9, 0.2, 1.1], [1.9, 0, 0.8]].forEach(([x, y, r]) => cl.add(at(sphere(r, '#ffffff', { rough: 1 }), x, y, 0))); cl.position.set(-12 + i * 8, 9 + (i % 2), -18); S.scene.add(cl); S.cache.set('cloud' + i, cl); }
  },
  draw(S, t, st, cam, hud) {
    for (let i = 0; i < 4; i++) { const cl = S.get('cloud' + i); cl.position.x = -14 + ((i * 8 + t * 0.4) % 32); }
    const items = [['lex3a', 0.4, P.parliament, 'LEGISLATURE', 'makes', PAL.teal], ['lex3b', 3.0, P.officeBlock, 'EXECUTIVE', 'implements', PAL.purple], ['lex3c', 5.6, P.courthouse, 'JUDICIARY', 'interprets / applies', PAL.mistake]];
    for (const [key, x, fn, lab, sub, c] of items) {
      const t0 = st.at(key) - 0.4;
      const b = S.get('b' + key, () => fn());
      const k = easeOutBack(prog(t, t0, 1.0), 1.1);
      b.position.set(x, lerp(-3.5, 0, k), -1.0);
      b.rotation.y = -0.15;
      let hl = win(t, st.at(key), st.end(key), 0.3);
      if (key === 'lex3c') hl = Math.max(hl, win(t, st.at('lex3d'), st.end('lex3d'), 0.3));
      const L = S.get('l' + key, () => new THREE.PointLight('#ffd166', 0, 6));
      L.position.set(x, 2.2, 1.0); L.intensity = 12 * hl;
      const s = pop(t, t0 + 0.6, 0.5);
      chip3(S, 'c' + key, lab, x, 0.62, 1.0, { bg: c, size: 34, s });
      chip3(S, 's' + key, sub, x, 0.25, 1.0, { bg: '#ffffff', fg: PAL.ink, size: 28, s });
    }
    if (t >= st.at('lex3d')) {
      const k = easeOut(prog(t, st.at('lex3d'), 1.2));
      const pr = S.get('principle', () => P.paper('PRINCIPLE', PAL.mistake, 2, 0.6));
      pr.position.set(5.6, 2.7 + 0.5 * k, -0.4); pr.rotation.set(0, Math.sin(t) * 0.3, 0);
      setOpacity(pr, k * (1 - prog(t, st.at('summary') + 0.2, 0.5)));
    }
    const kpose = poseTrack(t, [[0, 'idle'], [st.at('kito3'), 'think'], [st.end('kito3'), 'hips']]);
    person(S, st, t, 'KITO', -1.4, 0.9, { pose: kpose, mood: st.during('kito3', t) ? 'thinking' : 'neutral', ry: st.during('kito3', t) || st.during('lex3d', t) ? -0.5 : 0.4 });
    const lpose = poseTrack(t, [[0, 'idle'], [st.at('lex3a') - 0.3, 'point_up'], [st.end('lex3c'), 'idle'], [st.at('lex3d'), 'present']]);
    person(S, st, t, 'LEX', -3.3, 0.9, { pose: lpose, mood: 'happy', ry: 0.5 });
    camTrack(cam, t, [
      K(0, [-2.0, 1.8, 6.5], [-2.2, 1.3, 0]),
      K(st.at('lex3a') - 0.5, [-0.6, 2.6, 10.5], [0.8, 1.4, 0]),
      K(st.at('lex3a'), [-0.2, 2.4, 9.0], [0.6, 1.5, -1]),
      K(st.at('lex3b'), [1.2, 2.4, 9.0], [2.2, 1.5, -1]),
      K(st.at('lex3c'), [2.6, 2.5, 9.0], [3.6, 1.5, -1]),
      K(st.at('kito3'), [1.2, 2.8, 11.8], [1.2, 1.5, 0]),
      K(st.dur, [1.3, 2.9, 12.2], [1.2, 1.5, 0]),
    ]);
    if (t >= st.at('summary') - 0.2) {
      const s = pop(t, st.at('summary') - 0.2, 0.5);
      hud.draw('sum', 1700, 120, 960, 110, (g, w, h) => {
        g.fillStyle = PAL.ink; rr(g, 0, 0, w, h, 26); g.fill();
        let x = 50; g.textBaseline = 'middle';
        for (const [lab, sub, c] of [['Legislature', 'makes', '#9fe3df'], ['Executive', 'implements', '#c9c1ff'], ['Judiciary', 'interprets / applies', '#ffb4a2']]) {
          g.font = font(44, 700); g.fillStyle = c; g.fillText(lab, x, h / 2); x += g.measureText(lab).width;
          g.font = font(44, 500); g.fillStyle = '#fff'; g.fillText(' = ' + sub, x, h / 2); x += g.measureText(' = ' + sub).width + 60;
        }
      }, s);
    }
  },
};

// ============================================================== SCENE 4
function decisionTex(withObiter) {
  return canvasTex('decision' + withObiter, 600, 400, (g, w, h) => {
    g.fillStyle = '#ffffff'; g.fillRect(0, 0, w, h);
    g.fillStyle = PAL.accent; g.fillRect(0, 0, w, 80);
    g.fillStyle = PAL.ink; g.font = font(40, 700); g.textAlign = 'center'; g.fillText('EARLIER DECISION', w / 2, 55);
    g.textAlign = 'left';
    if (!withObiter) {
      g.fillStyle = 'rgba(255,182,39,0.25)'; rr(g, 110, 110, 460, 120, 14); g.fill();
      g.fillStyle = PAL.teal; g.font = font(40, 700); g.fillText('RATIO DECIDENDI', 135, 160);
      g.fillStyle = PAL.ink; g.font = font(30, 500); g.fillText('legal reason necessary', 135, 204);
      // gavel icon
      g.save(); g.translate(60, 170); g.rotate(-0.5); g.fillStyle = '#a26d4a'; rr(g, -30, -22, 60, 30, 8); g.fill(); g.fillStyle = '#8c5a3c'; g.fillRect(-5, 6, 10, 60); g.restore();
    } else {
      g.clearRect(0, 0, w, h);
      g.fillStyle = PAL.grey; g.font = font(36, 600); g.fillText('obiter dicta', 135, 300);
      g.font = font(28, 500); g.fillText('additional observations', 135, 340);
      g.fillStyle = '#dfe5ea'; rr(g, 380, 270, 150, 40, 20); g.fill(); g.fillStyle = '#5b6670'; g.font = font(22, 600); g.fillText('persuasive', 400, 298);
    }
  });
}

function panelTex(kind) {
  const spec = { reverse: ['REVERSE', PAL.teal], overrule: ['OVERRULE', PAL.purple], distinguish: ['DISTINGUISH', PAL.mistake] }[kind];
  return canvasTex('panel' + kind, 350, 560, (g, w, h) => {
    g.fillStyle = '#fff'; g.fillRect(0, 0, w, h);
    g.fillStyle = spec[1]; g.fillRect(0, 0, w, 86);
    g.fillStyle = '#fff'; g.font = font(42, 700); g.textAlign = 'center'; g.fillText(spec[0], w / 2, 58);
    g.textAlign = 'center';
    const doc = (x, y, ww, hh, rot, title, c) => {
      g.save(); g.translate(x, y); g.rotate(rot);
      g.fillStyle = 'rgba(0,0,0,0.15)'; g.fillRect(-ww / 2 + 5, -hh / 2 + 6, ww, hh);
      g.fillStyle = '#fff'; g.strokeStyle = '#c9c9c9'; g.lineWidth = 3; g.fillRect(-ww / 2, -hh / 2, ww, hh); g.strokeRect(-ww / 2, -hh / 2, ww, hh);
      g.fillStyle = c; g.fillRect(-ww / 2, -hh / 2, ww, 30);
      if (title) { g.fillStyle = '#fff'; g.font = font(20, 700); g.fillText(title, 0, -hh / 2 + 22); }
      g.strokeStyle = '#c4ccd4'; g.lineWidth = 6; for (let i = 0; i < 3; i++) { g.beginPath(); g.moveTo(-ww / 2 + 14, -hh / 2 + 55 + i * 26); g.lineTo(ww / 2 - 14, -hh / 2 + 55 + i * 26); g.stroke(); }
      g.restore();
    };
    g.fillStyle = PAL.ink; g.font = font(28, 600);
    if (kind === 'reverse') {
      g.fillStyle = '#dfe5ea'; g.strokeStyle = '#8a96a3'; g.lineWidth = 3;
      for (let i = 0; i < 3; i++) { g.fillRect(45 + i * 90, 440 - (i + 1) * 90, 90, (i + 1) * 90); g.strokeRect(45 + i * 90, 440 - (i + 1) * 90, 90, (i + 1) * 90); }
      g.fillStyle = '#5b6670'; g.font = font(24, 600); g.fillText('Trial', 90, 340); g.fillText('Appeal', 270, 160);
      doc(130, 250, 70, 90, 0, '', PAL.teal); doc(270, 110, 70, 90, 0, '', PAL.teal);
      g.strokeStyle = PAL.accent; g.lineWidth = 8; g.beginPath(); g.moveTo(170, 230); g.lineTo(240, 150); g.stroke();
      g.fillStyle = PAL.mistake; g.beginPath(); g.arc(150, 300, 22, 0, 7); g.fill(); g.strokeStyle = '#fff'; g.lineWidth = 6; g.beginPath(); g.moveTo(141, 291); g.lineTo(159, 309); g.moveTo(159, 291); g.lineTo(141, 309); g.stroke();
      g.fillStyle = PAL.ink; g.font = font(30, 600); g.fillText('same case', w / 2, 500);
    } else if (kind === 'overrule') {
      doc(110, 210, 120, 150, -0.1, 'Case A', PAL.grey);
      g.strokeStyle = PAL.mistake; g.lineWidth = 9; g.beginPath(); g.moveTo(50, 140); g.lineTo(170, 280); g.moveTo(170, 140); g.lineTo(50, 280); g.stroke();
      g.strokeStyle = PAL.ink; g.lineWidth = 7; g.beginPath(); g.moveTo(140, 330); g.lineTo(200, 330); g.stroke();
      g.fillStyle = PAL.ink; g.beginPath(); g.moveTo(215, 330); g.lineTo(195, 318); g.lineTo(195, 342); g.fill();
      doc(250, 330, 120, 150, 0.1, 'Case B', PAL.purple);
      g.fillStyle = PAL.ink; g.font = font(28, 600); g.fillText('later case,', w / 2, 470); g.fillText('rule changes', w / 2, 506);
    } else {
      doc(90, 230, 120, 160, -0.07, 'Earlier', PAL.grey); doc(260, 230, 120, 160, 0.07, 'Now', PAL.accent);
      g.fillStyle = PAL.teal; g.beginPath(); g.arc(90, 240, 22, 0, 7); g.fill(); g.fillRect(70, 270, 40, 40);
      g.beginPath(); g.arc(260, 240, 22, 0, 7); g.fill();
      g.fillStyle = PAL.mistake; g.beginPath(); g.moveTo(260, 268); g.lineTo(285, 312); g.lineTo(235, 312); g.fill();
      g.fillStyle = PAL.mistake; g.font = '700 80px Nunito'; g.fillText('≠', 175, 260);
      g.fillStyle = PAL.ink; g.font = font(28, 600); g.fillText('material facts', w / 2, 450); g.fillText('differ', w / 2, 486);
    }
  });
}

const s4 = {
  setup(S) {
    studio(S.scene, '#eaf4ff', '#cfe3f7', '#b9d3ea');
    P.lights(S.scene, { sunPos: [-3, 9, 7], sky: '#eaf4ff' });
  },
  draw(S, t, st, cam, hud) {
    const pb = st.at('panels');
    const fa = 1 - easeInOut(prog(t, pb - 0.3, 0.5));
    // earlier decision card (3D slab)
    const card = S.get('card', () => {
      const g = new THREE.Group();
      const slab = rbox(2.5, 1.7, 0.08, 0.1, '#ffb627', { rough: 0.35, metal: 0.2 }); g.add(slab);
      const face = texPlane(decisionTex(false), 2.4 / 600, { lit: false }); face.position.z = 0.05; g.add(face);
      const ob = texPlane(decisionTex(true), 2.4 / 600, { lit: false }); ob.position.z = 0.051; g.add(ob);
      g.userData.ob = ob;
      const L = new THREE.PointLight('#fff1b8', 6, 5); L.position.set(0, 0, 1.2); g.add(L);
      return g;
    });
    const move = easeInOut(prog(t, st.at('lex4c') + 2.2, 1.2));
    const cs = pop(t, st.at('card'), 0.6) * lerp(1, 0.55, move);
    card.position.set(lerp(1.2, 1.2, move), lerp(2.3, 1.05, move), lerp(0, 0.75, move));
    card.rotation.set(lerp(0, -0.9, move), Math.sin(t * 0.8) * 0.12 * (1 - move), 0);
    card.scale.setScalar(Math.max(cs, 1e-4));
    setOpacity(card.userData.ob, easeInOut(prog(t, st.at('lex4b'), 0.5)));
    card.userData.ob.material.opacity *= fa;
    card.visible = fa > 0.01;
    // new case folder
    const fs = pop(t, st.at('lex4c') + 0.6, 0.5) * (fa > 0.01 ? 1 : 0);
    const folder = S.get('folder', () => {
      const g = new THREE.Group();
      g.add(at(rbox(2.0, 0.12, 1.3, 0.04, '#f2c46d'), 0, 0.06, 0));
      g.add(at(rbox(0.7, 0.06, 0.3, 0.03, '#e9b44c'), -0.6, 0.12, -0.55));
      const lab = texPlane(textTex('NEW CASE', 60, '#7a5208'), 0.004, { lit: true }); lab.rotation.x = -Math.PI / 2; lab.position.set(0, 0.125, 0.35); g.add(lab);
      return g;
    });
    folder.position.set(1.2, 0.5, 0.6); folder.scale.setScalar(Math.max(fs, 1e-4)); folder.visible = fs > 0.01;
    const stand = S.get('stand', () => at(cyl(0.6, 0.7, 0.5, '#9fc3e6'), 0, 0.25, 0));
    stand.position.set(1.2, 0.25, 0.6); stand.visible = fs > 0.01; stand.scale.set(1.6 * Math.max(fs, 1e-4), 1, 1.0 * Math.max(fs, 1e-4));
    // court ladder as 3D steps
    const la = easeInOut(prog(t, st.at('lex4c'), 0.6)) * fa;
    const labels = ['Supreme Court', 'Appeal Court', 'High Court', 'Lower courts'];
    labels.forEach((lab, i) => {
      const step = S.get('step' + i, () => rbox(1.5, 0.5, 0.9, 0.06, new THREE.Color(PAL.navy).lerp(new THREE.Color('#9fc3e6'), i / 3).getStyle()));
      step.position.set(4.0 + i * 0.25, lerp(-2, 2.75 - i * 0.62, easeOutBack(la, 1.2)), -0.6 + i * 0.35);
      step.visible = la > 0.01;
      chip3(S, 'stepl' + i, lab, 4.0 + i * 0.25, step.position.y + 0.02, 0.15 + i * 0.35, { bg: '#ffffff00', fg: '#ffffff', size: 30, a: la, s: la > 0.01 ? 1 : 0 });
    });
    chip3(S, 'binds', 'binds', 5.35, 1.85, 0.4, { bg: PAL.accent, fg: PAL.ink, size: 28, a: la, s: la > 0.01 ? 1 : 0 });
    [['Superior court', 4.0], ['Similar material facts', 5.4]].forEach(([lab, dt], i) => {
      const t0 = Math.min(st.at('lex4c') + dt, st.end('lex4c') - 0.2);
      const o = S.get('chk' + i, () => { const p = texPlane(checkTex(lab, 32), 0.0045); p.userData.billboard = true; p.renderOrder = 10; return p; });
      o.position.set(2.75, 1.1 - i * 0.4, 1.3); o.scale.setScalar(Math.max(pop(t, t0, 0.4) * fa, 1e-4)); o.visible = t >= t0 && fa > 0.01;
    });
    // phase B: three 3D panels
    [['lex4d', -0.1, 'reverse'], ['lex4e', 1.95, 'overrule'], ['lex4f', 4.0, 'distinguish']].forEach(([key, x, kind]) => {
      const tp = st.at(key) - 0.1;
      const pnl = S.get('p' + kind, () => {
        const g = new THREE.Group();
        g.add(rbox(1.85, 2.9, 0.1, 0.08, PAL.ink));
        const f = texPlane(panelTex(kind), 1.7 / 350, { lit: false }); f.position.z = 0.06; g.add(f);
        return g;
      });
      const k = easeOutBack(prog(t, tp, 0.6), 1.3);
      const hl = win(t, st.at(key), st.end(key), 0.3);
      pnl.visible = t >= tp;
      pnl.position.set(x, 1.75 + 0.12 * hl, -0.3 + 0.25 * hl);
      pnl.rotation.y = lerp(Math.PI / 2, -0.06 * (x - 2), k);
      pnl.scale.setScalar(1 + 0.04 * hl);
    });
    const lpose = poseTrack(t, [[0, 'idle'], [st.at('lex4a'), 'point'], [st.end('lex4c'), 'idle'], [st.at('lex4d'), 'point'], [st.at('lex4g'), 'present']]);
    person(S, st, t, 'LEX', -3.4, 0.8, { pose: lpose, mood: 'happy', ry: 0.5 });
    const npose = poseTrack(t, [[0, 'idle'], [st.at('lex4c') + 1.8, 'point'], [st.at('lex4c') + 4.0, 'idle']]);
    person(S, st, t, 'NIA', -1.9, 1.1, { pose: npose, mood: st.during('lex4c', t) ? 'excited' : 'neutral', ry: 0.45 });
    camTrack(cam, t, [
      K(0, [-1.0, 2.0, 7.5], [-1.0, 1.6, 0]),
      K(st.at('card') + 0.4, [-0.4, 2.2, 9.0], [0.4, 1.7, 0]),
      K(st.at('lex4a'), [-0.2, 2.3, 7.4], [0.5, 1.8, 0]),
      K(st.at('lex4c'), [0.3, 2.3, 7.2], [1.2, 1.8, 0]),
      K(st.at('lex4c') + 2.0, [0.6, 2.8, 10.0], [1.4, 1.5, 0]),
      K(pb, [0.6, 2.8, 10.0], [1.4, 1.5, 0]),
      K(st.at('lex4d'), [0.4, 2.2, 9.6], [1.2, 1.6, 0]),
      K(st.at('lex4g'), [0.0, 2.4, 10.4], [0.9, 1.5, 0]),
      K(st.dur, [0.0, 2.5, 10.8], [0.9, 1.5, 0]),
    ]);
    if (t >= st.at('lex4g')) chipDraw(hud, 'ban4', 'Read the facts · Court hierarchy · What was necessary?', 960, 1000, { bg: PAL.accent, fg: PAL.ink, size: 38, s: pop(t, st.at('lex4g') + 0.3, 0.5) });
  },
};

// ============================================================== SCENE 5
const s5 = {
  setup(S) {
    studio(S.scene, '#fff1ea', '#ffd9c7', '#f1c2ab');
    P.lights(S.scene, { sunPos: [-4, 9, 7] });
  },
  draw(S, t, st, cam, hud) {
    const gridT = st.at('lex5b') - 0.2;
    const ga = 1 - easeInOut(prog(t, gridT - 0.4, 0.4));
    const ghost = S.get('ghost', () => P.machine(true));
    ghost.position.set(0.9, 0.5, -0.4); P.spinMachine(ghost, t); ghost.visible = ga > 0.01;
    const ped = S.get('ped', () => at(cyl(1.1, 1.2, 0.5, '#8a96a3'), 0, 0.25, 0));
    ped.position.set(0.9, 0.25, -0.4); ped.visible = ga > 0.01;
    chip3(S, 'qm', '?', 0.9, 1.25, 0.2, { bg: '#ffffff', fg: PAL.mistake, size: 90, a: ga, s: ga > 0.01 ? 1 + 0.05 * Math.sin(t * 4) : 0 });
    chip3(S, 'uniq', 'Unique custom machine', 0.9, 2.15, -0.3, { bg: PAL.navy, size: 34, a: ga });
    if (t >= st.at('lex5a')) {
      const k = pop(t, st.at('lex5a') + 0.3, 0.5) * (ga > 0.01 ? 1 : 0);
      const coins = S.get('coins', () => P.coinStack(5));
      coins.position.set(3.0, 0, 0.2); coins.scale.setScalar(Math.max(k * 1.6, 1e-4)); coins.rotation.y = t;
      const ne = S.get('neq', () => { const p = texPlane(chipTex('≠', '#ffffff', PAL.mistake, 80, 'Nunito'), 0.0045); p.userData.billboard = true; return p; });
      ne.position.set(2.0, 0.9, 0.2); ne.scale.setScalar(Math.max(k, 1e-4));
      chip3(S, 'dmg', 'Damages not always adequate', 3.0, 1.45, 0.4, { bg: PAL.mistake, size: 30, s: k });
    }
    const tiles = [['lex5b', 0.0, -1.0, 'Specific performance'], ['lex5c', 2.3, -1.0, 'Injunction'], ['lex5d', 0.0, 0.9, 'Rescission'], ['lex5e', 2.3, 0.9, 'Rectification']];
    for (const [key, x, z, lab] of tiles) {
      const tp = st.at(key) - 0.1;
      if (t < tp) continue;
      const s = pop(t, tp, 0.5);
      const hl = win(t, st.at(key), st.end(key) + 0.2, 0.2);
      const base = S.get('base' + key, () => at(cyl(0.85, 0.9, 0.3, '#ffffff', { rough: 0.4 }), 0, 0.15, 0));
      base.position.set(x, 0.15, z); base.scale.set(s, 1, s);
      const ring = S.get('ring' + key, () => { const r = mesh(new THREE.TorusGeometry(0.87, 0.04, 8, 48), new THREE.MeshBasicMaterial({ color: PAL.accent, toneMapped: false })); r.rotation.x = Math.PI / 2; return r; });
      ring.position.set(x, 0.31, z); ring.scale.setScalar(Math.max(s, 1e-4)); ring.visible = hl > 0.05;
      const icon = S.get('icon' + key, () => ({ lex5b: P.truck, lex5c: P.stopSign, lex5d: () => { const g = new THREE.Group(); g.add(at(P.paper('DEAL', PAL.purple, 4, 0.5), 0, 0.55, 0)); const a = P.rewindArrow(); a.position.y = 0.55; g.add(a); g.userData.spin = a; return g; }, lex5e: () => { const g = new THREE.Group(); g.add(at(P.paper('TERMS', PAL.teal, 3, 0.55), 0, 0.55, 0)); const pc = P.pencil(); g.add(pc); g.userData.pencil = pc; return g; } })[key]());
      icon.position.set(x, 0.3, z); icon.scale.setScalar(Math.max(s * (1 + 0.06 * hl), 1e-4));
      icon.rotation.y = key === 'lex5b' ? t * 0.6 : Math.sin(t * 0.7 + x) * 0.25;
      if (icon.userData.spin) icon.userData.spin.rotation.z = -t * 2;
      if (icon.userData.pencil) { icon.userData.pencil.position.set(0.25 + Math.sin(t * 6) * 0.05, 0.45, 0.12); icon.userData.pencil.rotation.z = -0.6; }
      if (icon.userData.wheels) icon.userData.wheels.forEach((w) => (w.rotation.y = t * 5));
      chip3(S, 'lab' + key, lab, x, 1.65 + (key === 'lex5c' ? 0.2 : 0), z + 0.4, { bg: hl > 0.3 ? PAL.accent : '#ffffff', fg: PAL.ink, size: 32, s });
    }
    const kpose = poseTrack(t, [[0, 'hold_r'], [st.end('kito5') + 0.3, 'idle'], [st.at('lex5f'), 'hips']]);
    const kito = person(S, st, t, 'KITO', -3.6, 0.7, { pose: kpose, mood: t < st.end('kito5') ? 'angry' : 'thinking', ry: 0.45 });
    const money = S.get('cash', () => P.cash());
    if (t < st.end('kito5') + 0.4) { const hp = handPos(kito); money.position.set(hp.x, hp.y + 0.05, hp.z + 0.1); money.rotation.set(0, 0.3, Math.sin(t * 6) * 0.2); } else money.visible = false;
    const npose = poseTrack(t, [[0, 'idle'], [st.at('nia5a'), 'present'], [st.end('nia5a'), 'idle'], [st.at('nia5b'), 'think']]);
    person(S, st, t, 'NIA', -2.0, 0.9, { pose: npose, mood: st.during('nia5a', t) ? 'worried' : st.during('nia5b', t) ? 'thinking' : 'neutral', ry: t < st.end('nia5a') ? -0.6 : 0.4 });
    const lpose = poseTrack(t, [[0, 'idle'], [st.at('lex5b') - 0.3, 'point_l'], [st.end('lex5e'), 'idle'], [st.at('lex5f'), 'present']]);
    const lx = lerp(7.5, 4.6, easeOut(prog(t, 0.2, 1.2)));
    person(S, st, t, 'LEX', lx, 0.6, { pose: lpose, mood: 'happy', ry: -0.55 });
    camTrack(cam, t, [
      K(0, [-2.0, 1.9, 7.2], [-1.6, 1.4, 0]),
      K(st.at('lex5a'), [-1.2, 2.0, 8.0], [-0.6, 1.4, 0]),
      K(st.at('lex5a') + 1.5, [0.6, 2.4, 9.5], [1.2, 1.2, 0]),
      K(gridT, [0.6, 2.6, 9.5], [1.2, 1.1, 0]),
      K(st.at('lex5b') + 0.6, [1.0, 3.6, 8.0], [1.1, 0.8, -0.2]),
      K(st.at('lex5f'), [0.8, 3.3, 9.6], [0.9, 1.0, 0]),
      K(st.dur, [0.6, 3.2, 10.6], [0.6, 1.1, 0]),
    ]);
    if (t >= st.at('lex5f')) {
      const s = pop(t, st.at('lex5f') + 0.4, 0.4);
      hud.draw('stamp', 740, 160, 960, 930, (g, w, h) => {
        g.fillStyle = 'rgba(255,255,255,0.88)'; rr(g, 6, 6, w - 12, h - 12, 18); g.fill();
        g.strokeStyle = PAL.mistake; g.lineWidth = 10; rr(g, 6, 6, w - 12, h - 12, 18); g.stroke();
        g.fillStyle = PAL.mistake; g.textAlign = 'center'; g.font = font(64, 700); g.fillText('DISCRETIONARY', w / 2, 82);
        g.font = font(36, 600); g.fillText('not automatic', w / 2, 128);
      }, s > 0 ? 1.6 - 0.6 * Math.min(s, 1.2) : 0, Math.min(1, s), 2, 0.17);
    }
  },
};

// ============================================================== SCENE 6
const ORGS = [['UN', '#4f9dd0'], ['UNCITRAL', PAL.teal], ['WTO', PAL.purple], ['ICC', PAL.mistake], ['UNIDROIT', PAL.green], ['OECD', PAL.amber]];
const s6 = {
  setup(S) {
    bg(S.scene, '#0e1b2e', '#24426b');
    P.lights(S.scene, { sky: '#9fc3e6', ground: '#0e1b2e', sun: 2.4, sunPos: [-5, 6, 8] });
    S.scene.add(P.stars(900, 35));
    const disc = mesh(new THREE.CylinderGeometry(9, 9, 0.2, 64), mat('#1a2f4d', { rough: 0.25, metal: 0.4 }), { cast: false, receive: true });
    disc.position.y = -0.1; S.scene.add(disc);
  },
  draw(S, t, st, cam, hud) {
    const g = S.get('globe', () => P.globe(1.6));
    g.position.set(0.6, 2.3, -1.0); g.userData.ball.rotation.y = t * 0.35; g.rotation.z = 0.35;
    const focus = { UNCITRAL: 'lex6c', WTO: 'lex6d', ICC: 'lex6e' };
    const anyFocus = Object.values(focus).some((k) => st.during(k, t));
    ORGS.forEach(([n, c], i) => {
      const tp = st.at('lex6a') + 0.6 + i * 0.35;
      const ang = i * (Math.PI * 2 / ORGS.length) + t * 0.12;
      const x = 0.6 + Math.cos(ang) * 2.7, z = -1.0 + Math.sin(ang) * 2.0, y = 2.3 + Math.sin(ang) * 0.9 * 0.35 + Math.cos(ang * 2) * 0.15;
      const hl = n in focus ? win(t, st.at(focus[n]), st.end(focus[n]), 0.3) : 0;
      const a = !anyFocus || hl > 0.5 ? 1 : 0.4;
      chip3(S, 'org' + n, n, x, y, z, { bg: c, size: 44, s: pop(t, tp, 0.5) * (1 + 0.35 * hl), a });
    });
    const descs = { lex6c: 'Harmonised commercial-law texts', lex6d: 'Framework for trade cooperation', lex6e: 'Commercial rules (incl. Incoterms) · dispute resolution' };
    for (const [k, d] of Object.entries(descs)) {
      const a = win(t, st.at(k) + 0.2, st.end(k) + 0.2, 0.3);
      if (a > 0) hud.chip('d' + k, d, 960, 990, { bg: '#ffffff', fg: PAL.ink, size: 38, a });
    }
    const ca = win(t, st.at('lex6b'), st.at('cargo_in') - 0.3, 0.4);
    if (ca > 0) {
      hud.card('treaty', 1650, 330, 400, 200, { title: 'TREATY / CONVENTION', body: 'create shared rules', accent: PAL.teal, titleSize: 32, bodySize: 36 }, pop(t, st.at('lex6b'), 0.5), ca);
      hud.card('model', 1650, 590, 400, 200, { title: 'MODEL LAW', body: 'a template to adopt', accent: PAL.purple, titleSize: 32, bodySize: 36 }, pop(t, st.at('lex6b') + 2.0, 0.5), ca);
    }
    if (t >= st.at('cargo_in') - 0.1) {
      const k = easeOut(prog(t, st.at('cargo_in') - 0.1, 1.0));
      cargo(S, st, t, lerp(9, 3.8, k), 0, 1.0, { ry: -0.5, mood: st.during('cargo6', t) ? 'surprised' : undefined });
    }
    if (t >= st.at('lex6f')) hud.chip('forum', 'Court or arbitration? Agreement + applicable law', 960, 990, { bg: PAL.accent, fg: PAL.ink, size: 38, s: pop(t, st.at('lex6f') + 0.6, 0.5) });
    const lpose = poseTrack(t, [[0, 'idle'], [st.at('lex6a'), 'present'], [st.at('lex6c'), 'point'], [st.end('lex6e'), 'idle'], [st.at('lex6f'), 'present']]);
    person(S, st, t, 'LEX', -3.4, 0.8, { pose: lpose, mood: 'happy', ry: t > st.at('cargo_in') ? 0.7 : 0.45 });
    const ang = lerp(-0.25, 0.2, t / st.dur);
    camTrack(cam, t, [
      K(0, [0.6 + Math.sin(ang) * 11, 2.6, Math.cos(ang) * 11], [0.4, 1.9, -0.5]),
      K(st.dur * 0.5, [0.6 + Math.sin(0) * 10, 2.5, 10], [0.4, 1.9, -0.5]),
      K(st.at('cargo_in'), [0.6 + Math.sin(0.15) * 10, 2.4, 10], [0.5, 1.8, -0.3]),
      K(st.dur, [0.8, 2.3, 10.5], [0.5, 1.7, 0]),
    ]);
  },
};

// ============================================================== SCENE 7
const s7 = {
  setup(S) {
    bg(S.scene, '#1d2b3a', '#2d4058');
    P.lights(S.scene, { sunPos: [0, 10, 8], span: 14, sun: 2.4 });
    const court = P.courtroom(); court.position.set(-4.7, 0, 0); S.scene.add(court);
    const arb = P.arbRoom(); arb.position.set(4.7, 0, 0); S.scene.add(arb);
    S.scene.add(at(box(0.3, 6, 6, '#1d2b3a'), 0, 3, -0.2));
    const fl = P.floor('#3a4d63'); fl.position.y = -0.06; S.scene.add(fl);
  },
  draw(S, t, st, cam, hud) {
    const hlC = win(t, st.at('lex7a'), st.end('lex7a'), 0.3), hlA = win(t, st.at('lex7b'), st.end('lex7b'), 0.3);
    chip3(S, 'court', 'COURT', -4.7, 4.3, -1.5, { bg: PAL.navy, size: 48, s: 1 + 0.15 * hlC, k: 0.006 });
    chip3(S, 'arb', 'ARBITRATION', 4.7, 4.3, -1.5, { bg: PAL.teal, size: 48, s: 1 + 0.15 * hlA, k: 0.006 });
    ['Formal', 'Usually public'].forEach((lab, i) => chip3(S, 'ct' + i, lab, -6.8 + i * 0.4, 3.3 - i * 0.55, -1.5, { bg: '#ffffff', fg: PAL.ink, size: 34, s: pop(t, st.at('lex7a') + 0.8 + i * 1.2, 0.4), k: 0.006 }));
    const tags = ['Private', 'Flexible', 'Specialist expertise', 'Can be expensive', 'Limited grounds to challenge'];
    const span = st.end('lex7b') - st.at('lex7b');
    tags.forEach((lab, i) => chip3(S, 'at' + i, lab, 2.7 + (i % 2) * 2.3 + (i === 4 ? 1.0 : 0), 3.4 - Math.floor(i / 2) * 0.55, -1.5, { bg: i < 3 ? '#ffffff' : '#ffe1d6', fg: PAL.ink, size: 32, s: pop(t, st.at('lex7b') + 0.4 + i * span / 5.5, 0.4), k: 0.006 }));
    const lpose = poseTrack(t, [[0, 'idle'], [st.at('lex7a'), 'point_l'], [st.at('lex7b'), 'point'], [st.end('lex7b'), 'idle'], [st.at('lex7c'), 'present']]);
    person(S, st, t, 'LEX', 0, 3.4, { pose: lpose, mood: 'happy', look: st.during('lex7a', t) ? -0.5 : st.during('lex7b', t) ? 0.5 : 0 });
    if (t >= st.at('nia7') - 0.8) {
      const k = easeOut(prog(t, st.at('nia7') - 0.8, 0.8));
      person(S, st, t, 'NIA', lerp(-6, -1.5, k), 3.6, { pose: st.during('nia7', t) ? 'think' : 'idle', mood: 'thinking', ry: 0.4 });
    }
    const qa = easeInOut(prog(t, st.at('aud_in') - 0.1, 0.5));
    if (qa > 0) {
      const k = easeOut(prog(t, st.at('aud_in') - 0.1, 0.8));
      person(S, st, t, 'AUDITOR', lerp(-9, -2.6, k), 4.6, { pose: 'clipboard', mood: t > st.at('aud2') ? 'smile' : 'neutral', ry: 0.35 });
    }
    camTrack(cam, t, [
      K(0, [0, 3.4, 15.5], [0, 2.0, 0]),
      K(st.at('lex7a'), [0, 3.2, 14.5], [0, 2.0, 0]),
      K(st.at('lex7a') + 1.2, [-3.6, 2.5, 9.0], [-4.0, 2.0, 0]),
      K(st.at('lex7b'), [-3.4, 2.5, 9.2], [-3.8, 2.0, 0]),
      K(st.at('lex7b') + 1.4, [3.6, 2.5, 9.0], [4.0, 2.0, 0]),
      K(st.at('nia7') - 0.8, [3.4, 2.5, 9.4], [3.8, 2.0, 0]),
      K(st.at('nia7') + 0.6, [-0.6, 2.4, 10.5], [-0.6, 1.9, 2]),
      K(st.at('aud_in') - 0.2, [-0.6, 2.4, 10.5], [-0.6, 1.9, 2]),
      K(st.at('aud_in') + 0.9, [-2.6, 2.2, 10.4], [0.2, 1.9, 3.5]),
      K(st.dur, [-2.8, 2.2, 10.2], [0.2, 1.9, 3.5]),
    ]);
    // mediation overlay
    const ma = win(t, st.at('lex7c') - 0.2, st.at('aud_in') - 0.3, 0.4);
    if (ma > 0) {
      hud.rect('dim', 0, 0, 1920, 1080, '#0b1622', 0.35 * ma, -2);
      hud.draw('med', 940, 600, 960, 470, (g, w, h) => {
        g.fillStyle = '#fff'; rr(g, 0, 0, w, h, 32); g.fill();
        g.save(); rr(g, 0, 0, w, h, 32); g.clip(); g.fillStyle = PAL.amber; g.fillRect(0, 0, w, 90); g.restore();
        g.fillStyle = '#fff'; g.font = font(50, 700); g.textAlign = 'center'; g.fillText('MEDIATION', w / 2, 62);
        g.fillStyle = '#c39a6e'; g.beginPath(); g.ellipse(w / 2, 450, 300, 50, 0, 0, 7); g.fill();
        const fig = (x, y, s, c, sk) => { g.fillStyle = c; rr(g, x - 28 * s, y - 130 * s, 56 * s, 120 * s, 18 * s); g.fill(); g.fillStyle = sk; g.beginPath(); g.arc(x, y - 160 * s, 30 * s, 0, 7); g.fill(); g.fillStyle = '#1b1b1b'; g.beginPath(); g.arc(x - 10 * s, y - 164 * s, 4 * s, 0, 7); g.arc(x + 10 * s, y - 164 * s, 4 * s, 0, 7); g.fill(); };
        fig(w / 2 - 230, 470, 1, '#e07a5f', '#8d5a3b'); fig(w / 2 + 230, 470, 1, '#3d405b', '#e8b48f'); fig(w / 2, 420, 1.05, PAL.amber, '#5e3b25');
        for (const sg of [-1, 1]) { g.fillStyle = '#eef3f7'; g.strokeStyle = PAL.grey; g.lineWidth = 3; rr(g, w / 2 + sg * 140 - 60, 170, 120, 72, 20); g.fill(); g.stroke(); g.fillStyle = '#5b6670'; g.font = font(40, 700); g.fillText('…', w / 2 + sg * 140, 214); }
        g.fillStyle = PAL.ink; g.font = font(38, 600); g.fillText('helps the parties negotiate', w / 2, 530);
        g.fillStyle = PAL.mistake; g.font = font(34, 600); g.fillText('does not normally impose a decision', w / 2, 578);
      }, pop(t, st.at('lex7c') - 0.2, 0.5), ma);
    }
    if (qa > 0) {
      const ans = t >= st.at('aud2') - 0.15;
      hud.draw('quiz' + (ans ? 'A' : 'Q'), 1100, 480, 1250, 400, (g, w, h) => {
        g.fillStyle = '#fff'; rr(g, 0, 0, w, h, 32); g.fill();
        g.save(); rr(g, 0, 0, w, h, 32); g.clip(); g.fillStyle = PAL.ink; g.fillRect(0, 0, w, 90); g.restore();
        g.fillStyle = PAL.accent; g.font = font(46, 700); g.fillText('QUICK CHECK', 40, 62);
        g.fillStyle = PAL.ink; g.font = font(44, 600);
        wrapLines(g, "Which mechanism usually has a third party impose a binding decision under the parties' agreement?", w - 80).forEach((l, i) => g.fillText(l, 40, 150 + i * 56));
        ['Court', 'Arbitration', 'Mediation'].forEach((o, i) => {
          const x = 190 + i * 360, good = ans && o === 'Arbitration';
          g.font = font(42, 600); const tw = g.measureText(o).width + 60;
          g.fillStyle = good ? PAL.green : ans ? '#eef1f4' : '#dfe5ea'; rr(g, x - tw / 2, 330, tw, 70, 35); g.fill();
          g.fillStyle = good ? '#fff' : ans ? '#9aa5b0' : PAL.ink; g.textAlign = 'center'; g.fillText(o, x, 380); g.textAlign = 'left';
        });
      }, pop(t, st.at('aud_in'), 0.5), qa);
      const t0 = st.at('think'), t1 = st.end('think');
      if (t >= t0 - 0.2 && t <= t1 + 0.3) {
        const rem = clamp((t1 - t) / (t1 - t0)), n = Math.max(1, Math.ceil(rem * 4));
        hud.draw('ring' + n + '_' + Math.round(rem * 40), 220, 260, 1700, 860, (g) => {
          g.fillStyle = '#fff'; g.beginPath(); g.arc(110, 100, 80, 0, 7); g.fill();
          g.strokeStyle = PAL.accent; g.lineWidth = 16; g.lineCap = 'round'; g.beginPath(); g.arc(110, 100, 66, -Math.PI / 2, -Math.PI / 2 + Math.PI * 2 * rem); g.stroke();
          g.fillStyle = PAL.ink; g.font = font(70, 700); g.textAlign = 'center'; g.fillText(String(n), 110, 124);
          g.fillStyle = '#fff'; g.font = font(30, 700); g.strokeStyle = PAL.ink; g.lineWidth = 6; g.strokeText('PAUSE & THINK', 110, 230); g.fillText('PAUSE & THINK', 110, 230);
        });
      }
      if (ans) hud.chip('answer', 'Answer: ARBITRATION', 1250, 780, { bg: PAL.green, size: 56, s: pop(t, st.at('aud2') - 0.15, 0.5) });
    }
  },
};

// ============================================================== SCENE 8
const RECAP = [['nia8a', 'Civil vs criminal', PAL.teal, -2.3, 2.95, -0.06], ['nia8b', 'Legislature · Executive · Judiciary', PAL.purple, -0.85, 2.95, 0.05], ['nia8c', 'Ratio vs obiter', PAL.mistake, 0.6, 2.95, -0.03], ['nia8d', 'Damages vs equitable remedies', PAL.amber, -1.6, 1.8, 0.04], ['nia8e', 'Court vs ADR', PAL.green, -0.1, 1.8, -0.05]];

function recapCard(lab, c) {
  const t = canvasTex('recap' + lab, 250, 160, (g, w, h) => {
    g.fillStyle = '#fffdf5'; g.fillRect(0, 0, w, h); g.fillStyle = c; g.fillRect(0, 0, w, 28);
    g.fillStyle = PAL.ink; g.font = font(30, 600); g.textAlign = 'center';
    const ls = wrapLines(g, lab, 220); ls.forEach((l, i) => g.fillText(l, w / 2, 60 + i * 36 + (3 - ls.length) * 16));
  });
  const g = new THREE.Group();
  const p = texPlane(t, 1.25 / 250, { lit: true }); g.add(p);
  const back = box(1.25, 0.8, 0.02, '#fffdf5'); back.position.z = -0.012; g.add(back);
  const pn = P.pin(c); pn.position.set(0, 0.33, 0); g.add(pn);
  return g;
}

const s8 = {
  setup(S) {
    bg(S.scene, '#fbf3e4', '#f1e2c8');
    P.lights(S.scene, { sunPos: [-3, 8, 7] });
    const off = P.office(S.scene, { harbour: true, sign: false, windowX: 2.9, windowW: 2.6 });
    const cb = P.corkboard(); cb.position.set(-0.85, 2.4, -2.45); S.scene.add(cb);
    // passing ship clipped to the window
    const wx = 2.9, ww = 2.6, wh = ww * 0.62, wy = 2.6;
    const planes = [new THREE.Plane(new THREE.Vector3(1, 0, 0), -(wx - ww / 2)), new THREE.Plane(new THREE.Vector3(-1, 0, 0), wx + ww / 2), new THREE.Plane(new THREE.Vector3(0, 1, 0), -(wy - wh / 2)), new THREE.Plane(new THREE.Vector3(0, -1, 0), wy + wh / 2)];
    const sh = P.ship();
    sh.traverse((o) => { if (o.material) { o.material = o.material.clone(); o.material.clippingPlanes = planes; o.castShadow = false; } });
    sh.scale.setScalar(0.13); S.scene.add(sh); S.cache.set('wship', sh);
    // end-card set (far away, revealed by a cut)
    const end = new THREE.Group(); end.position.set(0, 0, -200);
    const seaM = P.sea(80, '#2b86c5'); end.add(seaM);
    const big = P.ship(); big.scale.setScalar(0.9); end.add(big);
    S.scene.add(end); S.cache.set('end', end); end.userData.sea = seaM; end.userData.ship = big;
    S.officeBg = S.scene.background;
    bg(S.scene, '#6fc0f5', '#d9f1ff'); S.endBg = S.scene.background; S.scene.background = S.officeBg;
  },
  draw(S, t, st, cam, hud) {
    const te = st.at('n3') - 0.4;
    const ending = t >= te + 0.35;
    const sh = S.get('wship');
    const ts = st.at('ship') - 0.6;
    const k = prog(t, ts, 7.0);
    sh.position.set(lerp(2.9 - 2.1, 2.9 + 2.1, k), 2.38 + Math.sin(t * 2) * 0.01, -2.47);
    sh.visible = t >= ts && !ending;
    const cg = sh.userData.cargo; poseCargo(cg, { mouth: st.mouth('CARGO', t), t, look: 0.4 });
    for (const [key, lab, c, x, y, rot] of RECAP) {
      const tp = st.at(key) - 0.25;
      const card = S.get('rc' + key, () => recapCard(lab, c));
      const kk = easeOutBack(prog(t, tp, 0.45), 1.6);
      card.visible = t >= tp;
      card.position.set(-0.85 + x + 0.85, lerp(y + 1.5, y, kk), lerp(-0.5, -2.36, kk));
      card.rotation.set(0, lerp(0.8, 0, kk), rot * kk);
    }
    const npose = poseTrack(t, [[0, 'idle'], [st.at('nia8a') - 0.3, 'point_up'], [st.end('nia8e'), 'idle'], [st.at('cargo8'), 'wave']]);
    person(S, st, t, 'NIA', -3.8, -0.6, { pose: npose, mood: 'happy', ry: t < st.at('ship') ? 0.35 : 0.6 });
    const lpose = poseTrack(t, [[0, 'idle'], [st.at('lex8'), 'present'], [st.at('ship'), 'point']]);
    person(S, st, t, 'LEX', 1.9, 1.2, { pose: lpose, mood: 'happy', ry: t < st.at('lex8') ? -0.5 : 0.3 });
    const end = S.get('end');
    end.visible = ending;
    S.scene.background = ending ? S.endBg : S.officeBg;
    if (ending) {
      P.animateSea(end.userData.sea, t, 0.15);
      const bs = end.userData.ship;
      bs.position.set(lerp(-3, 2, prog(t, te, 12)), 0.15 + Math.sin(t * 2) * 0.08, 0); bs.rotation.set(Math.sin(t * 1.4) * 0.03, -0.35, Math.sin(t * 1.7) * 0.02);
      poseCargo(bs.userData.cargo, { t, mood: 'happy' });
      camTrack(cam, t, [K(te, [0, 3.0, 12 - 200], [0, 2.4, -200], 40), K(st.dur, [1.5, 2.6, 10.5 - 200], [0.5, 2.2, -200], 40)]);
      hud.text('nt', 'NEXT TIME', 960, 140, 44, '#ffffff', { outline: PAL.ink, ow: 10 });
      hud.chip('ep2', 'EPISODE 2', 960, 225, { bg: PAL.teal, size: 38 });
      hud.text('ep2t', 'The Contract Across the Ocean', 960, 340, 96, PAL.accent, { outline: '#0b1622', ow: 14 }, pop(t, te + 0.4, 0.5));
      hud.text('disc', 'Learning aid · fictional characters and hypothetical facts · verify against current ACCA documents', 960, 1040, 28, '#ffffff', { weight: 500, outline: '#0b1622', ow: 8 });
    } else {
      camTrack(cam, t, [
        K(0, [-1.4, 2.4, 8.5], [-0.9, 1.8, -1]),
        K(st.at('nia8a'), [-1.2, 2.5, 6.8], [-0.9, 2.2, -2]),
        K(st.end('nia8e'), [-1.0, 2.5, 6.6], [-0.7, 2.2, -2]),
        K(st.at('ship') - 0.6, [1.0, 2.2, 7.4], [1.6, 1.9, -1.5]),
        K(st.at('cargo8'), [3.6, 2.35, 3.4], [2.9, 2.45, -2.5]),
        K(te, [3.6, 2.35, 3.2], [2.9, 2.45, -2.5]),
      ]);
    }
    // dip to navy for the cut
    const dip = win(t, te, te + 0.35, 0.35);
    if (dip > 0) hud.rect('dip', 0, 0, 1920, 1080, '#13233a', dip, 3);
  },
};

export const SCENES = { title, s1, s2, s3, s4, s5, s6, s7, s8 };
export { Stage };
