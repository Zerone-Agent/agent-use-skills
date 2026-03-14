#!/usr/bin/env python3
"""Deterministic helpers for auditing and safely changing OpenClaw config."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import difflib


def _run(
    command: list[str],
    *,
    env: dict[str, str] | None = None,
    check: bool = False,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        text=True,
        capture_output=True,
        env=env,
        check=check,
    )


def _clean_lines(text: str) -> list[str]:
    return [line.rstrip() for line in text.splitlines() if line.strip()]


def _strip_ansi(text: str) -> str:
    ansi = re.compile(r"\x1b\[[0-9;]*[A-Za-z]")
    return ansi.sub("", text)


def _extract_path_from_output(text: str) -> str | None:
    for line in reversed(_clean_lines(_strip_ansi(text))):
        candidate = line.strip()
        if candidate.startswith("~") or candidate.startswith("/"):
            return str(Path(candidate).expanduser())
    return None


def _resolve_config_path() -> tuple[Path, str]:
    proc = _run(["openclaw", "config", "file"])
    cli_path = _extract_path_from_output(proc.stdout or proc.stderr)
    if proc.returncode == 0 and cli_path:
        return Path(cli_path), "cli"

    fallback = Path.home() / ".openclaw" / "openclaw.json"
    return fallback, "fallback"


def _env_for_path(path: Path) -> dict[str, str]:
    env = os.environ.copy()
    env["OPENCLAW_CONFIG_PATH"] = str(path)
    return env


def _json_dumps(data: Any) -> str:
    return json.dumps(data, ensure_ascii=True, indent=2, sort_keys=True)


def cmd_resolve_path(args: argparse.Namespace) -> int:
    path, source = _resolve_config_path()
    payload = {
        "configPath": str(path),
        "source": source,
        "exists": path.exists(),
    }
    if args.json:
        print(_json_dumps(payload))
    else:
        print(str(path))
    return 0


def cmd_backup(args: argparse.Namespace) -> int:
    path = Path(args.path).expanduser() if args.path else _resolve_config_path()[0]
    if not path.exists():
        print(_json_dumps({"ok": False, "error": f"Config file not found: {path}"}))
        return 1

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%SZ")
    backup_path = path.with_name(f"{path.name}.bak.{timestamp}")
    shutil.copy2(path, backup_path)
    payload = {
        "ok": True,
        "configPath": str(path),
        "backupPath": str(backup_path),
    }
    print(_json_dumps(payload) if args.json else str(backup_path))
    return 0


def _parse_validate_output(proc: subprocess.CompletedProcess[str], path: Path) -> dict[str, Any]:
    stdout = (proc.stdout or "").strip()
    stderr = (proc.stderr or "").strip()
    payload: dict[str, Any] = {
        "command": "openclaw config validate --json",
        "configPath": str(path),
        "exitCode": proc.returncode,
        "stdout": stdout,
        "stderr": stderr,
    }

    try:
        parsed = json.loads(stdout) if stdout else {}
    except json.JSONDecodeError:
        parsed = {}

    if isinstance(parsed, dict):
        payload.update(parsed)

    if "valid" not in payload:
        payload["valid"] = proc.returncode == 0 and not stderr

    return payload


def cmd_validate(args: argparse.Namespace) -> int:
    path = Path(args.path).expanduser() if args.path else _resolve_config_path()[0]
    proc = _run(
        ["openclaw", "config", "validate", "--json"],
        env=_env_for_path(path),
    )
    payload = _parse_validate_output(proc, path)
    if args.doctor:
        doctor_proc = _run(
            ["openclaw", "doctor", "--non-interactive"],
            env=_env_for_path(path),
        )
        combined = "\n".join(part for part in [doctor_proc.stdout, doctor_proc.stderr] if part)
        payload["doctor"] = {
            "command": "openclaw doctor --non-interactive",
            "exitCode": doctor_proc.returncode,
            "summary": _doctor_summary(combined),
        }
    if args.json:
        print(_json_dumps(payload))
    else:
        output_lines: list[str] = []
        if payload.get("stdout"):
            output_lines.append(str(payload["stdout"]))
        if payload.get("stderr"):
            output_lines.append(str(payload["stderr"]))
        if args.doctor and payload.get("doctor", {}).get("summary"):
            output_lines.append("Doctor summary:")
            output_lines.extend(str(item) for item in payload["doctor"]["summary"])
        print("\n".join(output_lines).strip())
    return 0 if payload.get("valid") else 1


def _doctor_summary(text: str) -> list[str]:
    lines = _clean_lines(_strip_ansi(text))
    summary: list[str] = []
    for line in lines:
        normalized = line.strip().strip("│ ").strip()
        if normalized.startswith("- "):
            summary.append(normalized)
        elif normalized.startswith("Config warnings"):
            summary.append(normalized)
    seen: set[str] = set()
    deduped: list[str] = []
    for item in summary:
        if item not in seen:
            deduped.append(item)
            seen.add(item)
    return deduped


def cmd_doctor(args: argparse.Namespace) -> int:
    path = Path(args.path).expanduser() if args.path else _resolve_config_path()[0]
    proc = _run(
        ["openclaw", "doctor", "--non-interactive"],
        env=_env_for_path(path),
    )
    combined = "\n".join(part for part in [proc.stdout, proc.stderr] if part)
    payload = {
        "command": "openclaw doctor --non-interactive",
        "configPath": str(path),
        "exitCode": proc.returncode,
        "summary": _doctor_summary(combined),
        "stdout": (proc.stdout or "").strip(),
        "stderr": (proc.stderr or "").strip(),
    }
    print(_json_dumps(payload) if args.json else combined.strip())
    return 0 if proc.returncode == 0 else proc.returncode


def cmd_audit(args: argparse.Namespace) -> int:
    path, source = _resolve_config_path()
    validate_proc = _run(
        ["openclaw", "config", "validate", "--json"],
        env=_env_for_path(path),
    )
    payload: dict[str, Any] = {
        "configPath": str(path),
        "pathSource": source,
        "exists": path.exists(),
        "validate": _parse_validate_output(validate_proc, path),
    }
    if args.doctor:
        doctor_proc = _run(
            ["openclaw", "doctor", "--non-interactive"],
            env=_env_for_path(path),
        )
        combined = "\n".join(part for part in [doctor_proc.stdout, doctor_proc.stderr] if part)
        payload["doctor"] = {
            "command": "openclaw doctor --non-interactive",
            "exitCode": doctor_proc.returncode,
            "summary": _doctor_summary(combined),
        }
    print(_json_dumps(payload) if args.json else payload["configPath"])
    return 0 if payload["validate"].get("valid") else 1


def cmd_diff(args: argparse.Namespace) -> int:
    before = Path(args.before).expanduser()
    after = Path(args.after).expanduser()
    missing = [str(path) for path in [before, after] if not path.exists()]
    if missing:
        payload = {
            "ok": False,
            "error": "Missing diff input file(s)",
            "missing": missing,
        }
        print(_json_dumps(payload) if args.json else payload["error"])
        return 1

    before_text = before.read_text()
    after_text = after.read_text()
    diff_lines = list(
        difflib.unified_diff(
            before_text.splitlines(),
            after_text.splitlines(),
            fromfile=str(before),
            tofile=str(after),
            lineterm="",
        )
    )
    modified_paths = _collect_changed_paths(before_text, after_text)
    payload = {
        "before": str(before),
        "after": str(after),
        "changed": before_text != after_text,
        "modifiedPaths": modified_paths,
        "diff": diff_lines,
    }
    if args.json:
        print(_json_dumps(payload))
    else:
        print("\n".join(diff_lines))
    return 0


def _load_manifest(args: argparse.Namespace) -> dict[str, Any]:
    if args.manifest:
        return json.loads(Path(args.manifest).expanduser().read_text())
    if args.stdin:
        return json.load(sys.stdin)
    raise ValueError("report requires --manifest or --stdin")


def _listify(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def _render_items(title: str, items: list[Any]) -> list[str]:
    lines = [f"## {title}"]
    if not items:
        lines.append("- None")
        return lines
    for item in items:
        if isinstance(item, dict):
            summary = item.get("summary") or item.get("path") or _json_dumps(item)
            lines.append(f"- {summary}")
        else:
            lines.append(f"- {item}")
    return lines


def cmd_report(args: argparse.Namespace) -> int:
    manifest = _load_manifest(args)
    lines = ["# OpenClaw Config Audit Report", ""]

    lines.append("## Sources")
    for source in _listify(manifest.get("sources")):
        lines.append(f"- {source}")
    if not _listify(manifest.get("sources")):
        lines.append("- None provided")

    lines.extend(
        [
            "",
            "## Active Config",
            f"- Path: {manifest.get('configPath', 'unknown')}",
            f"- Backup: {manifest.get('backupPath', 'not created')}",
            "",
        ]
    )

    pre = manifest.get("preValidation", {})
    post = manifest.get("postValidation", {})
    lines.extend(
        [
            "## Validation",
            f"- Before: {'valid' if pre.get('valid') else 'invalid'}",
            f"- After: {'valid' if post.get('valid') else 'unknown'}",
            "",
        ]
    )

    lines.extend(_render_items("Startup Blockers", _listify(manifest.get("blockingIssues"))))
    lines.append("")
    lines.extend(_render_items("Auto Fixes", _listify(manifest.get("autoFixes"))))
    lines.append("")
    lines.extend(_render_items("Deferred Issues", _listify(manifest.get("deferredIssues"))))
    lines.append("")
    lines.extend(_render_items("Recommendations", _listify(manifest.get("recommendations"))))
    lines.append("")
    lines.extend(_render_items("Modified Paths", _listify(manifest.get("modifiedPaths"))))
    lines.append("")

    restart_needed = bool(manifest.get("restartNeeded"))
    restart_reason = manifest.get("restartReason") or "No restart required."
    lines.extend(
        [
            "## Restart",
            f"- Needed: {'yes' if restart_needed else 'no'}",
            f"- Reason: {restart_reason}",
            "",
        ]
    )

    print("\n".join(lines).rstrip())
    return 0


def _collect_changed_paths(before_text: str, after_text: str) -> list[str]:
    path_pattern = re.compile(r'^(\s*)"([^"]+)"\s*:')
    before_lines = before_text.splitlines()
    after_lines = after_text.splitlines()

    def paths_for(lines: list[str]) -> dict[int, str]:
        stack: list[tuple[int, str, str]] = []
        mapping: dict[int, str] = {}

        def current_context() -> str:
            if not stack:
                return "root"
            return stack[-1][1]

        for index, line in enumerate(lines):
            stripped = line.strip()
            while stack and stripped and stripped[0] in "}]":
                stack.pop()
                stripped = stripped[1:].lstrip()
            match = path_pattern.match(line)
            if match:
                indent = len(match.group(1))
                key = match.group(2)
                while stack and stack[-1][0] >= indent:
                    stack.pop()
                base_parts = [item[1] for item in stack if item[1] != "root"]
                current = ".".join(base_parts + [key]) if base_parts else key
                mapping[index] = current
                if stripped.endswith("{"):
                    stack.append((indent, current, "object"))
                elif stripped.endswith("["):
                    stack.append((indent, f"{current}[]", "array"))
            else:
                mapping[index] = current_context()
                leading = stripped[:1]
                indent = len(line) - len(line.lstrip())
                if leading == "{":
                    stack.append((indent, current_context(), "object"))
                elif leading == "[":
                    stack.append((indent, f"{current_context()}[]", "array"))
        return mapping

    before_map = paths_for(before_lines)
    after_map = paths_for(after_lines)
    diff = difflib.ndiff(before_lines, after_lines)
    changed: list[str] = []
    before_idx = 0
    after_idx = 0
    for line in diff:
        tag = line[:2]
        if tag == "  ":
            before_idx += 1
            after_idx += 1
        elif tag == "- ":
            changed.append(before_map.get(before_idx, "unknown"))
            before_idx += 1
        elif tag == "+ ":
            changed.append(after_map.get(after_idx, "unknown"))
            after_idx += 1
    ordered: list[str] = []
    seen: set[str] = set()
    for item in changed:
        if item not in seen:
            ordered.append(item)
            seen.add(item)
    return ordered


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="OpenClaw config guard helpers")
    subparsers = parser.add_subparsers(dest="command", required=True)

    resolve_parser = subparsers.add_parser("resolve-path")
    resolve_parser.add_argument("--json", action="store_true")
    resolve_parser.set_defaults(func=cmd_resolve_path)

    backup_parser = subparsers.add_parser("backup")
    backup_parser.add_argument("--path")
    backup_parser.add_argument("--json", action="store_true")
    backup_parser.set_defaults(func=cmd_backup)

    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("--path")
    validate_parser.add_argument("--doctor", action="store_true")
    validate_parser.add_argument("--json", action="store_true")
    validate_parser.set_defaults(func=cmd_validate)

    doctor_parser = subparsers.add_parser("doctor")
    doctor_parser.add_argument("--path")
    doctor_parser.add_argument("--json", action="store_true")
    doctor_parser.set_defaults(func=cmd_doctor)

    audit_parser = subparsers.add_parser("audit")
    audit_parser.add_argument("--doctor", action="store_true")
    audit_parser.add_argument("--json", action="store_true", default=True)
    audit_parser.set_defaults(func=cmd_audit)

    diff_parser = subparsers.add_parser("diff")
    diff_parser.add_argument("--before", required=True)
    diff_parser.add_argument("--after", required=True)
    diff_parser.add_argument("--json", action="store_true")
    diff_parser.set_defaults(func=cmd_diff)

    report_parser = subparsers.add_parser("report")
    report_group = report_parser.add_mutually_exclusive_group(required=True)
    report_group.add_argument("--manifest")
    report_group.add_argument("--stdin", action="store_true")
    report_parser.set_defaults(func=cmd_report)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
