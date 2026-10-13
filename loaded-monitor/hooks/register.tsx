import { atom, read, update } from 'claude-code'
import type { Register } from 'claude-code'

import type { Snapshot, Item, Origin } from '../types'
import own from '../own'

const PANE = 'loaded-monitor'
const isOpen = atom({ plugin: 'loaded-monitor', key: 'isOpen' } as const, false)
const snap = atom({ plugin: 'loaded-monitor', key: 'snap' } as const, null)

const uniq = (xs: string[]) => [...new Set(xs)].sort()

// Origin: mine = listed in own.json (by name or marketplace); builtin = Claude Code core; else installed.
const originOf = (name: string, builtin = false): Origin => {
  const [base, market] = name.split('@')
  if (own.names.includes(base) || (market && own.marketplaces.includes(market))) return 'mine'
  return builtin ? 'builtin' : 'installed'
}
const items = (xs: string[], builtin = false): Item[] => uniq(xs).map(name => ({ name, origin: originOf(name, builtin) }))

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
        ...Object.keys(enabled).filter(k => enabled[k]),
        ...cmds.flatMap((c: any) => (c.plugin ? [c.plugin] : [])),
      ]),
      skills: items(cmds.filter((c: any) => c.source === 'plugin' || c.source === 'user').map((c: any) => c.name)),
      commands: items(cmds.filter((c: any) => c.source === 'builtin').map((c: any) => c.name), true),
      tools: items(tools.filter((t: any) => !t.mcp).map((t: any) => t.name), true),
      mcp: [...byServer].map(([server, n]) => ({ server, tools: n, origin: originOf(server) })),
      agents: items(agents.map((a: any) => a.id)),
    }
}

async function refresh($: any) {
  const fresh = await collect($)
  await update($, snap, () => fresh)
}

function body($: any, e: any, s: Snapshot) {
    const { Box, Text, Button } = $.ui.resolve(e)
    const mark = (o: Origin) => (o === 'mine' ? '●' : o === 'installed' ? '○' : '·')
    const color = (o: Origin) => (o === 'mine' ? 'green' : undefined)
    const line = (label: string, xs: { name: string; origin: Origin }[]) => (
      <Text>
        <Text bold>{label} ({xs.length}): </Text>
        {xs.length ? xs.map(x => (
          <Text key={x.name} color={color(x.origin)} dimColor={x.origin !== 'mine'}>{mark(x.origin)}{x.name}{' '}</Text>
        )) : <Text dimColor>-</Text>}
      </Text>
    )
    return (
      <Box flexDirection="column">
        {line('Plugins/Mods', s.plugins)}
        {line('Skills & user commands', s.skills)}
        {line('Tools', s.tools)}
        {line('MCP servers', s.mcp.map(m => ({ name: `${m.server} (${m.tools})`, origin: m.origin })))}
        {line('Agents', s.agents)}
        <Text dimColor>● mine   ○ installed   · built-in</Text>
        <Button key="refresh" label="Refresh" onPress={() => refresh($)} />
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

  on('command.run', { command: 'loaded' }, async $ => {
    await refresh($)
    await $.ui.open({ id: PANE, title: 'Loaded' })
    return { text: 'Loaded-monitor pane opened.' }
  })

  on('ui.render', { component: 'Pane', requestId: PANE }, async ($, e) => {
    let s = await read($, snap)
    if (!s) {
      await refresh($)
      s = await read($, snap)
    }
    const { Text } = $.ui.resolve(e)
    return s ? body($, e, s) : <Text dimColor>Loading...</Text>
  })

  on('ui.render', { component: 'AbovePrompt' }, async ($, e, next) => {
    const { Box, Button } = $.ui.resolve(e)
    const open = await read($, isOpen)
    const s = await read($, snap)
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
            {body($, e, s)}
          </Box>
        )}
        {rest}
      </Box>
    )
  })
}
