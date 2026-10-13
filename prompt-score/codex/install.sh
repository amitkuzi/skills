#!/usr/bin/env sh
# Installs prompt-score into Codex: ~/.codex/skills/prompt-score (skill + script)
set -e
here=$(cd "$(dirname "$0")" && pwd)
dest="${CODEX_HOME:-$HOME/.codex}/skills/prompt-score"
mkdir -p "$dest"
cp "$here/skill/prompt-score/SKILL.md" "$here/score.mjs" "$dest/"
echo "Installed to $dest. In Codex, the prompt-score skill scores each prompt."
