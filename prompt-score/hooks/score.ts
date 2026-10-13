import type { Check, Scored } from '../types'

const has = (t: string, re: RegExp) => re.test(t)

export function scorePrompt(text: string): Scored {
  const t = text.trim()
  const words = t.split(/\s+/).filter(Boolean).length
  const checks: Check[] = []
  const add = (name: string, max: number, got: number, tip: string) =>
    checks.push({ name, max, got: Math.max(0, Math.min(max, Math.round(got))), tip })

  add(
    'Clear goal',
    15,
    (has(t, /\b(create|build|write|fix|add|implement|refactor|review|analy[sz]e|compare|design|explain|generate|plan|debug|summari[sz]e|convert|find)\b/i) ||
    has(t, /(צור|כתוב|תקן|הוסף|בנה|נתח|השווה|תכנן|הסבר|סכם|מצא)/)
      ? 10
      : 3) + (words >= 8 ? 5 : words >= 4 ? 2 : 0),
    'Open with one concrete action verb and the single outcome you want.',
  )
  add(
    'Context',
    15,
    (has(t, /\b(because|currently|so that|background|context|we are|i am|project|existing|goal is)\b/i) ||
    has(t, /(כי|כרגע|הקשר|פרויקט|מטרה)/)
      ? 8
      : 0) + (has(t, /[\w./\\-]+\.\w{1,5}\b|`[^`]+`|https?:\/\//) ? 7 : 0),
    'Say why, what exists today, and point at files, links or code.',
  )
  add(
    'Constraints',
    15,
    has(t, /\b(must|should|only|don't|do not|never|avoid|without|at most|at least|limit|max|min)\b/i) ||
      has(t, /(חייב|רק|אסור|בלי|הימנע|מקסימום|מינימום)/)
      ? 15
      : 0,
    'State must / must-not rules: scope, tech, style, limits.',
  )
  add(
    'Output format',
    15,
    has(t, /\b(format|table|list|bullet|json|markdown|yaml|csv|steps|sections?|summary|diff|code block|in hebrew|in english)\b/i) ||
      has(t, /(טבלה|רשימה|בעברית|באנגלית|פורמט|סעיפים)/)
      ? 15
      : 0,
    'Say what the answer should look like: format, language, length.',
  )
  add(
    'Success criteria / examples',
    15,
    has(t, /\b(test|verify|done when|acceptance|criteria|example|e\.g\.|for instance|expected|success)\b/i) ||
      has(t, /(בדיקה|אימות|קריטריון|לדוגמה|צפוי)/)
      ? 15
      : 0,
    'Define "done" or give an example of good output.',
  )
  add(
    'Specifics',
    10,
    (has(t, /\d/) ? 4 : 0) +
      (has(t, /[A-Z][a-z]+[A-Z]|_\w+|\(\)|\bv?\d+\.\d+/) ? 3 : 0) +
      (has(t, /"[^"]+"|'[^']+'/) ? 3 : 0),
    'Use names, numbers, versions and quoted literals instead of vague words.',
  )
  add(
    'Structure',
    10,
    (has(t, /\n\s*([-*]|\d+[.)])\s/) ? 6 : 0) +
      (t.includes('\n') ? 2 : 0) +
      (has(t, /^#|\n#|:\s*\n|<\w+>/) ? 2 : 0),
    'Break it up: bullets, numbered steps, or labelled sections.',
  )
  add(
    'Length fit',
    5,
    words < 4 ? 0 : words < 12 ? 2 : words <= 400 ? 5 : 3,
    words < 12 ? 'Too terse: add detail.' : 'Trim anything that is not needed.',
  )

  const total = checks.reduce((s, c) => s + c.got, 0)
  return { score: Math.max(1, Math.min(100, total)), checks, preview: t.slice(0, 60) }
}

export const tier = (s: number) =>
  s >= 80 ? 'excellent' : s >= 60 ? 'good' : s >= 40 ? 'fair' : 'weak'
