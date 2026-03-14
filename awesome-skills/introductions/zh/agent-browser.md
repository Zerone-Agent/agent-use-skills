# Agent Browser

**Agent Browser** 是一个基于 Rust 的高性能无头浏览器自动化 CLI 工具，支持 Node.js 备选方案。它允许 AI Agent 通过结构化的命令行指令进行网页导航、点击、输入及快照获取。

## 标签

文档与办公 | 待验证

## 核心理念

- **Agent 友好**：通过 `snapshot -i` 提供带有简化引用（如 `@e1`, `@e2`）的交互元素列表，极大降低了 Agent 解析复杂 DOM 的难度。
- **高性能**：底层采用 Rust 实现（支持 Playwright/Puppeteer 协议），确保了极速的启动和执行性能。
- **结构化交互**：所有操作（点击、填充、获取文本）均通过一致的命令行接口完成，便于集成到自动化工作流中。

## 核心功能与工作流

1.  **网页快照**：`snapshot -i` 获取页面当前的交互元素及其引用，供后续指令使用。
2.  **交互操作**：支持 `click`、`fill`、`hover`、`scroll` 等所有标准浏览器操作，直接使用快照中的 `@ref`。
3.  **状态管理**：支持 `state save/load` 保存和恢复会话状态（如 Cookie、localStorage），方便跳过登录流程。
4.  **多媒体捕获**：提供网页截图、PDF 生成以及录像（Video Recording）功能，用于结果验证或 Demo 展示。

## 技能库概览

- **核心命令**：`agent-browser` CLI 提供导航、分析、交互和信息获取四大类指令。
- **会话隔离**：支持 `--session` 参数，可同时维护多个独立的浏览器上下文。
- **高级调试**：支持 `--headed` 模式显示浏览器窗口，以及控制台、错误日志查看。

## 安装与支持

Agent Browser 目前仅支持以下平台：

- [OpenClaw](../../openclaw/agent-browser/INSTALL-zh.md)

---
更多信息请查看：[Agent Browser GitHub](https://github.com/vercel-labs/agent-browser)
