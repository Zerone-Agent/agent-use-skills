---
name: agentuse-share
description: A standardized workflow for adding a new AI coding skill to the awesome-skills repository, including research, writing introduction docs, creating platform-specific installation guides, and generating bilingual (Chinese & English) versions.
---

# AgentUse Share Skill

This skill defines the complete standardized workflow for adding a new Skill to the `awesome-skills` repository.

## Repository Directory Structure

```
awesome-skills/
├── skills/                        # Skill SKILL.md & scripts
│   ├── <skill-name>/              # (Optional) Skill source directory
│   │   └── SKILL.md               #   Original SKILL.md provided by the skill author
├── introductions/                 # Skill introduction documents
│   └── en/                        # English introductions
│       └── <skill-name>.md
│   ├── zh/                        # Chinese introductions
│   │   └── <skill-name>.md
├── claudecode/                    # Claude Code platform install guides
│   └── <skill-name>/
│       ├── INSTALL-zh.md
│       └── INSTALL-en.md
├── codex/                         # Codex platform install guides
│   └── <skill-name>/
│       └── INSTALL-en.md
│       ├── INSTALL-zh.md
├── cursor/                        # Cursor platform install guides
│   └── <skill-name>/
│       └── INSTALL-en.md
│       ├── INSTALL-zh.md
├── openclaw/                      # OpenClaw platform install guides
│   └── <skill-name>/
│       └── INSTALL-en.md
│       ├── INSTALL-zh.md
├── opencode/                      # OpenCode platform install guides
│   └── <skill-name>/
│       └── INSTALL-en.md
│       ├── INSTALL-zh.md
└── qoder/                         # Qoder platform install guides
    └── <skill-name>/
        └── INSTALL-en.md
        ├── INSTALL-zh.md
```

## Workflow

### Step 1: Research the Target Skill

First, check whether a `SKILL.md` file is already provided within this repository at `awesome-skills/skills/<skill-name>/SKILL.md`.

#### Case A: SKILL.md Already Exists in the Repository

If `awesome-skills/skills/<skill-name>/SKILL.md` exists, use it as the **primary source of information**:

- Read the `SKILL.md` file directly — it typically contains a comprehensive description of the skill, including its purpose, features, usage instructions, and workflow.
- Supplement with the skill's GitHub repository or official documentation **only if** the SKILL.md does not contain sufficient information (e.g., missing supported platforms list, or lacking detail on core philosophy).
- Focus on extracting the following from the SKILL.md:
  - **What it is**: The core definition and positioning of the Skill.
  - **Core philosophy**: What are the design principles.
  - **Key features and workflow**: What capabilities it provides and how it operates.
  - **Skills library composition**: What sub-skills are included.
  - **Supported platforms**: Determine exactly which AI coding agents/platforms the Skill supports. This is critical — only create installation guides for platforms that are explicitly supported. Skip any unsupported platforms entirely.

> **Tip**: The SKILL.md is typically more detailed and authoritative than a README. Use it as the foundation for writing the introduction documents in Steps 2 and 3 and the installation guides (INSTALL.md) in Step 4. **Please refer to the `content-research-writer` skill's writing style to ensure the generated documentation is professional, structured, and includes clear action items.**

#### Case B: No SKILL.md in the Repository

If no `SKILL.md` exists under `awesome-skills/skills/<skill-name>/`:

- Visit the target Skill's **GitHub repository** or official documentation.
- Use the `read_url_content` tool to fetch the README page content.
- Focus on gathering the following information:
  - **What it is**: The core definition and positioning of the Skill.
  - **Core philosophy**: What are the design principles.
  - **Key features and workflow**: What capabilities it provides and how it operates.
  - **Skills library composition**: What sub-skills are included.
  - **Supported platforms**: Determine exactly which AI coding agents/platforms the Skill supports (e.g., Claude Code, Cursor, Codex, OpenCode, OpenClaw, Qoder). This is critical — only create installation guides for platforms that are explicitly supported. Skip any unsupported platforms entirely.

### Step 2: Write the Chinese Introduction Document

> If a `SKILL.md` was found in Step 1 (Case A), base the introduction on the information from that file. Summarize and restructure the content to fit the introduction template below. Do NOT copy the SKILL.md verbatim — instead, distill it into a concise, reader-friendly introduction.

- **File path**: `awesome-skills/introductions/zh/<skill-name>.md`
- **Content structure** (reference template):

```markdown
# <Skill Name>

**<Skill Name>** is ... (one-line summary)

## Tags

Category | Status

## Core Philosophy
- Point 1
- Point 2
- ...

## Key Features & Workflow
1. **Feature A**: Description...
2. **Feature B**: Description...
...

## Skills Library Overview
- **Category 1**: List of sub-skills...
- **Category 2**: List of sub-skills...

## Installation & Support
<Skill Name> supports the following AI editors and platforms:
- [Claude Code](../../claudecode/<skill-name>/INSTALL-zh.md)   <!-- only if supported -->
- [Cursor](../../cursor/<skill-name>/INSTALL-zh.md)             <!-- only if supported -->
- [Codex](../../codex/<skill-name>/INSTALL-zh.md)               <!-- only if supported -->
- [OpenCode](../../opencode/<skill-name>/INSTALL-zh.md)         <!-- only if supported -->
- [OpenClaw](../../openclaw/<skill-name>/INSTALL-zh.md)         <!-- only if supported -->
- [Qoder](../../qoder/<skill-name>/INSTALL-zh.md)               <!-- only if supported -->

---
For more information, visit: [GitHub - <repo>](<url>)
```

> **Note**: The Chinese introduction should be written in Chinese. The template above shows the structure only.

### Step 3: Write the English Introduction Document

> Same as Step 2 — if a `SKILL.md` exists, use it as the primary information source for the English version as well.

- **File path**: `awesome-skills/introductions/en/<skill-name>.md`
- Content should be the English translation of the Chinese version from Step 2.
- Ensure the `## Tags` section uses English terms (e.g., "Category | Status").
- Installation links should point to `INSTALL-en.md` files.

### Step 4: Create Platform-Specific Installation Guides

Based on the supported platforms identified in **Step 1**, create bilingual installation guides **only** for those platforms. Skip any platform that the Skill does not support.

Each installation guide should include:
1. **Installation steps**: Specific commands or operations.
2. **Verify installation**: How to confirm the installation was successful.
3. **Update method** (if applicable): How to update to the latest version.
4. **Detailed documentation links** (if applicable): Links to further official documentation.

All available platforms and their corresponding file paths:

| Platform    | English                                            | Chinese                                            |
|-------------|----------------------------------------------------|----------------------------------------------------|
| Claude Code | `claudecode/<skill-name>/INSTALL-en.md`            | `claudecode/<skill-name>/INSTALL-zh.md`            |
| Codex       | `codex/<skill-name>/INSTALL-en.md`                 | `codex/<skill-name>/INSTALL-zh.md`                 |
| Cursor      | `cursor/<skill-name>/INSTALL-en.md`                | `cursor/<skill-name>/INSTALL-zh.md`                |
| OpenClaw    | `openclaw/<skill-name>/INSTALL-en.md`              | `openclaw/<skill-name>/INSTALL-zh.md`              |
| OpenCode    | `opencode/<skill-name>/INSTALL-en.md`              | `opencode/<skill-name>/INSTALL-zh.md`              |
| Qoder       | `qoder/<skill-name>/INSTALL-en.md`                 | `qoder/<skill-name>/INSTALL-zh.md`                 |

> **Important**: Only create rows for platforms that the Skill actually supports, as determined during Step 1 research. Do NOT create installation guides for unsupported platforms.

### Step 5: Cross-Check

After all files are complete, perform the following checks:
1. **Link validity**: Ensure all installation guide links in the introduction documents have correct paths.
2. **Bilingual consistency**: Both language versions should have matching structure and content.
3. **Information accuracy**: Installation commands and steps should match the official documentation.

## Important Notes

- All documents must be provided in **both Chinese** (`-zh.md`) and **English** (`-en.md`) versions.
- The "Installation & Support" section in introduction documents should use a **hyperlinked list** pointing to each platform's installation guide, rather than embedding installation commands directly.
- File naming should use **kebab-case** (lowercase with hyphens), e.g., `superpowers`, `ui-ux-pro-max-skill`.
- If the target Skill's GitHub repository cannot be accessed via browser, use the `read_url_content` tool to fetch page content.
