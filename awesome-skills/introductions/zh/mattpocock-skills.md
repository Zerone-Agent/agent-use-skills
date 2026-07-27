# Matt Pocock Skills

**Matt Pocock Skills** 是 TypeScript 教育者 Matt Pocock（Total TypeScript 创办人）从自己日常 `.agents/` 目录里整理出的实战技能集——刻意保持小、易改、可组合，跨模型可用，目标是把软件工程基本功带进 AI 编码工作流，"为真正的工程师而非 vibe coding"。

## 标签

💻 开发与测试 | ✅ 已验证

## Core Philosophy

- **修复四大失败模式**：基于多年工程经验，针对 AI Agent 最常见的四类翻车——对齐失败、表达冗长、代码不工作、代码熵增（泥球）——逐个给出可复用的工作流。
- **小而可改、可组合**：每个技能单一职责、独立可改、跨模型通用；不像 GSD/BMAD/Spec-Kit 那样整体接管流程并剥夺你的控制权。
- **用户调用 vs 模型调用**：明确区分两类技能。用户调用（如 `/grill-me`）只能人工触发，负责编排；模型调用（如 `tdd`）可由 Agent 自动加载，承载可复用的工程纪律。用户调用之间不能互相调用。
- **共享术语即生产力**：通过 `CONTEXT.md` + ADR 沉淀领域语言，让 Agent 用一个词代替二十个词，减少 token、提升一致性、便于代码导航。
- **反馈循环是速度上限**：红绿重构、静态类型、浏览器访问、自动测试——基本功比任何花哨工具更重要。

## Key Features & Workflow

1. **一键安装、按需选用**：22 个活跃技能分布在 `engineering/` 与 `productivity/` 两个分类下；安装到本地后由 Agent 根据上下文自动加载或用户显式 `/invoke`。
2. **核心入口 `/ask-matt`**：一个路由器技能，根据当前情境推荐应该用哪个用户调用技能。
3. **盘问式澄清**：`/grill-me`（非代码）与 `/grill-with-docs`（代码项目）通过逐分支盘问把决策树全部锁定，再开始动代码；后者还会同步更新 `CONTEXT.md` 与 ADR。
4. **规格 → 票据 → 实现**：`/to-spec` 把当前对话压成规格 → `/to-tickets` 切成 tracer-bullet 票（带阻塞边）→ `/implement` 按 TDD 在预定点驱动 `/tdd` + 收尾时 `/code-review`。
5. **架构治理**：`/improve-codebase-architecture` 周期性扫描"深模块化机会"，输出可视化 HTML 报告并盘问所选项目；`codebase-design` 提供共享的设计词汇（深接口、清洁接缝、可测性）。
6. **调试与排错**：`diagnosing-bugs` 提供"复现 → 最小化 → 假设 → 插桩 → 修复 → 回归测试"的标准循环；`resolving-merge-conflicts` 按 hunk 逐个解冲突，按双方原始意图追溯而非 `--abort`。
7. **辅助工作流**：`triage`（按状态机给 issue 打标签）、`wayfinder`（把超大不确定工作切成一组"决策票据"逐个解决）、`research`（基于高可信原始资料做调研，输出带引用的 markdown）、`prototype`（快速原型验证设计问题）、`handoff`（压缩当前会话为移交文档）、`teach`（多会话教学）、`writing-great-skills`（写技能的元参考）。

## Skills Library Overview

- **Engineering · 用户调用**：`ask-matt`（路由）、`grill-with-docs`、`triage`、`improve-codebase-architecture`、`setup-matt-pocock-skills`（每仓库一次性配置）、`to-spec`、`to-tickets`、`implement`、`wayfinder`。
- **Engineering · 模型调用**：`prototype`、`diagnosing-bugs`、`research`、`tdd`、`domain-modeling`、`codebase-design`、`code-review`、`resolving-merge-conflicts`。
- **Productivity · 用户调用**：`grill-me`、`handoff`、`teach`、`writing-great-skills`。
- **Productivity · 模型调用**：`grilling`（`grill-me` / `grill-with-docs` 背后的可复用盘问循环）。

## Installation & Support

Matt Pocock Skills supports the following AI editors and platforms:
- [Claude Code](../../claudecode/mattpocock-skills/INSTALL-zh.md)
- [Cursor](../../cursor/mattpocock-skills/INSTALL-zh.md)
- [Codex](../../codex/mattpocock-skills/INSTALL-zh.md)
- [OpenCode](../../opencode/mattpocock-skills/INSTALL-zh.md)
- [OpenClaw](../../openclaw/mattpocock-skills/INSTALL-zh.md)
- [OpenAgent](../../openagent/mattpocock-skills/INSTALL-zh.md)
- [Qoder](../../qoder/mattpocock-skills/INSTALL-zh.md)

---
For more information, visit: [GitHub - mattpocock/skills](https://github.com/mattpocock/skills) · [Newsletter](https://www.aihero.dev/s/skills-newsletter)
