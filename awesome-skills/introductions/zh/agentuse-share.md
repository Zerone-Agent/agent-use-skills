# AgentUse Share

**AgentUse Share** 是一个标准化的工作流技能，旨在帮助开发者和 AI Agent 将新的 AI 编程技能（Skill）高效地添加到 `awesome-skills` 仓库中。它涵盖了从调研、初稿撰写到多平台安装指南生成的全过程。

## 标签

开发与测试 | 已验证

## 核心理念

- **标准化 (Standardization)**：定义统一的 Skill 目录结构和文档规范，确保社区贡献的高质量。
- **调研驱动 (Research-Driven)**：强调基于原始 `SKILL.md` 或官方仓库进行深入调研，确保信息的准确性。
- **多平台支持 (Multi-Platform)**：自动为每个 Skill 生成适配不同 AI 编辑器（如 Claude Code, Cursor 等）的安装指南。
- **双语化 (Bilingual)**：强制要求同步生成中英文文档，扩大技能的受众群体。

## 主要功能与工作流

1. **目标技能调研 (Target Skill Research)**：自动识别仓库内是否存在原始 `SKILL.md`，或通过网络检索获取技能的核心定义、设计哲学和功能特性。
2. **中文介绍文档生成 (Chinese Introduction)**：基于调研结果，按照标准模板提炼并生成技能的中文介绍。
3. **英文介绍文档生成 (English Introduction)**：同步翻译并生成对应的英文介绍，确保内容的一致性。
4. **平台适配安装指南 (Platform-Specific Guides)**：识别技能支持的 AI 编辑器平台，并为每个平台生成专属的中英文安装与验证指南。
5. **一致性检查 (Cross-Check)**：自动验证文档间的链接有效性、内容准确性以及双语对齐情况。

## 技能库概览

该技能主要包含以下子流程：
- **调研子技能**：利用 `read_url_content` 等工具获取外部技能信息。
- **写作子技能**：参照 `content-research-writer` 风格进行专业化写作。
- **安装指南模板**：针对不同平台（Claude Code, Cursor, Codex, OpenCode 等）的标准化模版。

## 安装与支持

AgentUse Share 支持以下 AI 编辑器和平台：
- [Claude Code](../../claudecode/agentuse-share/INSTALL-zh.md)
- [Cursor](../../cursor/agentuse-share/INSTALL-zh.md)
- [Codex](../../codex/agentuse-share/INSTALL-zh.md)
- [OpenCode](../../opencode/agentuse-share/INSTALL-zh.md)
- [OpenClaw](../../openclaw/agentuse-share/INSTALL-zh.md)
- [Qoder](../../qoder/agentuse-share/INSTALL-zh.md)

---
了解更多信息，请访问：[GitHub - Zerone-Agent/agent-use-skills](https://github.com/Zerone-Agent/agent-use-skills)
