// Turns design/loaded-panel.html (the approved UI) into a live page: the sample DATA is replaced by the
// session's real items, the spec column is dropped, and design/panel-extra.{js,css} add the Info / Tutorial
// dialog, the Logs tab (live stream) and the CLI-command actions.
export type Row = {
  g: string
  n: string
  m: string
  s: 'run' | 'load' | 'err' | 'off'
  sc: string
  i?: string
  l?: string
  k?: string
  d?: string
  v?: string
  id?: string
  tools?: string[]
  cmd?: Record<string, string>
}

export function buildHtml(template: string, data: Record<string, Row[]>, extraJs = '', extraCss = ''): string {
  const json = JSON.stringify({ ...data, Logs: [] }).replace(/</g, '\\u003c')
  let h = template
  // The design is an artifact fragment; opened as a file it needs its own doctype, charset and viewport.
  if (!/<!doctype/i.test(h)) h = `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body>\n${h}\n</body></html>`
  h = h.replace(/var DATA = \{[\s\S]*?\r?\n\};/, `var DATA = ${json};`)
  h = h.replace(/<aside class="spec">[\s\S]*?<\/aside>/, '')
  h = h.replace('</style>', `${extraCss}\n</style>`)
  // The original render() becomes render0(); panel-extra.js defines the render() that wraps it.
  h = h.replace('function render(){', 'function render0(){')
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
  h = h.replace("state.openMenu = 'Plugins3';", `state.openMenu = null;\n${extraJs}\n`)
  return h
}
