# Weekly Report

**Weekly Report** is a personal weekly report generation assistant skill that transforms scattered work records into well-structured, standardized weekly reports, with support for Word document conversion.

## Tags

🗂️ Documents & Office | ✅ Verified

## Core Principles

- **Professional & Objective**: Maintain an objective, professional tone, avoiding colloquial expressions
- **Concise & Accurate**: Each work item is succinct, focusing on results rather than processes
- **Data-Driven**: Prioritize retaining specific data support (e.g., "improved by 50%", "fixed 3 bugs")
- **Clear Structure**: Strictly follow the division between current week's work and next week's plan
- **Smart Polishing**: Transform colloquial descriptions into professional written language

## Key Features & Workflows

### Scenario 1: Generate Report from Work Content

1. **Information Collection**: Gather key information such as name, work content, and next week's plan
2. **Date Acquisition**: Automatically calculate current week's date range or extract from user input
3. **Content Polishing**: Transform colloquial descriptions into professional written language, extract key achievements
4. **Markdown Generation**: Generate structured report following standard format
5. **User Confirmation**: Display preview and ask if adjustments are needed
6. **Word Conversion**: Optional conversion to formal Word document

### Scenario 2: Markdown to Word

1. **Confirm Requirements**: Confirm source Markdown file path
2. **Execute Conversion**: Generate well-formatted Word document using template
3. **Deliver Results**: Inform user of document save location

## Tool Scripts

| Script | Function |
|--------|----------|
| `weekly_range.py` | Automatically calculate current week's date range |
| `md_to_docx.py` | Convert Markdown report to Word document |
| `template.docx` | Word document format template |

## Dependencies

- `python-docx` - Read and generate Word documents
- `markdown` - Parse Markdown format
- `beautifulsoup4` - HTML processing

## Trigger Scenarios

- User mentions "weekly report", "this week's work", "organize work content"
- Need to generate personal work weekly report
- Convert Markdown to Word document

## Installation & Support

Weekly Report supports the following AI editors and platforms:
- [Claude Code](../../claudecode/weekly-report/INSTALL-en.md)
- [Codex](../../codex/weekly-report/INSTALL-en.md)
- [Cursor](../../cursor/weekly-report/INSTALL-en.md)
- [OpenCode](../../opencode/weekly-report/INSTALL-en.md)
- [OpenClaw](../../openclaw/weekly-report/INSTALL-en.md)
- [Zerone](../../zerone/weekly-report/INSTALL-en.md)
- [Qoder](../../qoder/weekly-report/INSTALL-en.md)

---
For more information, visit: [GitHub - Zerone-Agent/agent-use-skills](https://github.com/Zerone-Agent/agent-use-skills)