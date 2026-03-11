# AGENTS.md - AI Agent Guidelines

## Project Overview

AgentUse Skills is a curated library of reusable procedural knowledge for AI Agents. This repository provides standardized skills that enable AI coding agents to follow structured workflows for software development tasks.

## Build/Lint/Test Commands

This is a documentation-only repository with no build or test pipeline. The repository structure is validated through the following:

### Repository Validation
```bash
# List all markdown files to verify structure
find . -name "*.md" -type f

# Verify skill file structure
ls -la .agent/skills/*/SKILL.md
ls -la awesome-skills/*/superpowers/INSTALL-*.md
```

### Running Single Validation Checks
There are no automated tests. Manual validation includes:
1. Verify each skill has both Chinese (`-zh.md`) and English (`-en.md`) versions
2. Verify installation guides exist for each supported platform
3. Check that all internal links are valid

## Code Style Guidelines

### File Structure Conventions

**Directory Structure:**
```
awesome-skills/
├── skills/
│   ├── zh/<skill-name>.md      # Chinese introduction
│   └── en/<skill-name>.md      # English introduction
├── claudecode/<skill-name>/
│   ├── INSTALL-zh.md
│   └── INSTALL-en.md
├── cursor/<skill-name>/
├── codex/<skill-name>/
├── opencode/<skill-name>/
├── openclaw/<skill-name>/
└── qoder/<skill-name>/
```

**Naming Conventions:**
- Use **kebab-case** for all file and directory names (e.g., `superpowers`, `ui-ux-pro-max-skill`)
- Skill names in `SKILL.md` use lowercase with hyphens
- Platform directories are lowercase (e.g., `claudecode`, `opencode`)

### Documentation Style

**Skill Introduction Documents (`skills/{zh,en}/<skill-name>.md`):**
```markdown
# <Skill Name>

**<Skill Name>** is ... (one-line summary)

## Core Philosophy
- Point 1
- Point 2

## Key Features & Workflow
1. **Feature A**: Description...
2. **Feature B**: Description...

## Skills Library Overview
- **Category 1**: List of sub-skills...

## Installation & Support
<Skill Name> supports the following AI editors and platforms:
- [Claude Code](../../claudecode/<skill-name>/INSTALL-en.md)
- [Cursor](../../cursor/<skill-name>/INSTALL-en.md)
- [OpenCode](../../opencode/<skill-name>/INSTALL-en.md)

---
For more information, visit: [GitHub - <repo>](<url>)
```

**Installation Guide Documents (`INSTALL-*.md`):**
- Include numbered steps with clear commands
- Add verification steps to confirm successful installation
- Link to detailed documentation when applicable
- End with reference link to original project

### Bilingual Requirements

- All documents must exist in **both Chinese** (`-zh.md`) and **English** (`-en.md`)
- Content structure must match between language versions
- Use consistent terminology across translations
- Chinese documents go in `zh/` directories, English in `en/`

### SKILL.md Format

Each skill must include a `SKILL.md` file with:
1. YAML frontmatter with `name` and `description`
2. Clear workflow steps with numbered phases
3. Directory structure diagrams where applicable
4. Important notes and edge cases

Example frontmatter:
```yaml
---
name: skill-name
description: A standardized workflow for...
---
```

### Markdown Formatting

- Use GitHub-flavored markdown
- Headers use ATX style (`#`, `##`, `###`)
- Code blocks specify language for syntax highlighting
- Tables use standard markdown table syntax
- Links use relative paths within the repository
- Maximum line length: 120 characters (except code blocks)

### Git Conventions

**Branch Naming:**
- `feature/<skill-name>` - Adding new skills
- `docs/<description>` - Documentation updates
- `fix/<description>` - Bug fixes

**Commit Messages:**
- Use conventional commits format: `type(scope): description`
- Types: `feat`, `docs`, `fix`, `refactor`, `chore`
- Scope: skill name or affected area

### Content Guidelines

**Do:**
- Keep skill descriptions concise and actionable
- Use active voice in workflow instructions
- Include verification steps for all procedures
- Link to official documentation for external references
- Maintain parallel structure in bilingual content

**Don't:**
- Embed installation commands directly in introduction docs (use hyperlinked lists instead)
- Create installation guides for unsupported platforms
- Mix Chinese and English content in the same file
- Use absolute URLs for internal repository links

### Quality Checklist

Before submitting any skill:
- [ ] Both language versions created with matching structure
- [ ] Installation guides for all supported platforms
- [ ] All internal links verified
- [ ] Kebab-case naming throughout
- [ ] SKILL.md includes complete workflow
- [ ] References link to official sources

### Platform Support Matrix

When documenting platform support, verify actual compatibility:
- **Claude Code**: Uses `/plugin add` or `/plugin-add` commands
- **Cursor**: Uses `/plugin-add` in Agent mode
- **OpenCode**: Uses `skill` tool with file-based loading
- **Codex**: File-based skill loading
- **OpenClaw**: Platform-specific integration
- **Qoder**: Platform-specific integration

Only create installation guides for platforms explicitly supported by the skill.

---

## Existing Rules

No Cursor rules (`.cursor/rules/` or `.cursorrules`) or Copilot rules (`.github/copilot-instructions.md`) are currently defined in this repository.
