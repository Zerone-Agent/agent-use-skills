# OpenClaw Config Guard

**OpenClaw Config Guard** is a safety-first maintenance skill for auditing and repairing OpenClaw configuration with deterministic validation, backups, rollback, and change reporting.

## Tags

⚙️ System Automation | ✅ Verified

## Core Philosophy
- **Audit before repair**: Validate the active configuration and classify findings before changing anything.
- **Trust official evidence**: Use official OpenClaw documentation and CLI output as the source of truth instead of memory.
- **Fix only proven blockers**: Auto-fix only startup-blocking issues when the correct repair is clearly documented.
- **Preserve recovery paths**: Create backups before writes, re-validate after changes, and roll back immediately if validation fails.

## Key Features & Workflow

1. **Active Config Resolution**: Detects the effective `openclaw.json` path with CLI-based lookup and a safe fallback.
2. **Deterministic Audit**: Wraps `openclaw config validate --json` and optional `openclaw doctor --non-interactive` into a consistent audit flow.
3. **Finding Classification**: Separates startup blockers from non-blocking recommendations so repairs stay conservative.
4. **Safe Repair Boundaries**: Prefers `openclaw config set` and `openclaw config unset`, avoids undocumented edits, and never runs `openclaw doctor --fix` by default.
5. **Backup and Rollback**: Creates timestamped backups before writes and restores them if post-change validation fails.
6. **Change Reporting**: Produces diffs, modified path summaries, and report-ready output for reviewable repair decisions.

## Skills Library Overview

- **Primary Skill**: `openclaw-config-guard` defines the audit-first repair workflow and reporting requirements.
- **Helper Script**: `scripts/config_guard.py` provides deterministic commands for path resolution, audit, validation, backup, diff, and reporting.
- **Reference Pack**: `references/official-sources.md` lists the OpenClaw documentation that must be consulted before making config judgments.

## Installation & Support

OpenClaw Config Guard supports the following AI editors and platforms:
- [OpenClaw](../../openclaw/openclaw-config-guard/INSTALL-en.md)

---
For more information, visit: [GitHub - Zerone-Agent/agent-use-skills](https://github.com/Zerone-Agent/agent-use-skills)
