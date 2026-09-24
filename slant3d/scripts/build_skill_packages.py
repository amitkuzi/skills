#!/usr/bin/env python3
"""Build separate explicit-invocation Claude Code and Codex skill packages."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


def _copy_tree(source: Path, destination: Path) -> None:
    shutil.copytree(
        source,
        destination,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".pytest_cache"),
    )


def _hash_files(root: Path) -> dict[str, str]:
    return {
        path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(root.rglob("*"))
        if path.is_file() and path.name != "package-manifest.json"
    }


def _write_manifest(package: Path, platform: str) -> None:
    manifest = {
        "schema_version": "1.0",
        "skill": "slant3d",
        "platform": platform,
        "implicit_invocation": False,
        "files": _hash_files(package),
    }
    (package / "package-manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def build(output_root: Path) -> dict[str, Path]:
    source_root = Path(__file__).parents[1].resolve(strict=True)
    output = output_root.expanduser().resolve()
    if output == source_root or source_root in output.parents and output.name != "dist":
        raise ValueError("Output must be a dedicated package directory, normally slant3d/dist")
    if output.exists():
        raise ValueError(f"Output already exists; preserve or remove it explicitly before rebuilding: {output}")

    source_skill = (source_root / "SKILL.md").read_text(encoding="utf-8")
    if "disable-model-invocation: true" not in source_skill:
        raise ValueError("Source SKILL.md must explicitly disable Claude model invocation")
    openai = (source_root / "agents" / "openai.yaml").read_text(encoding="utf-8")
    if "allow_implicit_invocation: false" not in openai:
        raise ValueError("Codex manifest must explicitly disable implicit invocation")

    claude = output / "claude-code" / "slant3d"
    codex = output / "codex" / "slant3d"
    for package in (claude, codex):
        package.mkdir(parents=True)
        shutil.copy2(source_root / "README.md", package / "README.md")
        shutil.copy2(source_root / "LICENSE", package / "LICENSE")
        _copy_tree(source_root / "references", package / "references")
        _copy_tree(source_root / "scripts", package / "scripts")
        _copy_tree(source_root / "docs", package / "docs")
        _copy_tree(source_root / "plans", package / "plans")
        _copy_tree(source_root / "research", package / "research")
        (package / "tests").mkdir()
        for evidence_name in ("behavior-scenarios.md", "behavior-validation-results.md"):
            shutil.copy2(source_root / "tests" / evidence_name, package / "tests" / evidence_name)

    (claude / "SKILL.md").write_text(source_skill, encoding="utf-8")
    codex_skill = source_skill.replace("disable-model-invocation: true\n", "", 1)
    (codex / "SKILL.md").write_text(codex_skill, encoding="utf-8")
    (codex / "agents").mkdir()
    shutil.copy2(source_root / "agents" / "openai.yaml", codex / "agents" / "openai.yaml")

    _write_manifest(claude, "claude-code")
    _write_manifest(codex, "codex")
    return {"claude_code": claude, "codex": codex}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).parents[1] / "dist")
    args = parser.parse_args()
    try:
        packages = build(args.output)
    except (OSError, ValueError) as error:
        print(json.dumps({"error": str(error)}, indent=2))
        return 2
    print(json.dumps({name: str(path) for name, path in packages.items()}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
