# Deep Research

**Deep Research** 是一个自主多步骤研究技能，利用 Google Gemini Deep Research Agent 执行深度调研任务。与标准 LLM 查询的即时回复不同，Deep Research 是一个"分析师盒子"，能够自主规划、搜索、阅读和综合信息，生成全面、带引用的研究报告。

## 标签

🗂️ 文档与办公 | ✅ 已验证

## 核心理念
- **自主研究**：Agent 自动规划研究策略，无需人工干预即可完成多轮搜索和分析。
- **深度综合**：不只是简单检索信息，而是跨多个来源进行深度分析和综合。
- **带引用输出**：所有研究结果都附带来源引用，确保可溯源和可验证。
- **灵活交互**：支持实时流式输出、异步轮询、历史查询和追问等多种交互模式。

## 主要功能与工作流

1. **研究任务启动**：通过一条自然语言查询启动深度研究任务，Agent 将自主规划搜索策略。
2. **实时流式输出**：支持流式传输研究进度，实时显示思考过程和报告生成。
3. **异步研究**：可以启动研究任务后不等待完成，后续通过状态查询获取结果。
4. **继续对话**：基于之前的研究结果进行追问和深入探讨。
5. **结构化输出格式**：支持指定输出格式，如"执行摘要 → 对比表 → 建议"等自定义结构。
6. **历史管理**：自动缓存研究历史记录，支持查看和回溯历史研究任务。
7. **多种输出模式**：支持 Markdown 人类可读报告、JSON 结构化数据和原始 API 响应。

## 适用场景

- 市场分析与竞争格局研究
- 技术文献调研与综述
- 尽职调查
- 历史研究与时间线梳理
- 框架、产品、技术的对比分析

## 成本与时间

| 指标 | 数值 |
|------|------|
| 时间 | 每个任务 2-10 分钟 |
| 成本 | 每个任务 $2-5（按复杂度变化） |
| Token 消耗 | ~250k-900k 输入，~60k-80k 输出 |

## 安装与支持

Deep Research 支持以下 AI 编辑器和平台：
- [Claude Code](../../claudecode/deep-research/INSTALL-zh.md)
- [Cursor](../../cursor/deep-research/INSTALL-zh.md)
- [Codex](../../codex/deep-research/INSTALL-zh.md)
- [OpenCode](../../opencode/deep-research/INSTALL-zh.md)
- [OpenClaw](../../openclaw/deep-research/INSTALL-zh.md)
- [Qoder](../../qoder/deep-research/INSTALL-zh.md)

---
了解更多信息，请访问：[GitHub - Zerone-Agent/agent-use-skills](https://github.com/Zerone-Agent/agent-use-skills)
