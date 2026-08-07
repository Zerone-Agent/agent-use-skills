# Obsidian CLI - Agent-Ready Certification

**Obsidian CLI** has officially passed the **Agent-Ready** certification!

📺 **Demo Video**：[Watch on Bilibili → Obsidian CLI × AI Agent Demo](https://www.bilibili.com/video/BV1ydA7zUE5A)

Obsidian 1.12 (released February 27, 2026) introduced an official CLI and TUI (Terminal User Interface), making it one of the first knowledge management applications natively optimized for AI Agent interaction.

## Certification Highlights

- **Native CLI Support**: Directly manipulate your vault via the `obsidian` command-line tool — no raw file parsing needed.
- **130+ Commands**: Covers all core features — note CRUD, daily notes, search, properties, tags, tasks, link analysis, sync management, developer tools, and more.
- **Semantic Search**: Leverages Obsidian's own search index for structured, tag-aware, link-aware queries.
- **Graph Queries**: Access the knowledge graph via `obsidian backlinks` and `obsidian orphans` without scanning every file.
- **Exceptional Performance**: Orphan detection is **60x faster** than grep; token consumption can be reduced by up to **70,000x**.
- **Ecosystem Integration**: Natively supported by Claude Code, Cursor, Codex, OpenCode, OpenClaw, Zerone, Qoder, and more.

## Why is it Agent-Ready?

Obsidian CLI successfully meets all the core criteria of the Agent-Ready certification:

- **Atomic Action Exposure**: Core features are fully exposed via 130+ CLI commands — `obsidian search`, `obsidian read`, `obsidian create`, `obsidian append`, `obsidian daily:prepend`, `obsidian backlinks`, `obsidian orphans`, `obsidian eval` — requiring no UI interaction.
- **Structured Feedback**: Search results and graph queries are emitted as structured text to `stdout`, with `format=json` support for JSON output, ready for Agent parsing and consumption.
- **Security Guardrails**: Requires the Obsidian desktop app to be running and users to explicitly enable and register the CLI via settings, keeping humans in full control.
- **Verified Integration**: Claude Code, Cursor, OpenCode, and others can load the skill natively; the community has built MCP wrappers (`@joemugen/obsidian-cli-mcp`), Agent Client plugins, and REST API bridges.

## Core CLI Commands

| Command | Description |
|---------|-------------|
| `obsidian search query="<text>"` | Search notes using Obsidian's semantic index |
| `obsidian read path="<path>"` | Read the content of a specific note |
| `obsidian create path="<path>"` | Create a new note |
| `obsidian append path="<path>" content="..."` | Append content to a note |
| `obsidian daily:read` | Read today's daily note |
| `obsidian daily:append content="..."` | Append content to today's daily note |
| `obsidian backlinks path="<path>"` | Query backlinks for a given note |
| `obsidian orphans` | List all orphaned notes in the vault |
| `obsidian tasks` | Query all tasks across the vault |
| `obsidian eval code="<js>"` | Execute JavaScript (Obsidian API) |

## Performance Benchmarks

| Task | Traditional (grep) | Obsidian CLI | Improvement |
|------|--------------------|--------------|-------------|
| Orphan note detection | 15.6s | 0.26s | **60x** |
| Vault full-text search | 1.95s | 0.32s | **6x** |
| Token usage (MCP vs CLI) | ~7M tokens | ~100 tokens | **70,000x** |

---

- [Obsidian CLI Skill - GitHub](https://github.com/pablo-mano/Obsidian-CLI-skill)
- [Obsidian CLI Official Docs](https://help.obsidian.md/cli)
- [Obsidian 1.12 Changelog](https://obsidian.md/changelog/2026-02-27-desktop-v1.12.4/)
- [Obsidian CLI: Why Your AI Agent Just Got 70,000x Cheaper to Run](https://prokopov.me/posts/obsidian-cli-changes-everything-for-ai-agents/)
