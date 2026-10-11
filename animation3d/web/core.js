// Core of the 3D renderer: easing, materials, canvas-texture labels and an
// immediate-mode object cache so scene code reads like the 2D version.
import * as THREE from 'three';

export const W = 1920, H = 1080;

// ------------------------------------------------------------- easing
export const clamp = (x, a = 0, b = 1) => (x < a ? a : x > b ? b : x);
export const prog = (t, t0, d) => (d <= 0 ? (t >= t0 ? 1 : 0) : clamp((t - t0) / d));
export const easeInOut = (x) => { x = clamp(x); return x * x * (3 - 2 * x); };
export const easeOut = (x) => 1 - (1 - clamp(x)) ** 3;
export const easeOutBack = (x, s = 1.70158) => { x = clamp(x) - 1; return x * x * ((s + 1) * x + s) + 1; };
export const lerp = (a, b, k) => a + (b - a) * k;
export const pop = (t, t0, d = 0.45) => easeOutBack(prog(t, t0, d), 2.2);
export const win = (t, t0, t1, f = 0.35) =>
  t < t0 || t > t1 + f ? 0 : easeInOut(prog(t, t0, f)) * (1 - easeInOut(prog(t, t1, f)));
export const rad = (d) => (d * Math.PI) / 180;

export const PAL = {
  ink: '#1d2b3a', navy: '#1f3a5f', teal: '#0f8b8d', accent: '#ffb627', mistake: '#e4572e',
  purple: '#7768ae', green: '#3bb273', cream: '#fff8ec', grey: '#8a96a3', amber: '#f2a541',
};

// ------------------------------------------------------------- materials
const matCache = new Map();
export function mat(color, o = {}) {
  const key = color + JSON.stringify(o);
  if (!matCache.has(key)) {
    matCache.set(key, new THREE.MeshStandardMaterial({
      color: PAL[color] || color, roughness: o.rough ?? 0.55, metalness: o.metal ?? 0,
      emissive: o.emissive || '#000000', emissiveIntensity: o.ei ?? 1,
      transparent: !!o.opacity, opacity: o.opacity ?? 1, side: o.side ?? THREE.FrontSide,
    }));
  }
  return matCache.get(key);
}

export function mesh(geo, material, { cast = true, receive = false } = {}) {
  const m = new THREE.Mesh(geo, material);
  m.castShadow = cast;
  m.receiveShadow = receive;
  return m;
}

export const box = (w, h, d, c, o) => mesh(new THREE.BoxGeometry(w, h, d), mat(c, o));
export const sphere = (r, c, o, seg = 24) => mesh(new THREE.SphereGeometry(r, seg, Math.round(seg * 0.75)), mat(c, o));
export const cyl = (rt, rb, h, c, o, seg = 24) => mesh(new THREE.CylinderGeometry(rt, rb, h, seg), mat(c, o));
export const capsule = (r, len, c, o) => mesh(new THREE.CapsuleGeometry(r, len, 6, 14), mat(c, o));

export function rbox(w, h, d, r, c, o) {
  // rounded box via extruded rounded rectangle
  const s = new THREE.Shape();
  const x = -w / 2, y = -h / 2;
  s.moveTo(x + r, y);
  s.lineTo(x + w - r, y); s.quadraticCurveTo(x + w, y, x + w, y + r);
  s.lineTo(x + w, y + h - r); s.quadraticCurveTo(x + w, y + h, x + w - r, y + h);
  s.lineTo(x + r, y + h); s.quadraticCurveTo(x, y + h, x, y + h - r);
  s.lineTo(x, y + r); s.quadraticCurveTo(x, y, x + r, y);
  const bev = Math.min(r * 0.5, d * 0.3);
  const g = new THREE.ExtrudeGeometry(s, { depth: d - 2 * bev, bevelEnabled: true, bevelThickness: bev, bevelSize: bev * 0.8, bevelSegments: 3, curveSegments: 8 });
  g.translate(0, 0, -(d - 2 * bev) / 2);
  return mesh(g, mat(c, o));
}

export function group(...children) {
  const g = new THREE.Group();
  children.forEach((c) => c && g.add(c));
  return g;
}

export function at(obj, x = 0, y = 0, z = 0, ry = 0, rx = 0, rz = 0, s = 1) {
  obj.position.set(x, y, z);
  obj.rotation.set(rx, ry, rz);
  if (typeof s === 'number') obj.scale.setScalar(s); else obj.scale.set(...s);
  return obj;
}

export function setOpacity(obj, a) {
  obj.traverse((o) => {
    if (o.material) {
      if (!o.userData.ownMat) { o.material = o.material.clone(); o.userData.ownMat = true; }
      o.material.transparent = a < 0.999 || o.userData.alwaysTransparent;
      o.material.opacity = a * (o.userData.baseOpacity ?? 1);
    }
  });
}

// ------------------------------------------------------------- canvas textures
export const FONT = 'Fredoka';
function ctx2d(w, h) {
  const c = document.createElement('canvas');
  c.width = Math.ceil(w); c.height = Math.ceil(h);
  return [c, c.getContext('2d')];
}
export function rr(g, x, y, w, h, r) {
  g.beginPath();
  g.moveTo(x + r, y); g.arcTo(x + w, y, x + w, y + h, r); g.arcTo(x + w, y + h, x, y + h, r);
  g.arcTo(x, y + h, x, y, r); g.arcTo(x, y, x + w, y, r); g.closePath();
}
export function font(size, weight = 500) { return `${weight} ${size}px ${FONT}`; }
export function wrapLines(g, text, maxW) {
  const words = text.split(' '); const out = []; let cur = '';
  for (const w of words) {
    const t = (cur + ' ' + w).trim();
    if (g.measureText(t).width <= maxW || !cur) cur = t; else { out.push(cur); cur = w; }
  }
  if (cur) out.push(cur);
  return out;
}

function texOf(c) {
  const t = new THREE.CanvasTexture(c);
  t.colorSpace = THREE.SRGBColorSpace;
  t.anisotropy = 4;
  return t;
}

const texCache = new Map();
export function canvasTex(key, w, h, draw) {
  if (!texCache.has(key)) {
    const S = 2;
    const [c, g] = ctx2d(w * S, h * S);
    g.scale(S, S);
    draw(g, w, h);
    texCache.set(key, { tex: texOf(c), w, h });
  }
  return texCache.get(key);
}

export function chipTex(text, bg = PAL.teal, fg = '#ffffff', size = 34, family = FONT) {
  const [, m] = ctx2d(10, 10);
  m.font = `600 ${size}px ${family}`;
  const w = m.measureText(text).width + size * 1.2, h = size * 1.7;
  return canvasTex(`chip|${text}|${bg}|${fg}|${size}|${family}`, w + 8, h + 8, (g) => {
    g.fillStyle = 'rgba(0,0,0,0.18)'; rr(g, 6, 8, w, h, h / 2); g.fill();
    g.fillStyle = PAL[bg] || bg; rr(g, 2, 2, w, h, h / 2); g.fill();
    g.fillStyle = PAL[fg] || fg; g.font = `600 ${size}px ${family}`; g.textAlign = 'center';
    g.textBaseline = 'middle'; g.fillText(text, 2 + w / 2, 2 + h / 2 + size * 0.04);
  });
}

export function cardTex(key, w, h, { title, body, accent = PAL.teal, titleSize = 40, bodySize = 34, fill = '#ffffff', align = 'left', bodyColor = PAL.ink } = {}) {
  return canvasTex(`card|${key}|${w}|${h}`, w + 14, h + 18, (g) => {
    g.fillStyle = 'rgba(0,0,0,0.18)'; rr(g, 10, 14, w, h, 26); g.fill();
    g.fillStyle = fill; rr(g, 2, 2, w, h, 26); g.fill();
    let top = 30;
    if (title) {
      g.save(); rr(g, 2, 2, w, h, 26); g.clip();
      g.fillStyle = PAL[accent] || accent; g.fillRect(2, 2, w, titleSize + 34); g.restore();
      g.fillStyle = '#fff'; g.font = font(titleSize, 600); g.textBaseline = 'alphabetic';
      g.textAlign = align;
      g.fillText(title, align === 'center' ? 2 + w / 2 : 32, titleSize + 12);
      top = titleSize + 58;
    }
    if (body) {
      g.font = font(bodySize, 500); g.fillStyle = bodyColor; g.textAlign = align;
      wrapLines(g, body, w - 60).forEach((ln, i) =>
        g.fillText(ln, align === 'center' ? 2 + w / 2 : 32, top + bodySize + i * bodySize * 1.25 - 6));
    }
  });
}

export function paperTex(title = '', accent = PAL.teal, lines = 5, stamp = null) {
  const w = 300, h = 400;
  return canvasTex(`paper|${title}|${accent}|${lines}|${stamp}`, w, h, (g) => {
    g.fillStyle = '#ffffff'; g.fillRect(0, 0, w, h);
    g.fillStyle = PAL[accent] || accent; g.fillRect(0, 0, w, 70);
    if (title) {
      g.fillStyle = '#fff'; g.font = font(title.length > 8 ? 36 : 44, 700); g.textAlign = 'center';
      g.textBaseline = 'middle'; g.fillText(title, w / 2, 37);
    }
    g.strokeStyle = '#c4ccd4'; g.lineWidth = 12; g.lineCap = 'round';
    for (let i = 0; i < lines; i++) {
      const y = 120 + i * ((h - 160) / Math.max(lines, 1));
      g.beginPath(); g.moveTo(36, y); g.lineTo(w - 36 - (i === lines - 1 ? 60 : 0), y); g.stroke();
    }
    if (stamp) {
      g.save(); g.translate(w * 0.62, h * 0.72); g.rotate(-0.25);
      g.strokeStyle = stamp[1]; g.lineWidth = 8; rr(g, -90, -34, 180, 68, 12); g.stroke();
      g.fillStyle = stamp[1]; g.font = font(36, 700); g.textAlign = 'center'; g.textBaseline = 'middle';
      g.fillText(stamp[0], 0, 2); g.restore();
    }
  });
}

// a flat plane textured with a canvas; world size from px * k
export function texPlane(t, k = 0.004, { lit = false, double = false } = {}) {
  const geo = new THREE.PlaneGeometry(t.w * k, t.h * k);
  const m = lit
    ? new THREE.MeshStandardMaterial({ map: t.tex, transparent: true, roughness: 0.8, side: double ? THREE.DoubleSide : THREE.FrontSide })
    : new THREE.MeshBasicMaterial({ map: t.tex, transparent: true, toneMapped: false, depthWrite: false, side: double ? THREE.DoubleSide : THREE.FrontSide });
  const p = new THREE.Mesh(geo, m);
  p.userData.alwaysTransparent = true;
  return p;
}

// ------------------------------------------------------------- immediate-mode stage
export class Stage {
  constructor(scene) {
    this.scene = scene || new THREE.Scene();
    this.cache = new Map();
  }
  begin() { for (const o of this.cache.values()) o.visible = false; }
  get(id, factory) {
    let o = this.cache.get(id);
    if (!o) { o = factory(); this.cache.set(id, o); this.scene.add(o); }
    o.visible = true;
    return o;
  }
}

// billboard chip in the 3D world
export function chip3(st, id, text, x, y, z, { bg = PAL.teal, fg = '#fff', size = 34, s = 1, a = 1, k = 0.0045 } = {}) {
  const o = st.get(id, () => { const p = texPlane(chipTex(text, bg, fg, size), k); p.userData.billboard = true; p.renderOrder = 10; return p; });
  o.position.set(x, y, z); o.scale.setScalar(Math.max(s, 1e-4)); setOpacity(o, a);
  o.visible = s > 0.001 && a > 0.001;
  return o;
}

// ------------------------------------------------------------- HUD (pixel space, origin top-left)
export class Hud extends Stage {
  constructor() {
    super(new THREE.Scene());
    this.cam = new THREE.OrthographicCamera(0, W, H, 0, -10, 10);
  }
  place(o, x, y, s = 1, a = 1, rot = 0) {
    o.position.set(x, H - y, o.position.z);
    o.scale.setScalar(Math.max(s, 1e-4)); o.rotation.z = -rot;
    setOpacity(o, a);
    o.visible = s > 0.001 && a > 0.001;
    return o;
  }
  tex(id, t, x, y, s = 1, a = 1, rot = 0, z = 0) {
    const o = this.get(id, () => { const p = texPlane(t, 1); p.position.z = z; return p; });
    return this.place(o, x, y, s, a, rot);
  }
  chip(id, text, x, y, { bg = PAL.teal, fg = '#fff', size = 34, s = 1, a = 1, z = 0 } = {}) {
    return this.tex(id, chipTex(text, bg, fg, size), x, y, s, a, 0, z);
  }
  card(id, x, y, w, h, opts, s = 1, a = 1, z = 0) {
    return this.tex(id, cardTex(id, w, h, opts), x, y, s, a, 0, z);
  }
  rect(id, x, y, w, h, color, a = 1, z = -1) {
    const o = this.get(id, () => {
      const m = new THREE.Mesh(new THREE.PlaneGeometry(1, 1), new THREE.MeshBasicMaterial({ color, transparent: true, toneMapped: false, depthWrite: false }));
      m.position.z = z; return m;
    });
    o.position.set(x + w / 2, H - (y + h / 2), z); o.scale.set(w, h, 1);
    o.material.opacity = a; o.visible = a > 0.001;
    return o;
  }
  text(id, str, x, y, size, color = '#fff', opts = {}, s = 1, a = 1, z = 1) {
    return this.tex(id, textTex(str, size, color, opts), x, y, s, a, 0, z);
  }
  draw(id, w, h, x, y, drawFn, s = 1, a = 1, z = 0, rot = 0) {
    // custom canvas drawing, cached by id
    return this.tex(id, canvasTex('hud|' + id, w, h, drawFn), x, y, s, a, rot, z);
  }
}

export function checkTex(label, size = 34, color = PAL.green) {
  const [, m] = ctx2d(10, 10);
  m.font = font(size, 600);
  const w = m.measureText(label).width + size * 2.6, h = size * 1.7;
  return canvasTex(`check|${label}|${size}|${color}`, w + 8, h + 8, (g) => {
    g.fillStyle = 'rgba(255,255,255,0.92)'; rr(g, 2, 2, w, h, h / 2); g.fill();
    g.fillStyle = color; g.beginPath(); g.arc(2 + h / 2, 2 + h / 2, h * 0.36, 0, 7); g.fill();
    g.strokeStyle = '#fff'; g.lineWidth = size * 0.16; g.lineCap = 'round'; g.lineJoin = 'round';
    const cx = 2 + h / 2, cy = 2 + h / 2, r = h * 0.18;
    g.beginPath(); g.moveTo(cx - r, cy); g.lineTo(cx - r * 0.25, cy + r * 0.75); g.lineTo(cx + r, cy - r * 0.7); g.stroke();
    g.fillStyle = PAL.ink; g.font = font(size, 600); g.textBaseline = 'middle';
    g.fillText(label, 2 + h + size * 0.3, 2 + h / 2 + size * 0.04);
  });
}

export function textTex(str, size, color = '#fff', { weight = 700, outline = null, ow = 12, family = FONT } = {}) {
  const [, m] = ctx2d(10, 10);
  m.font = `${weight} ${size}px ${family}`;
  const w = m.measureText(str).width + ow * 2 + 8, h = size * 1.4 + ow * 2;
  return canvasTex(`text|${str}|${size}|${color}|${weight}|${outline}|${family}`, w, h, (g) => {
    g.font = `${weight} ${size}px ${family}`; g.textAlign = 'center'; g.textBaseline = 'middle';
    if (outline) { g.lineJoin = 'round'; g.strokeStyle = outline; g.lineWidth = ow; g.strokeText(str, w / 2, h / 2); }
    g.fillStyle = PAL[color] || color; g.fillText(str, w / 2, h / 2);
  });
}
