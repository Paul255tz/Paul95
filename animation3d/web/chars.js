// 3D cast built from primitives, with a simple rig: shoulders/elbows, head,
// eyes (blink + look), brows (mood) and a lip-synced mouth.
import * as THREE from 'three';
import { box, capsule, cyl, group, mat, mesh, rad, sphere, lerp, at } from './core.js';

export const LOOKS = {
  NIA: { skin: '#8d5a3b', hair: '#1c1410', style: 'puff', top: '#0f8b8d', bottom: '#2d3142', collar: 'blazer', shirt: '#fff3d6', earrings: true, seed: 0.3, width: 0.92 },
  KITO: { skin: '#5e3b25', hair: '#120c08', style: 'short', top: '#f28c28', bottom: '#3d405b', collar: 'shirt', shirt: '#f28c28', seed: 1.7, width: 1.05 },
  LEX: { skin: '#c98b62', hair: '#e2e2e2', style: 'prof', top: '#1f3a5f', bottom: '#1f3a5f', collar: 'bow', shirt: '#ffffff', tie: '#ffb627', glasses: 'round', beard: true, seed: 2.9, width: 1.08 },
  AUDITOR: { skin: '#e8b48f', hair: '#5a4632', style: 'neat', top: '#6c7a89', bottom: '#4a5562', collar: 'tie', shirt: '#ffffff', tie: '#0f8b8d', glasses: 'square', seed: 4.1, width: 0.98 },
};

export const POSES = {
  idle: { L: [8, -8], R: [8, -8] },
  point: { L: [8, -8], R: [95, 10] },
  point_up: { L: [8, -8], R: [140, 8] },
  point_l: { L: [95, 10], R: [8, -8] },
  present: { L: [50, -30], R: [90, 20] },
  wave: { L: [8, -8], R: [150, 25] },
  hips: { L: [40, -100], R: [40, -100] },
  think: { L: [25, -95], R: [-25, -150] },
  hold_r: { L: [8, -8], R: [12, -80] },
  wave_paper: { L: [8, -8], R: [160, 10] },
  shrug: { L: [55, -120], R: [55, -120] },
  cheer: { L: [150, 15], R: [150, 15] },
  demand: { L: [40, -100], R: [110, 30] },
  clipboard: { L: [15, -95], R: [8, -8] },
};

export function poseTrack(t, keys, dur = 0.35) {
  let cur = keys[0][1], prev = cur, start = -1e9;
  for (const [kt, name] of keys) if (t >= kt) { prev = cur; cur = name; start = kt; }
  let k = Math.min(1, Math.max(0, (t - start) / dur));
  k = k * k * (3 - 2 * k);
  const a = POSES[prev], b = POSES[cur];
  return { L: [lerp(a.L[0], b.L[0], k), lerp(a.L[1], b.L[1], k)], R: [lerp(a.R[0], b.R[0], k), lerp(a.R[1], b.R[1], k)] };
}

export function blink(t, seed) {
  const ph = (t + seed * 1.37) % 4.1;
  return ph < 0.13 ? 0.08 + (Math.abs(ph - 0.065) / 0.065) * 0.92 : 1;
}

// ------------------------------------------------------------- face
function makeFace(L, scale = 1) {
  const f = new THREE.Group();
  const eyes = [], pupils = [], brows = [];
  for (const sg of [-1, 1]) {
    const eye = sphere(0.062, '#ffffff', { rough: 0.25 });
    eye.scale.set(1, 1.15, 0.55);
    eye.position.set(sg * 0.1, 0.03, 0.235);
    f.add(eye); eyes.push(eye);
    const pupil = sphere(0.034, '#161616', { rough: 0.2 });
    pupil.position.set(sg * 0.1, 0.025, 0.268);
    pupil.scale.set(1, 1.1, 0.5);
    const glint = sphere(0.011, '#ffffff', { emissive: '#ffffff' });
    glint.position.set(0.012, 0.014, 0.018);
    pupil.add(glint);
    f.add(pupil); pupils.push(pupil);
    const brow = capsule(0.014, 0.075, '#2a1a14');
    brow.rotation.z = Math.PI / 2;
    brow.position.set(sg * 0.1, 0.13, 0.24);
    f.add(brow); brows.push(brow);
  }
  const nose = sphere(0.035, L.skin);
  nose.position.set(0, -0.04, 0.27); nose.scale.set(1, 0.9, 0.8);
  f.add(nose);
  // mouth: open (dark ellipsoid + tongue) or closed (curved tube)
  const mouthOpen = new THREE.Group();
  const cav = sphere(0.07, '#5a1d1d', { rough: 0.9 }); cav.scale.set(1, 1, 0.35);
  const tongue = sphere(0.04, '#e06b6b'); tongue.position.set(0, -0.025, 0.01); tongue.scale.set(1.1, 0.6, 0.4);
  const teeth = box(0.09, 0.018, 0.02, '#ffffff'); teeth.position.set(0, 0.045, 0.012);
  mouthOpen.add(cav, tongue, teeth);
  mouthOpen.position.set(0, -0.135, 0.235);
  f.add(mouthOpen);
  const smile = mesh(new THREE.TorusGeometry(0.06, 0.012, 8, 20, Math.PI * 0.8), mat('#3a1f17'));
  smile.rotation.z = Math.PI + Math.PI * 0.1;
  smile.position.set(0, -0.11, 0.245);
  f.add(smile);
  return { f, eyes, pupils, brows, mouthOpen, smile };
}

function makeHead(L) {
  const h = new THREE.Group();
  const skull = sphere(0.27, L.skin, { rough: 0.6 }, 32);
  skull.scale.set(1, 1.08, 0.96);
  h.add(skull);
  for (const sg of [-1, 1]) {
    const ear = sphere(0.055, L.skin); ear.scale.set(0.6, 1, 0.8); ear.position.set(sg * 0.265, 0.0, 0);
    h.add(ear);
    if (L.earrings) { const e = sphere(0.025, '#ffb627', { metal: 0.6, rough: 0.3 }); e.position.set(sg * 0.27, -0.08, 0.02); h.add(e); }
    const cheek = sphere(0.04, '#e8746a', { opacity: 0.35 }); cheek.scale.set(1.2, 0.7, 0.3); cheek.position.set(sg * 0.15, -0.07, 0.235); h.add(cheek);
  }
  const hair = mat(L.hair, { rough: 0.85 });
  if (L.style === 'puff') {
    const back = mesh(new THREE.SphereGeometry(0.34, 28, 20), hair); back.position.set(0, 0.06, -0.08); back.scale.set(1.15, 1.0, 0.95);
    const bun = mesh(new THREE.SphereGeometry(0.2, 24, 16), hair); bun.position.set(0, 0.36, -0.06);
    const cap = mesh(new THREE.SphereGeometry(0.285, 28, 16, 0, Math.PI * 2, 0, Math.PI * 0.42), hair); cap.position.set(0, 0.03, 0.01); cap.rotation.x = -0.25;
    h.add(back, bun, cap);
  } else if (L.style === 'short') {
    const cap = mesh(new THREE.SphereGeometry(0.29, 28, 16, 0, Math.PI * 2, 0, Math.PI * 0.4), hair); cap.position.set(0, 0.02, -0.01); cap.rotation.x = -0.18; cap.scale.set(1, 1.15, 1);
    h.add(cap);
  } else if (L.style === 'neat') {
    const cap = mesh(new THREE.SphereGeometry(0.29, 28, 16, 0, Math.PI * 2, 0, Math.PI * 0.45), hair); cap.position.set(0, 0.03, -0.01); cap.rotation.set(-0.22, 0, 0.1);
    const swoop = mesh(new THREE.SphereGeometry(0.12, 16, 12), hair); swoop.position.set(0.08, 0.22, 0.15); swoop.scale.set(1.5, 0.5, 0.8);
    h.add(cap, swoop);
  } else if (L.style === 'prof') {
    for (const sg of [-1, 1]) { const tuft = mesh(new THREE.SphereGeometry(0.1, 16, 12), hair); tuft.position.set(sg * 0.25, 0.08, -0.02); tuft.scale.set(0.8, 1.2, 1.1); h.add(tuft); }
    const back = mesh(new THREE.SphereGeometry(0.2, 20, 12), hair); back.position.set(0, 0.0, -0.17); back.scale.set(1.2, 1, 0.6); h.add(back);
  }
  if (L.beard) {
    const b = mesh(new THREE.SphereGeometry(0.27, 28, 16, 0, Math.PI * 2, Math.PI * 0.5, Math.PI * 0.5), hair);
    b.position.set(0, -0.02, 0.03); b.scale.set(1.0, 1.25, 0.98); h.add(b);
    for (const sg of [-1, 1]) { const m = sphere(0.055, L.hair); m.scale.set(1.3, 0.55, 0.6); m.position.set(sg * 0.055, -0.09, 0.255); h.add(m); }
  }
  const face = makeFace(L);
  h.add(face.f);
  if (L.glasses) {
    const gm = mat('#2a2a2a', { rough: 0.3, metal: 0.4 });
    for (const sg of [-1, 1]) {
      const ring = L.glasses === 'round'
        ? mesh(new THREE.TorusGeometry(0.075, 0.012, 8, 28), gm)
        : mesh(new THREE.TorusGeometry(0.08, 0.012, 4, 4), gm);
      if (L.glasses !== 'round') { ring.rotation.z = Math.PI / 4; ring.scale.set(1.15, 0.85, 1); }
      ring.position.set(sg * 0.1, 0.03, 0.27); h.add(ring);
    }
    const bridge = box(0.06, 0.012, 0.012, '#2a2a2a'); bridge.position.set(0, 0.04, 0.28); h.add(bridge);
  }
  return { h, face };
}

function arm(L, sg) {
  const shoulder = new THREE.Group();
  const top = mat(L.top, { rough: 0.7 });
  const upper = mesh(new THREE.CapsuleGeometry(0.075, 0.24, 6, 12), top); upper.position.y = -0.16;
  const elbow = new THREE.Group(); elbow.position.y = -0.33;
  const fore = mesh(new THREE.CapsuleGeometry(0.068, 0.22, 6, 12), top); fore.position.y = -0.14;
  const hand = sphere(0.068, L.skin); hand.position.y = -0.31;
  elbow.add(fore, hand);
  shoulder.add(upper, elbow);
  return { shoulder, elbow, hand };
}

export function makePerson(name) {
  const L = LOOKS[name];
  const root = new THREE.Group();
  const body = new THREE.Group();
  root.add(body);
  const w = L.width;
  const bottom = mat(L.bottom, { rough: 0.75 });
  for (const sg of [-1, 1]) {
    const leg = mesh(new THREE.CapsuleGeometry(0.09, 0.55, 6, 12), bottom); leg.position.set(sg * 0.12 * w, 0.4, 0);
    const shoe = sphere(0.1, '#2b2b2b', { rough: 0.4 }); shoe.scale.set(0.95, 0.55, 1.5); shoe.position.set(sg * 0.13 * w, 0.05, 0.05);
    body.add(leg, shoe);
  }
  const torso = mesh(new THREE.CylinderGeometry(0.27 * w, 0.23 * w, 0.62, 28), mat(L.top, { rough: 0.7 }));
  torso.scale.z = 0.68; torso.position.y = 1.0;
  const shoulders = mesh(new THREE.SphereGeometry(0.27 * w, 28, 12, 0, Math.PI * 2, 0, Math.PI / 2), mat(L.top, { rough: 0.7 }));
  shoulders.scale.set(1, 0.4, 0.68); shoulders.position.y = 1.31;
  const hip = mesh(new THREE.SphereGeometry(0.23 * w, 24, 12, 0, Math.PI * 2, Math.PI / 2, Math.PI / 2), bottom);
  hip.scale.set(1, 0.5, 0.68); hip.position.y = 0.69;
  body.add(torso, shoulders, hip);
  // collar details on the chest
  const front = 0.27 * w * 0.68 * 0.93;
  if (L.collar === 'shirt') {
    for (const sg of [-1, 1]) { const c = box(0.12, 0.05, 0.03, L.shirt === L.top ? '#ffd2a1' : L.shirt); c.position.set(sg * 0.06, 1.3, front - 0.01); c.rotation.set(0.3, 0, sg * 0.5); body.add(c); }
    for (let i = 0; i < 4; i++) { const b = sphere(0.014, '#7a4a1a'); b.position.set(0, 1.22 - i * 0.12, front - 0.005 + i * 0.008); body.add(b); }
  } else {
    const v = mesh(new THREE.ConeGeometry(0.1, 0.28, 3), mat(L.shirt)); v.rotation.set(Math.PI, 0, 0); v.scale.z = 0.25; v.position.set(0, 1.2, front - 0.02); body.add(v);
    for (const sg of [-1, 1]) { const lap = box(0.07, 0.3, 0.025, '#000', {}); lap.material = mat(L.top, { rough: 0.5 }); lap.material = mat(new THREE.Color(L.top).multiplyScalar(0.8).getStyle()); lap.position.set(sg * 0.085, 1.18, front + 0.005); lap.rotation.z = sg * 0.35; body.add(lap); }
    if (L.collar === 'bow') {
      for (const sg of [-1, 1]) { const c = mesh(new THREE.ConeGeometry(0.045, 0.09, 12), mat(L.tie)); c.rotation.z = sg * Math.PI / 2; c.position.set(-sg * 0.045, 1.32, front + 0.02); body.add(c); }
      const k = sphere(0.022, L.tie); k.position.set(0, 1.32, front + 0.03); body.add(k);
    }
    if (L.collar === 'tie') { const t = box(0.05, 0.24, 0.02, L.tie); t.position.set(0, 1.18, front + 0.01); body.add(t); }
    for (let i = 0; i < 2; i++) { const b = sphere(0.016, '#222'); b.position.set(0.02, 0.98 - i * 0.12, front + 0.005); body.add(b); }
  }
  const neck = cyl(0.06, 0.07, 0.16, L.skin); neck.position.y = 1.4; body.add(neck);
  const headPivot = new THREE.Group(); headPivot.position.y = 1.46;
  const { h, face } = makeHead(L); h.position.y = 0.27;
  headPivot.add(h); body.add(headPivot);
  const arms = {};
  for (const [side, sg] of [['L', -1], ['R', 1]]) {
    const a = arm(L, sg);
    a.shoulder.position.set(sg * 0.29 * w, 1.29, 0);
    body.add(a.shoulder); arms[side] = a;
  }
  root.userData.rig = { L, body, headPivot, face, arms, name };
  return root;
}

export function posePerson(root, { pose = 'idle', mouth = 0, mood = 'neutral', look = 0, t = 0, talking = false, bob = 0, turn = 0 } = {}) {
  const r = root.userData.rig;
  const pz = typeof pose === 'string' ? POSES[pose] : pose;
  r.body.position.y = bob;
  r.body.rotation.y = turn;
  const breathe = Math.sin(t * 2.1 + r.L.seed) * 0.008;
  r.body.scale.set(1, 1 + breathe, 1);
  for (const [side, sg] of [['L', -1], ['R', 1]]) {
    const [a1, a2] = pz[side];
    const a = r.arms[side];
    a.shoulder.rotation.set(a2 < -60 ? -0.45 : -0.08, 0, sg * rad(a1));
    a.elbow.rotation.set(a2 < -60 ? -0.5 : -0.05, 0, sg * rad(a2));
  }
  // head
  r.headPivot.rotation.y = look * 0.45;
  r.headPivot.rotation.x = talking ? Math.sin(t * 9 + r.L.seed) * 0.035 * mouth - 0.02 : Math.sin(t * 1.3) * 0.015;
  r.headPivot.rotation.z = Math.sin(t * 0.9 + r.L.seed) * 0.03;
  setFace(r.face, { mouth, mood, look, t, seed: r.L.seed });
}

export function setFace(face, { mouth = 0, mood = 'neutral', look = 0, t = 0, seed = 0 }) {
  const bl = blink(t, seed);
  face.eyes.forEach((e) => (e.scale.y = 1.15 * bl));
  face.pupils.forEach((p, i) => {
    p.visible = bl > 0.35;
    p.position.x = (i ? 1 : -1) * 0.1 + look * 0.02;
  });
  const [inner, outer] = { angry: [-0.03, 0.01], worried: [0.025, -0.005], surprised: [0.035, 0.035], excited: [0.03, 0.03], thinking: [0.02, 0.02] }[mood] || [0, 0];
  face.brows.forEach((b, i) => {
    const sg = i ? 1 : -1;
    b.position.y = 0.13 + (inner + outer) / 2;
    b.rotation.z = Math.PI / 2 + sg * (outer - inner) * 6 * -1;
  });
  if (mouth < 0.06) {
    face.mouthOpen.visible = false; face.smile.visible = true;
    const happy = ['happy', 'smile', 'excited'].includes(mood);
    const sad = ['worried', 'angry'].includes(mood);
    face.smile.rotation.z = sad ? Math.PI * 0.1 : Math.PI + Math.PI * 0.1;
    face.smile.position.y = sad ? -0.16 : -0.11;
    face.smile.scale.set(happy ? 1 : 0.75, happy ? 1 : 0.45, 1);
  } else {
    face.mouthOpen.visible = true; face.smile.visible = false;
    face.mouthOpen.scale.set(0.7 + 0.35 * mouth, 0.25 + 1.0 * mouth, 1);
  }
}

// ------------------------------------------------------------- Captain Cargo
export function makeCargo() {
  const root = new THREE.Group();
  const body = new THREE.Group(); root.add(body);
  const orange = '#d9480f';
  const crate = box(1.5, 0.95, 0.95, orange, { rough: 0.5, metal: 0.15 }); crate.position.y = 0.55; body.add(crate);
  const ridge = mat('#b83c0c', { rough: 0.5, metal: 0.15 });
  for (let i = -6; i <= 6; i++) {
    for (const z of [0.48, -0.48]) { const r = mesh(new THREE.BoxGeometry(0.04, 0.85, 0.03), ridge); r.position.set(i * 0.11, 0.55, z); if (Math.abs(i) > 3 || z < 0) body.add(r); }
  }
  for (const y of [0.09, 1.01]) { const b = box(1.54, 0.05, 0.99, '#a83a0c'); b.position.y = y; body.add(b); }
  const plate = box(0.82, 0.68, 0.04, '#e5622a'); plate.position.set(0, 0.55, 0.48); body.add(plate);
  const faceG = makeFace({ skin: '#e5622a' });
  faceG.f.scale.setScalar(1.7); faceG.f.position.set(0, 0.6, 0.1);
  faceG.f.children.forEach((c) => { if (c.geometry && c.geometry.type === 'SphereGeometry' && c.material.color.getHexString() === 'e5622a') c.visible = false; });
  body.add(faceG.f);
  // arms
  const arms = [];
  for (const sg of [-1, 1]) {
    const p = new THREE.Group(); p.position.set(sg * 0.76, 0.6, 0);
    const a = capsule(0.04, 0.3, '#a83a0c'); a.position.y = 0.18; a.rotation.z = -sg * 0.3;
    const g = sphere(0.08, '#ffffff'); g.position.set(sg * 0.07, 0.38, 0);
    p.add(a, g); body.add(p); arms.push(p);
  }
  // captain hat
  const hat = new THREE.Group(); hat.position.set(0.08, 1.04, 0); hat.rotation.z = -0.1;
  const brim = cyl(0.42, 0.42, 0.04, '#1f3a5f'); brim.position.set(0, 0.02, 0.05); brim.scale.z = 0.9;
  const crown = mesh(new THREE.SphereGeometry(0.34, 24, 12, 0, Math.PI * 2, 0, Math.PI / 2), mat('#ffffff', { rough: 0.4 })); crown.scale.set(1.05, 0.75, 0.95); crown.position.y = 0.06;
  const band = cyl(0.36, 0.36, 0.09, '#1f3a5f'); band.position.y = 0.09;
  const badge = sphere(0.06, '#ffb627', { metal: 0.6, rough: 0.3 }); badge.position.set(0, 0.17, 0.32); badge.scale.z = 0.4;
  hat.add(brim, crown, band, badge); body.add(hat);
  root.userData.rig = { body, face: faceG, arms };
  return root;
}

export function poseCargo(root, { mouth = 0, mood = 'happy', look = 0, t = 0, bobAmp = 0.04 } = {}) {
  const r = root.userData.rig;
  r.body.position.y = 0.06 + Math.sin(t * 2.4) * bobAmp;
  r.body.rotation.y = look * 0.35;
  r.body.rotation.z = Math.sin(t * 1.7) * 0.02;
  r.arms.forEach((a, i) => (a.rotation.z = Math.sin(t * 3 + i) * 0.25 + (i ? -0.2 : 0.2)));
  setFace(r.face, { mouth, mood, look, t, seed: 6 });
}

// ------------------------------------------------------------- mini figures
export function makeMini(body = '#7768ae', skin = '#a86f4c', { wig = false, scale = 1 } = {}) {
  const g = new THREE.Group();
  const legs = capsule(0.1, 0.3, new THREE.Color(body).multiplyScalar(0.7).getStyle()); legs.position.y = 0.25;
  const torso = capsule(0.15, 0.25, body); torso.position.y = 0.62;
  const head = sphere(0.15, skin); head.position.y = 1.0;
  g.add(legs, torso, head);
  for (const sg of [-1, 1]) { const e = sphere(0.022, '#161616'); e.position.set(sg * 0.05, 1.02, 0.135); g.add(e); }
  if (wig) {
    for (let i = -2; i <= 2; i++) { const c = sphere(0.06, '#f4f4f4'); c.position.set(i * 0.06, 1.14, -0.02); g.add(c); }
    for (const sg of [-1, 1]) for (let j = 0; j < 3; j++) { const c = sphere(0.05, '#f4f4f4'); c.position.set(sg * 0.15, 1.06 - j * 0.07, -0.02); g.add(c); }
  }
  g.scale.setScalar(scale);
  return g;
}
