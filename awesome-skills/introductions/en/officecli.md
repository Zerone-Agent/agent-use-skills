# OfficeCLI

**OfficeCLI** is the world's first Office suite purpose-built for AI agents, enabling them to create, read, and edit Word, Excel, and PowerPoint documents with a single command. Open-source, single binary, no Office installation required, zero dependencies.

## Tags

🗂️ Documents & Office | ✅ Verified

## Core Philosophy

- **AI-Native Design**: All commands support structured `--json` output, path-based addressing, and progressive complexity (L1 Read → L2 DOM → L3 Raw XML)
- **Zero Dependencies**: Single self-contained binary with embedded .NET runtime, cross-platform (macOS / Linux / Windows)
- **Built-in Rendering Engine**: No Office needed — agents can *see* their output (HTML / PNG / live preview). The render → look → fix loop works in CI, Docker, and headless environments
- **Self-Healing Workflow**: Structured error codes with suggestions enable agents to self-correct without human intervention

## Key Features & Workflow

1. **Three-Layer Architecture**: L1 semantic views (`view`) → L2 DOM operations (`get`/`set`/`add`/`remove`) → L3 raw XML (`raw`/`raw-set`)
2. **Built-in Rendering Engine**: `view html` / `view screenshot` / `watch` natively output HTML and PNG with live preview support
3. **Formula & Pivot Engine**: 150+ Excel functions auto-evaluated on write; native OOXML pivot tables with one command
4. **Template Merge**: `merge` replaces `{{key}}` placeholders — design once, fill N times
5. **Round-trip Dump**: `dump` serializes documents into replayable batch JSON for learning from existing documents
6. **MCP Server**: Built-in MCP support — register with one command for Claude Code / Cursor / VS Code etc.
7. **Resident Mode & Batch**: Keep documents in memory for near-zero latency; batch mode for atomic multi-command execution
8. **Specialized Sub-skills**: Academic papers, pitch decks, Morph animations, 3D presentations, financial models, data dashboards, and more

## Skills Library Overview

- **Word (.docx)**: Paragraphs, tables, styles, headers/footers, images, equations, comments, footnotes, watermarks, bookmarks, TOC, charts, hyperlinks, sections, form fields, content controls, fields, OLE objects, full i18n & RTL support
- **Excel (.xlsx)**: Cells, sheets, tables, sort, conditional formatting, charts, pivot tables, slicers, named ranges, data validation, images, sparklines, comments, autofilter, shapes, CSV import
- **PowerPoint (.pptx)**: Slides, shapes, pictures, tables, charts, animations, Morph transitions, 3D models, slide zoom, equations, themes, connectors, video/audio, groups, notes, comments, placeholders

## Installation & Support

OfficeCLI supports the following AI editors and platforms:

- [Claude Code](../../claudecode/officecli/INSTALL-en.md)
- [Cursor](../../cursor/officecli/INSTALL-en.md)
- [Codex](../../codex/officecli/INSTALL-en.md)
- [OpenCode](../../opencode/officecli/INSTALL-en.md)
- [OpenClaw](../../openclaw/officecli/INSTALL-en.md)
- [Zerone](../../zerone/officecli/INSTALL-en.md)
- [Qoder](../../qoder/officecli/INSTALL-en.md)

---
For more information, visit: [GitHub - iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI)
