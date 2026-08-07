---
name: agentuse-share
description: Use this skill whenever you need to add a new skill to awesome-skills, document an existing skill, create installation guides, or set up bilingual documentation. Trigger when user mentions "add skill", "document skill", "create install guide", "write skill introduction", "add to awesome-skills", or when working with the awesome-skills repository structure. Also trigger when asked to create bilingual (Chinese/English) documentation for any skill.
---

# AgentUse Share Skill

This skill defines the complete standardized workflow for adding a new Skill to the `awesome-skills` repository.

## Repository Directory Structure

See [references/directory-structure.md](references/directory-structure.md) for the complete directory structure and naming conventions.

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

> **Tip**: The SKILL.md is typically more detailed and authoritative than a README. Use it as the foundation for writing the introduction documents in Steps 2 and 3 and the installation guides (INSTALL.md) in Step 4. **Please refer to the `content-research-writer` skill's writing style to ensure the generated documentation is professional, structured, and includes clear action items.** The content-research-writer skill is located at `awesome-skills/skills/content-research-writer/SKILL.md`.

#### Case B: No SKILL.md in the Repository

If no `SKILL.md` exists under `awesome-skills/skills/<skill-name>/`:

- Visit the target Skill's **GitHub repository** or official documentation.
- Use the `webfetch` tool (or equivalent URL fetching tool available in your environment) to fetch the README page content.
- Focus on gathering the following information:
  - **What it is**: The core definition and positioning of the Skill.
  - **Core philosophy**: What are the design principles.
  - **Key features and workflow**: What capabilities it provides and how it operates.
  - **Skills library composition**: What sub-skills are included.
  - **Supported platforms**: Determine exactly which AI coding agents/platforms the Skill supports (e.g., Claude Code, Cursor, Codex, OpenCode, OpenClaw, Zerone, Qoder). This is critical — only create installation guides for platforms that are explicitly supported. Skip any unsupported platforms entirely.

### Step 2: Write the Chinese Introduction Document

> If a `SKILL.md` was found in Step 1 (Case A), base the introduction on the information from that file. Summarize and restructure the content to fit the introduction template. Do NOT copy the SKILL.md verbatim — instead, distill it into a concise, reader-friendly introduction.

- **File path**: `awesome-skills/introductions/zh/<skill-name>.md`
- **Template**: See [references/introduction-template.md](references/introduction-template.md)

### Step 3: Write the English Introduction Document

> Same as Step 2 — if a `SKILL.md` exists, use it as the primary information source for the English version as well.

- **File path**: `awesome-skills/introductions/en/<skill-name>.md`
- **Template**: See [references/introduction-template.md](references/introduction-template.md)
- Content should be the English translation of the Chinese version from Step 2.

### Step 4: Create Platform-Specific Installation Guides

Based on the supported platforms identified in **Step 1**, create bilingual installation guides **only** for those platforms. Skip any platform that the Skill does not support.

#### Installation Guide Templates

**CRITICAL**: All installation guides MUST use bash commands that AI agents can execute. Do NOT use plugin commands like `/plugin install` or `/plugin marketplace add` because AI agents cannot execute these commands.

- **External Repository Skills**: See [references/install-guide-external-template.md](references/install-guide-external-template.md)
- **Internal Repository Skills** (agent-use-skills): See [references/install-guide-internal-template.md](references/install-guide-internal-template.md)

Each installation guide should include:
1. **Prerequisites**: Required software and dependencies
2. **Installation steps**: Bash commands that AI agents can execute
3. **Verify installation**: How to confirm the installation was successful
4. **Update method**: How to update to the latest version
5. **Getting Help**: Links to GitHub repository and issue tracker

All available platforms and their corresponding file paths are documented in [references/directory-structure.md](references/directory-structure.md).

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
