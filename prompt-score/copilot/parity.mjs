// Checks that copilot/score.py gives the same line as codex/score.mjs. Usage: node copilot/parity.mjs
import { execFileSync } from 'node:child_process'
import { join, dirname } from 'node:path'
import { fileURLToPath } from 'node:url'

const here = dirname(fileURLToPath(import.meta.url))
const prompts = [
  'fix it',
  'Write a Python function parse_csv() that reads `data/in.csv` because the current loader fails.\nRules:\n- must not use pandas\n- at most 40 lines\nOutput: a code block and a 3-bullet summary in English.\nDone when: test_parse passes, e.g. \'a,b\' -> [\'a\',\'b\'] for v2.1.',
  'תקן את הבאג בקובץ app.js כי הוא קורס. רק שינוי מינימלי, תשובה בעברית בטבלה, לדוגמה צפוי פלט 42',
  '# Goal\nExplain how OAuth works:\n1. flows\n2. tokens',
  'Summarize this article in markdown sections, at least 3 sections, for instance about https://example.com/x without jargon.',
]
const run = (cmd, args) => execFileSync(cmd, args, { encoding: 'utf8', env: { ...process.env, PYTHONIOENCODING: 'utf-8' } }).trim()

let failed = 0
for (const p of prompts) {
  const node = run('node', [join(here, '../codex/score.mjs'), p])
  const py = run('python', ['-I', join(here, 'score.py'), p])
  if (node !== py) { failed++; console.log(`DIFF for ${JSON.stringify(p.slice(0, 40))}\n  node: ${node}\n  py:   ${py}`) }
}
console.log(failed ? `${failed} of ${prompts.length} prompts differ` : `All ${prompts.length} prompts match`)
process.exit(failed ? 1 : 0)
