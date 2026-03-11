# 贡献指南 (Contributing Guide)

[English](CONTRIBUTING.md) | 中文

感谢你对 AgentUse Skills 的关注！本仓库致力于为 AI Agent 提供状态标准化的程序化知识。

我们鼓励 **AI 优先 (AI-native) 的贡献流程**。如果你正在使用 AI 编程助手（如 Claude Code, Cursor, OpenCode 等），可以通过本项目内置的 `agentuse-share` 技能快速自动化完成贡献流程。

## 🚀 快速贡献：驱动 AI Agent

本项目提供的 `agentuse-share` 技能可以自动化完成调研、文档生成以及多平台安装指南的创建。

### 场景一：基于远程仓库链接贡献
如果你想将一个开源的 AI 技能（含有 `SKILL.md`）集成到本仓库：

1. **告知 Agent**：直接向你的 AI Agent 发送如下指令：
   > “请使用 `agentuse-share` 技能，根据以下仓库链接完成贡献：[GitHub Repo URL]”
2. **自动化流程**：Agent 会自动访问该链接、提取核心功能、生成 `awesome-skills/introductions/` 下的中英文介绍文档，并创建对应平台的安装指南。

### 场景二：基于本地技能文件贡献
如果你已经编写好了技能的 `SKILL.md`，或者想手动准备技能源码：

1. **准备文件**：在 `awesome-skills/skills/` 目录下创建一个以技能名（kebab-case）命名的文件夹，并将 `SKILL.md` 放入其中。
   - 路径示例：`awesome-skills/skills/my-new-skill/SKILL.md`
2. **告知 Agent**：向 AI Agent 发送如下指令：
   > “我已经在 `awesome-skills/skills/my-new-skill/` 放置了 `SKILL.md`，请使用 `agentuse-share` 技能完成后续的文档生成和格式化工作。”
3. **自动化流程**：Agent 会自动检测到本地的 `SKILL.md`（对应 `agentuse-share` 的 Case A），对其内容进行精练，并生成必要的 `introductions/` 和各平台目录（如 `cursor/`, `claudecode/`）下的文件。

---

## 🛠 手动贡献流程

如果你倾向于手动操作，请遵循以下步骤：

1. **Fork** 本仓库。
2. **创建分支**：`feature/xxx-skill`。
3. **遵循目录规范**：参考 [AGENTS.md](./AGENTS.md) 中的目录结构。
   - 技能介绍：`awesome-skills/introductions/{zh,en}/<skill-name>.md`
   - 安装指南：`awesome-skills/{platform}/<skill-name>/INSTALL-*.md`
4. **命名规范**：所有文件夹和文件名使用 `kebab-case`。
5. **双语要求**：**必须**同时提供中文 (`-zh.md`) 和英文 (`-en.md`) 版本。
6. **提交 PR**：通过 Pull Request 提交你的修改。

## 📝 质量检查清单

在提交 PR 之前，请确保：
- [ ] 已同时创建中文和英文版本。
- [ ] 仅为技能实际支持的平台创建了安装指南。
- [ ] 所有内部链接（相对路径）均有效。
- [ ] 文档格式符合 [AGENTS.md](./AGENTS.md) 的要求。

## 💬 获取帮助

如果有任何疑问，欢迎提交 Issue。

---
© 2026 AgentUse Team.
