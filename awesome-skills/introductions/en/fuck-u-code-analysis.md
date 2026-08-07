# Fuck-U-Code Analysis

**Fuck-U-Code Analysis** is a code quality analysis and review skill that runs `fuck-u-code analyze` to score code across 7 dimensions and 11 metrics (0-100 scale), then outputs actionable remediation recommendations prioritized by severity and weight.

## Tags

💻 Dev & Testing | ✅ Verified

## Core Philosophy
- **Quantitative-Driven Review**: Precise AST-based metrics that judge code quality with data, not intuition.
- **Weight-Priority Triage**: Complexity 32% > Duplication 20% > Size 18% > Structure 12% > Error Handling 8% > Documentation 5% > Naming 5%, cross-sorted by weight and severity to determine fix priority.
- **Actionable Remediation**: Every recommendation references a specific metric value, function name, and line number, capped at 30 words.
- **Language-Specific Thresholds**: 14 programming languages (Go, JS, TS, Python, Java, C, C++, Rust, C#, Lua, PHP, Ruby, Swift, Shell) each have independent evaluation thresholds respecting language idioms.

## Key Features & Workflow

1. **Run Analysis**: Execute `fuck-u-code analyze . -f json -o /tmp/fuc-report.json` to get a structured JSON report, with support for exclude patterns, concurrency control, and multiple output formats.
2. **Identify Critical Files**: Extract overall and per-file scores from the report, focusing on files scoring below 60 (the "shit mountain" zone).
3. **Drill into Metrics**: For each problem file, examine 11 metrics' `normalizedScore`, `severity`, and `locations[]` to pinpoint exact function names and line numbers.
4. **Write Remediation Report**: Sort by severity and weight, generating specific fix plans with file, function, and line references for each issue.
5. **AI Code Review**: Integrates 5 AI providers (OpenAI / Anthropic / DeepSeek / Gemini / Ollama) for intelligent review of the worst-scoring files.

## Metrics Overview

| Dimension | Metrics | Weight |
|-----------|---------|--------|
| Complexity | Cyclomatic, Cognitive, Nesting Depth | 32% |
| Duplication | Code Duplication | 20% |
| Size | Function Length, File Length, Parameter Count | 18% |
| Structure | Structure Analysis | 12% |
| Error Handling | Error Handling | 8% |
| Documentation | Comment Ratio | 5% |
| Naming | Naming Convention | 5% |

## Installation & Support

Fuck-U-Code Analysis supports the following AI editors and platforms:
- [Claude Code](../../claudecode/fuck-u-code-analysis/INSTALL-en.md)
- [Cursor](../../cursor/fuck-u-code-analysis/INSTALL-en.md)
- [Codex](../../codex/fuck-u-code-analysis/INSTALL-en.md)
- [OpenCode](../../opencode/fuck-u-code-analysis/INSTALL-en.md)
- [OpenClaw](../../openclaw/fuck-u-code-analysis/INSTALL-en.md)
- [Zerone](../../zerone/fuck-u-code-analysis/INSTALL-en.md)
- [Qoder](../../qoder/fuck-u-code-analysis/INSTALL-en.md)

---
For more information, visit: [GitHub - Zerone-Agent/fuck-u-code](https://github.com/Zerone-Agent/fuck-u-code)
