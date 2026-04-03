/* PathFinder VJTI — Gauge & Animation JavaScript */
'use strict';

/* ════════════════════════════════════════
   RADIAL GAUGE (Canvas-based)
   ════════════════════════════════════════ */
function drawGauge(canvasId, score, color) {
  const canvas = document.getElementById(canvasId);
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  const W = canvas.width  = 200;
  const H = canvas.height = 200;
  const cx = W / 2, cy = H / 2, r = 80;

  // Color by score
  let fillColor;
  if (score >= 75)      fillColor = '#a78bfa';   // purple — excellent
  else if (score >= 55) fillColor = '#22d3ee';   // cyan   — on track
  else if (score >= 35) fillColor = '#facc15';   // yellow — warning
  else                  fillColor = '#f87171';   // red    — danger

  if (color) fillColor = color;  // override if explicitly passed

  const startAngle = Math.PI * 0.75;           // 7 o'clock
  const endAngle   = Math.PI * 2.25;           // 5 o'clock
  const range      = endAngle - startAngle;
  const sweepAngle = (score / 100) * range;

  ctx.clearRect(0, 0, W, H);

  // Track ring
  ctx.beginPath();
  ctx.arc(cx, cy, r, startAngle, endAngle);
  ctx.strokeStyle = 'rgba(255,255,255,0.08)';
  ctx.lineWidth = 14;
  ctx.lineCap = 'round';
  ctx.stroke();

  // Glow behind fill
  ctx.save();
  ctx.shadowColor = fillColor;
  ctx.shadowBlur  = 22;

  // Filled arc
  ctx.beginPath();
  ctx.arc(cx, cy, r, startAngle, startAngle + sweepAngle);
  ctx.strokeStyle = fillColor;
  ctx.lineWidth   = 14;
  ctx.lineCap     = 'round';
  ctx.stroke();
  ctx.restore();

  // Tick marks
  for (let i = 0; i <= 10; i++) {
    const angle = startAngle + (i / 10) * range;
    const inner = r - 20, outer = r - 10;
    ctx.beginPath();
    ctx.moveTo(cx + inner * Math.cos(angle), cy + inner * Math.sin(angle));
    ctx.lineTo(cx + outer * Math.cos(angle), cy + outer * Math.sin(angle));
    ctx.strokeStyle = 'rgba(255,255,255,0.18)';
    ctx.lineWidth = 1.5;
    ctx.stroke();
  }

  // Needle dot at tip
  const tipX = cx + r * Math.cos(startAngle + sweepAngle);
  const tipY = cy + r * Math.sin(startAngle + sweepAngle);
  ctx.beginPath();
  ctx.arc(tipX, tipY, 5, 0, Math.PI * 2);
  ctx.fillStyle = fillColor;
  ctx.shadowColor = fillColor;
  ctx.shadowBlur = 14;
  ctx.fill();
}

/* ════════════════════════════════════════
   ANIMATED NUMBER COUNT-UP
   ════════════════════════════════════════ */
function animateCount(el, target, duration = 1400) {
  let start = null;
  const from = 0;

  function step(ts) {
    if (!start) start = ts;
    const progress = Math.min((ts - start) / duration, 1);
    const eased    = 1 - Math.pow(1 - progress, 3);   // ease-out-cubic
    el.textContent = Math.round(from + (target - from) * eased);
    if (progress < 1) requestAnimationFrame(step);
  }
  requestAnimationFrame(step);
}

/* ════════════════════════════════════════
   PROGRESS BAR ANIMATION
   ════════════════════════════════════════ */
function animateBars() {
  document.querySelectorAll('.bar-fill[data-width]').forEach(bar => {
    setTimeout(() => {
      bar.style.width = bar.dataset.width + '%';
    }, 200);
  });
  document.querySelectorAll('.leader-bar-fill[data-width]').forEach(bar => {
    setTimeout(() => {
      bar.style.width = bar.dataset.width + '%';
    }, 400);
  });
}

/* ════════════════════════════════════════
   INIT on DOM ready
   ════════════════════════════════════════ */
document.addEventListener('DOMContentLoaded', () => {

  /* — Gauge — */
  const gaugeCanvas = document.getElementById('gaugeCanvas');
  if (gaugeCanvas) {
    const score = parseInt(gaugeCanvas.dataset.score, 10) || 0;
    drawGauge('gaugeCanvas', score);

    /* Animate score number */
    const scoreEl = document.getElementById('gaugeScore');
    if (scoreEl) animateCount(scoreEl, score, 1600);
  }

  /* — Animated bars — */
  animateBars();

  /* ── Form: interest card click also updates hidden-radio visually ── */
  document.querySelectorAll('.interest-card').forEach(card => {
    card.addEventListener('click', () => {
      card.querySelector('input[type="radio"]').checked = true;
    });
  });

  /* ── Form spinner on submit ── */
  const form = document.getElementById('profileForm');
  if (form) {
    form.addEventListener('submit', () => {
      const btn = form.querySelector('.btn-submit');
      if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<span class="spinner"></span> Analyzing…';
      }
    });
  }

  /* ── Scroll-reveal: cards fade in when they enter viewport ── */
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('visible');
        observer.unobserve(e.target);
      }
    });
  }, { threshold: 0.08 });

  document.querySelectorAll('.roadmap-item').forEach(el => observer.observe(el));

  /* ── Kick off live preview (index page only) ── */
  initLivePreview();
});

/* ════════════════════════════════════════
   LIVE SCORING ENGINE
   Exact JS port of career_logic_engine.py
   ════════════════════════════════════════ */

const NORM_JS = { leetcode: 700, cf_rating: 2400, github: 20, projects: 5, flutter: 4 };

const WEIGHTS_JS = {
  AppDev: { leetcode: 0.20, cf_rating: 0.05, github_repos: 0.10, projects: 0.35, flutter_bonus: 0.30 },
  WebDev: { leetcode: 0.20, cf_rating: 0.05, github_repos: 0.30, projects: 0.40, flutter_bonus: 0.05 },
  CP:     { leetcode: 0.20, cf_rating: 0.70, github_repos: 0.05, projects: 0.05, flutter_bonus: 0.00 },
  AI:     { leetcode: 0.25, cf_rating: 0.05, github_repos: 0.20, projects: 0.50, flutter_bonus: 0.00 },
};

const STATE_RULES_JS = [
  { test: p => p.year <= 2 && p.lc >= 350 && p.proj === 0,
    state: 'ProjectRequired', color: 'warning',   emoji: '⚠️' },
  { test: p => p.interest === 'AppDev' && p.flutter > 0 && p.lc >= 100,
    state: 'Ready',           color: 'success',   emoji: '✅' },
  { test: p => p.interest === 'CP'     && p.cf >= 1600,
    state: 'Excellent',       color: 'excellent', emoji: '🏆' },
  { test: p => p.interest === 'CP'     && p.cf >= 1200 && p.lc >= 200,
    state: 'OnTrack',         color: 'info',      emoji: '📈' },
  { test: p => p.interest === 'WebDev' && p.proj >= 1 && p.gh >= 5,
    state: 'Ready',           color: 'success',   emoji: '✅' },
  { test: p => p.interest === 'AI'     && p.proj >= 1 && p.lc >= 150,
    state: 'Ready',           color: 'success',   emoji: '✅' },
  { test: p => p.proj === 0,
    state: 'ProjectRequired', color: 'warning',   emoji: '🚧' },
];

const COLOR_MAP = {
  success:   ['rgba(74,222,128,.15)',  'rgba(74,222,128,.35)',  '#4ade80'],
  warning:   ['rgba(250,204,21,.15)',  'rgba(250,204,21,.40)',  '#facc15'],
  excellent: ['rgba(139,92,246,.20)',  'rgba(139,92,246,.50)',  '#a78bfa'],
  info:      ['rgba(6,182,212,.15)',   'rgba(6,182,212,.40)',   '#22d3ee'],
  danger:    ['rgba(248,113,113,.12)', 'rgba(248,113,113,.35)', '#f87171'],
};

function normJS(v, ceil) { return Math.min(v / ceil, 1); }

function calcScoreJS(lc, cf, gh, proj, flutter, interest) {
  const w = WEIGHTS_JS[interest] || WEIGHTS_JS.AppDev;
  const comps = {
    LeetCode:   normJS(lc,      NORM_JS.leetcode)  * w.leetcode      * 100,
    CF_Rating:  normJS(cf,      NORM_JS.cf_rating) * w.cf_rating     * 100,
    GitHub:     normJS(gh,      NORM_JS.github)    * w.github_repos  * 100,
    Projects:   normJS(proj,    NORM_JS.projects)  * w.projects      * 100,
    Flutter:    normJS(flutter, NORM_JS.flutter)   * w.flutter_bonus * 100,
  };
  const total = Math.min(Object.values(comps).reduce((a,b) => a+b, 0), 100);
  return { total: Math.round(total * 10) / 10, comps };
}

function diagnoseStateJS(lc, cf, gh, proj, flutter, interest, year, score) {
  const p = { lc, cf, gh, proj, flutter, interest, year };
  for (const rule of STATE_RULES_JS) {
    if (rule.test(p)) return rule;
  }
  if (score >= 75) return { state: 'Excellent', color: 'excellent', emoji: '🏆' };
  if (score >= 55) return { state: 'OnTrack',   color: 'info',      emoji: '📈' };
  return              { state: 'SkillGap',    color: 'danger',    emoji: '🔧' };
}

function drawMiniGauge(canvas, score) {
  const ctx = canvas.getContext('2d');
  const W = canvas.width = 120, H = canvas.height = 120;
  const cx = W/2, cy = H/2, r = 46;
  const fill = score >= 75 ? '#a78bfa' : score >= 55 ? '#22d3ee' : score >= 35 ? '#facc15' : '#f87171';
  const sa = Math.PI * 0.75, ea = Math.PI * 2.25, range = ea - sa;
  ctx.clearRect(0,0,W,H);
  ctx.beginPath(); ctx.arc(cx,cy,r,sa,ea);
  ctx.strokeStyle='rgba(255,255,255,0.08)'; ctx.lineWidth=10; ctx.lineCap='round'; ctx.stroke();
  ctx.save(); ctx.shadowColor=fill; ctx.shadowBlur=16;
  ctx.beginPath(); ctx.arc(cx,cy,r,sa,sa+(score/100)*range);
  ctx.strokeStyle=fill; ctx.lineWidth=10; ctx.lineCap='round'; ctx.stroke();
  ctx.restore();
  // tip dot
  const tipAngle = sa + (score/100)*range;
  ctx.beginPath(); ctx.arc(cx+r*Math.cos(tipAngle), cy+r*Math.sin(tipAngle), 4, 0, Math.PI*2);
  ctx.fillStyle=fill; ctx.shadowColor=fill; ctx.shadowBlur=12; ctx.fill();
}

/* ════════════════════════════════════════
   LIVE PREVIEW WIDGET (injected into form)
   ════════════════════════════════════════ */
function initLivePreview() {
  const form = document.getElementById('profileForm');
  if (!form) return;   // only on index page

  const previewHTML = `
<div id="livePreview" style="
  margin-bottom:1.5rem;
  background:linear-gradient(135deg,rgba(139,92,246,.10),rgba(6,182,212,.07));
  border:1px solid rgba(139,92,246,.28);
  border-radius:16px;
  padding:1.4rem 1.6rem;
  display:flex;
  align-items:center;
  gap:1.8rem;
  flex-wrap:wrap;
  transition:border-color .3s;
">
  <!-- Mini gauge -->
  <div style="position:relative;width:120px;height:120px;flex-shrink:0;">
    <canvas id="liveGaugeCanvas" width="120" height="120"></canvas>
    <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;pointer-events:none;">
      <span id="liveScore" style="font-size:1.9rem;font-weight:900;background:linear-gradient(135deg,#8b5cf6,#06b6d4);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;transition:all .2s;">0</span>
      <span style="font-size:.6rem;color:#475569;letter-spacing:.1em;text-transform:uppercase;font-weight:700;">/100</span>
    </div>
  </div>

  <!-- Right: state + bars -->
  <div style="flex:1;min-width:210px;">
    <div style="display:flex;align-items:center;gap:.6rem;margin-bottom:.9rem;flex-wrap:wrap;">
      <span id="liveEmoji" style="font-size:1.1rem;">🔧</span>
      <span id="liveState" style="font-size:.8rem;font-weight:700;padding:.22rem .75rem;border-radius:999px;border:1px solid;transition:all .3s;">SkillGap</span>
      <span style="font-size:.68rem;color:#475569;font-weight:700;letter-spacing:.08em;text-transform:uppercase;">Live Preview</span>
    </div>
    <div style="display:flex;flex-direction:column;gap:.38rem;">
      ${[['LeetCode','LeetCode'],['CF_Rating','CF Rating'],['GitHub','GitHub'],['Projects','Projects'],['Flutter','Flutter']].map(([id,label]) => `
      <div style="display:flex;align-items:center;gap:.55rem;">
        <span style="font-size:.68rem;color:#64748b;min-width:66px;font-weight:600;">${label}</span>
        <div style="flex:1;height:4px;background:rgba(255,255,255,.07);border-radius:999px;overflow:hidden;">
          <div id="liveBar_${id}" style="height:100%;width:0%;background:linear-gradient(90deg,#8b5cf6,#06b6d4);border-radius:999px;transition:width .35s cubic-bezier(.4,0,.2,1);"></div>
        </div>
        <span id="liveVal_${id}" style="font-size:.7rem;color:#8b5cf6;min-width:30px;text-align:right;font-family:monospace;font-weight:600;">0.0</span>
      </div>`).join('')}
    </div>
  </div>
</div>`;

  // Inject before the Stats section (3rd .form-section)
  const sections = form.querySelectorAll('.form-section');
  if (sections[2]) {
    sections[2].insertAdjacentHTML('beforebegin', previewHTML);
  } else {
    // fallback: prepend inside form
    form.querySelector('.form-section').insertAdjacentHTML('beforebegin', previewHTML);
  }

  function readForm() {
    const interest = (form.querySelector('input[name="interest"]:checked') || {}).value || 'AppDev';
    const lc       = parseInt(form.querySelector('#leetcode').value)         || 0;
    const cf       = parseInt(form.querySelector('#cf_rating').value)        || 0;
    const gh       = parseInt(form.querySelector('#github_repos').value)     || 0;
    const flutter  = parseInt(form.querySelector('#flutter_projects').value) || 0;
    const projRaw  = (form.querySelector('#projects').value || '');
    const proj     = projRaw.split(',').filter(p => p.trim().length > 0).length;
    const year     = parseInt(form.querySelector('#year').value) || 2;
    return { interest, lc, cf, gh, proj, flutter, year };
  }

  function updatePreview() {
    const { interest, lc, cf, gh, proj, flutter, year } = readForm();
    const { total, comps } = calcScoreJS(lc, cf, gh, proj, flutter, interest);
    const diag = diagnoseStateJS(lc, cf, gh, proj, flutter, interest, year, total);

    // Score
    document.getElementById('liveScore').textContent = total.toFixed(1);

    // Gauge redraw
    drawMiniGauge(document.getElementById('liveGaugeCanvas'), total);

    // State badge
    const stateEl = document.getElementById('liveState');
    document.getElementById('liveEmoji').textContent = diag.emoji;
    stateEl.textContent = diag.state;
    const [bg, border, color] = COLOR_MAP[diag.color] || COLOR_MAP.danger;
    stateEl.style.background = bg;
    stateEl.style.borderColor = border;
    stateEl.style.color = color;

    // Bars
    const barMap = [
      ['LeetCode',  comps.LeetCode],
      ['CF_Rating', comps.CF_Rating],
      ['GitHub',    comps.GitHub],
      ['Projects',  comps.Projects],
      ['Flutter',   comps.Flutter],
    ];
    barMap.forEach(([id, val]) => {
      const b = document.getElementById('liveBar_' + id);
      const v = document.getElementById('liveVal_' + id);
      if (b) b.style.width = Math.min((val / 30) * 100, 100) + '%';
      if (v) v.textContent = (val || 0).toFixed(1);
    });
  }

  // Wire all form inputs
  ['leetcode','cf_rating','github_repos','flutter_projects','year'].forEach(id => {
    const el = document.getElementById(id);
    if (el) el.addEventListener('input', updatePreview);
  });
  const projEl = document.getElementById('projects');
  if (projEl) projEl.addEventListener('input', updatePreview);
  form.querySelectorAll('input[name="interest"]').forEach(r => r.addEventListener('change', updatePreview));

  // Initial render with defaults
  updatePreview();
}

