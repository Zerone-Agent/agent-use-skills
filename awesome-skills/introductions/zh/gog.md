# Gog (Google Workspace CLI)

**Gog** 是一个强大的命令行工具（CLI），用于管理和操作 Google Workspace 的核心服务，包括 Gmail、日历、云端硬盘（Drive）、联系人、表格（Sheets）和文档（Docs）。

## 标签

🗂️ 文档与办公 | 🔍 待验证

## 核心理念

- **一站式管理**：通过统一的 `gog` 指令，实现对 Google 生态系统的全方位操控。
- **Agent 友好**：支持 JSON 输出格式（`--json`），方便 AI Agent 提取并处理邮件内容、日历事件或表格数据。
- **安全优先**：基于 OAuth 认证流程，确保 Agent 仅在用户授权的范围内执行操作。

## 核心功能与工作流

1. **Gmail 操作**：支持邮件搜索（搜索语法与网页版一致）及邮件发送。
2. **云端硬盘管理**：支持文件搜索与列出，方便 Agent 查找参考文档。
3. **表格数据交互**：支持读取（get）、更新（update）和追加（append）表格数据，非常适合 Agent 自动记录数据或生成报表。
4. **日历与联系人**：支持查看日程安排和管理联系人信息。
5. **文档导出**：支持将 Google Docs 导出为纯文本等格式，方便 Agent 阅读内容。

## 技能库概览

- **核心指令**：`gog` CLI 封装，涵盖各子服务操作。
- **身份认证**：通过 `gog auth` 进行 OAuth 凭据配置。
- **环境变量**：支持设置 `GOG_ACCOUNT` 环境变量以简化命令调用。

## 安装与支持

Gog 目前仅支持以下平台：

- [OpenClaw](../../openclaw/gog/INSTALL-zh.md)

---
更多信息请查看：[Gog 官方文档](https://gogcli.sh)
