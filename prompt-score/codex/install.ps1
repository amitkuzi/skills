# Installs prompt-score into Codex: ~/.codex/skills/prompt-score (skill + script)
$ErrorActionPreference = 'Stop'
$codex = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME '.codex' }
$dest = Join-Path $codex 'skills\prompt-score'
New-Item -ItemType Directory -Force $dest | Out-Null
Copy-Item (Join-Path $PSScriptRoot 'skill\prompt-score\SKILL.md') $dest -Force
Copy-Item (Join-Path $PSScriptRoot 'score.mjs') $dest -Force
Write-Host "Installed to $dest. In Codex, the prompt-score skill scores each prompt."
