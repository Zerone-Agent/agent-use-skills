# Obsidian CLI

**Obsidian CLI** 是 Obsidian 官方推出的命令行工具（v1.12+），让 AI Agent 能够直接通过终端控制 Obsidian 桌面应用，实现对笔记库的全面操作。

## 标签

🗂️ 文档与办公 | ✅ 已验证

## 核心理念

- 通过 IPC 与运行中的 Obsidian 桌面实例通信，实现零延迟的实时操作
- 所有参数统一使用 `key=value` 语法，输出默认为纯文本，完美支持 Unix 管道
- 覆盖 Obsidian 所有核心功能，从笔记读写到插件管理、同步控制、开发者工具一应俱全

## 主要功能与工作流

1. **笔记读写与管理**: 读取、创建、追加、移动、重命名、删除笔记，支持模板创建
2. **日记操作**: 读取今日日记、追加内容、在日记中插入待办事项
3. **全文搜索**: 支持路径限定、结果数量限制、JSON 格式输出、上下文搜索
4. **属性与标签管理**: 读写 frontmatter 属性、标签统计与过滤
5. **任务管理**: 跨库查询任务、按文件/日记筛选、切换任务完成状态
6. **链接分析**: 反向链接、孤立笔记、未解析链接、死链检测
7. **同步管理**: Obsidian Sync 状态检查、版本历史、文件恢复
8. **开发者工具**: JavaScript 执行（eval）、截图、DOM/CSS 检查、控制台日志
9. **自动化集成**: 支持 cron 任务、AI Agent 自动化工作流、无头服务器运行

## 命令概览

该 CLI 提供 **130+ 条命令**，涵盖以下分组：

- **files**: 笔记增删改查与文件发现
- **daily**: 日记操作
- **search**: 全文搜索
- **properties / tags**: 元数据与标签管理
- **tasks**: 任务查询与管理
- **links**: 图谱与链接分析
- **bookmarks / templates / plugins**: 书签、模板、插件管理
- **sync / history**: 同步控制与文件版本恢复
- **dev**: JavaScript 执行、截图、调试工具
- **vault**: 库信息与应用控制

## 安装与支持

Obsidian CLI 支持以下 AI 编辑器和平台：

- [Claude Code](../../claudecode/obsidian-cli/INSTALL-zh.md)
- [Cursor](../../cursor/obsidian-cli/INSTALL-zh.md)
- [Codex](../../codex/obsidian-cli/INSTALL-zh.md)
- [OpenCode](../../opencode/obsidian-cli/INSTALL-zh.md)
- [OpenClaw](../../openclaw/obsidian-cli/INSTALL-zh.md)
- [Zerone](../../zerone/obsidian-cli/INSTALL-zh.md)
- [Qoder](../../qoder/obsidian-cli/INSTALL-zh.md)

---
更多信息请访问：[GitHub - pablo-mano/Obsidian-CLI-skill](https://github.com/pablo-mano/Obsidian-CLI-skill)
