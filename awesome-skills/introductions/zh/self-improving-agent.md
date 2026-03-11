# Self-Improving Agent

**Self-Improving Agent** 是一个用于捕获学习经验、错误和修正建议的技能，旨在实现 AI 智能体的持续改进。

## 核心理念

- **持续进化**：通过记录操作失败、用户更正、知识漏洞和最佳实践，让 AI 能够从中学习并避免重复错误。
- **知识沉淀**：将零散的学习点提炼并晋升（Promote）为项目内存（如 `CLAUDE.md`）或全局工作空间指南（如 `SOUL.md`）。
- **多智能体协作**：在 OpenClaw 等平台下，支持在不同会话和智能体之间共享学习成果。

## 核心功能与工作流

1. **结构化记录**：提供 `LEARNINGS.md`（学习）、`ERRORS.md`（错误）和 `FEATURE_REQUESTS.md`（需求）的标准化模板。
2. **学习晋升机制**：根据出现频率（Recurrence-Count）和重要性，自动或手动将学习点转化为持久的提示词指南。
3. **自动触发与钩子**：支持通过 Git 钩子或 Agent 提交钩子（如 `UserPromptSubmit`）自动提醒记录学习。
4. **技能提取**：当某个解决方案足够成熟且具通用性时，支持一键将其提取为独立的可复用技能。

## 技能库概览

- **日志管理**：位于 `.learnings/` 目录下的结构化 Markdown 文件。
- **脚本工具集**：包含 `activator.sh`（激活器）、`error-detector.sh`（错误探测）和 `extract-skill.sh`（技能提取脚本）。
- **工作空间集成**：针对 OpenClaw 的 `AGENTS.md`、`SOUL.md`、`TOOLS.md` 等文件的深度集成。

## 安装与支持

Self-Improving Agent 目前主要支持以下平台：

- [OpenClaw](../../openclaw/self-improving-agent/INSTALL-zh.md)

---
更多信息请查看：[GitHub - peterskoett/self-improving-agent](https://github.com/peterskoett/self-improving-agent)
