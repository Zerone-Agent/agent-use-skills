# AgentUse Share

**AgentUse Share** is a standardized workflow skill designed to help developers and AI Agents efficiently contribute new AI coding skills to the `awesome-skills` repository. it covers the entire process from research and initial drafting to generating platform-specific installation guides.

## Tags

Dev & Testing | Verified

## Core Philosophy

- **Standardization**: Defines a unified directory structure and documentation specification for Skills, ensuring high-quality community contributions.
- **Research-Driven**: Emphasizes in-depth research based on original `SKILL.md` files or official repositories to ensure information accuracy.
- **Multi-Platform Support**: Automatically generates installation guides for different AI editors (e.g., Claude Code, Cursor, etc.) for each Skill.
- **Bilingual**: Mandates the synchronized generation of both Chinese and English documentation to broaden the skill's reach.

## Key Features & Workflow

1. **Target Skill Research**: Automatically identifies if an original `SKILL.md` exists within the repository, or retrieves core definitions, design philosophies, and features via web search.
2. **Chinese Introduction Generation**: Distills research findings into a standardized Chinese introduction document.
3. **English Introduction Generation**: Synchronously translates and generates the corresponding English introduction, ensuring content consistency.
4. **Platform-Specific Guides**: Identifies supported AI editor platforms and generates exclusive bilingual installation and verification guides for each.
5. **Cross-Check**: Automatically verifies link validity between documents, content accuracy, and bilingual alignment.

## Skills Library Overview

This skill primarily includes the following sub-processes:
- **Research Sub-skill**: Utilizes tools like `read_url_content` to fetch external skill information.
- **Writing Sub-skill**: Professional writing based on the `content-research-writer` style.
- **Installation Templates**: Standardized templates for various platforms (Claude Code, Cursor, Codex, OpenCode, etc.).

## Installation & Support

AgentUse Share supports the following AI editors and platforms:
- [Claude Code](../../claudecode/agentuse-share/INSTALL-en.md)
- [Cursor](../../cursor/agentuse-share/INSTALL-en.md)
- [Codex](../../codex/agentuse-share/INSTALL-en.md)
- [OpenCode](../../opencode/agentuse-share/INSTALL-en.md)
- [OpenClaw](../../openclaw/agentuse-share/INSTALL-en.md)
- [Qoder](../../qoder/agentuse-share/INSTALL-en.md)

---
For more information, visit: [GitHub - Zerone-Agent/agent-use-skills](https://github.com/Zerone-Agent/agent-use-skills)
