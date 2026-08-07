# Obsidian CLI

**Obsidian CLI** is the official command-line tool from Obsidian (v1.12+) that enables AI Agents to control the Obsidian desktop app directly from the terminal, providing full vault manipulation capabilities.

## Tags

🗂️ Documents & Office | ✅ Verified

## Core Philosophy

- Communicates with a running Obsidian desktop instance via IPC for zero-latency real-time operations
- All parameters use unified `key=value` syntax, with plain text output by default — perfect for Unix pipes
- Covers all core Obsidian features, from note CRUD to plugin management, sync control, and developer tools

## Key Features & Workflow

1. **Note Read/Write & Management**: Read, create, append, move, rename, delete notes with template support
2. **Daily Notes**: Read today's note, append content, insert tasks into daily notes
3. **Full-Text Search**: Path-scoped search, result limits, JSON output, context-aware search
4. **Properties & Tags**: Read/write frontmatter properties, tag statistics and filtering
5. **Task Management**: Cross-vault task queries, filter by file/daily note, toggle task completion
6. **Link Analysis**: Backlinks, orphaned notes, unresolved links, dead-end detection
7. **Sync Management**: Obsidian Sync status check, version history, file restoration
8. **Developer Tools**: JavaScript execution (eval), screenshots, DOM/CSS inspection, console logging
9. **Automation Integration**: Supports cron jobs, AI Agent workflows, headless server operation

## Command Overview

The CLI provides **130+ commands** across these groups:

- **files**: Note CRUD and file discovery
- **daily**: Daily note operations
- **search**: Full-text search
- **properties / tags**: Metadata and tag management
- **tasks**: Task querying and management
- **links**: Graph and link analysis
- **bookmarks / templates / plugins**: Bookmark, template, and plugin management
- **sync / history**: Sync control and file version recovery
- **dev**: JavaScript execution, screenshots, debugging tools
- **vault**: Vault info and app control

## Installation & Support

Obsidian CLI supports the following AI editors and platforms:

- [Claude Code](../../claudecode/obsidian-cli/INSTALL-en.md)
- [Cursor](../../cursor/obsidian-cli/INSTALL-en.md)
- [Codex](../../codex/obsidian-cli/INSTALL-en.md)
- [OpenCode](../../opencode/obsidian-cli/INSTALL-en.md)
- [OpenClaw](../../openclaw/obsidian-cli/INSTALL-en.md)
- [Zerone](../../zerone/obsidian-cli/INSTALL-en.md)
- [Qoder](../../qoder/obsidian-cli/INSTALL-en.md)

---
For more information, visit: [GitHub - pablo-mano/Obsidian-CLI-skill](https://github.com/pablo-mano/Obsidian-CLI-skill)
