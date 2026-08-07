# Repository Directory Structure

```
awesome-skills/
├── skills/                        # Skill SKILL.md & scripts
│   └── <skill-name>/              # Skill source directory
│       ├── SKILL.md               #   Required: Skill definition with YAML frontmatter
│       ├── _meta.json             #   Optional: Metadata for skill market
│       ├── scripts/               #   Optional: Python/JS/Shell scripts
│       ├── assets/                #   Optional: Static files (templates, images)
│       ├── references/            #   Optional: Reference documentation
│       ├── agents/                #   Optional: Agent configuration files
│       └── requirements.txt       #   Optional: Python dependencies
├── introductions/                 # Skill introduction documents
│   ├── en/                        # English introductions
│   │   └── <skill-name>.md
│   └── zh/                        # Chinese introductions
│       └── <skill-name>.md
├── claudecode/                    # Claude Code platform install guides
│   └── <skill-name>/
│       ├── INSTALL-en.md
│       └── INSTALL-zh.md
├── codex/                         # Codex platform install guides
│   └── <skill-name>/
│       ├── INSTALL-en.md
│       └── INSTALL-zh.md
├── cursor/                        # Cursor platform install guides
│   └── <skill-name>/
│       ├── INSTALL-en.md
│       └── INSTALL-zh.md
├── openclaw/                      # OpenClaw platform install guides
│   └── <skill-name>/
│       ├── INSTALL-en.md
│       └── INSTALL-zh.md
├── zerone/                     # Zerone platform install guides
│   └── <skill-name>/
│       ├── INSTALL-en.md
│       └── INSTALL-zh.md
├── opencode/                      # OpenCode platform install guides
│   └── <skill-name>/
│       ├── INSTALL-en.md
│       └── INSTALL-zh.md
└── qoder/                         # Qoder platform install guides
    └── <skill-name>/
        ├── INSTALL-en.md
        └── INSTALL-zh.md
```

## Naming Conventions

- Use **kebab-case** for all file and directory names (e.g., `superpowers`, `ui-ux-pro-max-skill`)
- Skill names in `SKILL.md` use lowercase with hyphens
- Platform directories are lowercase (e.g., `claudecode`, `opencode`)
- Script files use kebab-case (e.g., `md_to_docx.py`, `generate_image.py`)

## Platform Install Guide Paths

| Platform    | English                                            | Chinese                                            |
|-------------|----------------------------------------------------|----------------------------------------------------|
| Claude Code | `claudecode/<skill-name>/INSTALL-en.md`            | `claudecode/<skill-name>/INSTALL-zh.md`            |
| Codex       | `codex/<skill-name>/INSTALL-en.md`                 | `codex/<skill-name>/INSTALL-zh.md`                 |
| Cursor      | `cursor/<skill-name>/INSTALL-en.md`                | `cursor/<skill-name>/INSTALL-zh.md`                |
| OpenClaw    | `openclaw/<skill-name>/INSTALL-en.md`              | `openclaw/<skill-name>/INSTALL-zh.md`              |
| Zerone   | `zerone/<skill-name>/INSTALL-en.md`             | `zerone/<skill-name>/INSTALL-zh.md`             |
| OpenCode    | `opencode/<skill-name>/INSTALL-en.md`              | `opencode/<skill-name>/INSTALL-zh.md`              |
| Qoder       | `qoder/<skill-name>/INSTALL-en.md`                 | `qoder/<skill-name>/INSTALL-zh.md`                 |
```