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
- **[Agent-Ready Certification](agent-ready/README.md)**: A specialized program for software vendors to bridge traditional applications with the AI Agent ecosystem through standardized APIs and verified integrations.

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
| **[agent-browser](awesome-skills/introductions/en/agent-browser.md)** | A fast Rust-based headless browser automation CLI with Node.js fallback. Enables Agent navigation, interaction, and snapshots. | 🔍 Pending Verification |
| **[content-research-writer](awesome-skills/introductions/en/content-research-writer.md)** | A collaborative writing partner that helps research, outline, draft, and refine content with proper citations while preserving your voice. | 🔍 Pending Verification |
| **[deep-research](awesome-skills/introductions/en/deep-research.md)** | Autonomous multi-step deep research skill powered by Gemini Deep Research Agent for market analysis, literature reviews, due diligence, and more — producing detailed, cited reports. | 🔍 Pending Verification |
| **[twitter-algorithm-optimizer](awesome-skills/introductions/en/twitter-algorithm-optimizer.md)** | Analyze and optimize tweets for maximum reach using Twitter's open-source algorithm insights. | 🔍 Pending Verification |
| **[humanizer](awesome-skills/introductions/en/humanizer.md)** | Remove signs of AI-generated writing from text to make it sound more natural and human-written. | 🔍 Pending Verification |
| **[tavily-search](awesome-skills/introductions/en/tavily-search.md)** | AI-optimized web search via Tavily API. Returns concise, relevant results for AI agents. | 🔍 Pending Verification |
| **[summarize](awesome-skills/introductions/en/summarize.md)** | Fast CLI to summarize URLs, local files (PDFs, images, audio), and YouTube links using multiple LLM providers. | 🔍 Pending Verification |
| **[gog](awesome-skills/introductions/en/gog.md)** | Google Workspace CLI for Gmail, Calendar, Drive, Contacts, Sheets, and Docs. | 🔍 Pending Verification |
| **[obsidian](awesome-skills/introductions/en/obsidian.md)** | Work with Obsidian vaults (Markdown notes) and automate via obsidian-cli. Supports smart search and safe refactoring. | 🔍 Pending Verification |

### Design & Creative

| Skill Name | Description | Status |
| :--- | :--- | :--- |
| **[ui-ux-pro-max-skill](awesome-skills/introductions/en/ui-ux-pro-max-skill.md)** | AI-powered design intelligence with 67 UI styles, 96 color palettes, and 100 industry-specific reasoning rules. | ✅ Verified |
| **[imagen](awesome-skills/introductions/en/imagen.md)** | Generate images using Google Gemini's image generation capabilities. Pure Python implementation with zero dependencies. | 🔍 Pending Verification |
| **[canvas-design](awesome-skills/introductions/en/canvas-design.md)** | Create museum-quality visual art through deep design philosophies, emphasizing master-level craftsmanship and minimal text. | 🔍 Pending Verification |
| **[frontend-slides](awesome-skills/introductions/en/frontend-slides.md)** | Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files, with 12 curated visual styles. | 🔍 Pending Verification |

### Dev & Testing

| Skill Name | Description | Status |
| :--- | :--- | :--- |
| **[agentuse-share](awesome-skills/introductions/en/agentuse-share.md)** | A standardized workflow for contributing new skills to this repository, including research, documentation, and installation guide generation. | ✅ Verified |
| **[superpowers](awesome-skills/introductions/en/superpowers.md)** | Battle-tested 20+ core skills including TDD, debugging, and collaboration patterns. | ✅ Verified |
| **[playwright-skill](awesome-skills/introductions/en/playwright-skill.md)** | Complete browser automation with Playwright. Auto-detects dev servers, performs testing, screenshots, and UX validation. | 🔍 Pending Verification |
| **[prompt-engineering](awesome-skills/introductions/en/prompt-engineering.md)** | Advanced prompt engineering techniques including Few-Shot, CoT, and persuasion principles to maximize Agent performance. | 🔍 Pending Verification |
| **[self-improving-agent](awesome-skills/introductions/en/self-improving-agent.md)** | Captures learnings, errors, and corrections to enable continuous improvement. Promotes learnings to project memory. | 🔍 Pending Verification |

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
