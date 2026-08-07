# OpenCLI

**OpenCLI** is a CLI tool library that turns websites, browser sessions, Electron apps, and local tools into deterministic interfaces. It reuses logged-in browser states, automates live workflows, and crystallizes repeated actions into reusable CLI commands.

## Tags

🛠️ Productivity Tools | ✅ Verified

## Core Philosophy

OpenCLI's design philosophy emphasizes:
- **Account-safe**: Reuses Chrome/Chromium login state; credentials never leave the browser
- **Deterministic output**: Same command, same output schema — pipeable, scriptable, CI-friendly
- **Zero LLM cost**: No tokens consumed at runtime; run 10,000 times and pay nothing
- **AI Agent ready**: Provides API exploration, adapter generation, auth strategy discovery, and direct browser control

## Key Features & Workflow

1. **Built-in adapters**: 87+ pre-built adapters covering Bilibili, Zhihu, Xiaohongshu, Reddit, Twitter/X, HackerNews, and more
2. **Direct browser control**: `opencli browser` gives AI agents direct control — click, type, extract, screenshot
3. **Adapter generation**: Generate new adapters from real browser behavior via `explore`, `synthesize`, `generate`, `cascade`
4. **CLI Hub**: Unified discovery, auto-install, and passthrough for external CLI tools (gh, docker, obsidian, etc.)
5. **Desktop app control**: Drive Electron apps via CDP (Cursor, Codex, ChatGPT, Notion, etc.)

## Skills Library Overview

OpenCLI provides the following skills for AI agents:

- **opencli-usage**: Complete guide for running OpenCLI commands to interact with websites/desktop apps, covering 87+ adapters
- **opencli-browser**: Browser automation skill — navigate, click, type, extract, wait
- **opencli-explorer**: Full adapter exploration guide — API discovery, auth strategy, adapter writing, testing
- **opencli-oneshot**: Quick one-shot CLI generation — URL + goal description to generate adapter
- **opencli-autofix**: Automatic adapter repair — diagnose → patch → retry → file upstream issue
- **smart-search**: Smart search router — routes queries to optimal OpenCLI search sources by topic

## Installation & Support

OpenCLI supports the following AI editors and platforms:

- [Claude Code](../../claudecode/opencli/INSTALL-en.md)
- [Cursor](../../cursor/opencli/INSTALL-en.md)
- [Codex](../../codex/opencli/INSTALL-en.md)
- [OpenCode](../../opencode/opencli/INSTALL-en.md)
- [OpenClaw](../../openclaw/opencli/INSTALL-en.md)
- [Zerone](../../zerone/opencli/INSTALL-en.md)
- [Qoder](../../qoder/opencli/INSTALL-en.md)

---
For more information, visit: [GitHub - jackwener/OpenCLI](https://github.com/jackwener/OpenCLI)