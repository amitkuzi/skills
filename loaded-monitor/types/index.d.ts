export type Origin = 'mine' | 'installed' | 'builtin'
export type Item = { name: string; origin: Origin }

export type Snapshot = {
  plugins: Item[]
  skills: Item[]
  commands: Item[]
  tools: Item[]
  mcp: { server: string; tools: number; origin: Origin }[]
  agents: Item[]
}

declare module 'claude-code' {
  interface PluginState {
    'loaded-monitor': { isOpen: boolean; snap: Snapshot | null }
  }
}
