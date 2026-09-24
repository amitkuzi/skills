#!/usr/bin/env python3
"""Launch the Blender mesh reporter in a factory-startup background process."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


def _version_key(path: Path) -> tuple[int, ...]:
    values = re.findall(r"\d+", " ".join(path.parts[-4:]))
    return tuple(int(value) for value in values) or (0,)


def _standard_blender_candidates() -> list[Path]:
    candidates: list[Path] = []
    if os.name == "nt":
        roots = {
            value
            for key in ("ProgramW6432", "ProgramFiles", "ProgramFiles(x86)")
            if (value := os.environ.get(key))
        }
        for root in roots:
            candidates.extend(Path(root).glob("Blender Foundation/Blender*/blender.exe"))
    elif sys.platform == "darwin":
        candidates.extend(
            [
                Path("/Applications/Blender.app/Contents/MacOS/Blender"),
                Path.home() / "Applications/Blender.app/Contents/MacOS/Blender",
            ]
        )
    else:
        candidates.extend([Path("/snap/bin/blender"), Path("/usr/local/bin/blender")])
    return candidates


def _find_blender(explicit: Path | None) -> Path:
    if explicit is not None:
        resolved = explicit.expanduser().resolve(strict=True)
        if not resolved.is_file():
            raise ValueError(f"Blender is not a regular file: {resolved}")
        return resolved
    found = shutil.which("blender")
    if found:
        return Path(found).resolve(strict=True)
    installed = [path for path in _standard_blender_candidates() if path.is_file()]
    if installed:
        return max(installed, key=_version_key).resolve(strict=True)
    raise ValueError("Blender was not found; provide --blender or install Blender separately")


def _validate_paths(source: Path, output: Path) -> tuple[Path, Path]:
    resolved_source = source.expanduser().resolve(strict=True)
    if not resolved_source.is_file():
        raise ValueError(f"Input is not a regular file: {resolved_source}")
    resolved_output = output.expanduser().resolve()
    if resolved_output == resolved_source:
        raise ValueError("Output must not overwrite input")
    if resolved_output.exists():
        raise ValueError(f"Output already exists: {resolved_output}")
    return resolved_source, resolved_output


def _load_verified_report(output: Path) -> dict[str, Any]:
    if not output.is_file():
        raise RuntimeError("Blender exited without creating the requested report")
    try:
        report = json.loads(output.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise RuntimeError(f"Blender created an invalid JSON report: {error}") from error
    if not isinstance(report, dict) or report.get("schema_version") != "1.0":
        raise RuntimeError("Blender report schema is missing or unsupported")
    if report.get("error"):
        raise RuntimeError(f"Blender analysis failed: {report['error']}")
    required_types = {"source": str, "blender": dict, "objects": list, "limitations": list}
    missing = [name for name, expected in required_types.items() if not isinstance(report.get(name), expected)]
    if missing:
        raise RuntimeError(f"Blender report is missing required fields: {', '.join(missing)}")
    if not report["objects"]:
        raise RuntimeError("Blender report contains no mesh objects")
    return report


def run(
    source: Path,
    output: Path,
    blender: Path | None = None,
    timeout_seconds: int = 120,
) -> dict[str, Any]:
    resolved_source, resolved_output = _validate_paths(source, output)
    executable = _find_blender(blender)
    backend = Path(__file__).with_name("blender_mesh_report.py").resolve(strict=True)
    resolved_output.parent.mkdir(parents=True, exist_ok=True)
    environment = os.environ.copy()
    environment["SLANT3D_BLENDER_INPUT"] = str(resolved_source)
    environment["SLANT3D_BLENDER_OUTPUT"] = str(resolved_output)
    try:
        completed = subprocess.run(
            [str(executable), "--background", "--factory-startup", "--python", str(backend)],
            check=False,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
            env=environment,
        )
    except subprocess.TimeoutExpired as error:
        raise RuntimeError(f"Blender analysis timed out after {timeout_seconds} seconds") from error
    if completed.returncode != 0:
        raise RuntimeError(
            f"Blender exited with code {completed.returncode}: {(completed.stderr or completed.stdout).strip()}"
        )
    report = _load_verified_report(resolved_output)
    report["launcher"] = {
        "executable": str(executable),
        "background": True,
        "factory_startup": True,
        "timeout_seconds": timeout_seconds,
    }
    resolved_output.write_text(json.dumps(report, indent=2, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")
    return report


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--blender", type=Path, help="Optional Blender executable path")
    parser.add_argument("--timeout-seconds", type=int, default=120)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    try:
        report = run(args.input, args.output, args.blender, args.timeout_seconds)
    except (OSError, RuntimeError, ValueError) as error:
        print(json.dumps({"schema_version": "1.0", "error": str(error)}, indent=2))
        return 2
    print(json.dumps(report, indent=2, sort_keys=True, allow_nan=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
