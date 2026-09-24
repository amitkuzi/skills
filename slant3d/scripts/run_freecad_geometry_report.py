#!/usr/bin/env python3
"""Launch the FreeCAD geometry reporter without passing user paths through FreeCAD argv."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import re
from pathlib import Path
from typing import Any


def _bounded_diagnostics(text: str, replacements: dict[str, str]) -> list[str]:
    sanitized = text
    for raw, replacement in replacements.items():
        sanitized = sanitized.replace(raw, replacement)
    return [line[:300] for line in sanitized.splitlines() if line.strip()][:20]


def _format_process_diagnostics(stdout: str, stderr: str, replacements: dict[str, str]) -> str:
    lines = _bounded_diagnostics(stderr, replacements) + _bounded_diagnostics(stdout, replacements)
    return " | ".join(lines[:20])


def _standard_freecad_candidates() -> list[Path]:
    candidates: list[Path] = []
    if os.name == "nt":
        roots = {
            value
            for key in ("ProgramW6432", "ProgramFiles", "ProgramFiles(x86)")
            if (value := os.environ.get(key))
        }
        for root in roots:
            candidates.extend(Path(root).glob("FreeCAD*/bin/FreeCADCmd.exe"))
    elif sys.platform == "darwin":
        candidates.extend(
            [
                Path("/Applications/FreeCAD.app/Contents/Resources/bin/FreeCADCmd"),
                Path.home() / "Applications/FreeCAD.app/Contents/Resources/bin/FreeCADCmd",
            ]
        )
    else:
        candidates.extend([Path("/snap/bin/freecadcmd"), Path("/usr/local/bin/freecadcmd")])
    return candidates


def _version_key(path: Path) -> tuple[int, ...]:
    versions = re.findall(r"\d+", " ".join(part for part in path.parts[-4:]))
    return tuple(int(value) for value in versions) or (0,)


def _find_freecad_cmd(explicit: Path | None) -> Path:
    if explicit is not None:
        resolved = explicit.expanduser().resolve(strict=True)
        if not resolved.is_file():
            raise ValueError(f"FreeCADCmd is not a regular file: {resolved}")
        return resolved
    found = shutil.which("FreeCADCmd") or shutil.which("freecadcmd")
    if found:
        return Path(found).resolve(strict=True)
    installed = [path for path in _standard_freecad_candidates() if path.is_file()]
    if installed:
        return max(installed, key=_version_key).resolve(strict=True)
    raise ValueError("FreeCADCmd was not found; provide --freecad-cmd or install FreeCAD separately")


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
        raise RuntimeError("FreeCAD exited without creating the requested report")
    try:
        report = json.loads(output.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise RuntimeError(f"FreeCAD created an invalid JSON report: {error}") from error
    if not isinstance(report, dict) or report.get("schema_version") != "1.0":
        raise RuntimeError("FreeCAD report schema is missing or unsupported")
    if report.get("error"):
        raise RuntimeError(f"FreeCAD analysis failed: {report['error']}")
    required_types = {
        "source": str,
        "freecad": dict,
        "objects": list,
        "limitations": list,
    }
    missing = [name for name, expected in required_types.items() if not isinstance(report.get(name), expected)]
    if missing:
        raise RuntimeError(f"FreeCAD report is missing required fields: {', '.join(missing)}")
    return report


def run(
    source: Path,
    output: Path,
    freecad_cmd: Path | None = None,
    timeout_seconds: int = 120,
) -> dict[str, Any]:
    resolved_source, resolved_output = _validate_paths(source, output)
    executable = _find_freecad_cmd(freecad_cmd)
    backend = Path(__file__).with_name("freecad_geometry_report.py").resolve(strict=True)
    resolved_output.parent.mkdir(parents=True, exist_ok=True)
    environment = os.environ.copy()
    environment["SLANT3D_FREECAD_INPUT"] = str(resolved_source)
    environment["SLANT3D_FREECAD_OUTPUT"] = str(resolved_output)
    try:
        completed = subprocess.run(
            [str(executable), "--safe-mode", str(backend)],
            check=False,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
            env=environment,
        )
    except subprocess.TimeoutExpired as error:
        raise RuntimeError(f"FreeCAD analysis exceeded {timeout_seconds} seconds") from error
    replacements = {
        str(resolved_source): "<input>",
        str(resolved_output): "<output>",
        str(backend): "<backend>",
    }
    process_diagnostics = _format_process_diagnostics(completed.stdout, completed.stderr, replacements)
    if completed.returncode != 0:
        suffix = f" Diagnostics: {process_diagnostics}" if process_diagnostics else ""
        raise RuntimeError(
            f"FreeCAD exited with code {completed.returncode}; report is not accepted as successful.{suffix}"
        )
    try:
        report = _load_verified_report(resolved_output)
    except RuntimeError as error:
        suffix = f" Diagnostics: {process_diagnostics}" if process_diagnostics else ""
        raise RuntimeError(f"{error}.{suffix}") from error
    diagnostics = _bounded_diagnostics(completed.stderr, replacements)
    report["launcher"] = {
        "freecad_exit_code": completed.returncode,
        "safe_mode_requested": True,
        "stderr_present": bool(completed.stderr.strip()),
        "stderr_diagnostics": diagnostics,
    }
    resolved_output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--freecad-cmd", type=Path)
    parser.add_argument("--timeout-seconds", type=int, default=120)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    if args.timeout_seconds <= 0:
        print(json.dumps({"schema_version": "1.0", "error": "Timeout must be positive."}, indent=2))
        return 2
    try:
        report = run(args.input, args.output, args.freecad_cmd, args.timeout_seconds)
    except (OSError, RuntimeError, ValueError) as error:
        print(json.dumps({"schema_version": "1.0", "error": str(error)}, indent=2))
        return 2
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
