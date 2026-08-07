# Reports Summary

**Reports Summary** 是一个专业的周报汇总助手技能，能够从零散的员工周报中提取关键信息，生成结构清晰的汇总报告，并支持转换为 Word 文档。

## 标签

🗂️ 文档与办公 | ✅ 已验证

## 核心理念

- **客观专业**：保持语气客观、专业，避免口语化表达
- **精炼准确**：每条总结言简意赅，聚焦结果而非过程
- **数据驱动**：优先保留具体数据支撑（如"提升50%"、"修复3个bug"）
- **结构清晰**：严格遵守各级标题结构，确保文档层次分明
- **隐私保护**：在最终汇总中隐去具体员工姓名
- **智能合并**：多人参与同一项目时自动合并相似内容

## 主要功能与工作流

### 场景 1：从周报文件生成汇总

1. **周报读取**：支持读取单个或批量读取 .docx 周报文件
2. **内容分析**：提取亮点、撰写工作总结、分类汇总、去重合并
3. **Markdown 生成**：按照标准格式生成结构化周报
4. **用户确认**：展示预览并询问是否需要调整
5. **Word 转换**：可选转换为正式 Word 文档

### 场景 2：Markdown 转 Word

1. **确认需求**：确认源 Markdown 文件路径
2. **执行转换**：使用模板生成格式规范的 Word 文档
3. **交付结果**：告知用户文档保存路径

## 工具脚本

| 脚本 | 功能 |
|------|------|
| `read_reports.py` | 批量读取 .docx 周报文件，返回 JSON 格式内容 |
| `md_to_docx.py` | 将 Markdown 周报转换为 Word 文档 |
| `template.docx` | Word 文档格式模板 |

## 依赖环境

- `python-docx` - 读取和生成 Word 文档
- `markdown` - 解析 Markdown 格式
- `beautifulsoup4` - HTML 处理

## 触发场景

- 用户提及"周报"、"汇总"、"总结"、"报告整理"
- 需要处理 .docx 周报文件
- 生成团队工作汇总
- 将 Markdown 转为 Word 文档

## 安装与支持

Reports Summary 支持以下 AI 编辑器和平台：
- [Claude Code](../../claudecode/reports-summary/INSTALL-zh.md)
- [Codex](../../codex/reports-summary/INSTALL-zh.md)
- [Cursor](../../cursor/reports-summary/INSTALL-zh.md)
- [OpenCode](../../opencode/reports-summary/INSTALL-zh.md)
- [OpenClaw](../../openclaw/reports-summary/INSTALL-zh.md)
- [Zerone](../../zerone/reports-summary/INSTALL-zh.md)
- [Qoder](../../qoder/reports-summary/INSTALL-zh.md)

---
了解更多信息，请访问：[GitHub - Zerone-Agent/agent-use-skills](https://github.com/Zerone-Agent/agent-use-skills)