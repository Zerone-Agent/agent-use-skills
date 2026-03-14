---
name: openclaw-config-guard
author: soal2  (https://github.com/soal2)
description: Audit and safely repair OpenClaw configuration with deterministic validation, backups, rollback, and change reporting. Use when asked to review or modify `openclaw.json`, check whether OpenClaw can still start, safely fix startup-blocking config errors, or audit OpenClaw config before deciding on changes.
---

# OpenClaw Config Guard

Audit first. Repair only when the fix is proven. Protect startup over aesthetics.

## Required Sources

Before making any judgment, open the official docs listed in [references/official-sources.md](references/official-sources.md). Treat them as the source of truth for schema, allowed values, and repair guidance. Do not rely on memory for config rules.

## Workflow

1. Resolve the active config path:

```bash
python3 "<skill-dir>/scripts/config_guard.py" resolve-path --json
```

If that fails, fall back to `~/.openclaw/openclaw.json`.

2. Run a deterministic audit before touching the file:

```bash
python3 "<skill-dir>/scripts/config_guard.py" audit --doctor
```

This wraps:
- `openclaw config validate --json`
- optional `openclaw doctor --non-interactive`

3. Classify findings:
- `startup blockers`: JSON5 parse failures, schema validation failures, unknown keys, wrong types, invalid enum values, missing required structure, or clearly conflicting settings that prevent startup.
- `recommendations`: suspicious but non-blocking items such as duplicate plugin IDs, stale-but-working config, style cleanup, or non-critical hardening suggestions.

4. Decide whether you may auto-fix:
- Only auto-fix if the issue is a startup blocker.
- Only auto-fix if the docs or CLI output clearly show the correct repair.
- Prefer `openclaw config set` / `openclaw config unset` for exact path edits.
- Use manual JSON5 edits only when the CLI cannot express the required change and preserving comments or structure matters.
- Never run `openclaw doctor --fix` by default.
- Never restart OpenClaw by default.

5. Backup before any write:

```bash
python3 "<skill-dir>/scripts/config_guard.py" backup --json
```

6. Re-validate after any write:

```bash
python3 "<skill-dir>/scripts/config_guard.py" validate --doctor --json
```

If post-change validation fails, roll back immediately from the backup and say so in the report.

7. Summarize what changed:

```bash
python3 "<skill-dir>/scripts/config_guard.py" diff --before /path/to/before --after /path/to/after --json
```

If you want a deterministic report frame, prepare a JSON manifest and run:

```bash
python3 "<skill-dir>/scripts/config_guard.py" report --manifest /path/to/manifest.json
```

`<skill-dir>` means the directory that contains this `SKILL.md`. Resolve relative paths against this skill directory instead of assuming any environment variable is set.

## Decision Boundaries

- Do not change non-blocking issues without user approval.
- Do not guess undocumented keys or values.
- Do not rewrite the whole config just to normalize formatting.
- Do not claim success without rerunning validation.
- Do not leave the user without a backup path, modified paths list, and post-change validation result.

## Report Requirements

The final Markdown report must include:
- official sources consulted
- active config path
- pre-change validation result
- startup blockers found
- automatic fixes applied
- issues intentionally not auto-fixed and why
- non-blocking recommendations for user decision
- modified config paths
- backup path
- post-change validation result
- whether manual restart is needed, and why

## Resources

- Official source list: [references/official-sources.md](references/official-sources.md)
- Deterministic helper script: [scripts/config_guard.py](scripts/config_guard.py)
