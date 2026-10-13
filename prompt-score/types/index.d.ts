export type Check = { name: string; got: number; max: number; tip: string }
export type Scored = { score: number; checks: Check[]; preview: string }

declare module 'claude-code' {
  interface PluginState {
    'prompt-score': {
      last: Scored | null
      history: number[]
      view: 'none' | 'breakdown' | 'tips' | 'rewrite' | 'history'
      rewrite: string
      isHidden: boolean
    }
  }
}
