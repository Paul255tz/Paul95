// 3D props, sets and environments.
import * as THREE from 'three';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';
import {
  PAL, at, box, canvasTex, capsule, cyl, font, group, mat, mesh, paperTex, rbox, rr, sphere, texPlane,
} from './core.js';
import { makeCargo, makeMini } from './chars.js';

// ------------------------------------------------------------- lighting
export function lights(scene, { sky = '#dff1ff', ground = '#d9c3a0', sun = 2.2, hemi = 0.9, sunPos = [4, 9, 6], env = 0.45, span = 9 } = {}) {
  const h = new THREE.HemisphereLight(sky, ground, hemi);
  const d = new THREE.DirectionalLight('#fff4e0', sun);
  d.position.set(...sunPos);
  d.castShadow = true;
  d.shadow.mapSize.set(2048, 2048);
  Object.assign(d.shadow.camera, { left: -span, right: span, top: span, bottom: -span, near: 0.5, far: 40 });
  d.shadow.bias = -0.0004;
  d.shadow.normalBias = 0.02;
  d.shadow.radius = 4;
  const fillL = new THREE.DirectionalLight('#cfe3ff', 0.6);
  fillL.position.set(-6, 4, 5);
  scene.add(h, d, fillL);
  scene.userData.envIntensity = env;
  return d;
}

let envTex = null;
export function useEnvironment(renderer, scene, intensity = 0.45) {
  if (!envTex) {
    const pm = new THREE.PMREMGenerator(renderer);
    envTex = pm.fromScene(new RoomEnvironment(), 0.04).texture;
  }
  scene.environment = envTex;
  scene.environmentIntensity = intensity;
}

export function floor(color = '#c9a27a', size = 60, y = 0) {
  const f = mesh(new THREE.PlaneGeometry(size, size), mat(color, { rough: 0.9 }), { cast: false, receive: true });
  f.rotation.x = -Math.PI / 2; f.position.y = y;
  return f;
}

export function wall(color, w = 30, h = 12, z = -3) {
  const m = mesh(new THREE.PlaneGeometry(w, h), mat(color, { rough: 0.95 }), { cast: false, receive: true });
  m.position.set(0, h / 2, z);
  return m;
}

// ------------------------------------------------------------- canvas art
export function skylineTex(harbour = false) {
  return canvasTex('skyline' + harbour, 1024, 640, (g, w, h) => {
    const sky = g.createLinearGradient(0, 0, 0, h); sky.addColorStop(0, '#8fd3ff'); sky.addColorStop(1, '#e3f6ff');
    g.fillStyle = sky; g.fillRect(0, 0, w, h);
    g.fillStyle = '#ffd166'; g.beginPath(); g.arc(w * 0.8, h * 0.2, 60, 0, 7); g.fill();
    const base = h * (harbour ? 0.62 : 0.8);
    let x = -10, seed = 3;
    const rnd = () => ((seed = (seed * 16807) % 2147483647) / 2147483647);
    while (x < w) {
      const bw = 70 + rnd() * 90, bh = 110 + rnd() * 240;
      g.fillStyle = ['#7aa6c2', '#5f8aa8', '#94b8cf', '#6f97b3'][Math.floor(rnd() * 4)];
      g.fillRect(x, base - bh, bw, bh + 2);
      g.fillStyle = 'rgba(223,243,255,0.7)';
      for (let wy = base - bh + 16; wy < base - 14; wy += 34) for (let wx = x + 12; wx < x + bw - 18; wx += 28) g.fillRect(wx, wy, 13, 16);
      x += bw + 8;
    }
    if (harbour) {
      const sea = g.createLinearGradient(0, base, 0, h); sea.addColorStop(0, '#2b86c5'); sea.addColorStop(1, '#1b5f93');
      g.fillStyle = sea; g.fillRect(0, base, w, h - base);
    } else { g.fillStyle = '#9bbf7a'; g.fillRect(0, base, w, h - base); }
  });
}

export function globeTex() {
  return canvasTex('globe', 1024, 512, (g, w, h) => {
    const oc = g.createLinearGradient(0, 0, 0, h); oc.addColorStop(0, '#3d9be0'); oc.addColorStop(0.5, '#2a7fc9'); oc.addColorStop(1, '#1b5f93');
    g.fillStyle = oc; g.fillRect(0, 0, w, h);
    const blob = (x, y, rx, ry, c) => { g.fillStyle = c; g.beginPath(); g.ellipse(x * w, y * h, rx * w, ry * h, 0, 0, 7); g.fill(); };
    const lands = [[0.2, 0.3, 0.09, 0.13], [0.26, 0.62, 0.05, 0.16], [0.5, 0.3, 0.06, 0.09], [0.53, 0.58, 0.06, 0.17], [0.7, 0.3, 0.13, 0.12], [0.82, 0.7, 0.05, 0.06], [0.1, 0.45, 0.04, 0.05]];
    for (const [x, y, rx, ry] of lands) { blob(x, y, rx, ry, '#5cc27a'); blob(x + rx * 0.2, y - ry * 0.2, rx * 0.55, ry * 0.5, '#78d48f'); }
    g.fillStyle = '#f2f7fb'; g.fillRect(0, 0, w, 22); g.fillRect(0, h - 22, w, 22);
  });
}

// ------------------------------------------------------------- office set
export function office(scene, { harbour = false, sign = true, windowX = 2.6, windowW = 3.0 } = {}) {
  const g = new THREE.Group();
  g.add(floor('#c9a27a'));
  const back = wall('#f4ead9', 30, 12, -2.6); g.add(back);
  // wainscot + stripes
  const skirt = box(30, 0.9, 0.06, '#e6d3b3'); skirt.position.set(0, 0.45, -2.55); g.add(skirt);
  for (let i = -14; i <= 14; i += 1.2) { const s = box(0.5, 11, 0.01, '#fbf4e8'); s.position.set(i, 6.5, -2.59); s.castShadow = false; g.add(s); }
  // window
  const wh = windowW * 0.62;
  const win = new THREE.Group(); win.position.set(windowX, 2.6, -2.55);
  const frame = box(windowW + 0.2, wh + 0.2, 0.12, '#ffffff'); win.add(frame);
  const view = mesh(new THREE.PlaneGeometry(windowW, wh), new THREE.MeshBasicMaterial({ map: skylineTex(harbour).tex, toneMapped: false }), { cast: false });
  view.position.z = 0.065; win.add(view);
  for (const [w, h, x, y] of [[0.07, wh, 0, 0], [windowW, 0.07, 0, 0]]) { const b = box(w, h, 0.05, '#ffffff'); b.position.set(x, y, 0.09); win.add(b); }
  const sill = box(windowW + 0.5, 0.08, 0.3, '#e9dcc4'); sill.position.set(0, -wh / 2 - 0.12, 0.1); win.add(sill);
  g.add(win);
  if (sign) {
    const t = canvasTex('logo', 440, 130, (c, w, h) => {
      c.fillStyle = PAL.teal; rr(c, 0, 0, w, h, 26); c.fill();
      c.fillStyle = PAL.accent; c.beginPath(); c.arc(68, 65, 38, 0, 7); c.fill();
      c.fillStyle = PAL.teal; c.beginPath(); c.moveTo(38, 78); c.lineTo(68, 36); c.lineTo(98, 78); c.fill();
      c.fillStyle = '#fff'; c.font = font(54, 650); c.fillText('SafariTech', 125, 70);
      c.fillStyle = '#d8fbf8'; c.font = font(26, 600); c.fillText('TRADING LTD', 128, 108);
    });
    const p = texPlane(t, 0.0055, { lit: true }); p.position.set(-2.4, 3.1, -2.55); g.add(p);
  }
  g.add(at(plant(), -3.9, 0, -1.6, 0, 0, 0, 1.1));
  scene.add(g);
  return { group: g, win, view };
}

export function plant() {
  const g = new THREE.Group();
  const pot = cyl(0.26, 0.2, 0.42, '#e07a5f'); pot.position.y = 0.21; g.add(pot);
  const leafM = mat('#2e9a60', { rough: 0.6 }), leafM2 = mat('#3bb273', { rough: 0.6 });
  for (let i = 0; i < 9; i++) {
    const l = mesh(new THREE.SphereGeometry(0.12, 12, 10), i % 2 ? leafM : leafM2);
    l.scale.set(0.6, 2.4, 0.3);
    const a = (i / 9) * Math.PI * 2;
    l.position.set(Math.cos(a) * 0.12, 0.7, Math.sin(a) * 0.12);
    l.rotation.set(Math.sin(a) * 0.5, 0, -Math.cos(a) * 0.5);
    g.add(l);
  }
  return g;
}

export function desk() {
  const g = new THREE.Group();
  const top = rbox(2.8, 0.12, 1.1, 0.04, '#8c5a3c', { rough: 0.5 }); top.position.y = 0.95; top.receiveShadow = true;
  const body = box(2.6, 0.85, 0.95, '#a26d4a', { rough: 0.6 }); body.position.y = 0.46; body.receiveShadow = true;
  g.add(top, body);
  for (const y of [0.7, 0.32]) { const d = box(1.0, 0.3, 0.02, '#8c5a3c'); d.position.set(-0.7, y, 0.48); const k = sphere(0.03, '#e9c46a', { metal: 0.6 }); k.position.set(-0.7, y, 0.5); g.add(d, k); }
  // laptop
  const lap = new THREE.Group(); lap.position.set(0.75, 1.01, 0.05);
  const base = box(0.8, 0.03, 0.55, '#2d3142', { metal: 0.4, rough: 0.35 });
  const lid = new THREE.Group(); lid.position.set(0, 0, -0.27); lid.rotation.x = -0.25;
  const scr = box(0.8, 0.52, 0.03, '#3d405b', { metal: 0.4, rough: 0.35 }); scr.position.y = 0.26;
  const glow = mesh(new THREE.PlaneGeometry(0.72, 0.44), new THREE.MeshBasicMaterial({ color: '#9fe3df', toneMapped: false })); glow.position.set(0, 0.26, 0.017);
  lid.add(scr, glow); lap.add(base, lid); lap.rotation.y = -0.35; g.add(lap);
  const mug = cyl(0.08, 0.07, 0.18, '#e4572e'); mug.position.set(1.25, 1.1, 0.25);
  const handle = mesh(new THREE.TorusGeometry(0.05, 0.015, 8, 16), mat('#e4572e')); handle.position.set(1.34, 1.1, 0.25);
  g.add(mug, handle);
  return g;
}

export function paper(title, accent, lines = 5, w = 0.45, stamp = null) {
  const p = texPlane(paperTex(title, accent, lines, stamp), w / 300, { lit: true, double: true });
  p.castShadow = true;
  return p;
}

export function legalBook() {
  const g = new THREE.Group();
  const coverM = mat('#9b3a3a', { rough: 0.5 });
  const spine = box(0.06, 0.08, 0.5, '#7a2e2e'); spine.position.y = 0.04; g.add(spine);
  const covers = [];
  for (const sg of [-1, 1]) {
    const hinge = new THREE.Group();
    const cover = mesh(new THREE.BoxGeometry(0.4, 0.02, 0.5), coverM); cover.position.x = sg * 0.2;
    const pages = box(0.37, 0.05, 0.46, '#fffaf0'); pages.position.set(sg * 0.2, sg > 0 ? 0.03 : -0.03, 0);
    hinge.add(cover, pages); g.add(hinge); covers.push(hinge);
  }
  g.userData.covers = covers;
  return g;
}

export function setBook(book, k) {
  const [l, r] = book.userData.covers;
  // closed: left cover folded over right
  l.rotation.z = (1 - k) * -Math.PI * 0.98 - 0.12 * k;
  l.position.y = 0.06;
  r.rotation.z = 0.12 * k;
  r.position.y = 0.02;
}

// ------------------------------------------------------------- legal objects
export function gavel() {
  const g = new THREE.Group();
  const handle = cyl(0.04, 0.05, 0.9, '#8c5a3c'); handle.position.y = -0.2; g.add(handle);
  const head = cyl(0.13, 0.13, 0.45, '#a26d4a', { rough: 0.4 }); head.rotation.z = Math.PI / 2; head.position.y = 0.25;
  for (const sg of [-1, 1]) { const b = cyl(0.145, 0.145, 0.06, '#e9c46a', { metal: 0.6, rough: 0.3 }); b.rotation.z = Math.PI / 2; b.position.set(sg * 0.2, 0.25, 0); g.add(b); }
  g.add(head);
  return g;
}

export function scales(color = '#ffb627') {
  const g = new THREE.Group();
  const gold = { metal: 0.7, rough: 0.3 };
  g.add(at(cyl(0.03, 0.04, 1.2, color, gold), 0, 0.6, 0));
  g.add(at(cyl(0.25, 0.3, 0.06, color, gold), 0, 0.03, 0));
  const beam = new THREE.Group(); beam.position.y = 1.15;
  beam.add(at(cyl(0.025, 0.025, 1.2, color, gold), 0, 0, 0, 0, 0, Math.PI / 2));
  for (const sg of [-1, 1]) {
    const pan = mesh(new THREE.SphereGeometry(0.2, 20, 10, 0, Math.PI * 2, Math.PI / 2, Math.PI / 2), mat(color, gold));
    pan.position.set(sg * 0.58, -0.45, 0); beam.add(pan);
    beam.add(at(cyl(0.008, 0.008, 0.45, '#555'), sg * 0.58, -0.22, 0));
  }
  g.add(beam);
  g.userData.beam = beam;
  return g;
}

export function coinStack(n = 3) {
  const g = new THREE.Group();
  for (let i = 0; i < n; i++) g.add(at(cyl(0.18, 0.18, 0.06, '#f2b632', { metal: 0.8, rough: 0.25 }), Math.sin(i * 2) * 0.02, 0.035 + i * 0.065, 0));
  return g;
}

export function cash() {
  const g = new THREE.Group();
  const t = canvasTex('bill', 240, 120, (c, w, h) => {
    c.fillStyle = '#5cb85c'; c.fillRect(0, 0, w, h); c.strokeStyle = '#2e7d32'; c.lineWidth = 8; c.strokeRect(8, 8, w - 16, h - 16);
    c.beginPath(); c.arc(w / 2, h / 2, 32, 0, 7); c.stroke(); c.fillStyle = '#2e7d32'; c.font = font(44, 700); c.textAlign = 'center'; c.fillText('$', w / 2, h / 2 + 16);
  });
  for (let i = 0; i < 3; i++) { const p = texPlane(t, 0.0016, { lit: true, double: true }); p.position.set(i * 0.03, i * 0.03, i * 0.01); p.rotation.z = i * 0.08; g.add(p); }
  return g;
}

export function machine(ghost = false) {
  const o = ghost ? { opacity: 0.35 } : {};
  const g = new THREE.Group();
  g.add(at(rbox(1.5, 1.1, 0.9, 0.1, '#5f8aa8', { ...o, metal: 0.3, rough: 0.4 }), 0, 0.65, 0));
  g.add(at(box(0.6, 0.45, 0.05, '#bfe6ff', { ...o, emissive: '#3a6f8f', ei: 0.3 }), -0.3, 0.85, 0.46));
  ['#e4572e', '#ffb627', '#3bb273'].forEach((c, i) => g.add(at(sphere(0.06, c, { ...o, emissive: c, ei: 0.4 }), 0.35 + (i % 2) * 0.18, 1.0 - i * 0.15, 0.46)));
  const gears = [];
  for (const [x, sp] of [[-0.35, 1], [0.25, -1]]) {
    const gear = new THREE.Group(); gear.position.set(x, 0.38, 0.47);
    gear.add(at(cyl(0.17, 0.17, 0.06, '#8a96a3', { ...o, metal: 0.6, rough: 0.3 }), 0, 0, 0, 0, Math.PI / 2));
    for (let k = 0; k < 8; k++) gear.add(at(box(0.07, 0.07, 0.06, '#8a96a3', { ...o, metal: 0.6 }), Math.cos(k * Math.PI / 4) * 0.2, Math.sin(k * Math.PI / 4) * 0.2, 0, 0, 0, k * Math.PI / 4));
    gear.userData.sp = sp; gears.push(gear); g.add(gear);
  }
  g.add(at(box(1.7, 0.1, 1.0, '#3a5d75', o), 0, 0.05, 0));
  g.userData.gears = gears;
  return g;
}
export function spinMachine(m, t) { m.userData.gears.forEach((gr) => (gr.rotation.z = t * 1.6 * gr.userData.sp)); }

export function truck() {
  const g = new THREE.Group();
  g.add(at(rbox(0.9, 0.55, 0.55, 0.05, '#ffb627'), -0.15, 0.45, 0));
  g.add(at(rbox(0.38, 0.42, 0.52, 0.06, '#0f8b8d'), 0.52, 0.38, 0));
  g.add(at(box(0.05, 0.18, 0.4, '#bfe6ff', { emissive: '#5a8fa8', ei: 0.3 }), 0.72, 0.45, 0));
  const wheels = [];
  for (const x of [-0.42, 0.5]) for (const z of [-0.27, 0.27]) {
    const w = at(cyl(0.13, 0.13, 0.08, '#2d3142'), x, 0.13, z, 0, Math.PI / 2); wheels.push(w); g.add(w);
  }
  g.userData.wheels = wheels;
  return g;
}

export function stopSign() {
  const g = new THREE.Group();
  g.add(at(cyl(0.03, 0.03, 1.0, '#8a96a3', { metal: 0.6 }), 0, 0.5, 0));
  const t = canvasTex('stop', 256, 256, (c, w, h) => {
    c.fillStyle = '#e4572e'; c.beginPath();
    for (let i = 0; i < 8; i++) { const a = Math.PI / 8 + i * Math.PI / 4; c.lineTo(w / 2 + Math.cos(a) * 124, h / 2 + Math.sin(a) * 124); }
    c.fill(); c.strokeStyle = '#fff'; c.lineWidth = 12; c.stroke();
    c.fillStyle = '#fff'; c.font = font(70, 700); c.textAlign = 'center'; c.textBaseline = 'middle'; c.fillText('STOP', w / 2, h / 2 + 4);
  });
  const face = at(cyl(0.38, 0.38, 0.05, '#e4572e', {}, 8), 0, 1.15, 0, 0, Math.PI / 2, Math.PI / 8);
  const decal = texPlane(t, 0.0031, { lit: true }); decal.position.set(0, 1.15, 0.03);
  g.add(face, decal);
  return g;
}

export function rewindArrow() {
  const g = new THREE.Group();
  const ring = mesh(new THREE.TorusGeometry(0.42, 0.04, 10, 40, Math.PI * 1.5), mat('#e4572e'));
  const head = mesh(new THREE.ConeGeometry(0.1, 0.2, 16), mat('#e4572e'));
  head.position.set(0.42, -0.02, 0); head.rotation.z = Math.PI;
  g.add(ring, head);
  return g;
}

export function pencil() {
  const g = new THREE.Group();
  g.add(at(cyl(0.04, 0.04, 0.6, '#ffb627'), 0, 0.3, 0));
  g.add(at(mesh(new THREE.ConeGeometry(0.04, 0.12, 12), mat('#f4d6a0')), 0, -0.06, 0, 0, 0, Math.PI));
  g.add(at(cyl(0.041, 0.041, 0.08, '#e07a5f'), 0, 0.62, 0));
  return g;
}

// ------------------------------------------------------------- buildings
function column(h, c = '#fff6e4') { return cyl(0.09, 0.1, h, c, { rough: 0.5 }, 16); }

export function parliament() {
  const g = new THREE.Group();
  g.add(at(box(2.2, 1.2, 1.2, '#f2e3c6'), 0, 0.6, 0));
  for (let i = 0; i < 6; i++) g.add(at(column(1.1), -0.9 + i * 0.36, 0.55, 0.7));
  g.add(at(box(2.5, 0.18, 1.6, '#e3cfa8'), 0, 1.25, 0.1));
  g.add(at(cyl(0.65, 0.7, 0.3, '#e3cfa8'), 0, 1.48, 0));
  g.add(at(mesh(new THREE.SphereGeometry(0.62, 32, 16, 0, Math.PI * 2, 0, Math.PI / 2), mat('#4f9dd0', { rough: 0.3, metal: 0.2 })), 0, 1.6, 0));
  g.add(at(cyl(0.02, 0.02, 0.6, '#555'), 0, 2.5, 0));
  g.add(at(box(0.35, 0.2, 0.02, '#e4572e'), 0.18, 2.7, 0));
  return g;
}

export function officeBlock() {
  const g = new THREE.Group();
  const t = canvasTex('officewin', 256, 512, (c, w, h) => {
    c.fillStyle = '#7aa6c2'; c.fillRect(0, 0, w, h);
    c.fillStyle = '#dff3ff';
    for (let r = 0; r < 9; r++) for (let k = 0; k < 4; k++) c.fillRect(18 + k * 60, 20 + r * 54, 42, 34);
  });
  const m = new THREE.MeshStandardMaterial({ map: t.tex, roughness: 0.4, metalness: 0.2 });
  const b = mesh(new THREE.BoxGeometry(1.7, 2.6, 1.3), m); b.position.y = 1.3; g.add(b);
  g.add(at(box(0.5, 0.5, 0.05, '#3d405b'), 0, 0.25, 0.66));
  g.add(at(box(1.8, 0.1, 1.4, '#4b7894'), 0, 2.65, 0));
  g.add(at(cyl(0.02, 0.02, 0.5, '#555'), 0, 2.95, 0));
  g.add(at(box(0.3, 0.18, 0.02, '#3bb273'), 0.16, 3.1, 0));
  return g;
}

export function courthouse() {
  const g = new THREE.Group();
  g.add(at(box(2.3, 0.2, 1.6, '#d9d4cc'), 0, 0.1, 0));
  g.add(at(box(2.1, 0.15, 1.45, '#e7e2d9'), 0, 0.27, 0));
  g.add(at(box(1.9, 1.3, 0.9, '#efeae2'), 0, 1.0, -0.2));
  for (let i = 0; i < 5; i++) g.add(at(column(1.3, '#f4f1ec'), -0.8 + i * 0.4, 1.0, 0.55));
  g.add(at(box(2.2, 0.2, 1.5, '#e7e2d9'), 0, 1.75, 0));
  const ped = new THREE.Shape(); ped.moveTo(-1.15, 0); ped.lineTo(1.15, 0); ped.lineTo(0, 0.6); ped.closePath();
  const pg = new THREE.ExtrudeGeometry(ped, { depth: 1.5, bevelEnabled: false }); pg.translate(0, 0, -0.75);
  g.add(at(mesh(pg, mat('#efeae2')), 0, 1.85, 0));
  g.add(at(scales('#b07b0e'), 0, 1.95, 0.78, 0, 0, 0, 0.3));
  return g;
}

// ------------------------------------------------------------- doors
export function doorway(color, label, hingeRight = false) {
  const g = new THREE.Group();
  const dark = new THREE.Color(color).multiplyScalar(0.6).getStyle();
  g.add(at(box(0.15, 2.6, 0.3, dark), -0.88, 1.3, 0), at(box(0.15, 2.6, 0.3, dark), 0.88, 1.3, 0), at(box(1.91, 0.15, 0.3, dark), 0, 2.6, 0));
  const sg = hingeRight ? -1 : 1;
  const hinge = new THREE.Group(); hinge.position.set(-0.8 * sg, 0, 0.05);
  const leaf = rbox(1.6, 2.5, 0.08, 0.04, color, { rough: 0.5 }); leaf.position.set(0.8 * sg, 1.26, 0);
  const knob = sphere(0.06, '#ffd166', { metal: 0.7, rough: 0.3 }); knob.position.set(1.42 * sg, 1.25, 0.08);
  for (const y of [0.7, 1.85]) hinge.add(at(box(1.2, 0.8, 0.02, dark), 0.8 * sg, y, 0.05));
  hinge.add(leaf, knob);
  g.add(hinge);
  g.userData.hinge = hinge;
  // interior room behind the door
  const room = new THREE.Group(); room.position.z = -0.9;
  room.add(at(box(1.62, 2.5, 0.05, color === PAL.teal ? '#cdeeea' : '#e2dbf7'), 0, 1.25, -0.6));
  room.add(at(box(1.62, 0.05, 1.3, '#d2c0a8'), 0, 0.02, 0));
  g.add(room);
  g.userData.room = room;
  return g;
}

// ------------------------------------------------------------- globe / sea / ship
export function globe(r = 1.6) {
  const g = new THREE.Group();
  const s = mesh(new THREE.SphereGeometry(r, 64, 40), new THREE.MeshStandardMaterial({ map: globeTex().tex, roughness: 0.45, metalness: 0.05 }));
  g.add(s);
  const halo = mesh(new THREE.SphereGeometry(r * 1.08, 48, 32), new THREE.MeshBasicMaterial({ color: '#9fe3df', transparent: true, opacity: 0.12, side: THREE.BackSide, toneMapped: false }), { cast: false });
  g.add(halo);
  g.userData.ball = s;
  return g;
}

export function stars(n = 600, rad = 40) {
  const pos = new Float32Array(n * 3);
  let seed = 11; const rnd = () => ((seed = (seed * 16807) % 2147483647) / 2147483647);
  for (let i = 0; i < n; i++) {
    const th = rnd() * Math.PI * 2, ph = Math.acos(2 * rnd() - 1);
    pos.set([Math.sin(ph) * Math.cos(th) * rad, Math.abs(Math.cos(ph)) * rad * 0.8 + 1, -Math.abs(Math.sin(ph) * Math.sin(th)) * rad], i * 3);
  }
  const geo = new THREE.BufferGeometry(); geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
  return new THREE.Points(geo, new THREE.PointsMaterial({ color: '#ffffff', size: 0.12, transparent: true, opacity: 0.8, toneMapped: false }));
}

export function sea(size = 80, color = '#2b86c5') {
  const geo = new THREE.PlaneGeometry(size, size, 80, 80);
  geo.rotateX(-Math.PI / 2);
  const m = mesh(geo, new THREE.MeshStandardMaterial({ color, roughness: 0.25, metalness: 0.1, flatShading: true }), { cast: false, receive: true });
  m.userData.base = Float32Array.from(geo.attributes.position.array);
  return m;
}
export function animateSea(m, t, amp = 0.12) {
  const p = m.geometry.attributes.position, b = m.userData.base;
  for (let i = 0; i < p.count; i++) {
    const x = b[i * 3], z = b[i * 3 + 2];
    p.array[i * 3 + 1] = Math.sin(x * 0.6 + t * 1.6) * amp + Math.cos(z * 0.8 + t * 1.2) * amp * 0.7;
  }
  p.needsUpdate = true;
  m.geometry.computeVertexNormals();
}

export function ship() {
  const g = new THREE.Group();
  const hullShape = new THREE.Shape();
  hullShape.moveTo(-3.4, 0.6); hullShape.lineTo(3.2, 0.6); hullShape.lineTo(2.7, -0.4); hullShape.lineTo(-3.1, -0.4); hullShape.closePath();
  const hg = new THREE.ExtrudeGeometry(hullShape, { depth: 1.6, bevelEnabled: true, bevelSize: 0.05, bevelThickness: 0.05 }); hg.translate(0, 0, -0.8);
  g.add(mesh(hg, mat('#e4572e', { rough: 0.45 })));
  g.add(at(box(6.5, 0.1, 1.7, '#ffffff'), -0.1, 0.25, 0));
  g.add(at(box(6.2, 0.06, 1.5, '#7a5c45'), -0.1, 0.66, 0));
  const cols = ['#3bb273', '#1f3a5f', '#ffb627', '#7768ae'];
  [[-2.7, 1.0, 0], [-1.6, 1.0, 0], [-2.7, 1.58, 0], [-1.6, 1.58, 1]].forEach(([x, y], i) => g.add(at(box(1.05, 0.56, 1.3, cols[i], { rough: 0.5, metal: 0.2 }), x, y, 0)));
  g.add(at(box(0.9, 1.4, 1.2, '#ffffff'), 2.2, 1.4, 0));
  for (let i = 0; i < 3; i++) g.add(at(box(0.18, 0.18, 0.02, '#8fd3ff', { emissive: '#4a8fb8', ei: 0.4 }), 1.95 + i * 0.25, 1.8, 0.61));
  g.add(at(cyl(0.16, 0.18, 0.6, '#e4572e'), 2.3, 2.4, 0));
  const t = canvasTex('shipname', 512, 80, (c, w, h) => { c.fillStyle = '#fff'; c.font = font(60, 700); c.textAlign = 'center'; c.fillText('SAFARITECH', w / 2, 62); });
  const name = texPlane(t, 0.004, { lit: true }); name.position.set(0, 0.0, 0.86); g.add(name);
  const cargo = makeCargo(); cargo.position.set(0.3, 0.68, 0); cargo.scale.setScalar(1.0);
  g.add(cargo);
  g.userData.cargo = cargo;
  return g;
}

// ------------------------------------------------------------- court rooms
export function courtroom() {
  const g = new THREE.Group();
  g.add(at(box(9, 6, 0.1, '#e9d8bd'), 0, 3, -3));
  for (let i = -4; i <= 4; i += 1.6) g.add(at(box(0.25, 6, 0.2, '#d8c09b'), i, 3, -2.9));
  g.add(at(box(9, 0.1, 8, '#b88d62'), 0, -0.05, 0));
  const bench = rbox(3.6, 1.4, 1.0, 0.05, '#8c5a3c', { rough: 0.5 }); bench.position.set(0, 0.7, -1.8); g.add(bench);
  g.add(at(box(3.9, 0.12, 1.2, '#6b4430'), 0, 1.45, -1.8));
  const judge = makeMini('#1b1b1b', '#c98b62', { wig: true, scale: 1.25 }); judge.position.set(0, 0.6, -2.3); g.add(judge);
  const sc = scales('#b07b0e'); sc.position.set(1.3, 1.5, -1.8); sc.scale.setScalar(0.45); g.add(sc);
  const crowd = [['#e07a5f', '#8d5a3b'], ['#3d405b', '#e8b48f'], ['#81b29a', '#5e3b25'], ['#f2cc8f', '#c98b62'], ['#7768ae', '#a86f4c'], ['#0f8b8d', '#e8b48f']];
  crowd.forEach(([b, s], i) => { const m = makeMini(b, s, { scale: 0.95 }); m.position.set(-3.2 + i * 1.28, 0, 1.9); m.rotation.y = Math.PI; g.add(m); });
  g.add(at(box(8, 0.5, 0.15, '#6b4430'), 0, 0.5, 1.4));
  return g;
}

export function arbRoom() {
  const g = new THREE.Group();
  g.add(at(box(9, 6, 0.1, '#e6f4f1'), 0, 3, -3));
  g.add(at(box(9, 0.1, 8, '#a7c4bc'), 0, -0.05, 0));
  const door = rbox(1.2, 2.3, 0.1, 0.05, '#7a5c45'); door.position.set(3.2, 1.15, -2.9); g.add(door);
  g.add(at(rbox(0.3, 0.26, 0.08, 0.04, '#ffb627', { metal: 0.5 }), 3.2, 1.2, -2.8));
  g.add(at(mesh(new THREE.TorusGeometry(0.1, 0.03, 8, 16, Math.PI), mat('#b07b0e', { metal: 0.6 })), 3.2, 1.33, -2.8));
  const table = cyl(1.4, 1.4, 0.1, '#8c5a3c', { rough: 0.4 }); table.position.set(0, 0.8, -0.5); g.add(table);
  g.add(at(cyl(0.12, 0.2, 0.8, '#5e3b25'), 0, 0.4, -0.5));
  const people = [['#e07a5f', '#8d5a3b', -1.7, 0.4], ['#3d405b', '#e8b48f', 1.7, -0.4], ['#0f8b8d', '#5e3b25', 0, 0]];
  people.forEach(([b, s, x, ry], i) => { const m = makeMini(b, s, { scale: 1.2 }); m.position.set(x, 0, i === 2 ? -1.9 : -0.5); m.rotation.y = i === 2 ? 0 : (x < 0 ? Math.PI / 2 : -Math.PI / 2); g.add(m); });
  g.add(at(sphere(0.09, '#ffb627', { metal: 0.6 }), 0.0, 1.0, -1.65));
  return g;
}

export function corkboard() {
  const g = new THREE.Group();
  g.add(at(rbox(4.6, 2.9, 0.12, 0.08, '#8c5a3c'), 0, 0, 0));
  const t = canvasTex('cork', 512, 320, (c, w, h) => {
    c.fillStyle = '#d9a066'; c.fillRect(0, 0, w, h);
    for (let i = 0; i < 400; i++) { c.fillStyle = `rgba(150,100,60,${0.15 + (i % 5) * 0.06})`; c.fillRect((i * 97.3) % w, (i * 53.7) % h, 3, 3); }
    c.fillStyle = '#5e3b25'; c.font = font(30, 700); c.textAlign = 'center'; c.fillText('EPISODE 1 RECAP', w / 2, 40);
  });
  const face = texPlane(t, 0.0085, { lit: true }); face.position.z = 0.065; g.add(face);
  return g;
}

export function pin(color) {
  const g = new THREE.Group();
  g.add(at(sphere(0.07, color, { rough: 0.3 }), 0, 0, 0.08));
  g.add(at(cyl(0.01, 0.01, 0.1, '#999'), 0, 0, 0.03, 0, Math.PI / 2));
  return g;
}

export { makeCargo, makeMini };
