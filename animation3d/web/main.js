// Page entry: builds each scene on first use and renders single frames on demand.
import * as THREE from 'three';
import { Hud, PAL, Stage, easeInOut, prog, win } from './core.js';
import { SCENES, ST } from './scenes.js';
import { useEnvironment } from './props.js';

const canvas = document.getElementById('c');
let renderer, cam, hud, TL;
const stages = {};

window.init = async (timeline, width = 1280, height = 720) => {
  await Promise.all([document.fonts.load('600 40px Fredoka'), document.fonts.load('700 40px Fredoka'),
    document.fonts.load('500 40px Fredoka'), document.fonts.load('700 40px Nunito')]);
  TL = timeline;
  renderer = new THREE.WebGLRenderer({ canvas, antialias: true, preserveDrawingBuffer: true });
  renderer.setPixelRatio(1);
  renderer.setSize(width, height, false);
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  renderer.toneMapping = THREE.NeutralToneMapping;
  renderer.toneMappingExposure = 1.0;
  renderer.localClippingEnabled = true;
  renderer.autoClear = false;
  cam = new THREE.PerspectiveCamera(35, 16 / 9, 0.1, 400);
  hud = new Hud();
  return true;
};

function stageFor(key) {
  if (!stages[key]) {
    const S = new Stage();
    SCENES[key].setup(S);
    useEnvironment(renderer, S.scene, S.scene.userData.envIntensity ?? 0.45);
    stages[key] = S;
  }
  return stages[key];
}

function overlay(t, sc, idx) {
  if (sc.key !== 'title') {
    const a = win(t, 0.4, 3.6, 0.4);
    if (a > 0) hud.chip('scene' + idx, `SCENE ${idx}  ·  ${sc.title}`, 0, 0, { bg: '#1d2b3a', size: 30, a }).position.x += 0;
    const chip = hud.cache.get('scene' + idx);
    if (chip && chip.visible) { const w = chip.geometry.parameters.width; hud.place(chip, 34 + w / 2, 62, 1, a); }
  }
  const fade = Math.max(1 - easeInOut(prog(t, 0, 0.35)), easeInOut(prog(t, sc.dur - 0.3, 0.3)));
  hud.rect('fade', 0, 0, 1920, 1080, '#0b1622', fade, 5);
}

window.frame = (idx, t, quality = 0.92) => {
  const sc = TL.scenes[idx];
  const S = stageFor(sc.key);
  S.begin(); hud.begin();
  const st = new ST(sc);
  SCENES[sc.key].draw(S, t, st, cam, hud);
  overlay(t, sc, idx);
  cam.updateMatrixWorld();
  S.scene.traverse((o) => { if (o.userData.billboard) o.quaternion.copy(cam.quaternion); });
  renderer.clear();
  renderer.render(S.scene, cam);
  renderer.clearDepth();
  renderer.render(hud.scene, hud.cam);
  return canvas.toDataURL('image/jpeg', quality);
};
window.ready = true;
