# OpenCLI

**OpenCLI** 是一个将网站、浏览器会话、Electron 应用和本地工具转化为确定性接口的 CLI 工具库。它可复用已登录的浏览器状态，自动化实时工作流，并将重复操作固化为可复用的 CLI 命令。

## 标签

🛠️ 效率工具 | ✅ 已验证

## 核心理念

OpenCLI 的设计哲学强调：
- **账号安全**：复用 Chrome/Chromium 的登录状态，凭证不离开浏览器
- **确定性输出**：相同命令、相同输出结构，适合管道处理、脚本化和 CI 环境
- **零 LLM 成本**：运行时不消耗 token，执行 10000 次也不付费
- **AI Agent 就绪**：提供探索 API、生成适配器、级联认证策略、浏览器直控等能力

## 主要功能与工作流

1. **内置适配器**：87+ 预构建适配器，覆盖 Bilibili、知乎、小红书、Reddit、Twitter/X、HackerNews 等平台
2. **浏览器直控**：`opencli browser` 命令让 AI Agent 直接控制浏览器进行点击、输入、提取、截图
3. **适配器生成**：通过 `explore`、`synthesize`、`generate`、`cascade` 从真实浏览器行为生成新适配器
4. **CLI Hub**：统一发现、自动安装、透传外部 CLI 工具（gh、docker、obsidian 等）
5. **桌面应用控制**：通过 CDP 驱动 Electron 应用（Cursor、Codex、ChatGPT、Notion 等）

## 技能库概览

OpenCLI 为 AI Agent 提供以下技能：

- **opencli-usage**：运行 OpenCLI 命令与网站/桌面应用交互的完整指南，覆盖 87+ 适配器
- **opencli-browser**：浏览器自动化技能，支持导航、点击、输入、提取、等待等操作
- **opencli-explorer**：适配器探索式开发完全指南，从 API 发现到测试验证
- **opencli-oneshot**：单点快速 CLI 生成，URL + 一句话描述即可生成适配器
- **opencli-autofix**：自动修复损坏的适配器，诊断 → 修补 → 重试 → 提交上游
- **smart-search**：智能搜索路由器，根据话题将查询路由到最佳 OpenCLI 搜索源

## 安装与支持

OpenCLI 支持以下 AI 编辑器和平台：

- [Claude Code](../../claudecode/opencli/INSTALL-zh.md)
- [Cursor](../../cursor/opencli/INSTALL-zh.md)
- [Codex](../../codex/opencli/INSTALL-zh.md)
- [OpenCode](../../opencode/opencli/INSTALL-zh.md)
- [OpenClaw](../../openclaw/opencli/INSTALL-zh.md)
- [Zerone](../../zerone/opencli/INSTALL-zh.md)
- [Qoder](../../qoder/opencli/INSTALL-zh.md)

---
了解更多信息，请访问：[GitHub - jackwener/OpenCLI](https://github.com/jackwener/OpenCLI)