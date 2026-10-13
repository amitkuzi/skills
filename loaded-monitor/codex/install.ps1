# Installs loaded-monitor into Codex: ~/.codex/skills/loaded (skill + script + own.json)
$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$codex = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME '.codex' }
$dest = Join-Path $codex 'skills\loaded'
New-Item -ItemType Directory -Force $dest | Out-Null
Copy-Item (Join-Path $PSScriptRoot 'skill\loaded\SKILL.md') $dest -Force
Copy-Item (Join-Path $PSScriptRoot 'loaded.mjs') $dest -Force
Copy-Item (Join-Path $root 'own.json') $dest -Force
Write-Host "Installed to $dest. In Codex, ask: 'what is loaded' (or use the loaded skill)."
