import { test, expect } from 'claude-code/testing'
import { scorePrompt } from './score'

test('an engineered prompt scores far above a vague one', () => {
  const weak = scorePrompt('fix it')
  const strong = scorePrompt(
    [
      'Refactor `src/auth.ts` because login currently fails for expired tokens.',
      '- Must keep the public API unchanged',
      '- Do not add dependencies',
      'Output a diff plus a short summary in a list. Done when all 12 tests pass, e.g. "expired token" returns 401.',
    ].join('\n'),
  )
  expect(weak.score).toBeGreaterThanOrEqual(1)
  expect(strong.score).toBeLessThanOrEqual(100)
  expect(strong.score).toBeGreaterThan(weak.score + 40)
})
