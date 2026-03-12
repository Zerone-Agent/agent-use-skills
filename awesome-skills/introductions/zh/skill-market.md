# Skill Market

**Skill Market** 是一个自动化的技能发现与安装技能，允许 AI Agent 从 Zerone Skill Market (https://api.zerone.market/api) 查找、浏览并安装全新的技能。

## 核心理念
- **自动化集成**：消除手动下载和配置技能的繁琐过程，实现一键式技能扩展。
- **环境感知**：自动检测当前 Agent 框架（如 Claude Code, Cursor 等），并匹配最合适的安装方案。
- **渐进式扩展**：支持按需发现，避免在初始上下文中加载不必要的技能脚本。

## 关键功能与工作流
1. **浏览与发现**：通过 `market.py list` 获取全量可用技能列表及其详细描述。
2. **详细信息查询**：通过 `info <skill-name>` 深入了解特定技能的功能、支持的框架及版本信息。
3. **框架兼容性检查**：在安装前自动核对当前 Agent 环境与技能的兼容性，确保安装成功。
4. **自动化安装**：自动执行安装教程中的步骤，将新技能直接集成到 `.agent/skills/` 目录中。

## 技能库概览
- **Market API 交互**：封装了与 Zerone Market 后端的完整通信逻辑。
- **本地环境管理**：负责本地技能目录的初始化、技能下载及框架特定的配置更新。

## 安装与支持
Skill Market 能够完美支持以下 AI 编辑器与平台：
- [Claude Code](../../claudecode/skill-market/INSTALL-zh.md)
- [Cursor](../../cursor/skill-market/INSTALL-zh.md)
- [Codex](../../codex/skill-market/INSTALL-zh.md)
- [OpenCode](../../opencode/skill-market/INSTALL-zh.md)
- [OpenClaw](../../openclaw/skill-market/INSTALL-zh.md)
- [Qoder](../../qoder/skill-market/INSTALL-zh.md)

---
更多信息请访问：[GitHub - Zerone Agent](https://github.com/zerone-agent/agent-use-skills)
