export type Origin = 'mine' | 'installed' | 'builtin'
export type Item = { name: string; origin: Origin; status: string; kind: string; desc?: string; link?: string; note?: string }

export type Snapshot = {
  plugins: Item[]
  skills: Item[]
  commands: Item[]
  tools: Item[]
  mcp: { server: string; tools: number; origin: Origin; status: string }[]
  agents: Item[]
}

declare module 'claude-code' {
  interface PluginState {
    'loaded-monitor': { isOpen: boolean; paneOpen: boolean; tab: string; confirm: string | null; snap: Snapshot | null }
  }
}
