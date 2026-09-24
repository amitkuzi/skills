# slant3d

An explicit-invocation Agent Skill for assessing and adapting CAD and mesh models for repeatable FDM
production with FreeCAD and Blender. It is slicer-, printer-, material-, nozzle-, and layer-height-
agnostic. The workflow audits first, proposes detailed changes, and edits a copy only after approval.

The complete 635-video long-form catalog was screened. All 185 definite and 49 probable candidates
received full-caption review; 219 videos contributed 970 timestamped claim records. Channel advice
remains conditional until the applicable independent, toolpath, and physical evidence is available.

## What it covers

- Native FreeCAD (`.FCStd`), STEP/STP/STPZ, IGES/IGS, and BREP/BRP exact-geometry analysis.
- STL, 3MF, and OBJ mesh/package analysis.
- Analysis-only DXF and SVG routing.
- Conservative routing for SolidWorks, Fusion, Inventor, CATIA, Parasolid, AMF, and unknown inputs.
- Single parts and assemblies, including interfaces, tolerance strategy, assembly order, and a
  separate print-orientation proposal for every part.
- Separate approval before any model edit and an additional separate approval before part splitting.
- Qualitative strength/load-path review. FEA is an optional separate workflow only when its required
  inputs and acceptance criteria exist.

## Explicit invocation

The packages are intentionally configured not to load automatically. Invoke the skill by name:

- Claude Code: `/slant3d Audit this STEP assembly for production FDM. Give me the read-only report
  and change proposal; do not edit anything yet.`
- Codex: use the prompt below.

```text
Use $slant3d to audit this STEP assembly for production FDM. Give me the read-only report and change
proposal; do not edit anything yet.
```

## Install

### Requirements

- Python 3.11 or newer to run the preflight scripts, tests, and package builder.
- FreeCAD and Blender are optional. Install them only when their geometry analyzers are needed; a
  missing application blocks only the checks that depend on it.
- Clone this repository normally. `slant3d` is a regular folder in the `skills` repository and not a
  Git submodule or nested repository.

```text
git clone https://github.com/amitkuzi/skills.git
cd skills/slant3d
python -m unittest discover -s tests
python scripts/build_skill_packages.py
```

The builder creates target-specific packages under `dist/` without overwriting an existing build.
If `dist/` already exists, preserve or remove that generated folder explicitly before rebuilding.

### Claude Code

Install the generated `dist/claude-code/slant3d` directory as the skill named `slant3d`.

Windows PowerShell:

```powershell
$skillDestination = Join-Path ([Environment]::GetFolderPath("UserProfile")) ".claude\skills\slant3d"
if (Test-Path -LiteralPath $skillDestination) { throw "Destination already exists: $skillDestination" }
New-Item -ItemType Directory -Force -Path (Split-Path $skillDestination) | Out-Null
Copy-Item -LiteralPath ".\dist\claude-code\slant3d" -Destination $skillDestination -Recurse
```

macOS/Linux:

```bash
mkdir -p ~/.claude/skills
cp -R ./dist/claude-code/slant3d ~/.claude/skills/slant3d
```

Invoke it explicitly:

```text
/slant3d Audit this STEP assembly for production FDM. Do not edit anything yet.
```

### Codex

Install the generated `dist/codex/slant3d` directory as the skill named `slant3d`.

Windows PowerShell:

```powershell
$skillDestination = Join-Path ([Environment]::GetFolderPath("UserProfile")) ".codex\skills\slant3d"
if (Test-Path -LiteralPath $skillDestination) { throw "Destination already exists: $skillDestination" }
New-Item -ItemType Directory -Force -Path (Split-Path $skillDestination) | Out-Null
Copy-Item -LiteralPath ".\dist\codex\slant3d" -Destination $skillDestination -Recurse
```

macOS/Linux:

```bash
mkdir -p ~/.codex/skills
cp -R ./dist/codex/slant3d ~/.codex/skills/slant3d
```

Invoke it explicitly:

```text
Use $slant3d to audit this STEP assembly for production FDM. Do not edit anything yet.
```

The Claude package keeps `disable-model-invocation: true`; the Codex package keeps
`allow_implicit_invocation: false`. Do not install the source directory in place of a generated
target package, because their platform manifests intentionally differ.

## Build details

From this source folder, run:

```text
python scripts/build_skill_packages.py
```

The command creates two independent packages without overwriting an existing build:

- `dist/claude-code/slant3d` — includes Claude Code's `disable-model-invocation: true` frontmatter.
- `dist/codex/slant3d` — includes Codex's `agents/openai.yaml` with implicit invocation disabled.

Copy only the package for the target agent into that product's user or project skills directory.
FreeCAD and Blender are optional local backends: missing applications block only the checks that need
them. The skill never installs software or uploads a model automatically.

The packages contain the full research/evidence archive for auditability, but the skill loads the
compact references first and consults detailed evidence only when a rule or proposal needs tracing.

Typical destinations:

- Claude Code project: `.claude/skills/slant3d`; user-wide: `~/.claude/skills/slant3d`.
- Codex user-wide: `$CODEX_HOME/skills/slant3d` (normally `~/.codex/skills/slant3d`).

On Windows, `~` is the current user's profile directory. On macOS and Linux it is the home directory.

## Documents

- English best-practices reference: `references/production-design.md`
- Hebrew best-practices document: `docs/production-design-best-practices.he.md`
- Input-format and analyzer policy: `references/input-formats.md`
- Phase 2 local-LLM plan: `plans/phase-2-local-llm.md`
- Research scope, catalog, screening, claims, and validation: `research/`
- Coverage summary and limitations: `research/coverage-summary-2026-09-24.md`
- Behavioral scenarios and executed-evidence status: `tests/behavior-scenarios.md` and
  `tests/behavior-validation-results.md`
