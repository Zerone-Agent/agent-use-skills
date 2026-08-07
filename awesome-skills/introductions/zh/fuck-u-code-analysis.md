# Fuck-U-Code Analysis

**Fuck-U-Code Analysis** 是一个代码质量分析与审查技能，通过运行 `fuck-u-code analyze` 对代码进行 7 个维度、11 项指标的量化评分（0-100 分），并基于严重度和权重输出可执行的修复建议。

## 标签

💻 开发与测试 | ✅ 已验证

## 核心理念
- **量化驱动审查**：基于 AST 解析的精确度量，用数据而非直觉评判代码质量。
- **权重优先分级**：复杂度 32% > 重复 20% > 体积 18% > 结构 12% > 错误处理 8% > 文档 5% > 命名 5%，按权重与严重度交叉排序确定修复优先级。
- **可执行修复建议**：每条建议必须引用具体指标值、函数名和行号，且不超过 30 个词。
- **语言特定阈值**：14 种编程语言（Go、JS、TS、Python、Java、C、C++、Rust、C#、Lua、PHP、Ruby、Swift、Shell）各有独立的评判阈值，尊重语言惯例。

## 主要功能与工作流

1. **运行分析 (Run Analysis)**：执行 `fuck-u-code analyze . -f json -o /tmp/fuc-report.json`，获取结构化 JSON 报告，支持排除模式、并发控制和多种输出格式。
2. **识别问题文件 (Identify Critical Files)**：从报告中提取整体评分和逐文件评分，聚焦得分低于 60 的"屎山"文件。
3. **下钻指标详情 (Drill into Metrics)**：对每个问题文件检查 11 项指标的 `normalizedScore`、`severity` 和 `locations[]`，精确定位到函数名和行号。
4. **输出修复报告 (Write Remediation Report)**：按严重度和权重排序，为每个问题生成包含文件、函数、行号引用的具体修复方案。
5. **AI 代码审查 (AI Code Review)**：集成 OpenAI / Anthropic / DeepSeek / Gemini / Ollama 五大 AI 供应商，对最差文件进行智能审查。

## 指标体系概览

| 维度 | 指标 | 权重 |
|------|------|------|
| 复杂度 | 圈复杂度、认知复杂度、嵌套深度 | 32% |
| 重复度 | 代码重复率 | 20% |
| 体积 | 函数长度、文件长度、参数数量 | 18% |
| 结构 | 结构分析 | 12% |
| 错误处理 | 错误处理覆盖率 | 8% |
| 文档 | 注释比率 | 5% |
| 命名 | 命名规范合规率 | 5% |

## 安装与支持

Fuck-U-Code Analysis 支持以下 AI 编辑器和平台：
- [Claude Code](../../claudecode/fuck-u-code-analysis/INSTALL-zh.md)
- [Cursor](../../cursor/fuck-u-code-analysis/INSTALL-zh.md)
- [Codex](../../codex/fuck-u-code-analysis/INSTALL-zh.md)
- [OpenCode](../../opencode/fuck-u-code-analysis/INSTALL-zh.md)
- [OpenClaw](../../openclaw/fuck-u-code-analysis/INSTALL-zh.md)
- [Zerone](../../zerone/fuck-u-code-analysis/INSTALL-zh.md)
- [Qoder](../../qoder/fuck-u-code-analysis/INSTALL-zh.md)

---
了解更多信息，请访问：[GitHub - Zerone-Agent/fuck-u-code](https://github.com/Zerone-Agent/fuck-u-code)
