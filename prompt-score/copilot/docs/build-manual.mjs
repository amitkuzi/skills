// Builds install-manual.html (fonts embedded, version/date from plugin.json) and install-manual.pdf (Edge headless).
// Usage: node build-manual.mjs [brandkitDir]
import { readFileSync, writeFileSync, existsSync } from 'node:fs'
import { execFileSync } from 'node:child_process'
import { join, dirname } from 'node:path'
import { fileURLToPath, pathToFileURL } from 'node:url'

const here = dirname(fileURLToPath(import.meta.url))
const brandkit = process.argv[2] || 'D:/Development/amitkuzi-brandkit'
const fonts = [
  ['Archivo', 'archivo-latin-wght-normal.woff2', ''],
  ['Public Sans', 'public-sans-latin-wght-normal.woff2', ''],
  ['Rubik', 'rubik-latin-wght-normal.woff2', 'U+0000-00FF'],
  ['Rubik', 'rubik-hebrew-wght-normal.woff2', 'U+0590-05FF, U+FB1D-FB4F'],
]
const edgePaths = [
  'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
  'C:/Program Files/Microsoft/Edge/Application/msedge.exe',
]

function readRelease() {
  const plugin = JSON.parse(readFileSync(join(here, '../../.claude-plugin/plugin.json'), 'utf8'))
  return { version: plugin.version, date: plugin.releaseDate }
}

function fontFaces() {
  const missing = fonts.filter(([, file]) => !existsSync(join(brandkit, 'fonts', file)))
  if (missing.length) {
    console.warn(`Fonts not embedded: ${missing.map(f => f[1]).join(', ')} not found in ${brandkit}/fonts. The manual falls back to Arial.`)
    return ''
  }
  return fonts.map(([family, file, range]) => {
    const data = readFileSync(join(brandkit, 'fonts', file)).toString('base64')
    return `@font-face{font-family:"${family}";src:url(data:font/woff2;base64,${data}) format("woff2");font-weight:100 900;font-display:block;${range ? `unicode-range:${range};` : ''}}`
  }).join('\n')
}

function buildHtml(release) {
  const html = readFileSync(join(here, 'manual.src.html'), 'utf8')
    .replace('/*FONTS*/', fontFaces())
    .replaceAll('{{VERSION}}', release.version)
    .replaceAll('{{DATE}}', release.date)
  const out = join(here, 'install-manual.html')
  writeFileSync(out, html)
  return out
}

function exportPdf(htmlPath) {
  const edge = edgePaths.find(existsSync)
  if (!edge) return console.warn('PDF not exported: Microsoft Edge was not found. Open install-manual.html and print to PDF (A4, background graphics on).')
  const pdf = htmlPath.replace(/\.html$/, '.pdf')
  execFileSync(edge, ['--headless=new', '--disable-gpu', '--no-pdf-header-footer', '--virtual-time-budget=5000',
    `--print-to-pdf=${pdf}`, pathToFileURL(htmlPath).href], { stdio: 'ignore' })
  return pdf
}

const release = readRelease()
const html = buildHtml(release)
const pdf = exportPdf(html)
console.log(`Manual v${release.version} (${release.date}): ${html}${pdf ? ` and ${pdf}` : ''}`)
