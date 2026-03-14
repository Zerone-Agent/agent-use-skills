# GitHub

**GitHub** 技能允许 AI Agent 通过官方的 `gh` CLI 直接操作 GitHub。它涵盖了从项目管理（Issues/PRs）到自动化运维（Actions/Runs）的全方位能力，让开发流水线更加智能。

## 标签

🗂️ 文档与办公 | 🔍 待验证

## 核心理念

- **官方集成**：基于 GitHub 官方 CLI 构建，确保操作的稳定性和安全性。
- **深度透视**：通过 `gh run` 监控 CI/CD 状态，甚至可以提取失败步骤的详细日志。
- **结构化查询**：支持 JSON 输出和 `jq` 过滤，方便 Agent 快速提取核心数据（如 PR 状态、Issue 编号）。
- **无限制访问**：内置 `gh api` 支持，可调用所有 GitHub REST API，覆盖所有高级操作场景。

## 核心功能与工作流

1. **Pull Request 管理**：查看 PR 的检查状态（checks）、合并冲突以及内容详情。
2. **Action 自动化**：列出工作流运行记录（run list），查看运行详情并获取失败日志（log-failed）。
3. **Issue 追踪**：列出项目中的待办事项，支持按属性过滤和结构化显示。
4. **仓库交互**：支持在非 Git 目录下通过 `--repo` 参数指定目标仓库进行跨项目操作。

## 技能库概览

- **核心工具**：封装了 `gh` 命令行。
- **CI/CD 集成**：重点强化了对 GitHub Actions 的监控能力。
- **API 扩展性**：通过 `gh api` 提供了无限的扩展可能。

## 安装与支持

GitHub 技能目前仅支持以下平台：

- [OpenClaw](../../openclaw/github/INSTALL-zh.md)

---
更多信息请查看：[GitHub CLI 官方文档](https://cli.github.com/manual/)
