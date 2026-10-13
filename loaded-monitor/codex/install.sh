#!/usr/bin/env sh
# Installs loaded-monitor into Codex: ~/.codex/skills/loaded (skill + script + own.json)
set -e
here=$(cd "$(dirname "$0")" && pwd)
dest="${CODEX_HOME:-$HOME/.codex}/skills/loaded"
mkdir -p "$dest"
cp "$here/skill/loaded/SKILL.md" "$here/loaded.mjs" "$here/../own.json" "$dest/"
echo "Installed to $dest. In Codex, ask: 'what is loaded' (or use the loaded skill)."
