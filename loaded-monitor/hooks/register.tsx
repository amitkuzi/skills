import { atom, read, update } from 'claude-code'
import type { Register } from 'claude-code'

import type { Snapshot, Item, Origin } from '../types'
import own from '../own'

const PANE = 'loaded-monitor'
const isOpen = atom({ plugin: 'loaded-monitor', key: 'isOpen' } as const, false)
const paneOpen = atom({ plugin: 'loaded-monitor', key: 'paneOpen' } as const, false)
const tab = atom({ plugin: 'loaded-monitor', key: 'tab' } as const, 'plugins')
const confirm = atom({ plugin: 'loaded-monitor', key: 'confirm' } as const, null)
const snap = atom({ plugin: 'loaded-monitor', key: 'snap' } as const, null)

// Amit Kuzi brand kit (dark variant, from design/loaded-panel.html)
const BRAND = { ember: '#E4632D', brass: '#C9A227', fg: '#F4EFE7', fg2: '#B5A797', line: '#3A332C', ok: '#6FCB93', err: '#F2877F', idle: '#A99C8B' }
// One single-width glyph per item type (terminal-safe, no emoji font needed).
const ICON: Record<string, string> = { mod: '⚙', skill: '✦', agent: '☻', command: '⌘', mcp: '⇄', tool: '⚒', plugin: '❖' }
const iconOf = (kind: string) => kind.split('+').map(k => ICON[k] ?? '•').join('')
const REPO = 'https://github.com/amitkuzi/skills'

type Meta = { kind: string; desc?: string; link?: string }

const jsonAt = async ($: any, path: string): Promise<any> => {
  try { return JSON.parse(await $.fs.read(path)) } catch { return null }
}

// Type + description + link per installed plugin, read from its folder in the plugin cache.
async function pluginMeta($: any): Promise<Record<string, Meta>> {
  const home = (await $.env.get('USERPROFILE')) ?? (await $.env.get('HOME'))
  if (!home) return {}
  const base = `${home}/.claude/plugins`
  const installed = await jsonAt($, `${base}/installed_plugins.json`)
  const markets = (await jsonAt($, `${base}/known_marketplaces.json`)) ?? {}
  const out: Record<string, Meta> = {}
  for (const [name, entries] of Object.entries<any>(installed?.plugins ?? installed ?? {})) {
    const dir = entries?.[0]?.installPath?.split('\\').join('/')
    if (!dir) continue
    const man = (await jsonAt($, `${dir}/.claude-plugin/plugin.json`)) ?? {}
    const hooks = await jsonAt($, `${dir}/hooks/hooks.json`)
    const has = async (rel: string) => { try { return await $.fs.exists(`${dir}/${rel}`) } catch { return false } }
    const kinds = [
      hooks?.modules ? 'mod' : '',
      (await has('skills')) ? 'skill' : '',
      (await has('agents')) ? 'agent' : '',
      (await has('commands')) ? 'command' : '',
      (await has('.mcp.json')) || man.mcpServers ? 'mcp' : '',
    ].filter(Boolean)
    const [baseName = '', market = ''] = name.split('@')
    const repo = typeof man.repository === 'string' ? man.repository : man.repository?.url
    const m = markets[market]?.source
    const link =
      man.homepage || repo ||
      (own.marketplaces.includes(market) ? `${REPO}/tree/master/${baseName}` : undefined) ||
      (m?.repo ? `https://github.com/${m.repo}` : m?.url?.replace('.git', ''))
    out[name] = { kind: kinds.join('+') || 'plugin', desc: man.description, link }
  }
  return out
}

const uniq = (xs: string[]) => [...new Set(xs)].sort()

// Origin: mine = listed in own.json (by name or marketplace); builtin = Claude Code core; else installed.
const originOf = (name: string, builtin = false): Origin => {
  const [base = '', market] = name.split('@')
  if (own.names.includes(base) || (market && own.marketplaces.includes(market))) return 'mine'
  return builtin ? 'builtin' : 'installed'
}
const items = (xs: string[], builtin = false, off: string[] = [], kind = '', meta: Record<string, Meta> = {}): Item[] =>
  uniq(xs).map(name => ({
    name, origin: originOf(name, builtin), status: off.includes(name) ? 'disabled' : 'loaded',
    kind: meta[name]?.kind ?? kind, desc: meta[name]?.desc, link: meta[name]?.link,
  }))

async function collect($: any): Promise<Snapshot> {
    const tools = await $.tool.list()
    const cmds = await $.command.list()
    const agents = await $.agent.list()
    const settings = await $.settings.read()
    const enabled = (settings.enabledPlugins ?? {}) as Record<string, boolean>
    const byServer = new Map<string, number>()
    for (const t of tools) {
      if (!t.mcp) continue
      const server = t.name.split('__')[1] ?? t.name
      byServer.set(server, (byServer.get(server) ?? 0) + 1)
    }
    const meta = await pluginMeta($)
    return {
      plugins: items([
        ...Object.keys(enabled),
        ...cmds.flatMap((c: any) => (c.plugin ? [c.plugin] : [])),
      ], false, Object.keys(enabled).filter(k => !enabled[k]), 'plugin', meta),
      skills: items(cmds.filter((c: any) => c.source === 'plugin' || c.source === 'user').map((c: any) => c.name), false, [], 'skill'),
      commands: items(cmds.filter((c: any) => c.source === 'builtin').map((c: any) => c.name), true, [], 'command'),
      tools: items(tools.filter((t: any) => !t.mcp).map((t: any) => t.name), true, [], 'tool'),
      mcp: [...byServer].map(([server, n]) => ({ server, tools: n, origin: originOf(server), status: 'running' })),
      agents: items(agents.map((a: any) => a.id), false, [], 'agent'),
    }
}

async function refresh($: any) {
  const fresh = await collect($)
  await update($, snap, () => fresh)
}

// One toggle for the band button, /loaded and hotkey: docked pane on the right, inline panel as fallback.
async function toggleView($: any): Promise<string> {
  if ((await read($, paneOpen)) || (await read($, isOpen))) {
    await close($)
    return 'closed'
  }
  await refresh($)
  const r = await $.ui.open({ id: PANE, title: 'Loaded', columns: 64 })
  if (r.isPlaced) {
    await update($, paneOpen, () => true)
    return 'pane'
  }
  await update($, isOpen, () => true)
  return 'inline'
}

async function close($: any) {
  await update($, isOpen, () => false)
  if (await read($, paneOpen)) {
    await update($, paneOpen, () => false)
    await $.ui.close({ id: PANE })
  }
}

const TABS = ['plugins', 'skills', 'tools', 'mcp', 'agents'] as const
const TITLE: Record<string, string> = { plugins: 'Plugins', skills: 'Skills', tools: 'Tools', mcp: 'MCP', agents: 'Agents' }

const rowsOf = (s: Snapshot, t: string): Item[] =>
  t === 'mcp' ? s.mcp.map(m => ({ name: m.server, origin: m.origin, status: m.status, kind: 'mcp', note: `${m.tools} tools` })) : (s[t as 'plugins'] as Item[])

async function act($: any, it: Item, kind: string, choice: string) {
  if (choice === 'info') {
    // Full details as a toast: name, type, origin, status, description, link (link only where one exists).
    const origin = it.origin === 'mine' ? 'DEV (made by you)' : it.origin === 'installed' ? 'WEB (installed from outside)' : 'CORE (built-in)'
    $.ui.toast([
      `${iconOf(it.kind || 'plugin')} ${it.name} · ${it.kind || 'item'}`,
      `${origin} · ${it.status}${it.note ? ' · ' + it.note : ''}`,
      it.desc,
      it.link ? `↗ ${it.link}` : undefined,
    ].filter(Boolean).join('\n'))
  } else if (choice === 'settings') {
    $.ui.toast(kind === 'plugins' ? `${it.name}: edit enabledPlugins in ~/.claude/settings.json` : `${it.name}: no settings for built-in items`)
  } else if (choice === 'remove') {
    await update($, confirm, () => it.name)
  } else if (choice === 'enable' || choice === 'disable' || choice === 'update') {
    $.ui.toast(`${choice} ${it.name}...`)
    const r = await $.process.run(['claude', 'plugin', choice, it.name], { timeoutMs: 120000 })
    $.ui.toast(r.exitCode === 0 ? `${it.name}: ${choice} done. Use Reload to apply.` : `${choice} failed: ${(r.stderr || r.stdout).slice(0, 120)}`)
    await refresh($)
  } else if (choice === 'reload') {
    await reload($)
  }
}

async function reload($: any) {
  try {
    await $.command.run({ name: 'reload-plugins' })
    $.ui.toast('Plugins reloaded.')
  } catch {
    $.ui.toast('Could not run /reload-plugins from here; type it in the prompt.')
  }
  await refresh($)
}

async function uninstall($: any, name: string) {
  await update($, confirm, () => null)
  const r = await $.process.run(['claude', 'plugin', 'uninstall', name], { timeoutMs: 60000 })
  $.ui.toast(r.exitCode === 0 ? `${name} removed. Restart to apply.` : `Remove failed: ${(r.stderr || r.stdout).slice(0, 120)}`)
  await refresh($)
}

function body($: any, e: any, s: Snapshot, t: string, pending: string | null) {
  const { Box, Text, Button, Select, Link } = $.ui.resolve(e)
  const dot = (st: string) => (st === 'running' || st === 'loaded' ? ['●', BRAND.ok] : st === 'disabled' ? ['○', BRAND.idle] : ['●', BRAND.err])
  const rows = rowsOf(s, t)
  const n = (k: string) => rowsOf(s, k).length
  return (
    <Box flexDirection="column">
      <Box>
        <Text bold color={BRAND.ember}>✻ Loaded  </Text>
        <Button key="refresh" label="↻" onPress={() => refresh($)} hotkey="r" />
        <Button key="close" label="✕" onPress={() => close($)} hotkey="x" />
      </Box>
      <Box>
        {TABS.map(k => (
          <Button key={`tab-${k}`} label={`${k === t ? '▸' : ' '}${TITLE[k]} ${n(k)}`} onPress={() => update($, tab, () => k)} />
        ))}
      </Box>
      {rows.length === 0 && <Text color={BRAND.fg2}>nothing loaded</Text>}
      {rows.map(it => {
        const [mark, color] = dot(it.status)
        const menu = t === 'plugins' && it.name.includes('@')
          ? [
              { value: 'info', label: 'Info' },
              { value: 'settings', label: 'Settings' },
              { value: it.status === 'disabled' ? 'enable' : 'disable', label: it.status === 'disabled' ? 'Enable' : 'Disable' },
              { value: 'update', label: 'Update' },
              { value: 'reload', label: 'Reload plugins' },
              { value: 'remove', label: 'Remove' },
            ]
          : [{ value: 'info', label: 'Info' }, { value: 'settings', label: 'Settings' }, { value: 'reload', label: 'Reload plugins' }]
        const tag = it.origin === 'mine' ? '[DEV]' : it.origin === 'installed' ? `[WEB${it.name.includes('@') ? ' ' + it.name.split('@')[1] : ''}]` : '[CORE]'
        const tagColor = it.origin === 'mine' ? BRAND.ember : it.origin === 'installed' ? BRAND.brass : BRAND.idle
        return (
          <Box key={it.name} flexDirection="column" borderStyle="round" borderColor={it.origin === 'mine' ? BRAND.ember : BRAND.line} paddingX={1}>
            <Box>
              <Text color={color}>{mark} </Text>
              <Text bold color={BRAND.fg} dimColor={it.status === 'disabled'}>{it.name.split('@')[0]}</Text>
              <Text bold color={tagColor}>  {tag}</Text>
              <Text color={BRAND.brass}> {it.kind ? `${iconOf(it.kind)} ${it.kind}` : ''}</Text>
            </Box>
            <Text color={BRAND.fg2}>{(it.desc ?? '').slice(0, 90) || `${it.status}${it.note ? ' · ' + it.note : ''}`}</Text>
            <Box>
              {it.link && <Link href={it.link} label="↗ link" />}
              <Text color={BRAND.fg2}>  {it.status}{it.note ? ` · ${it.note}` : ''}  </Text>
              <Select key={`menu-${t}-${it.name}`} label="⋯" options={menu} value="info" onSelect={(v: string) => act($, it, t, v)} />
            </Box>
            {pending === it.name && (
              <Box>
                <Text color={BRAND.err}>Remove {it.name}?  </Text>
                <Button key={`yes-${it.name}`} label="Remove" onPress={() => uninstall($, it.name)} />
                <Button key={`no-${it.name}`} label="Cancel" onPress={() => update($, confirm, () => null)} />
              </Box>
            )}
          </Box>
        )
      })}
      <Box flexDirection="column">
        <Text color={BRAND.fg2}>● on  ○ off   <Text color={BRAND.ember}>[DEV]</Text> mine  <Text color={BRAND.brass}>[WEB]</Text> internet  [CORE] built-in</Text>
        <Text color={BRAND.brass}>⚙ mod  ✦ skill  ☻ agent  ⌘ command  ⇄ mcp  ⚒ tool  ❖ plugin</Text>
      </Box>
    </Box>
  )
}

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    await $.command.register({
      name: 'loaded',
      description: 'Show loaded plugins, skills, tools and MCP servers',
    })
    return next(e)
  })

  // /loaded, the band button and hotkey `l` all toggle the same view (docked right pane, inline fallback).
  on('command.run', { command: 'loaded' }, async $ => {
    const r = await toggleView($)
    return { text: r === 'closed' ? 'Loaded closed.' : r === 'pane' ? 'Loaded opened on the right.' : 'Terminal too narrow for a side pane; opened inline above the prompt.' }
  })

  on('ui.close', { id: PANE }, async ($, e, next) => {
    await update($, paneOpen, () => false)
    return next(e)
  })

  on('ui.render', { component: 'Pane', requestId: PANE }, async ($, e) => {
    let s = await read($, snap)
    if (!s) {
      await refresh($)
      s = await read($, snap)
    }
    const { Text } = $.ui.resolve(e)
    const t = await read($, tab)
    const pending = await read($, confirm)
    return s ? body($, e, s, t, pending) : <Text dimColor>Loading...</Text>
  })

  on('ui.render', { component: 'AbovePrompt' }, async ($, e, next) => {
    const { Box, Button } = $.ui.resolve(e)
    const open = await read($, isOpen)
    const s = await read($, snap)
    const t = await read($, tab)
    const pending = await read($, confirm)
    // Compose with other mods' bands (e.g. prompt-score) instead of replacing them.
    const rest = await next(e)

    const paneIsOpen = await read($, paneOpen)
    const toggle = async () => { await toggleView($) }

    return (
      <Box flexDirection="column">
        <Button key="toggle" label={open || paneIsOpen ? '✻ Loaded ▾' : '✻ Loaded ▸'} onPress={toggle} hotkey="l" />
        {open && s && (
          <Box flexDirection="column" borderStyle="round" paddingX={1}>
            {body($, e, s, t, pending)}
          </Box>
        )}
        {rest}
      </Box>
    )
  })
}
