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

const uniq = (xs: string[]) => [...new Set(xs)].sort()

// Origin: mine = listed in own.json (by name or marketplace); builtin = Claude Code core; else installed.
const originOf = (name: string, builtin = false): Origin => {
  const [base = '', market] = name.split('@')
  if (own.names.includes(base) || (market && own.marketplaces.includes(market))) return 'mine'
  return builtin ? 'builtin' : 'installed'
}
const items = (xs: string[], builtin = false, off: string[] = []): Item[] =>
  uniq(xs).map(name => ({ name, origin: originOf(name, builtin), status: off.includes(name) ? 'disabled' : 'loaded' }))

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
    return {
      plugins: items([
        ...Object.keys(enabled),
        ...cmds.flatMap((c: any) => (c.plugin ? [c.plugin] : [])),
      ], false, Object.keys(enabled).filter(k => !enabled[k])),
      skills: items(cmds.filter((c: any) => c.source === 'plugin' || c.source === 'user').map((c: any) => c.name)),
      commands: items(cmds.filter((c: any) => c.source === 'builtin').map((c: any) => c.name), true),
      tools: items(tools.filter((t: any) => !t.mcp).map((t: any) => t.name), true),
      mcp: [...byServer].map(([server, n]) => ({ server, tools: n, origin: originOf(server), status: 'running' })),
      agents: items(agents.map((a: any) => a.id)),
    }
}

async function refresh($: any) {
  const fresh = await collect($)
  await update($, snap, () => fresh)
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
  t === 'mcp' ? s.mcp.map(m => ({ name: m.server, origin: m.origin, status: m.status, note: `${m.tools} tools` })) : (s[t as 'plugins'] as Item[])

async function act($: any, it: Item, kind: string, choice: string) {
  if (choice === 'info') {
    $.ui.toast(`${it.name}: ${it.status}, ${it.origin === 'mine' ? 'made by you' : it.origin}${it.note ? ', ' + it.note : ''}`)
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
  const { Box, Text, Button, Select } = $.ui.resolve(e)
  const dot = (st: string) => (st === 'running' ? ['●', 'green'] : st === 'disabled' ? ['○', undefined] : st === 'error' ? ['●', 'red'] : ['●', 'yellow'])
  const rows = rowsOf(s, t)
  const n = (k: string) => rowsOf(s, k).length
  return (
    <Box flexDirection="column">
      <Box>
        <Text bold>✻ Loaded  </Text>
        <Button key="refresh" label="↻" onPress={() => refresh($)} hotkey="r" />
        <Button key="close" label="✕" onPress={() => close($)} hotkey="x" />
      </Box>
      <Box>
        {TABS.map(k => (
          <Button key={`tab-${k}`} label={`${k === t ? '▸' : ' '}${TITLE[k]} ${n(k)}`} onPress={() => update($, tab, () => k)} />
        ))}
      </Box>
      {rows.length === 0 && <Text dimColor>nothing loaded</Text>}
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
        return (
          <Box key={it.name} flexDirection="column">
            <Box>
              <Text color={color}>{mark} </Text>
              <Text bold={it.origin === 'mine'} color={it.origin === 'mine' ? 'green' : undefined} dimColor={it.status === 'disabled'}>{it.name}</Text>
              <Text dimColor>  {it.status}{it.note ? ` · ${it.note}` : ''}  </Text>
              <Text bold color={it.origin === 'mine' ? 'green' : it.origin === 'installed' ? 'yellow' : undefined} dimColor={it.origin === 'builtin'}>
                {it.origin === 'mine' ? '[DEV]' : it.origin === 'installed' ? `[WEB${it.name.includes('@') ? ' ' + it.name.split('@')[1] : ''}]` : '[CORE]'}{' '}
              </Text>
              <Select key={`menu-${t}-${it.name}`} label="⋯" options={menu} value="info" onSelect={(v: string) => act($, it, t, v)} />
            </Box>
            {pending === it.name && (
              <Box>
                <Text color="red">Remove {it.name}?  </Text>
                <Button key={`yes-${it.name}`} label="Remove" onPress={() => uninstall($, it.name)} />
                <Button key={`no-${it.name}`} label="Cancel" onPress={() => update($, confirm, () => null)} />
              </Box>
            )}
          </Box>
        )
      })}
      <Text dimColor>● running  ○ disabled   [DEV] mine   [WEB] from the internet / marketplace   [CORE] built-in</Text>
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

  // /loaded toggles the side pane (open <-> close); the band button toggles the inline panel.
  on('command.run', { command: 'loaded' }, async $ => {
    if (await read($, paneOpen)) {
      await update($, paneOpen, () => false)
      await $.ui.close({ id: PANE })
      return { text: 'Loaded-monitor pane closed.' }
    }
    await refresh($)
    const r = await $.ui.open({ id: PANE, title: 'Loaded' })
    if (!r.isPlaced) {
      // Terminal too narrow for a side pane: fall back to the inline panel.
      await update($, isOpen, () => true)
      return { text: 'Terminal too narrow for a pane; opened the inline panel above the prompt.' }
    }
    await update($, paneOpen, () => true)
    return { text: 'Loaded-monitor pane opened. Run /loaded again to close.' }
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

    const toggle = async () => {
      const willOpen = !open
      await update($, isOpen, () => willOpen)
      if (willOpen) await refresh($)
    }

    return (
      <Box flexDirection="column">
        <Button key="toggle" label={open ? '✻ Loaded ▾' : '✻ Loaded ▸'} onPress={toggle} hotkey="l" />
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
