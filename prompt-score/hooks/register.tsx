import { atom, read, update } from 'claude-code'
import type { Register } from 'claude-code'

import type { Scored } from '../types'
import { scorePrompt, tier } from './score'

const last = atom({ plugin: 'prompt-score', key: 'last' } as const, null)
const history = atom({ plugin: 'prompt-score', key: 'history' } as const, [])
const view = atom({ plugin: 'prompt-score', key: 'view' } as const, 'none')
const rewrite = atom({ plugin: 'prompt-score', key: 'rewrite' } as const, '')
const isHidden = atom({ plugin: 'prompt-score', key: 'isHidden' } as const, false)

let lastText = ''

const BUSY = 'Improving...'
const FAILED = 'Could not improve the prompt.'

async function ready($: any): Promise<string> {
  const text: string = await read($, rewrite)
  return text && text !== BUSY && text !== FAILED ? text : ''
}

// Replaces the current prompt with the (possibly edited) rewrite and sends it.
async function run($: any) {
  const text = await ready($)
  if (!text) return
  await update($, view, () => 'none')
  void $.prompt.submit({ text })
}

async function act($: any, value: string) {
  if (value === 'hide') return update($, isHidden, () => true)
  if (value === 'rewrite') {
    await update($, view, () => 'rewrite')
    await update($, rewrite, () => BUSY)
    const r = await $.model.complete({
      model: 'haiku',
      prompt:
        'Rewrite this prompt to be a well-engineered prompt (clear goal, context, constraints, output format, success criteria). Keep the same intent and language. Reply with the rewritten prompt only.\n\n' +
        lastText,
    })
    return update($, rewrite, () => (r.isAnswered ? r.text : FAILED))
  }
  if (value === 'resubmit') return run($)
  return update($, view, () => (value === 'close' || value === 'menu' ? 'none' : value))
}

export const register: Register = on => {

  on('prompt.submit', async ($, e, next) => {
    const text = e.text.trim()
    if (text && !text.startsWith('/')) {
      lastText = e.text
      const s = scorePrompt(e.text)
      await update($, last, () => s)
      await update($, history, h => [...h, s.score].slice(-50))
      await update($, view, () => 'none')
      await update($, isHidden, () => false)
      $.ui.status(`prompt ${s.score}/100`)
    }
    return next(e)
  })

  on('ui.render', { component: 'UserMessage' }, async ($, e, next) => {
    const text = e.props.text.trim()
    if (e.props.origin.kind !== 'composer' || !text || text.startsWith('/')) return next(e)

    const { Box, Text } = $.ui.resolve(e)
    const s = scorePrompt(text)

    return (
      <Box flexDirection="row" justifyContent="space-between">
        <Box flexShrink={1}>
          <Text>{'> ' + text}</Text>
        </Box>
        <Box flexShrink={0} marginLeft={2}>
          <Text bold dimColor>{`[${s.score}/100 ${tier(s.score)}]`}</Text>
        </Box>
      </Box>
    )
  })

  on('ui.render', { component: 'AbovePrompt' }, async ($, e, next) => {
    const s: Scored | null = await read($, last)
    if (e.props.hasSurvey || s === null || (await read($, isHidden))) return next(e)

    const v = await read($, view)
    // Compose with other mods' bands (e.g. loaded-monitor) instead of replacing them.
    const rest = await next(e)
    const { Box, Text, Select, Button, Input } = $.ui.resolve(e)
    const rewritten: string = await read($, rewrite)
    const hist = await read($, history)
    const avg = Math.round(hist.reduce((a, b) => a + b, 0) / hist.length)

    return (
      <Box flexDirection="column">
        <Box>
          <Text bold>
            Prompt score {s.score}/100 ({tier(s.score)}){' '}
          </Text>
          <Select
            key="actions"
            label="Actions:"
            value="menu"
            options={[
              { value: 'menu', label: 'choose...' },
              { value: 'breakdown', label: 'Show breakdown' },
              { value: 'tips', label: 'Show improvement tips' },
              { value: 'rewrite', label: 'Rewrite my prompt (haiku)' },
              { value: 'history', label: 'History' },
              { value: 'close', label: 'Close details' },
              { value: 'hide', label: 'Hide score' },
            ]}
            onSelect={value => act($, value)}
          />
        </Box>
        {v === 'breakdown' &&
          s.checks.map(c => (
            <Text dimColor>
              {c.name}: {c.got}/{c.max}
            </Text>
          ))}
        {v === 'tips' &&
          s.checks
            .filter(c => c.got < c.max)
            .map(c => (
              <Text dimColor>
                - {c.name}: {c.tip}
              </Text>
            ))}
        {v === 'rewrite' && <Text dimColor>{rewritten}</Text>}
        {v === 'edit' && (
          <Input
            key="rewrite-edit"
            label="Edit:"
            value={rewritten}
            submitLabel="run"
            autoFocus
            onInput={value => void update($, rewrite, () => value)}
            onSubmit={() => void run($)}
          />
        )}
        {(v === 'rewrite' || v === 'edit') && (
          <Box>
            <Button key="rw-edit" label="Edit" hotkey="e" onPress={() => void update($, view, () => 'edit')} />
            <Text> </Text>
            <Button key="rw-run" label="Run" hotkey="r" variant="primary" onPress={() => void run($)} />
            <Text> </Text>
            <Button
              key="rw-copy"
              label="Copy"
              hotkey="c"
              onPress={async press => {
                const text = await ready($)
                if (text) await $.ui.copy({ text, surface: press.surface })
              }}
            />
            <Text> </Text>
            <Button key="rw-cancel" label="Cancel" hotkey="x" role="dismiss" onPress={() => void update($, view, () => 'none')} />
          </Box>
        )}
        {v === 'history' && (
          <Text dimColor>
            {hist.length} prompts, avg {avg}, recent: {hist.slice(-10).join(' ')}
          </Text>
        )}
        {rest}
      </Box>
    )
  })
}
