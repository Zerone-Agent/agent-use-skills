# OfficeCLI - Agent-Ready 认证

**OfficeCLI** 已经正式通过了 **Agent-Ready** 认证！

OfficeCLI 是全球首个专为 AI 智能体设计的 Office 套件 — 让 AI Agent 用一条命令即可创建、读取、编辑和渲染 Word、Excel、PowerPoint 文档。开源免费，单一可执行文件，无需安装 Office。

## 认证亮点

- **AI 原生设计**：专为 AI Agent 消费而设计 — 路径寻址、结构化 JSON 输出、渐进式复杂度（L1 → L2 → L3）
- **零依赖**：单一自包含二进制文件，.NET 运行时内嵌，跨平台运行（macOS / Linux / Windows）
- **内置渲染引擎**：Agent 可以"看见"自己的产出 — `view html`、`view screenshot`、`watch`（实时预览）— 无需 Office，在 CI / Docker / 无头环境均可运行
- **150+ Excel 函数自动求值**：写 `=SUM(A1:A2)`，立刻拿到计算结果 — 无需回环到 Office 重算
- **11 个专业子技能**：学术论文、融资路演、Morph 动画、3D 演示、财务模型、数据仪表盘等
- **内置 MCP 服务器**：一条命令注册 — `officecli mcp claude` / `officecli mcp cursor` / `officecli mcp vscode`
- **模板合并与 Dump 往返**：`merge` 替换 `{{key}}` 占位符；`dump` 将文档序列化为可重放的 batch JSON

## 为什么它是 Agent-Ready 的？

OfficeCLI 成功满足了 Agent-Ready 认证的所有核心标准：

- **原子化动作开放**：核心功能通过 CLI 命令全面暴露 — `create`、`view`、`get`、`set`、`add`、`remove`、`move`、`swap`、`query`、`batch`、`merge`、`dump`、`watch`、`validate` — 无需 UI 交互。三层架构：L1 语义视图、L2 DOM 操作、L3 原始 XML 兜底。
- **结构化反馈**：所有命令支持 `--json`，schema 一致。结构化错误码（`not_found`、`invalid_value`、`unsupported_property`）包含建议修正和有效范围 — 智能体无需人工介入即可自纠错。
- **安全护栏**：`validate` 校验 OpenXML 模式；`view issues` 枚举格式、内容和结构性问题；`watch` 提供实时预览供人工审查后交付。
- **经过验证的集成**：在 Claude Code、Cursor、Codex、OpenCode、OpenClaw、Zerone、Qoder 等主流 AI Agent 平台上经过广泛测试。安装时自动检测 AI 工具并完成配置。

## 核心 CLI 命令

| 命令 | 功能 |
|------|------|
| `officecli create <file>` | 创建空白 .docx / .xlsx / .pptx |
| `officecli view <file> <mode>` | 查看内容（outline / text / annotated / stats / issues / html / screenshot）|
| `officecli get <file> <path>` | 获取元素及子元素（`--json`、`--depth N`）|
| `officecli query <file> <selector>` | CSS 风格查询（`[attr=value]`、`:contains()`、`:has()`）|
| `officecli set <file> <path> --prop ...` | 修改元素属性 |
| `officecli add <file> <parent> --type ...` | 添加元素（或通过 `--from` 克隆）|
| `officecli remove <file> <path>` | 删除元素 |
| `officecli move <file> <path> --to ...` | 移动元素 |
| `officecli batch <file>` | 单次保存周期内执行多条操作 |
| `officecli merge <template> <output> <data>` | 模板合并 — 替换 `{{key}}` 占位符 |
| `officecli dump <file>` | 序列化为可重放的 batch JSON |
| `officecli watch <file>` | 浏览器实时 HTML 预览，自动刷新 |
| `officecli validate <file>` | OpenXML 模式校验 |
| `officecli mcp <platform>` | 注册 MCP 服务器，用于 AI 工具集成 |

## 对比

| 特性 | OfficeCLI | python-docx / openpyxl | Microsoft Office |
|------|-----------|----------------------|------------------|
| AI 原生 CLI + JSON | ✓ | ✗ | ✗ |
| 零安装（单一可执行文件） | ✓ | ✗（需 Python + pip） | ✗ |
| Word + Excel + PowerPoint | ✓ | 需要多个库 | ✓ |
| 内置渲染引擎 | ✓ | ✗ | ✗ |
| 跨格式模板合并（`{{key}}`） | ✓ | ✗ | ✗ |
| 实时预览 | ✓ | ✗ | ✗ |
| 无头 / CI 环境 | ✓ | ✓ | ✗ |

---

- [OfficeCLI GitHub 仓库](https://github.com/iOfficeAI/OfficeCLI)
- [OfficeCLI 官方网站](https://officecli.ai)
- [查看 OfficeCLI 完整文档](../../awesome-skills/introductions/zh/officecli.md)
