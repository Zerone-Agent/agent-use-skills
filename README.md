<p align="center">
  <a href="https://github.com/zerone-agent/agent-use-skills">
    <img alt="AgentUse Skills" src="resources/agent-use.jpg"/>
  </a>
</p>

# AgentUse Skills - Curated AI Skills Library

English | [中文](README-zh.md)

[![Last Updated](https://img.shields.io/badge/updated-Mar%202026-blue.svg)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> **AgentUse Skills** provide a set of **reusable and standardized procedural knowledge** for AI Agents.

We have deeply organized existing AI Skills, provided the most convenient installation tutorials, further enhanced and verified compatibility for mainstream Agent frameworks (e.g., Claude Code, Open Hands), ensuring that every skill is "ready-to-use" out of the box.

### ✨ Key Advantages

- **Deep Curation**: More than just a collection; we've standardized the functions, prompts, and scripts for each skill.
- **Convenient Installation**: One-click scripts and detailed docs to significantly lower the barrier to entry.
- **Framework Optimization**: Specialized tuning for different Agent frameworks, verified by rigorous automated testing.
- **Progressive Loading**: Efficient metadata discovery ensures support for massive skill libraries without overwhelming the context window.

## 🚀 Getting Started

### Supported Frameworks

AgentUse Skills supports the following AI Agent frameworks:

- **Claude Code**
- **Codex**
- **Cursor**
- **OpenCode**
- **OpenClaw**
- **Qoder**

Each framework provides its own skill loading mechanism. Please refer to the installation guides in each skill directory for framework-specific instructions.

## 🎯 Skill List

> [!NOTE]
> The skill library is being rapidly organized, and more high-quality skills will be available soon!

### Document & Office

| Skill Name | Description | Status |
| :--- | :--- | :--- |
| **[content-research-writer](awesome-skills/introductions/en/content-research-writer.md)** | A collaborative writing partner that helps research, outline, draft, and refine content with proper citations while preserving your voice. | 🔍 Pending Verification |

### Design & Creative

| Skill Name | Description | Status |
| :--- | :--- | :--- |
| **[ui-ux-pro-max-skill](awesome-skills/skills/en/ui-ux-pro-max-skill.md)** | AI-powered design intelligence with 67 UI styles, 96 color palettes, and 100 industry-specific reasoning rules. | ✅ Verified |

### Dev & Testing

| Skill Name | Description | Status |
| :--- | :--- | :--- |
| **[superpowers](awesome-skills/skills/en/superpowers.md)** | Battle-tested 20+ core skills including TDD, debugging, and collaboration patterns. | ✅ Verified |

### System Automation

| Skill Name | Description | Status |
| :--- | :--- | :--- |
| (TBD) | - | 🏗️ Organizing |

## 🛠️ Skill Development & Contribution

If you'd like to contribute new skills or improve existing ones:

1. **Structural Specification**: Each skill must follow the `SKILL.md` standard and include necessary `scripts/` and `resources/`.
2. **Verification Flow**: Ensure the skill passed verification in at least one mainstream framework.
3. **Submit PR**: We welcome your contributions via Pull Requests!

## 📖 Core Concept: Why Skills?

| Feature | Skills (This Repo) | Prompts | Project Context |
| :--- | :--- | :--- | :--- |
| **Reusability** | Extremely High; cross-session/project | Low; usually requires rewriting | Medium; workspace-specific |
| **Efficiency** | Progressive loading; saves tokens | Low; grows with conversation | Medium; depends on indexing |
| **Extensibility** | Supports complex scripts/resources | Pure text instructions only | Depends on file mounts |
| **Maintainability** | Centralized version management | Scattered distribution | Fragmented |

## 🔒 Security & Best Practices

⚠️ **Important Notice**: Skills may execute code in your environment. Please ensure you:
- Only install skills from trusted sources (like this repo).
- Read the instructions in `SKILL.md` carefully before production deployment.
- Follow the principle of least privilege, granting only necessary permissions to the Agent.

## 🤝 Acknowledgments & Contributors

A huge thanks to all developers contributing to the AI ecosystem!

---
© 2026 AgentUse Team. Released under the GPL-3.0 License.
