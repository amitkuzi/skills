#!/usr/bin/env node
// loaded-monitor for Codex: lists skills, plugins and MCP servers with a mine/installed indicator.
// Usage: node loaded.mjs [--json]
import { readFileSync, readdirSync, existsSync, statSync } from 'node:fs'
import { homedir } from 'node:os'
import { join, dirname } from 'node:path'
import { fileURLToPath } from 'node:url'

const here = dirname(fileURLToPath(import.meta.url))
const home = process.env.CODEX_HOME ?? join(homedir(), '.codex')
const ownPath = [join(here, '..', 'own.json'), join(here, 'own.json'), join(home, 'loaded-monitor-own.json')].find(existsSync)
const own = ownPath ? JSON.parse(readFileSync(ownPath, 'utf8')) : { names: [], marketplaces: [] }

const originOf = (name) => {
  const [base, market] = name.split('@')
  return own.names.includes(base) || (market && own.marketplaces.includes(market)) ? 'mine' : 'installed'
}
const dirs = (p) => (existsSync(p) ? readdirSync(p).filter((d) => !d.startsWith('.') && statSync(join(p, d)).isDirectory()) : [])

const cfgPath = join(home, 'config.toml')
const cfg = existsSync(cfgPath) ? readFileSync(cfgPath, 'utf8') : ''
const plugins = [...cfg.matchAll(/^\[plugins\."([^"]+)"\]\s*\n(?:(?!\[).*\n)*?\s*enabled\s*=\s*(true|false)/gm)]
  .filter((m) => m[2] === 'true').map((m) => m[1])
const mcp = [...cfg.matchAll(/^\[mcp_servers\.([\w-]+)\]/gm)].map((m) => m[1])

const snap = {
  plugins: plugins.sort().map((name) => ({ name, origin: originOf(name) })),
  skills: dirs(join(home, 'skills')).sort().map((name) => ({ name, origin: originOf(name) })),
  mcp: mcp.sort().map((name) => ({ name, origin: originOf(name) })),
}

if (process.argv.includes('--json')) {
  console.log(JSON.stringify(snap, null, 2))
} else {
  const mark = (o) => (o === 'mine' ? '●' : '○')
  for (const [label, xs] of Object.entries(snap)) {
    console.log(`\n${label} (${xs.length})`)
    for (const x of xs) console.log(`  ${mark(x.origin)} ${x.name}`)
  }
  const n = Object.values(snap).flat().filter((x) => x.origin === 'mine').length
  console.log(`\n● mine (${n})   ○ installed`)
}
