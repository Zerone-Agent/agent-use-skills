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

---

## 🚀 快速开始

### 1. 环境准备
确保您的系统中已安装 `uv`（推荐）：
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. 安装 Agent 框架支持
目前我们深度支持以下框架：

- **Claude Code**:
  ```bash
  /plugin add /path/to/agent-use-skills/skills/your-skill
  ```
- **Open Hands / 其他框架**:
  请参考各技能目录下的 `README.md` 获取特定的集成建议。

### 3. 使用技能
直接在对话中描述您的任务，Agent 会根据技能的元数据自动发现并加载相关的指令。

---

## 🎯 技能列表

> [!NOTE]
> 技能库正在加速整理中，更多高质量技能即将上线！

| 分类 | 技能名称 | 描述 | 状态 |
| :--- | :--- | :--- | :--- |
| **文档与办公** | (待补充) | - | 🏗️ 整理中 |
| **设计与创意** | (待补充) | - | 🏗️ 整理中 |
| **开发与测试** | (待补充) | - | 🏗️ 整理中 |
| **系统自动化** | (待补充) | - | 🏗️ 整理中 |

---

## 🛠️ 技能开发与贡献

如果您想贡献新的技能或改进现有技能：

1. **结构规范**：每个技能需遵循 `SKILL.md` 标准，并包含必要的 `scripts/` 与 `resources/`。
2. **验证流程**：确保技能在至少一个主流框架中通过验证。
3. **提交 PR**：欢迎通过 Pull Request 的形式提交您的贡献。

---

## 📖 核心概念：为什么选择 Skills？

| 特性 | Skills (本仓库) | 提示词 (Prompts) | 项目上下文 (Projects) |
| :--- | :--- | :--- | :--- |
| **复用性** | 极高，跨会话、跨项目通用 | 低，通常需要重写 | 中，局限于特定工作区 |
| **效率** | 渐进式加载，节省 Token | 低，随对话增长消耗 | 中，依赖索引 |
| **扩展性** | 支持携带复杂脚本与资源 | 仅限文本指令 | 依赖文件挂载 |
| **维护性** | 集中版本化管理 | 零散分布 | 碎片化 |

---

## 🔒 安全与最佳实践

⚠️ **重要提示**：技能可能会在您的环境中执行代码。请务必：
- 仅安装来自受信任来源（如本仓库）的技能。
- 在生产环境部署前，仔细阅读 `SKILL.md` 中的指令。
- 遵循最小权限原则，仅授予 Agent 必要的操作权限。

---

## 🤝 鸣谢与贡献者

非常感谢所有为 AI 生态做出贡献的开发者！

---
© 2026 AgentUse Team. Released under the GPL-3.0 License.
