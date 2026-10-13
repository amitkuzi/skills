/* loaded-monitor extras, appended to the design's script by web.ts:
   Info / Tutorial dialog, Logs tab (live stream polled from loaded-monitor-log.js), toast, CLI-command actions. */
var LOG = { updated: 0, totals: {}, ctx: null, limits: [], entries: [] };
state.detail = null;
state.paused = false;
var ICON_OF = { mod: '⚙', skill: '✦', agent: '☻', command: '⌘', mcp: '⇄', tool: '⚒', plugin: '❖' };
var KIND_TEXT = { run: 'Running', load: 'Loaded', err: 'Error', off: 'Disabled' };

function iconOf(k) { return String(k || 'plugin').split('+').map(function (x) { return ICON_OF[x] || '•'; }).join(''); }
function fmtN(n) { n = +n || 0; return n >= 1e6 ? (n / 1e6).toFixed(1) + 'M' : n >= 1e3 ? (n / 1e3).toFixed(1) + 'k' : String(n); }
function rowOf(key) { var m = /^(\D+)(\d+)$/.exec(key); return DATA[m[1]][+m[2]]; }

function toast(msg) {
  var t = document.getElementById('toast');
  if (!t) { t = document.createElement('div'); t.id = 'toast'; t.setAttribute('role', 'status'); document.body.appendChild(t); }
  t.textContent = msg; t.className = 'show';
  clearTimeout(toast.h); toast.h = setTimeout(function () { t.className = ''; }, 4500);
}

/* Settings / Remove copy the matching CLI command; Info / Tutorial open the dialog. */
function doAct(key, act) {
  var r = rowOf(key);
  if (act === 'Info' || act === 'Tutorial') { state.detail = { key: key, mode: act }; state.openMenu = null; render(); return; }
  var c = r.cmd && r.cmd[act];
  if (!c) { toast(r.n + ': no ' + act.toLowerCase() + ' action for built-in items.'); return; }
  if (navigator.clipboard) navigator.clipboard.writeText(c);
  toast('Copied. Paste in Claude Code: ' + c);
}

function tutorialFor(r) {
  var k = String(r.k || 'plugin').split('+'), steps = [], ex = '';
  if (k.indexOf('mcp') >= 0) {
    steps.push('Claude calls this server\'s tools itself when your request needs it.');
    steps.push('Name the service in the prompt so Claude picks it.');
    ex = 'Use ' + r.n + ' to ...';
  } else if (k.indexOf('skill') >= 0) {
    steps.push('Describe the task; Claude loads the skill when it matches.');
    steps.push('Or invoke it directly by typing /' + r.n + ' in the prompt.');
    ex = '/' + r.n;
  } else if (k.indexOf('agent') >= 0) {
    steps.push('Ask Claude to delegate to this agent.');
    ex = 'Use the ' + r.n + ' agent to ...';
  } else if (k.indexOf('command') >= 0) {
    steps.push('Type it in the prompt.');
    ex = '/' + r.n;
  } else if (k.indexOf('tool') >= 0) {
    steps.push('Claude calls this tool itself while working; you approve or deny it in the permission prompt.');
    ex = 'Ask for the result, e.g. "' + r.m + '"';
  } else if (k.indexOf('mod') >= 0) {
    steps.push('A mod changes Claude Code itself: panes, bands above the prompt, status line, slash commands.');
    steps.push('Open its README for the commands it adds.');
    ex = r.l ? 'README: ' + r.l : '/help';
  } else {
    steps.push('A plugin bundles skills, agents, commands or tools. Everything it adds appears in the other tabs.');
    ex = 'Check the Skills tab for what it adds';
  }
  return { steps: steps, ex: ex };
}

function dlgHtml() {
  if (!state.detail) return '';
  var r = rowOf(state.detail.key), info = state.detail.mode === 'Info';
  var head = '<div class="dh"><span class="dk">' + iconOf(r.k) + '</span><div><h3>' + esc(r.n) + '</h3><span class="dsub">' + esc(r.k || 'plugin') + ' · ' + esc(r.sc) + ' · ' + KIND_TEXT[r.s] + '</span></div><button class="icon-btn" data-x="1" aria-label="Close">✕</button></div>';
  var body = '';
  if (info) {
    var rows = [['Type', iconOf(r.k) + ' ' + (r.k || 'plugin')], ['Origin', r.sc === 'DEV' ? 'DEV (made by you)' : r.sc === 'WEB' ? 'WEB (installed from outside)' : 'CORE (built-in)'], ['Status', KIND_TEXT[r.s]]];
    if (r.v) rows.push(['Version', r.v]);
    if (r.id && r.id !== r.n) rows.push(['Id', r.id]);
    var dl = rows.map(function (x) { return '<dt>' + esc(x[0]) + '</dt><dd>' + esc(x[1]) + '</dd>'; }).join('');
    if (r.l) dl += '<dt>Source</dt><dd><a href="' + esc(r.l) + '" target="_blank" rel="noopener">' + esc(r.l) + '</a></dd>';
    body = '<dl>' + dl + '</dl>' + (r.d ? '<p class="dd">' + esc(r.d) + '</p>' : '');
    if (r.tools && r.tools.length) body += '<h4>Provides ' + r.tools.length + ' tools</h4><p class="chips2">' + r.tools.slice(0, 40).map(function (t) { return '<code>' + esc(t) + '</code>'; }).join(' ') + (r.tools.length > 40 ? ' …' : '') + '</p>';
  } else {
    var t = tutorialFor(r);
    body = (r.d ? '<h4>What it is</h4><p class="dd">' + esc(r.d) + '</p>' : '') +
      '<h4>How to use it</h4><ol>' + t.steps.map(function (s) { return '<li>' + esc(s) + '</li>'; }).join('') + '</ol>' +
      '<h4>Try</h4><pre>' + esc(t.ex) + '</pre>' +
      (r.tools && r.tools.length ? '<h4>Example tools</h4><p class="chips2">' + r.tools.slice(0, 8).map(function (x) { return '<code>' + esc(x) + '</code>'; }).join(' ') + '</p>' : '');
  }
  return '<div class="dlg-box" role="dialog" aria-modal="true" aria-label="' + esc(r.n) + '">' + head + body + '</div>';
}

function logsHtml() {
  var t = LOG.totals || {}, lim = (LOG.limits || []).map(function (l) { return '<span class="card"><b>' + Math.round(l.percentUsed) + '%</b>' + esc(l.kind) + '</span>'; }).join('');
  var ctx = LOG.ctx && LOG.ctx.percent != null ? '<span class="card"><b>' + Math.round(LOG.ctx.percent) + '%</b>context</span>' : '';
  var cards = '<li class="logsum">' +
    '<span class="card"><b>' + fmtN(t.calls) + '</b>tool calls</span>' +
    '<span class="card' + (t.errors ? ' bad' : '') + '"><b>' + fmtN(t.errors) + '</b>errors</span>' +
    '<span class="card"><b>' + fmtN(t.steps) + '</b>model steps</span>' +
    '<span class="card"><b>' + fmtN(t.input) + '</b>in tokens</span>' +
    '<span class="card"><b>' + fmtN(t.output) + '</b>out tokens</span>' +
    '<span class="card"><b>' + fmtN(t.cacheRead) + '</b>cache read</span>' + ctx + lim + '</li>' +
    '<li class="logbar"><button class="chip" data-lp="1" aria-pressed="' + state.paused + '">' + (state.paused ? 'Resume' : 'Pause') + ' stream</button>' +
    '<button class="chip" data-lc="1">Copy debug report</button>' +
    '<span class="lu">' + (LOG.updated ? 'updated ' + new Date(LOG.updated).toLocaleTimeString() : 'waiting for events…') + '</span></li>';
  var es = (LOG.entries || []).slice(-200).reverse();
  if (!es.length) return cards + '<li class="row"><span></span><span class="meta">No events yet. Tool calls, model steps and turns appear here as they happen.</span></li>';
  return cards + es.map(function (e) {
    var cls = e.ok === false ? 'bad' : '';
    return '<li class="logrow ' + cls + '"><span class="lt">' + new Date(e.t).toLocaleTimeString() + '</span><span class="lk">' + esc(e.k) + '</span><span class="ln">' + esc(e.n) + '</span><span class="lm">' + (e.ms != null ? e.ms + ' ms' : '') + (e.tok ? ' · ' + esc(e.tok) : '') + '</span>' + (e.note ? '<span class="lx">' + esc(e.note) + '</span>' : '') + '</li>';
  }).join('');
}

function render() {
  var list = document.getElementById('list'), top = list ? list.scrollTop : 0;
  render0();
  var logs = state.tab === 'Logs';
  document.querySelector('.p-tools').style.display = logs ? 'none' : '';
  var n = document.querySelector('.tab[data-t="Logs"] .n');
  if (n) n.textContent = (LOG.entries || []).length;
  if (logs) { list.innerHTML = logsHtml(); list.scrollTop = top; }
  var d = document.getElementById('dlg');
  if (!d) { d = document.createElement('div'); d.id = 'dlg'; document.body.appendChild(d); }
  d.innerHTML = dlgHtml();
  d.className = state.detail ? 'open' : '';
}

document.addEventListener('click', function (e) {
  if (e.target.closest('[data-x]') || e.target.id === 'dlg') { state.detail = null; render(); }
  else if (e.target.closest('[data-lp]')) { state.paused = !state.paused; render(); }
  else if (e.target.closest('[data-lc]')) { if (navigator.clipboard) navigator.clipboard.writeText(JSON.stringify(LOG, null, 2)); toast('Debug report copied (' + (LOG.entries || []).length + ' events).'); }
});
document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && state.detail) { state.detail = null; render(); } });

function pollLog() {
  if (state.paused) return;
  var s = document.createElement('script');
  s.src = 'loaded-monitor-log.js?t=' + Date.now();
  s.onload = function () { s.remove(); if (window.__LOADED_LOG) { LOG = window.__LOADED_LOG; if (state.tab === 'Logs') render(); } };
  s.onerror = function () { s.remove(); };
  document.head.appendChild(s);
}
setInterval(pollLog, 2000);
pollLog();
