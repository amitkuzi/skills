---
name: loaded
description: Show what this Codex session has loaded (skills, plugins, MCP servers), marking each as made by the user (●) or installed from elsewhere (○). Use when the user says /loaded, "what is loaded", or asks which skills or plugins are mine versus installed.
---

Run the listing script and show its output as-is:

```
node "$CODEX_HOME/skills/loaded/loaded.mjs"
```

(`CODEX_HOME` defaults to `~/.codex`.) `●` = made by the user, `○` = installed from elsewhere.
Ownership comes from `own.json` next to the script (names and marketplaces). To change what counts as "mine", edit that file.
