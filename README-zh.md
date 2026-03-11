<p align="center">
  <a href="https://github.com/zerone-agent/agent-use-skills">
    <img alt="AgentUse Skills" src="resources/agent-use.jpg"/>
  </a>
</p>

# AgentUse Skills - 精选 AI 技能库

[English](README.md) | 中文

[![Last Updated](https://img.shields.io/badge/updated-Mar%202026-blue.svg)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> **AgentUse Skills** 为 AI Agent 提供了一套**可复用、可标准化的程序化知识**。

我们对现有的 AI Skill 进行了深度整理，提供了最为便捷的安装教程，并针对主流的 Agent 框架（如 Claude Code, Open Hands 等）进行了性能增强与兼容性验证，确保每个技能都能“开箱即用”。

### ✨ 核心优势

- **深度精选与整理**：不仅仅是收集，我们对每个技能的功能、提示词和脚本进行了标准化重构。
- **便捷安装体验**：提供一键式安装脚本与详细的配置文档，大幅降低使用门槛。
- **框架增强与验证**：针对不同的 Agent 框架进行了针对调优，并经过严格的自动化测试验证其稳定性。
- **渐进式加载架构**：采用高效的元数据发现机制，确保在拥有海量技能的同时，不浪费 Agent 的上下文窗口。
- **[Agent-Ready 认证计划](agent-ready/README-zh.md)**：专门为软件厂商提供的认证计划，通过标准化 API 与验证集成，填补传统软件与 AI Agent 生态系统之间的鸿沟。

## 🚀 快速开始

### 支持的框架

AgentUse Skills 支持以下 AI Agent 框架：

- **Claude Code**
- **Codex**
- **Cursor**
- **OpenCode**
- **OpenClaw**
- **Qoder**

每个框架都有其独立的技能加载机制。请参考各技能目录下的安装指南获取具体框架的操作说明。

## 🎯 技能列表

> [!NOTE]
> 技能库正在加速整理中，更多高质量技能即将上线！

### 文档与办公

| 技能名称 | 描述 | 状态 |
| :--- | :--- | :--- |
| **[content-research-writer](awesome-skills/introductions/zh/content-research-writer.md)** | 内容写作协作技能，帮助调研、构建大纲、撰写草稿并优化内容，支持引用管理，同时保持你独特的写作风格。 | 🔍 待验证 |
| **[deep-research](awesome-skills/introductions/zh/deep-research.md)** | 自主多步骤深度研究技能，利用 Gemini Deep Research Agent 进行市场分析、文献综述、尽职调查等，生成带引用的详细报告。 | 🔍 待验证 |
| **[twitter-algorithm-optimizer](awesome-skills/introductions/zh/twitter-algorithm-optimizer.md)** | 基于 Twitter 开源算法洞察分析并优化推文，以获得最大的传播范围。 | 🔍 待验证 |
| **[tavily-search](awesome-skills/introductions/zh/tavily-search.md)** | 利用 Tavily API 为 AI Agent 优化的网络搜索技能。返回干净、相关的搜索结果。 | 🔍 待验证 |

### 设计与创意

| 技能名称 | 描述 | 状态 |
| :--- | :--- | :--- |
| **[ui-ux-pro-max-skill](awesome-skills/introductions/zh/ui-ux-pro-max-skill.md)** | AI 驱动的设计智能体，提供 67 种 UI 风格、96 种配色方案和 100 条行业特定推理规则。 | ✅ 已验证 |
| **[imagen](awesome-skills/introductions/zh/imagen.md)** | 利用 Google Gemini 的图像生成能力，在 AI 编码会话期间直接生成图像。纯 Python 实现，零依赖。 | 🔍 待验证 |
| **[canvas-design](awesome-skills/introductions/zh/canvas-design.md)** | 通过深度的设计哲学创作博物馆品质的视觉艺术作品，强调大师级工艺与极简文本。 | 🔍 待验证 |
| **[frontend-slides](awesome-skills/introductions/zh/frontend-slides.md)** | 创建精美、动画丰富的 HTML 演示文稿，支持从零创建或从 PowerPoint 转换，内置 12 种精选视觉风格。 | 🔍 待验证 |

### 开发与测试

| 技能名称 | 描述 | 状态 |
| :--- | :--- | :--- |
| **[agentuse-share](awesome-skills/introductions/zh/agentuse-share.md)** | 标准化 Skill 贡献工作流，涵盖调研、文档撰写及多平台安装指南生成。 | ✅ 已验证 |
| **[superpowers](awesome-skills/introductions/zh/superpowers.md)** | 20+ 核心技能，涵盖 TDD、调试和协作模式。 | ✅ 已验证 |
| **[playwright-skill](awesome-skills/introductions/zh/playwright-skill.md)** | 基于 Playwright 的全功能浏览器自动化技能，支持自动探测服务器、网页测试、截图及 UX 验证。 | 🔍 待验证 |
| **[prompt-engineering](awesome-skills/introductions/zh/prompt-engineering.md)** | 高级提示词工程模式，涵盖少样本学习、思维链及说服原则，旨在最大化 Agent 执行效率。 | 🔍 待验证 |
| **[self-improving-agent](awesome-skills/introductions/zh/self-improving-agent.md)** | 捕获学习经验、错误和修正建议，实现持续改进。支持将学习成果晋升为项目内存。 | 🔍 待验证 |

### 系统自动化

| 技能名称 | 描述 | 状态 |
| :--- | :--- | :--- |
| (待补充) | - | 🏗️ 整理中 |

## 🛠️ 技能开发与贡献

如果您想贡献新的技能或改进现有技能：

1. **结构规范**：每个技能需遵循 `SKILL.md` 标准，并包含必要的 `scripts/` 与 `resources/`。
2. **验证流程**：确保技能在至少一个主流框架中通过验证。
3. **提交 PR**：欢迎通过 Pull Request 的形式提交您的贡献。

## 📖 核心概念：为什么选择 Skills？

| 特性 | Skills (本仓库) | 提示词 (Prompts) | 项目上下文 (Projects) |
| :--- | :--- | :--- | :--- |
| **复用性** | 极高，跨会话、跨项目通用 | 低，通常需要重写 | 中，局限于特定工作区 |
| **效率** | 渐进式加载，节省 Token | 低，随对话增长消耗 | 中，依赖索引 |
| **扩展性** | 支持携带复杂脚本与资源 | 仅限文本指令 | 依赖文件挂载 |
| **维护性** | 集中版本化管理 | 零散分布 | 碎片化 |

## 🔒 安全与最佳实践

⚠️ **重要提示**：技能可能会在您的环境中执行代码。请务必：
- 仅安装来自受信任来源（如本仓库）的技能。
- 在生产环境部署前，仔细阅读 `SKILL.md` 中的指令。
- 遵循最小权限原则，仅授予 Agent 必要的操作权限。

## 🤝 鸣谢与贡献者

非常感谢所有为 AI 生态做出贡献的开发者！

---
© 2026 AgentUse Team. Released under the GPL-3.0 License.
