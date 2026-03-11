# Proactive Agent

**Proactive Agent** is an architecture and skill set designed to transform AI agents from "task followers" into "proactive partners." It encompasses a complete system for persistent memory management, self-improvement guidelines, and security hardening, ensuring agents can anticipate user needs, recover swiftly from context loss, and continuously optimize their performance.

## Core Philosophy

- **Anticipate Needs**: Instead of just asking "What should I do?", proactively think "What can I build that would genuinely delight my human?"
- **State Persistence**: Uses the **WAL (Write-Ahead Logging)** protocol and **Working Buffer** to ensure critical decisions and task progress "survive" context truncations in long conversations.
- **Relentless Resourcefulness**: Try 5-10 different approaches or tool combinations before reporting that a task "cannot be done."
- **Safe Evolution**: Uses ADL (Anti-Drift Limits) and VFM (Value-First Modification) protocols to ensure the agent stays stable and aligned with goals during self-optimization.

## Key Features & Workflow

1. **Three-Tier Memory**:
    - `SESSION-STATE.md`: Active "RAM" for the current task.
    - `memory/` (Daily Logs): Raw session captures.
    - `MEMORY.md`: Curated long-term wisdom and experience.
2. **WAL Protocol**: Logs corrections, preferences, decisions, and specific values to `SESSION-STATE.md` BEFORE responding to the human.
3. **Working Buffer**: Activates after 60% context usage to log exchanges in real-time, acting as a lifeline for recovery after context compaction.
4. **Autonomous Crons**: Distinguishes between "prompting jobs" and "execution jobs," using isolated sessions (`agentTurn`) to handle background maintenance autonomously.
5. **Reverse Prompting**: Actively asks questions about user preferences and missing information to eliminate unknown unknowns.

## Skills Library Overview

- **Core Assets**: Includes templates for `ONBOARDING.md`, `SOUL.md`, `AGENTS.md`, and other foundational definition files.
- **Toolkit**: Includes scripts like `security-audit.sh` and heartbeat check templates.
- **Protocols**: A suite of standardized agent behavior protocols including WAL, ADL, VFM, and more.

## Installation & Support

Proactive Agent currently supports the following platform:

- [OpenClaw](../../openclaw/proactive-agent/INSTALL-en.md)

---
For more information, visit: [Hal Stack 🦞](https://github.com/halthelobster/hal-stack)
