# gstack

**gstack** 是 Y Combinator 总裁 Garry Tan 公开的个人 Claude Code 配置——把单一 Agent 转化为一支由 23 位"专家角色"组成的虚拟工程团队，覆盖完整 sprint 流程 Think → Plan → Build → Review → Test → Ship → Reflect，目标是让一个兼职 builder 像 20 人团队那样发版。

## 标签

💻 开发与测试 | 🔍 待验证

## Core Philosophy

- **一人即团队**：在 AI 加持下，完整实现的边际成本接近零。Garry Tan 本人 2026 年前 60 天用 gstack 兼职交付 3 个生产服务 + 40+ feature，逻辑代码变更速度是 2013 年的 ~810 倍。
- **Boil the Ocean**：旧时代"别煮海"是因为工程时间是瓶颈；AI 让 90% 方案与 100% 方案的差距只剩几秒钟，所以每次都做完整版。Lake by lake，最后整个 ocean 都煮开。
- **Search Before Building**：三层知识体系——Layer 1（成熟模式，先查再质疑）、Layer 2（新兴热点，警惕 Mr. Market）、Layer 3（第一性原理，最有价值）。
- **流程即产品**：每个技能读取上游技能的产出——`/office-hours` 写的设计文档被 `/plan-ceo-review` 读、`/plan-eng-review` 写的测试计划被 `/qa` 接走、`/review` 找到的 bug 被 `/ship` 验证修复。完整链路无信息漏失。
- **真实浏览器、真实测试、真实 PR**：QA 不是模拟，而是用定制 Chromium 真点真测；ship 不是注释，而是同步主分支、跑测试、审计覆盖率、推送、开 PR 一条龙。

## Key Features & Workflow

1. **30 秒安装**：`git clone ~/.claude/skills/gstack && ./setup`。setup 自动按 host 把技能分发到对应平台的 `~/.<platform>/skills/gstack-*/`，安装定制 Chromium 与 Playwright，注册 MCP server。
2. **Team Mode**：在仓库内跑 `./setup --team && bin/gstack-team-init required`，提交 `.claude/` 与 `CLAUDE.md`，团队成员自动获得 gstack，每小时静默自动更新。
3. **Sprint 全链路**：从产品盘问（`/office-hours`）到战略评审（`/plan-ceo-review`）→ 架构锁定（`/plan-eng-review`）→ 设计评分（`/plan-design-review`）→ DX 评审（`/plan-devex-review`）→ 自动规划（`/autoplan`）→ 代码审查（`/review`）→ 真浏览器 QA（`/qa`）→ 发布（`/ship` / `/land-and-deploy` / `/canary`）→ 复盘（`/retro`）。
4. **设计专项**：`/design-consultation`（从零构建设计系统）、`/design-shotgun`（4-6 个 mockup 变体并排 + taste memory）、`/design-html`（基于 Pretext 计算布局的 production HTML）、`/design-review`（审计并直接修复，原子提交）。
5. **安全与性能**：`/cso`（OWASP Top 10 + STRIDE，17 条误报排除 + 8/10 置信度门 + 独立验证）、`/benchmark`（Core Web Vitals + 前后对比）、`/canary`（部署后控制台/性能/页面失败监控循环）。
6. **多 Agent 协同**：`/pair-agent` 让任何 AI Agent（OpenClaw、Hermes、Codex、Cursor）共享同一个浏览器，自动 ngrok 隧道、tab 隔离、限流、活动归属。
7. **Power Tools**：`/codex`（OpenAI Codex 二次审查）、`/careful`、`/freeze` / `/unfreeze`（暂停/恢复某些技能）、`/guard`、`/learn`（喂知识给 gstack）、`/document-release`、`/document-generate`、`/make-pdf`、`/diagram`。
8. **gbrain 集成**（可选）：通过 `/setup-gbrain` 把代码索引成可语义检索的知识库，让 gstack 能引用整个 monorepo 的上下文；`/sync-gbrain` 增量重建。

## Skills Library Overview

- **Think**：`/office-hours`（YC 风格 6 个强制提问，重写产品框架）。
- **Plan**：`/plan-ceo-review`（4 种 scope 模式）、`/plan-eng-review`（ASCII 数据流 / 状态机 / 测试矩阵）、`/plan-design-review`（10 分制评分 + AskUserQuestion）、`/plan-devex-review`（DX EXPANSION / POLISH / TRIAGE）、`/plan-tune`、`/autoplan`（自动跑全套规划）。
- **Build**：`/spec`、`/design-consultation`、`/design-shotgun`、`/design-html`、`/ios-clean`、`/ios-sync`。
- **Review**：`/review`（生产级 bug 检测 + 自动修复）、`/investigate`（Iron Law：无调查不修复，3 次失败后停止）、`/devex-review`、`/design-review`、`/cso`（OWASP + STRIDE）。
- **Test**：`/qa`（真浏览器 + 自动写回归测试）、`/qa-only`（仅报告）、`/ios-qa`、`/ios-fix`、`/benchmark`。
- **Ship**：`/ship`（同步 main + 跑测试 + 审计覆盖率 + 推 + 开 PR）、`/land-and-deploy`（合并 + 等 CI/部署 + 验证）、`/canary`（部署监控）。
- **Reflect**：`/retro`、`/document-release`、`/document-generate`。
- **Browse & Pair**：`/browse`、`/connect-chrome`、`/open-gstack-browser`、`/setup-browser-cookies`、`/pair-agent`、`/scrape`。
- **Utility**：`/make-pdf`、`/diagram`、`/learn`、`/gstack-upgrade`、`/freeze` / `/unfreeze` / `/guard` / `/careful`、`/hosts`、`/health`、`/codex`（用 Codex 做第二意见）。

## Installation & Support

gstack supports the following AI editors and platforms (via `./setup` or `--host <name>`):
- [Claude Code](../../claudecode/gstack/INSTALL-zh.md)
- [Cursor](../../cursor/gstack/INSTALL-zh.md)
- [Codex](../../codex/gstack/INSTALL-zh.md)
- [OpenCode](../../opencode/gstack/INSTALL-zh.md)
- [OpenClaw](../../openclaw/gstack/INSTALL-zh.md)

---
For more information, visit: [GitHub - garrytan/gstack](https://github.com/garrytan/gstack)
