# Obsidian

**Obsidian** is a skill designed to work with Obsidian vaults (plain Markdown notes) and automate tasks via `obsidian-cli`. It enables AI agents to manage, search, and update content within a local knowledge base.

## Tags

Document & Office | Pending Verification

## Core Philosophy

- **Local-First**: An Obsidian vault is just a normal folder on disk. This skill respects this by directly operating on `.md` files or interacting with the Obsidian desktop app via URI protocols.
- **Link Integrity**: When moving or renaming notes, it uses `obsidian-cli` to automatically update `[[wikilinks]]` across the entire vault, ensuring your knowledge graph remains intact.
- **Config-Aware**: Automatically identifies active vault paths from `obsidian.json`, avoiding the need for hardcoded paths.

## Key Features & Workflow

1. **Smart Search**: Supports searching by note titles (`search`) and full-text content retrieval (`search-content`).
2. **Automated Creation**: Quickly create notes with specific content through commands and optionally open them in the desktop client.
3. **Safe Refactoring**: Provides secure move and rename functionality that automatically handles link updates between notes.
4. **Flexible Editing**: Supports direct modification of `.md` files using file editors; Obsidian will pick up changes in real-time.

## Skills Library Overview

- **Core Commands**: Full encapsulation of `obsidian-cli` features.
- **Vault Management**: Automatic identification and switching between different Obsidian vaults.
- **Link Maintenance**: Handles complex note movement and renaming logic.

## Installation & Support

The Obsidian skill currently supports the following platform:

- [OpenClaw](../../openclaw/obsidian/INSTALL-en.md)

---
For more information, visit: [Obsidian Official Help](https://help.obsidian.md)
