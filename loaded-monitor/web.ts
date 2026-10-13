// Turns design/loaded-panel.html (the approved UI) into a live page: the sample DATA is replaced by the
// session's real items, the spec column is dropped, and the menu actions copy the matching CLI command.
export type Row = {
  g: string
  n: string
  m: string
  s: 'run' | 'load' | 'err' | 'off'
  sc: string
  i?: string
  l?: string
  cmd?: Record<string, string>
}

const ROW_HELPERS = `
function rowOf(key){ var m=/^(\\D+)(\\d+)$/.exec(key); return DATA[m[1]][+m[2]]; }
function doAct(key, act){
  var r = rowOf(key), c = r.cmd && r.cmd[act];
  var msg = act === 'Info' ? r.n + ' · ' + r.sc + ' · ' + r.m + (r.l ? '\\n' + r.l : '')
    : act === 'Tutorial' ? 'Ask Claude: "how do I use ' + r.n + '?"'
    : c ? 'Copied. Paste this in Claude Code:\\n' + c : 'No action for built-in items.';
  if (c && act !== 'Info' && navigator.clipboard) navigator.clipboard.writeText(c);
  alert(msg);
}
`

export function buildHtml(template: string, data: Record<string, Row[]>): string {
  const json = JSON.stringify(data).replace(/</g, '\\u003c')
  let h = template
  h = h.replace(/var DATA = \{[\s\S]*?\r?\n\};/, `var DATA = ${json};`)
  h = h.replace(/<aside class="spec">[\s\S]*?<\/aside>/, '')
  h = h.replace('</style>', '.board{grid-template-columns:minmax(0,520px)!important}</style>')
  h = h.replace('function render(){', `${ROW_HELPERS}\nfunction render(){`)
  h = h.replace(
    `'<span><span class="name">'+esc(r.n)+'</span>`,
    `'<span><span class="name">'+(r.l?'<a href="'+esc(r.l)+'" target="_blank" rel="noopener" style="color:inherit">'+esc(r.n)+' ↗</a>':esc(r.n))+'</span>`,
  )
  h = h.replace(
    "else if (act === 'ok') { state.removed[state.confirm] = true; state.confirm = null; }",
    "else if (act === 'ok') { doAct(state.confirm, 'Remove'); state.confirm = null; }",
  )
  h = h.replace(
    /else \{ state\.openMenu = null; \}(\r?\n\s*\})/,
    'else { var k0 = state.openMenu; state.openMenu = null; doAct(k0, act); }$1',
  )
  h = h.replace("state.openMenu = 'Plugins3';", "state.openMenu = null;")
  return h
}
