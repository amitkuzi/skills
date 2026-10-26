import type { Check, Scored } from '../types'

type Prompt = { text: string; words: number }
type Keywords = { english: RegExp; hebrew: RegExp }
type Rule = { name: string; max: number; points: (p: Prompt) => number; tip: (p: Prompt) => string }

const MIN_SCORE = 1
const MAX_SCORE = 100
const PREVIEW_LENGTH = 60

/** Score a prompt 1-100 by how well it states goal, context, constraints, format, success and structure. */
export function scorePrompt(text: string): Scored {
  const prompt = readPrompt(text)
  const checks = RULES.map(rule => runRule(rule, prompt))
  const score = totalScore(checks)
  return { score, checks, preview: previewOf(prompt) }
}

export const tier = (s: number) =>
  s >= 80 ? 'excellent' : s >= 60 ? 'good' : s >= 40 ? 'fair' : 'weak'

function readPrompt(raw: string): Prompt {
  const text = raw.trim()
  return { text, words: countWords(text) }
}

function runRule(rule: Rule, prompt: Prompt): Check {
  const got = clamp(Math.round(rule.points(prompt)), 0, rule.max)
  return { name: rule.name, max: rule.max, got, tip: rule.tip(prompt) }
}

function totalScore(checks: Check[]): number {
  const total = checks.reduce((sum, check) => sum + check.got, 0)
  return clamp(total, MIN_SCORE, MAX_SCORE)
}

function previewOf(prompt: Prompt): string {
  return prompt.text.slice(0, PREVIEW_LENGTH)
}

// --- rules: add a new check by adding an entry, scorePrompt stays unchanged ---

const ACTION_VERBS: Keywords = {
  english: /\b(create|build|write|fix|add|implement|refactor|review|analy[sz]e|compare|design|explain|generate|plan|debug|summari[sz]e|convert|find)\b/i,
  hebrew: /(צור|כתוב|תקן|הוסף|בנה|נתח|השווה|תכנן|הסבר|סכם|מצא)/,
}
const CONTEXT_WORDS: Keywords = {
  english: /\b(because|currently|so that|background|context|we are|i am|project|existing|goal is)\b/i,
  hebrew: /(כי|כרגע|הקשר|פרויקט|מטרה)/,
}
const CONSTRAINT_WORDS: Keywords = {
  english: /\b(must|should|only|don't|do not|never|avoid|without|at most|at least|limit|max|min)\b/i,
  hebrew: /(חייב|רק|אסור|בלי|הימנע|מקסימום|מינימום)/,
}
const FORMAT_WORDS: Keywords = {
  english: /\b(format|table|list|bullet|json|markdown|yaml|csv|steps|sections?|summary|diff|code block|in hebrew|in english)\b/i,
  hebrew: /(טבלה|רשימה|בעברית|באנגלית|פורמט|סעיפים)/,
}
const SUCCESS_WORDS: Keywords = {
  english: /\b(test|verify|done when|acceptance|criteria|example|e\.g\.|for instance|expected|success)\b/i,
  hebrew: /(בדיקה|אימות|קריטריון|לדוגמה|צפוי)/,
}

const FILE_LINK_OR_CODE = /[\w./\\-]+\.\w{1,5}\b|`[^`]+`|https?:\/\//
const DIGIT = /\d/
const IDENTIFIER_OR_VERSION = /[A-Z][a-z]+[A-Z]|_\w+|\(\)|\bv?\d+\.\d+/
const QUOTED_LITERAL = /"[^"]+"|'[^']+'/
const LIST_ITEM = /\n\s*([-*]|\d+[.)])\s/
const HEADING_OR_LABEL = /^#|\n#|:\s*\n|<\w+>/

const RULES: Rule[] = [
  {
    name: 'Clear goal',
    max: 15,
    points: p => pointsIf(mentionsAny(p.text, ACTION_VERBS), 10, 3) + goalLengthPoints(p.words),
    tip: () => 'Open with one concrete action verb and the single outcome you want.',
  },
  {
    name: 'Context',
    max: 15,
    points: p => pointsIf(mentionsAny(p.text, CONTEXT_WORDS), 8) + pointsIf(FILE_LINK_OR_CODE.test(p.text), 7),
    tip: () => 'Say why, what exists today, and point at files, links or code.',
  },
  {
    name: 'Constraints',
    max: 15,
    points: p => pointsIf(mentionsAny(p.text, CONSTRAINT_WORDS), 15),
    tip: () => 'State must / must-not rules: scope, tech, style, limits.',
  },
  {
    name: 'Output format',
    max: 15,
    points: p => pointsIf(mentionsAny(p.text, FORMAT_WORDS), 15),
    tip: () => 'Say what the answer should look like: format, language, length.',
  },
  {
    name: 'Success criteria / examples',
    max: 15,
    points: p => pointsIf(mentionsAny(p.text, SUCCESS_WORDS), 15),
    tip: () => 'Define "done" or give an example of good output.',
  },
  {
    name: 'Specifics',
    max: 10,
    points: p =>
      pointsIf(DIGIT.test(p.text), 4) +
      pointsIf(IDENTIFIER_OR_VERSION.test(p.text), 3) +
      pointsIf(QUOTED_LITERAL.test(p.text), 3),
    tip: () => 'Use names, numbers, versions and quoted literals instead of vague words.',
  },
  {
    name: 'Structure',
    max: 10,
    points: p =>
      pointsIf(LIST_ITEM.test(p.text), 6) +
      pointsIf(p.text.includes('\n'), 2) +
      pointsIf(HEADING_OR_LABEL.test(p.text), 2),
    tip: () => 'Break it up: bullets, numbered steps, or labelled sections.',
  },
  {
    name: 'Length fit',
    max: 5,
    points: p => lengthFitPoints(p.words),
    tip: p => (isTerse(p.words) ? 'Too terse: add detail.' : 'Trim anything that is not needed.'),
  },
]

// --- scoring helpers ---

function goalLengthPoints(words: number): number {
  if (words >= 8) return 5
  if (words >= 4) return 2
  return 0
}

function lengthFitPoints(words: number): number {
  if (words < 4) return 0
  if (isTerse(words)) return 2
  if (words <= 400) return 5
  return 3
}

function isTerse(words: number): boolean {
  return words < 12
}

function mentionsAny(text: string, keywords: Keywords): boolean {
  return keywords.english.test(text) || keywords.hebrew.test(text)
}

function pointsIf(condition: boolean, points: number, otherwise = 0): number {
  return condition ? points : otherwise
}

function countWords(text: string): number {
  return text.split(/\s+/).filter(Boolean).length
}

function clamp(value: number, min: number, max: number): number {
  return Math.max(min, Math.min(max, value))
}
