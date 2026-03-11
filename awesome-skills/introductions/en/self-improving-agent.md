# Self-Improving Agent

**Self-Improving Agent** is a skill designed to capture learnings, errors, and corrections to enable continuous improvement of AI agents.

## Core Philosophy

- **Continuous Evolution**: Enables AI to learn from operational failures, user corrections, knowledge gaps, and best practices to avoid repeating mistakes.
- **Knowledge Accumulation**: Distills and promotes scattered learning points into project memory (e.g., `CLAUDE.md`) or global workspace guidelines (e.g., `SOUL.md`).
- **Multi-Agent Collaboration**: Supports sharing learning outcomes across different sessions and agents, especially on platforms like OpenClaw.

## Key Features & Workflow

1. **Structured Logging**: Provides standardized templates for `LEARNINGS.md` (learnings), `ERRORS.md` (errors), and `FEATURE_REQUESTS.md` (feature requests).
2. **Learning Promotion**: Automatically or manually elevates learning points into durable prompt guidance based on recurrence count and priority.
3. **Automatic Triggers & Hooks**: Supports automatic reminders via Git hooks or Agent submission hooks (e.g., `UserPromptSubmit`).
4. **Skill Extraction**: Supports one-click extraction of mature and generic solutions into independent, reusable skills.

## Skills Library Overview

- **Log Management**: Structured Markdown files located in the `.learnings/` directory.
- **Script Toolkit**: Includes `activator.sh` (activator), `error-detector.sh` (error detector), and `extract-skill.sh` (skill extraction script).
- **Workspace Integration**: Deep integration with OpenClaw files such as `AGENTS.md`, `SOUL.md`, and `TOOLS.md`.

## Installation & Support

Self-Improving Agent currently primarily supports the following platform:

- [OpenClaw](../../openclaw/self-improving-agent/INSTALL-en.md)

---
For more information, visit: [GitHub - peterskoett/self-improving-agent](https://github.com/peterskoett/self-improving-agent)
