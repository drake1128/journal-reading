import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { CSS2DRenderer, CSS2DObject } from 'three/addons/renderers/CSS2DRenderer.js';
import { MeshoptDecoder } from 'three/addons/libs/meshopt_decoder.module.js';

const REGIONS = ['heart', 'lower-limb', 'head-neck'];
const params = new URLSearchParams(location.search);
const regionId = REGIONS.includes(params.get('r')) ? params.get('r') : 'heart';
const $ = id => document.getElementById(id);

// ---------- 狀態 ----------
const state = {
  lang: localStorage.getItem('a3d-lang') || 'both',
  labels: true, allLabels: false, xray: false,
  selected: null, solo: null,
};
const items = new Map();   // key → { meta, mesh, label, visible, opacity }
const groups = new Map();  // id → { meta, visible, opacity, el }
let manifest, radius, center = new THREE.Vector3();

// ---------- 場景 ----------
const stage = $('stage');
const renderer = new THREE.WebGLRenderer({ antialias: true, preserveDrawingBuffer: true });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.outputColorSpace = THREE.SRGBColorSpace;
stage.prepend(renderer.domElement);
const labelRenderer = new CSS2DRenderer();
labelRenderer.domElement.className = 'labels';
stage.prepend(labelRenderer.domElement);
renderer.domElement.after(labelRenderer.domElement);

const scene = new THREE.Scene();
scene.background = new THREE.Color('#f4f1ec');
const camera = new THREE.PerspectiveCamera(30, 1, 1, 20000);
scene.add(camera);
scene.add(new THREE.HemisphereLight('#ffffff', '#8a7f72', 1.4));
const headlight = new THREE.DirectionalLight('#ffffff', 1.6);
headlight.position.set(0.3, 0.6, 1);
camera.add(headlight);
const fill = new THREE.DirectionalLight('#ffffff', 0.5);
fill.position.set(-0.6, -0.4, -1);
camera.add(fill);

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.12;
controls.rotateSpeed = 0.8;
controls.screenSpacePanning = true;

// 放在隱藏的分頁（例如 Quarto tabset）裡時，畫面尺寸一開始是 0，
// 等第一次有尺寸時才套用初始視角
let pendingView = null;
function resize() {
  const w = stage.clientWidth, h = stage.clientHeight;
  if (!w || !h) return;
  renderer.setSize(w, h);
  labelRenderer.setSize(w, h);
  camera.aspect = w / h;
  camera.updateProjectionMatrix();
  if (pendingView && manifest) { const v = pendingView; pendingView = null; applyView(v, true); }
}
new ResizeObserver(resize).observe(stage);

// ---------- 文字 ----------
function name(meta) {
  if (state.lang === 'zh') return meta.zh;
  if (state.lang === 'en') return meta.en;
  return `${meta.zh}<small>${meta.en}</small>`;
}
function plainName(meta) {
  return state.lang === 'en' ? meta.en : meta.zh;
}

// ---------- 載入 ----------
async function load() {
  document.querySelectorAll('#tabs a').forEach(a => a.classList.toggle('active', a.dataset.r === regionId));
  manifest = await (await fetch(`data/${regionId}.json`)).json();
  document.title = `${manifest.title.zh}｜3D 血管解剖`;
  $('intro').textContent = manifest.intro;

  const loader = new GLTFLoader().setMeshoptDecoder(MeshoptDecoder);
  const gltf = await loader.loadAsync(`models/${regionId}.glb`, e => {
    if (e.total) $('loading').textContent = `模型載入中... ${Math.round(e.loaded / e.total * 100)}%`;
  });
  scene.add(gltf.scene);
  gltf.scene.updateMatrixWorld(true);

  const bmin = new THREE.Vector3(...manifest.bbox.min), bmax = new THREE.Vector3(...manifest.bbox.max);
  radius = bmin.distanceTo(bmax) / 2;
  camera.near = radius / 50; camera.far = radius * 40; camera.updateProjectionMatrix();
  controls.minDistance = radius * 0.05; controls.maxDistance = radius * 8;

  for (const g of manifest.groups) groups.set(g.id, { meta: g, visible: !g.hidden, opacity: g.opacity ?? 1 });
  for (const meta of manifest.items) {
    const mesh = gltf.scene.getObjectByName(meta.k);
    if (!mesh) continue;
    mesh.material = new THREE.MeshStandardMaterial({ color: meta.c, roughness: 0.55, metalness: 0.0, side: THREE.DoubleSide });
    mesh.userData.key = meta.k;
    const div = document.createElement('div');
    div.className = 'lbl';
    div.addEventListener('click', ev => { ev.stopPropagation(); select(meta.k); });
    const label = new CSS2DObject(div);
    label.center.set(0.04, 0.5);
    label.position.copy(mesh.worldToLocal(new THREE.Vector3(...meta.anchor)));
    mesh.add(label);
    items.set(meta.k, { meta, mesh, label, visible: true, opacity: meta.op ?? null });
  }
  buildPanel();
  buildViews();
  applyLang();
  refresh();
  $('loading').hidden = true;
  let first = manifest.views[0];
  const vi = manifest.views.findIndex(v => v.id === params.get('v'));
  if (vi >= 0) { first = manifest.views[vi]; document.querySelectorAll('#views button').forEach((b, j) => b.classList.toggle('on', vi === j)); }
  if (stage.clientWidth && stage.clientHeight) { resize(); applyView(first, true); }
  else pendingView = first;
}

// ---------- 可見度與透明度 ----------
function effOpacity(it) {
  const g = groups.get(it.meta.g);
  let o = it.opacity ?? g.opacity;
  if (state.xray && (it.meta.g === 'chamber' || it.meta.g === 'bone' || it.meta.g === 'muscle' || it.meta.g === 'soft')) o = Math.min(o, 0.15);
  return o;
}
function isShown(it) {
  if (state.solo) return state.solo.has(it.meta.k);
  return groups.get(it.meta.g).visible && it.visible;
}
function refresh() {
  for (const it of items.values()) {
    const shown = isShown(it);
    const o = effOpacity(it);
    const m = it.mesh.material;
    it.mesh.visible = shown && o > 0.01;
    m.opacity = o;
    m.transparent = o < 0.999;
    m.depthWrite = o >= 0.999;
    it.mesh.renderOrder = o < 0.999 ? 2 : 0;
    m.emissive.set(state.selected === it.meta.k ? '#5a4a00' : '#000000');
    const showLabel = state.labels && it.mesh.visible && o > 0.2 &&
      (state.allLabels || it.meta.lab || state.selected === it.meta.k);
    it.wantLabel = showLabel;
    it.label.visible = showLabel && !it.occluded;
    it.label.element.classList.toggle('sel', state.selected === it.meta.k);
    const row = document.querySelector(`.item[data-k="${it.meta.k}"] input`);
    if (row) row.checked = it.visible;
  }
  for (const g of groups.values()) {
    const cb = g.el?.querySelector('.gcheck');
    if (cb) cb.checked = g.visible;
  }
  occlusionDirty = true;
  $('btnLabels').classList.toggle('on', state.labels);
  $('btnAllLabels').classList.toggle('on', state.allLabels);
  $('btnXray').classList.toggle('on', state.xray);
  $('btnIsolate').classList.toggle('on', !!state.solo);
}

// ---------- 側欄 ----------
function buildPanel() {
  const root = $('groups');
  root.innerHTML = '';
  for (const g of groups.values()) {
    const sec = document.createElement('section');
    sec.className = 'group';
    sec.innerHTML = `
      <div class="ghead">
        <input type="checkbox" class="gcheck" ${g.visible ? 'checked' : ''} aria-label="顯示群組">
        <button class="gname" aria-expanded="false"><span class="gtitle"></span><span class="chev">▸</span></button>
        <input type="range" class="gop" min="0" max="1" step="0.05" value="${g.opacity}" title="透明度">
      </div>
      <ul class="glist" hidden></ul>`;
    g.el = sec;
    sec.querySelector('.gcheck').addEventListener('change', e => { g.visible = e.target.checked; state.solo = null; refresh(); });
    sec.querySelector('.gop').addEventListener('input', e => {
      g.opacity = +e.target.value;
      for (const it of items.values()) if (it.meta.g === g.meta.id) it.opacity = null;
      refresh();
    });
    const btn = sec.querySelector('.gname'), list = sec.querySelector('.glist');
    btn.addEventListener('click', () => {
      list.hidden = !list.hidden;
      btn.setAttribute('aria-expanded', String(!list.hidden));
      btn.querySelector('.chev').textContent = list.hidden ? '▸' : '▾';
    });
    for (const it of items.values()) {
      if (it.meta.g !== g.meta.id) continue;
      const li = document.createElement('li');
      li.className = 'item';
      li.dataset.k = it.meta.k;
      li.innerHTML = `<input type="checkbox" checked aria-label="顯示"><span class="sw" style="background:${it.meta.c}"></span><button class="iname"></button>`;
      li.querySelector('input').addEventListener('change', e => { it.visible = e.target.checked; state.solo = null; refresh(); });
      li.querySelector('.iname').addEventListener('click', () => { select(it.meta.k); });
      list.append(li);
    }
    root.append(sec);
  }
}

function buildViews() {
  const box = $('views');
  box.innerHTML = '';
  for (const v of manifest.views) {
    const b = document.createElement('button');
    b.textContent = v.zh;
    b.addEventListener('click', () => {
      box.querySelectorAll('button').forEach(x => x.classList.remove('on'));
      b.classList.add('on');
      applyView(v);
    });
    box.append(b);
  }
  box.firstChild?.classList.add('on');
}

function applyLang() {
  document.querySelectorAll('#lang button').forEach(b => b.classList.toggle('on', b.dataset.lang === state.lang));
  for (const g of groups.values()) {
    const t = g.el.querySelector('.gtitle');
    t.innerHTML = state.lang === 'en' ? g.meta.en : state.lang === 'zh' ? g.meta.zh : `${g.meta.zh}<small>${g.meta.en}</small>`;
  }
  for (const it of items.values()) {
    it.label.element.innerHTML = `<span class="dot"></span><span class="txt">${name(it.meta)}</span>`;
    const row = document.querySelector(`.item[data-k="${it.meta.k}"] .iname`);
    if (row) row.innerHTML = name(it.meta);
  }
  if (state.selected) showInfo(state.selected);
}

// ---------- 視角 ----------
function itemCenter(key) {
  const it = items.get(key);
  if (!it) return center.clone();
  return new THREE.Box3().setFromObject(it.mesh).getCenter(new THREE.Vector3());
}
function itemPoint(key, tpos) {
  const it = items.get(key);
  if (!it || !tpos) return itemCenter(key);
  const box = new THREE.Box3().setFromObject(it.mesh), c = box.getCenter(new THREE.Vector3());
  c.y = tpos === 'top' ? box.max.y : box.min.y;
  return c;
}
function viewDir(v) {
  if (v.from) return itemCenter(v.from).sub(itemCenter(v.target)).normalize();
  if (Array.isArray(v.dir)) return new THREE.Vector3(...v.dir).normalize();
  const lr = THREE.MathUtils.degToRad(v.dir.lr), cc = THREE.MathUtils.degToRad(v.dir.cc);
  // LAO = 由病人左前方看（+x 為病人左側），Cranial = 由頭側往下看
  return new THREE.Vector3(Math.sin(lr) * Math.cos(cc), Math.sin(cc), Math.cos(lr) * Math.cos(cc)).normalize();
}
let anim = null;
let viewAltered = false;
function applyView(v, instant = false) {
  // 視角可指定 hide（隱藏）或 solo（只顯示某些群組／構造）；切換到一般視角時復原
  if (v.hide || v.solo || viewAltered) {
    for (const it of items.values()) it.visible = !(v.hide || []).includes(it.meta.k);
    state.solo = v.solo ? new Set([...items.values()].filter(it => v.solo.includes(it.meta.k) || v.solo.includes(it.meta.g)).map(it => it.meta.k)) : null;
    viewAltered = !!(v.hide || v.solo);
    refresh();
  }
  const target = v.target ? itemPoint(v.target, v.tpos) : center.clone();
  const dir = viewDir(v);
  // span：畫面縱向要涵蓋的範圍 (mm)
  const dist = v.span ? v.span / 2 / Math.tan(THREE.MathUtils.degToRad(camera.fov / 2)) : fitDistance(dir);
  let up = new THREE.Vector3(...(v.up || [0, 1, 0]));
  if (v.upTo) up = itemCenter(v.upTo).sub(target).projectOnPlane(dir).normalize();
  const pos = target.clone().addScaledVector(dir, dist);
  moveCamera(pos, target, up, instant);
}
// 讓整個區域剛好放進畫面：依視線方向計算模型在畫面上的寬高
function fitDistance(dir) {
  const b = manifest.bbox, up = Math.abs(dir.y) > 0.9 ? new THREE.Vector3(0, 0, 1) : new THREE.Vector3(0, 1, 0);
  const right = new THREE.Vector3().crossVectors(up, dir).normalize(), up2 = new THREE.Vector3().crossVectors(dir, right);
  let w = 0, h = 0, d = 0;
  for (const x of [b.min[0], b.max[0]]) for (const y of [b.min[1], b.max[1]]) for (const z of [b.min[2], b.max[2]]) {
    const p = new THREE.Vector3(x, y, z);
    w = Math.max(w, Math.abs(p.dot(right))); h = Math.max(h, Math.abs(p.dot(up2))); d = Math.max(d, Math.abs(p.dot(dir)));
  }
  const t = Math.tan(THREE.MathUtils.degToRad(camera.fov / 2));
  return Math.max(h / t, w / (t * camera.aspect)) * 1.06 + d;
}
function moveCamera(pos, target, up, instant) {
  if (instant) {
    camera.position.copy(pos); camera.up.copy(up); controls.target.copy(target); controls.update();
    return;
  }
  const p0 = camera.position.clone(), t0 = controls.target.clone(), u0 = camera.up.clone();
  // 以球面插值移動，避免穿過模型
  const d0 = p0.clone().sub(t0), d1 = pos.clone().sub(target);
  const r0 = d0.length(), r1 = d1.length();
  const q0 = d0.normalize(), q1 = d1.normalize();
  const start = performance.now(), dur = 650;
  anim = now => {
    let s = Math.min(1, (now - start) / dur);
    s = s < 0.5 ? 2 * s * s : 1 - (-2 * s + 2) ** 2 / 2;
    const dir = slerpVec(q0, q1, s);
    const t = t0.clone().lerp(target, s);
    camera.up.copy(u0.clone().lerp(up, s).normalize());
    camera.position.copy(t).addScaledVector(dir, r0 + (r1 - r0) * s);
    controls.target.copy(t);
    if (s >= 1) { anim = null; occlusionDirty = true; }
  };
}
function slerpVec(a, b, s) {
  const dot = THREE.MathUtils.clamp(a.dot(b), -1, 1);
  if (dot > 0.9995) return a.clone().lerp(b, s).normalize();
  if (dot < -0.9995) {
    const axis = Math.abs(a.y) < 0.9 ? new THREE.Vector3(0, 1, 0) : new THREE.Vector3(1, 0, 0);
    return a.clone().applyAxisAngle(axis.cross(a).normalize(), Math.PI * s);
  }
  const th = Math.acos(dot) * s;
  const rel = b.clone().addScaledVector(a, -dot).normalize();
  return a.clone().multiplyScalar(Math.cos(th)).addScaledVector(rel, Math.sin(th));
}
function focusItem(key) {
  const it = items.get(key);
  const box = new THREE.Box3().setFromObject(it.mesh);
  const c = box.getCenter(new THREE.Vector3());
  const r = Math.max(box.getSize(new THREE.Vector3()).length() / 2, radius * 0.08);
  const dir = camera.position.clone().sub(controls.target).normalize();
  moveCamera(c.clone().addScaledVector(dir, r * 3.2), c, camera.up.clone(), false);
}

// ---------- 選取 ----------
function select(key) {
  state.selected = key;
  refresh();
  occlusionDirty = true;
  showInfo(key);
  document.querySelectorAll('.item').forEach(li => li.classList.toggle('sel', li.dataset.k === key));
}
function showInfo(key) {
  const it = items.get(key);
  if (!it) return;
  const g = groups.get(it.meta.g).meta;
  $('infoTitle').textContent = it.meta.zh;
  $('infoSub').textContent = `${it.meta.en}　·　${g.zh}`;
  $('infoNote').textContent = it.meta.note || '（尚無說明）';
  $('actFade').textContent = (it.opacity ?? 1) < 0.999 ? '不透明' : '半透明';
  $('info').hidden = false;
}
$('infoClose').onclick = () => { $('info').hidden = true; state.selected = null; refresh(); };
$('actFocus').onclick = () => state.selected && focusItem(state.selected);
$('actHide').onclick = () => {
  const it = items.get(state.selected); if (!it) return;
  it.visible = false; state.solo?.delete(it.meta.k); $('info').hidden = true; state.selected = null; refresh();
};
$('actFade').onclick = () => {
  const it = items.get(state.selected); if (!it) return;
  it.opacity = (it.opacity ?? groups.get(it.meta.g).opacity) < 0.999 ? 1 : 0.3; refresh(); showInfo(it.meta.k);
};
$('actSolo').onclick = () => { if (state.selected) { state.solo = new Set([state.selected]); refresh(); focusItem(state.selected); } };

// 點選：區分點擊與拖曳
const ray = new THREE.Raycaster(), ndc = new THREE.Vector2();
let down = null;
function pick(ev) {
  const r = renderer.domElement.getBoundingClientRect();
  ndc.set(((ev.clientX - r.left) / r.width) * 2 - 1, -((ev.clientY - r.top) / r.height) * 2 + 1);
  ray.setFromCamera(ndc, camera);
  const meshes = [...items.values()].filter(it => it.mesh.visible).map(it => it.mesh);
  const hits = ray.intersectObjects(meshes, false);
  // 優先選不透明的；全是半透明時選第一個
  const solid = hits.find(h => h.object.material.opacity >= 0.5);
  return (solid || hits[0])?.object.userData.key || null;
}
renderer.domElement.addEventListener('pointerdown', e => { down = [e.clientX, e.clientY]; });
renderer.domElement.addEventListener('pointerup', e => {
  if (!down || Math.hypot(e.clientX - down[0], e.clientY - down[1]) > 5) return;
  const k = pick(e);
  if (k) select(k); else { state.selected = null; $('info').hidden = true; refresh(); }
});
renderer.domElement.addEventListener('dblclick', e => { const k = pick(e); if (k) { select(k); focusItem(k); } });
const tip = document.createElement('div');
tip.className = 'tip'; stage.append(tip);
renderer.domElement.addEventListener('pointermove', e => {
  if (e.buttons) { tip.hidden = true; return; }
  const k = pick(e);
  renderer.domElement.style.cursor = k ? 'pointer' : 'grab';
  if (!k) { tip.hidden = true; return; }
  const r = stage.getBoundingClientRect();
  tip.hidden = false;
  tip.textContent = plainName(items.get(k).meta);
  tip.style.left = `${e.clientX - r.left + 14}px`;
  tip.style.top = `${e.clientY - r.top + 10}px`;
});
renderer.domElement.addEventListener('pointerleave', () => { tip.hidden = true; });

// ---------- 按鈕 ----------
$('btnLabels').onclick = () => { state.labels = !state.labels; refresh(); };
$('btnAllLabels').onclick = () => { state.allLabels = !state.allLabels; if (state.allLabels) state.labels = true; refresh(); };
$('btnXray').onclick = () => { state.xray = !state.xray; refresh(); };
$('btnIsolate').onclick = () => {
  if (state.solo) state.solo = null;
  else if (state.selected) state.solo = new Set([state.selected]);
  refresh();
};
$('btnShowAll').onclick = () => {
  state.solo = null;
  for (const g of groups.values()) g.visible = true;
  for (const it of items.values()) it.visible = true;
  refresh();
};
$('btnReset').onclick = () => {
  state.solo = null; state.xray = false; state.allLabels = false; state.labels = true;
  for (const g of groups.values()) { g.visible = !g.meta.hidden; g.opacity = g.meta.opacity ?? 1; g.el.querySelector('.gop').value = g.opacity; }
  for (const it of items.values()) { it.visible = true; it.opacity = it.meta.op ?? null; }
  state.selected = null; $('info').hidden = true;
  refresh();
  document.querySelectorAll('#views button').forEach((b, i) => b.classList.toggle('on', i === 0));
  applyView(manifest.views[0]);
};
$('btnFull').onclick = () => {
  if (document.fullscreenElement) document.exitFullscreen();
  else (stage.requestFullscreen || stage.webkitRequestFullscreen)?.call(stage);
};
$('btnPanel').onclick = () => document.body.classList.toggle('panel-open');
$('btnAbout').onclick = () => $('about').showModal();
document.querySelectorAll('#lang button').forEach(b => b.onclick = () => {
  state.lang = b.dataset.lang; localStorage.setItem('a3d-lang', state.lang); applyLang();
});
$('search').addEventListener('input', e => {
  const q = e.target.value.trim().toLowerCase();
  for (const g of groups.values()) {
    let any = false;
    g.el.querySelectorAll('.item').forEach(li => {
      const m = items.get(li.dataset.k).meta;
      const hit = !q || m.zh.toLowerCase().includes(q) || m.en.toLowerCase().includes(q) || m.k.includes(q);
      li.hidden = !hit; any ||= hit;
    });
    g.el.hidden = !any;
    const list = g.el.querySelector('.glist');
    if (q && any) list.hidden = false;
  }
});

// 截圖：把可見標籤畫進圖片
$('btnShot').onclick = () => {
  renderer.render(scene, camera);
  const src = renderer.domElement, dpr = renderer.getPixelRatio();
  const c = document.createElement('canvas');
  c.width = src.width; c.height = src.height;
  const ctx = c.getContext('2d');
  ctx.drawImage(src, 0, 0);
  ctx.font = `${13 * dpr}px "PingFang TC","Noto Sans TC",sans-serif`;
  ctx.textBaseline = 'middle';
  const w = stage.clientWidth, h = stage.clientHeight, v = new THREE.Vector3();
  for (const it of items.values()) {
    if (!it.label.visible) continue;
    it.label.getWorldPosition(v).project(camera);
    if (v.z > 1) continue;
    const x = (v.x + 1) / 2 * w * dpr, y = (1 - v.y) / 2 * h * dpr;
    const text = plainName(it.meta);
    const tw = ctx.measureText(text).width;
    ctx.fillStyle = '#222'; ctx.beginPath(); ctx.arc(x, y, 3 * dpr, 0, 7); ctx.fill();
    ctx.fillStyle = 'rgba(255,255,255,0.88)';
    ctx.fillRect(x + 6 * dpr, y - 10 * dpr, tw + 10 * dpr, 20 * dpr);
    ctx.fillStyle = '#222'; ctx.fillText(text, x + 11 * dpr, y);
  }
  const a = document.createElement('a');
  a.download = `${regionId}-${new Date().toISOString().slice(0, 10)}.png`;
  a.href = c.toDataURL('image/png');
  a.click();
};

// ---------- 方位指示 ----------
const AX = [
  { v: [1, 0, 0], a: '左 L', b: '右 R' },
  { v: [0, 1, 0], a: '頭 S', b: '足 I' },
  { v: [0, 0, 1], a: '前 A', b: '後 P' },
];
function drawGizmo() {
  const m = camera.matrixWorldInverse;
  const parts = [];
  for (const ax of AX) {
    const d = new THREE.Vector3(...ax.v).transformDirection(m);
    for (const [s, t] of [[1, ax.a], [-1, ax.b]]) {
      const x = d.x * 30 * s, y = -d.y * 30 * s;
      if (Math.abs(d.z) > 0.9) continue;
      parts.push({ z: d.z * s, svg: `<line x1="0" y1="0" x2="${x.toFixed(1)}" y2="${y.toFixed(1)}" class="${s > 0 ? 'pos' : 'neg'}"/><text x="${(x * 1.32).toFixed(1)}" y="${(y * 1.32).toFixed(1)}" class="${s > 0 ? 'pos' : 'neg'}">${t}</text>` });
    }
  }
  parts.sort((a, b) => a.z - b.z);
  $('gizmo').innerHTML = parts.map(p => p.svg).join('');
}

// ---------- 標籤遮擋 ----------
// 標籤錨點若被其他不透明構造擋住就先隱藏，旋轉停下後重新計算
let occlusionDirty = true, lastMove = 0;
controls.addEventListener('change', () => { occlusionDirty = true; lastMove = performance.now(); });
const occRay = new THREE.Raycaster(), wp = new THREE.Vector3();
function updateOcclusion() {
  const solids = [...items.values()].filter(it => it.mesh.visible && it.mesh.material.opacity >= 0.999).map(it => it.mesh);
  for (const it of items.values()) {
    if (!it.wantLabel) { it.occluded = false; continue; }
    it.label.getWorldPosition(wp);
    const d = wp.distanceTo(camera.position);
    occRay.set(camera.position, wp.clone().sub(camera.position).normalize());
    occRay.far = d - radius * 0.012;
    const hit = occRay.intersectObjects(solids, false).find(h => h.object !== it.mesh);
    it.occluded = !!hit && state.selected !== it.meta.k;
    it.label.visible = it.wantLabel && !it.occluded;
  }
}

// ---------- 迴圈 ----------
renderer.setAnimationLoop(now => {
  if (anim) anim(now);
  if (occlusionDirty && !anim && items.size && now - lastMove > 120) { occlusionDirty = false; updateOcclusion(); }
  controls.update();
  renderer.render(scene, camera);
  labelRenderer.render(scene, camera);
  drawGizmo();
});

load().catch(err => {
  $('loading').textContent = '載入失敗：' + err.message;
  console.error(err);
});
