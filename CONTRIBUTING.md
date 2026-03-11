# Contributing to AgentUse Skills

English | [中文](CONTRIBUTING-zh.md)

Thank you for your interest in contributing to AgentUse Skills! This repository provides standardized procedural knowledge for AI Agents.

We promote an **AI-native contribution workflow**. If you are using an AI coding agent (e.g., Claude Code, Cursor, OpenCode), you can use the built-in `agentuse-share` skill to automate the entire contribution process.

## 🚀 Fast-Track Contribution: Driving your AI Agent

The `agentuse-share` skill automates research, documentation generation, and installation guide creation.

### Scenario 1: Contribute from a GitHub Repository
If you want to contribute an existing AI skill from a public repository:

1. **Command**: Ask your AI Agent:
   > "Please use the `agentuse-share` skill to contribute from this repository: [GitHub URL]"
2. **Automation**: The agent will visit the URL, extract key features, generate bilingual introductions in `awesome-skills/introductions/`, and create platform-specific installation guides.

### Scenario 2: Contribute a Local Skill
If you have written a `SKILL.md` or want to manually prepare the skill source:

1. **Prepare**: Create a directory under `awesome-skills/skills/<skill-name>/` and place your `SKILL.md` there.
   - Example: `awesome-skills/skills/my-new-skill/SKILL.md`
2. **Command**: Ask your AI Agent:
   > "I have placed the `SKILL.md` in `awesome-skills/skills/<skill-name>/`. Please use the `agentuse-share` skill to finish the documentation and formatting."
3. **Automation**: The agent will detect the local `SKILL.md` (Case A in `agentuse-share`), distill its content, and generate the necessary files in the `introductions/` and platform directories (e.g., `cursor/`, `claudecode/`).

---

## 🛠 Manual Contribution Workflow

If you prefer to contribute manually, please follow these steps:

1. **Fork** the repository.
2. **Create a branch**: `feature/xxx-skill`.
3. **Follow Directory Structure**: Reference [AGENTS.md](./AGENTS.md) for the exact paths.
   - Introductions: `awesome-skills/introductions/{zh,en}/<skill-name>.md`
   - Install Guides: `awesome-skills/{platform}/<skill-name>/INSTALL-*.md`
4. **Naming Convention**: Use `kebab-case` for all files and directories.
5. **Bilingual Requirement**: You MUST provide both Chinese (`-zh.md`) and English (`-en.md`) versions.
6. **Submit PR**: Open a Pull Request with your changes.

## 📝 Quality Checklist

Before submitting your PR, please verify:
- [ ] Both English and Chinese versions are created.
- [ ] Installation guides are provided **only** for platforms the skill actually supports.
- [ ] All internal links (relative paths) are valid.
- [ ] Documentation follows the style guidelines in [AGENTS.md](./AGENTS.md).

## 💬 Getting Help

If you have any questions, feel free to open an Issue.

---
© 2026 AgentUse Team.
