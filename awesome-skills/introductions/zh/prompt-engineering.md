# Prompt Engineering

**Prompt Engineering** 是一套专为 AI Agent 设计的高级提示词工程模式和最佳实践。它集成了 Anthropic 官方建议、说服力心理学原则以及生产级 LLM 交互的实战模式。

## 核心理念

- **控制力与预测性**：通过结构化的指令层次和少样本学习（Few-Shot），确保 AI 输出的高度一致性和可控性。
- **思维链推理**：利用 Chain-of-Thought (CoT) 模式，让 Agent 在执行复杂逻辑前进行分步思考，显著提升结果准确度。
- **Agent 原生优化**：针对 Agent 的“工作记忆”（上下文窗口）进行优化，在保证信息量的同时最大限度节省 Token。
- **说服心理学**：应用权威感、承诺与一致性等社会心理学原则，确保 Agent 即使在复杂环境下也能严格遵循关键规约（如 TDD）。

## 核心功能与工作流

1. **高级模式库**：包含 Few-Shot、CoT、渐进式披露、指令层次结构等成熟的提示词模式。
2. **Agent 交互最佳实践**：提供上下文窗口管理、行为自由度设置（高/中/低）以及异常恢复策略。
3. **说服性指令设计**：如何编写具有“约束力”的指令，通过心理学手段降低 Agent 在执行过程中的“由于”和“走捷径”行为。
4. **验证与迭代**：包括自我验证步骤的设计、性能优化（延迟与成本平衡）以及 RAG 集成模式。

## 技能库概览

- **提示词模式**：从基础指令到复杂的模板系统的一整套方法论。
- **说服原则**：解析 7 大提示词说服力原则，提升指令的执行成功率。
- **性能指南**：关于 Token 效率、延迟降低和 Stream 模式的优化建议。

## 安装与支持

Prompt Engineering 支持以下 AI 编辑器和平台：

- [Claude Code](../../claudecode/prompt-engineering/INSTALL-zh.md)
- [Cursor](../../cursor/prompt-engineering/INSTALL-zh.md)
- [Codex](../../codex/prompt-engineering/INSTALL-zh.md)
- [OpenCode](../../opencode/prompt-engineering/INSTALL-zh.md)
- [OpenClaw](../../openclaw/prompt-engineering/INSTALL-zh.md)
- [Qoder](../../qoder/prompt-engineering/INSTALL-zh.md)

---
更多信息请查看：[Anthropic Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
