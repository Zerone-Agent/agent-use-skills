# OfficeCLI

**OfficeCLI** 是全球首个专为 AI 智能体设计的 Office 套件，让 AI Agent 用一条命令即可创建、读取和编辑 Word、Excel、PowerPoint 文档。开源免费，单一可执行文件，无需安装 Office，零依赖。

## 标签

🗂️ 文档与办公 | ✅ 已验证

## 核心理念

- **AI 原生设计**：所有命令支持 `--json` 结构化输出，路径寻址，渐进式复杂度（L1 读取 → L2 DOM → L3 原始 XML）
- **零依赖**：单一自包含二进制文件，.NET 运行时内嵌，跨平台运行（macOS / Linux / Windows）
- **内置渲染引擎**：无需 Office，智能体可"看见"自己创建的内容（HTML / PNG / 实时预览），"渲染 → 看 → 改"循环在 CI / Docker / 无头环境均可运行
- **自愈式工作流**：结构化错误码 + 建议修正，智能体无需人工介入即可自纠错

## 主要功能与工作流

1. **三层架构**：L1 语义视图（`view`）→ L2 DOM 操作（`get`/`set`/`add`/`remove`）→ L3 原始 XML（`raw`/`raw-set`）
2. **内置渲染引擎**：`view html` / `view screenshot` / `watch` 原生输出 HTML 和 PNG，支持实时预览
3. **公式与透视引擎**：150+ Excel 函数写入即自动求值，一条命令生成原生 OOXML 数据透视表
4. **模板合并**：`merge` 替换 `{{key}}` 占位符，设计一次、填充 N 次
5. **Dump 往返**：`dump` 将文档序列化为可重放的 batch JSON，从现有文档学习
6. **MCP 服务器**：内置 MCP 支持，一条命令注册到 Claude Code / Cursor / VS Code 等
7. **驻留模式与批量执行**：文档保持在内存中实现零延迟操作，批量模式原子化多命令执行
8. **专业子技能**：学术论文、融资路演、Morph 动画、3D 演示、财务模型、数据仪表盘等

## 技能库概览

- **Word（.docx）**：段落、表格、样式、页眉页脚、图片、公式、批注、脚注、水印、书签、目录、图表、超链接、节、表单域、内容控件、域、OLE 对象、完整 i18n 与 RTL 支持
- **Excel（.xlsx）**：单元格、工作表、表格、排序、条件格式、图表、数据透视表、切片器、命名范围、数据验证、图片、迷你图、批注、自动筛选、形状、CSV 导入
- **PowerPoint（.pptx）**：幻灯片、形状、图片、表格、图表、动画、Morph 过渡、3D 模型、幻灯片缩放、公式、主题、连接线、视频/音频、组合、备注、批注、占位符

## 安装与支持

OfficeCLI 支持以下 AI 编辑器和平台：

- [Claude Code](../../claudecode/officecli/INSTALL-zh.md)
- [Cursor](../../cursor/officecli/INSTALL-zh.md)
- [Codex](../../codex/officecli/INSTALL-zh.md)
- [OpenCode](../../opencode/officecli/INSTALL-zh.md)
- [OpenClaw](../../openclaw/officecli/INSTALL-zh.md)
- [Zerone](../../zerone/officecli/INSTALL-zh.md)
- [Qoder](../../qoder/officecli/INSTALL-zh.md)

---
了解更多信息，请访问：[GitHub - iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI)
