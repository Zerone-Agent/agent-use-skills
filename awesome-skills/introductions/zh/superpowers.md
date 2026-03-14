# Superpowers

**Superpowers** 是一个为 AI 编程助手设计的 Agentic 技能框架和软件开发方法论。它建立在可组合的“技能”（Skills）系统之上，旨在通过标准化的工作流，将 AI 助手从简单的代码生成器提升为成熟的软件工程师。

## 标签

💻 开发与测试 | ✅ 已验证

## 核心理念
Superpowers 的设计哲学强调以下几点：
- **测试驱动开发 (TDD)**：坚持先写测试，始终验证代码的正确性。
- **系统化而非随机性**：用标准化的流程取代猜测和凭感觉开发。
- **降低复杂性**：以简洁为核心目标。
- **证据重于结论**：在宣告成功之前，必须有验证结果支持。

## 主要功能与工作流
Superpowers 提供了一个完整的开发生命周期管理：

1. **头脑风暴 (Brainstorming)**：在编写代码前激活，通过对话细化需求、探索替代方案，并形成经过验证的设计文档。
2. **Git 工作树 (Git Worktrees)**：在批准设计后创建隔离的工作空间，确保开发环境整洁且测试基准通过。
3. **制定计划 (Writing Plans)**：将工作分解为 2-5 分钟即可完成的微小任务，每个任务包含明确的文件路径、完整代码和验证步骤。
4. **子代理驱动开发 (Subagent-Driven Development)**：自动派遣子代理执行任务，并进行两阶段审查（需求合规性和代码质量）。
5. **强力 TDD (Test-Driven Development)**：强制执行“红-绿-重构”循环。如果代码在测试前编写，系统会将其删除以确保 TDD 的纯粹性。
6. **代码审查 (Requesting Code Review)**：在任务之间进行自动审查，严重问题将阻止后续进度。
7. **完成开发分支 (Finishing Branch)**：验证所有测试后，提供合并、提交 PR 或清理环境的选项。

## 技能库概览
- **测试/调试**：系统化调试、RED-GREEN-REFACTOR 循环、完成前验证。
- **协作/规划**：苏格拉底式设计细化、详细计划制定、并行代理调度。
- **元能力**：创建新技能的指南 (writing-skills)、系统使用手册。

## 安装与支持
Superpowers 支持多种主流 AI 编辑器和平台：
- [Claude Code](../../claudecode/superpowers/INSTALL-zh.md)
- [Cursor](../../cursor/superpowers/INSTALL-zh.md)
- [Codex](../../codex/superpowers/INSTALL-zh.md)
- [OpenCode](../../opencode/superpowers/INSTALL-zh.md)


---
了解更多信息，请访问：[GitHub - obra/superpowers](https://github.com/obra/superpowers)
