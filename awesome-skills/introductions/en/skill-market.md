# Skill Market

**Skill Market** is an automated skill discovery and installation skill that enables AI Agents to find, explore, and install new skills directly from the Zerone Skill Market (https://api.zerone.market/api).

## Tags

💻 Dev & Testing | ✅ Verified

## Core Philosophy
- **Automated Integration**: Eliminates manual downloads and configurations, providing a one-click experience for skill expansion.
- **Environment Awareness**: Automatically detects the current Agent framework (e.g., Claude Code, Cursor) and matches the best installation plan.
- **Progressive Expansion**: Supports on-demand discovery, avoiding the loading of unnecessary skill scripts in the initial context.

## Key Features & Workflow
1. **Browse & Discover**: Use `market.py list` to get a complete list of available skills and their detailed descriptions.
2. **Detail Query**: Learn more about a specific skill's functions, supported frameworks, and versioning via `info <skill-name>`.
3. **Compatibility Checking**: Automatically verifies compatibility between the current Agent environment and the skill before installation.
4. **Secure Installation**: Guides the user through a verified installation process, requiring explicit consent to execute downloaded scripts into the `.agent/skills/` directory.

## Skills Library Overview
- **Market API Interaction**: Encapulates the complete communication logic with the Zerone Market backend.
- **Local Environment Management**: Handles local skill directory initialization, skill downloads, and framework-specific configuration updates.

## Installation & Support
Skill Market supports the following AI editors and platforms:
- [Claude Code](../../claudecode/skill-market/INSTALL-en.md)
- [Cursor](../../cursor/skill-market/INSTALL-en.md)
- [Codex](../../codex/skill-market/INSTALL-en.md)
- [OpenCode](../../opencode/skill-market/INSTALL-en.md)
- [OpenClaw](../../openclaw/skill-market/INSTALL-en.md)
- [Qoder](../../qoder/skill-market/INSTALL-en.md)

---
For more information, visit: [GitHub - Zerone Agent](https://github.com/zerone-agent/agent-use-skills)
