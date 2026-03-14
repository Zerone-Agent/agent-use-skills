# Playwright Skill

**Playwright Skill** 是一个基于 [Playwright](https://playwright.dev/) 的全功能浏览器自动化技能。它旨在帮助开发者和 AI Agent 自动执行各种浏览器任务，包括网页测试、表单填充、截图采集、响应式设计检查、UX 验证以及复杂的登录流程自动化。

## 标签

开发与测试 | 待验证

## 核心理念

- **自动化与智能探测 (Automation & Detection)**：能够自动探测本地正在运行的开发服务器（Dev Servers），无需手动输入 URL。
- **临时性与无痕 (Ephemeral & Clean)**：所有生成的测试脚本均存放在 `/tmp` 目录下，执行完后由系统自动清理，不会污染项目代码库。
- **可视化调试 (Visible Debugging)**：默认开启非无头模式（`headless: false`），用户可以直观地观察到浏览器的自动化操作过程。
- **高可扩展性 (Extensible)**：不仅限于预设脚本，能够根据用户需求动态编写任意复杂的 Playwright 自动化代码。

## 主要功能与工作流

1. **开发服务器探测**：在测试本地项目前，自动扫描并识别正在运行的端口。
2. **动态脚本编写**：根据用户描述的任务（如“测试登录流程”或“检查移动端布局”），实时生成定制化的 Playwright 脚本。
3. **跨多平台执行**：通过统一的执行器（Executor）在指定的技能目录下安全运行。
4. **多维度验证**：
    - **截图与对比**：自动保存全屏或特定区域截图。
    - **响应式测试**：在不同分辨率（桌面、平板、手机）下验证页面布局。
    - **链接检查**：自动扫描并验证页面上的所有链接是否有效。
5. **结果反馈**：实时输出执行日志，并展示测试结果与产物（如截图）。

## 技能库概览

该技能包含以下核心组成部分：
- **核心执行器 (`run.js`)**：负责加载环境并安全执行测试代码。
- **辅助函数库 (`lib/helpers.js`)**：提供服务器探测、安全点击、表单填充等常用工具函数。
- **API 参考手册 (`API_REFERENCE.md`)**：详尽的 Playwright 操作指南，供进阶任务使用。

## 安装与支持

Playwright Skill 支持以下 AI 编辑器和平台：
- [Claude Code](../../claudecode/playwright-skill/INSTALL-zh.md)
- [Cursor](../../cursor/playwright-skill/INSTALL-zh.md)
- [Codex](../../codex/playwright-skill/INSTALL-zh.md)
- [OpenCode](../../opencode/playwright-skill/INSTALL-zh.md)
- [OpenClaw](../../openclaw/playwright-skill/INSTALL-zh.md)
- [Qoder](../../qoder/playwright-skill/INSTALL-zh.md)

---
了解更多信息，请访问：[GitHub - Zerone-Agent/agent-use-skills](https://github.com/Zerone-Agent/agent-use-skills)
