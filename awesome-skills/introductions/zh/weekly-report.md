# Weekly Report

**Weekly Report** 是一个个人周报生成助手技能，能够将零散的工作记录整理成结构清晰的规范周报，并支持转换为 Word 文档。

## 标签

🗂️ 文档与办公 | ✅ 已验证

## 核心理念

- **客观专业**：保持语气客观、专业，避免口语化表达
- **精炼准确**：每条工作项言简意赅，聚焦结果而非过程
- **数据驱动**：优先保留具体数据支撑（如"提升50%"、"修复3个bug"）
- **结构清晰**：严格遵守本周工作与下周计划的结构划分
- **智能润色**：将口语化描述改写为专业书面语

## 主要功能与工作流

### 场景 1：从工作内容生成周报

1. **信息收集**：收集姓名、工作内容、下周计划等关键信息
2. **日期获取**：自动计算当前周日期范围或从用户输入中提取
3. **内容润色**：将口语化描述改写为专业书面语，提炼关键成果
4. **Markdown 生成**：按照标准格式生成结构化周报
5. **用户确认**：展示预览并询问是否需要调整
6. **Word 转换**：可选转换为正式 Word 文档

### 场景 2：Markdown 转 Word

1. **确认需求**：确认源 Markdown 文件路径
2. **执行转换**：使用模板生成格式规范的 Word 文档
3. **交付结果**：告知用户文档保存路径

## 工具脚本

| 脚本 | 功能 |
|------|------|
| `weekly_range.py` | 自动计算当前周的日期范围 |
| `md_to_docx.py` | 将 Markdown 周报转换为 Word 文档 |
| `template.docx` | Word 文档格式模板 |

## 依赖环境

- `python-docx` - 读取和生成 Word 文档
- `markdown` - 解析 Markdown 格式
- `beautifulsoup4` - HTML 处理

## 触发场景

- 用户提及"周报"、"这周工作"、"整理工作内容"
- 需要生成个人工作周报
- 将 Markdown 转为 Word 文档

## 安装与支持

Weekly Report 支持以下 AI 编辑器和平台：
- [Claude Code](../../claudecode/weekly-report/INSTALL-zh.md)
- [Codex](../../codex/weekly-report/INSTALL-zh.md)
- [Cursor](../../cursor/weekly-report/INSTALL-zh.md)
- [OpenCode](../../opencode/weekly-report/INSTALL-zh.md)
- [OpenClaw](../../openclaw/weekly-report/INSTALL-zh.md)
- [Zerone](../../zerone/weekly-report/INSTALL-zh.md)
- [Qoder](../../qoder/weekly-report/INSTALL-zh.md)

---
了解更多信息，请访问：[GitHub - Zerone-Agent/agent-use-skills](https://github.com/Zerone-Agent/agent-use-skills)