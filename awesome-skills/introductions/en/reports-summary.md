# Reports Summary

**Reports Summary** is a professional weekly report summary assistant skill that extracts key information from scattered employee reports, generates well-structured summary reports, and supports conversion to Word documents.

## Tags

🗂️ Documents & Office | ✅ Verified

## Core Philosophy

- **Objective & Professional**: Maintain an objective, professional tone, avoiding colloquial expressions
- **Concise & Accurate**: Each summary is succinct, focusing on results rather than processes
- **Data-Driven**: Prioritize retaining concrete data support (e.g., "improved by 50%", "fixed 3 bugs")
- **Clear Structure**: Strictly follow heading hierarchy to ensure document clarity
- **Privacy Protection**: Remove specific employee names in the final summary
- **Smart Merging**: Automatically merge similar content when multiple people work on the same project

## Key Features & Workflow

### Scenario 1: Generate Summary from Report Files

1. **Report Reading**: Support reading single or batch .docx report files
2. **Content Analysis**: Extract highlights, write work summary, categorize, deduplicate and merge
3. **Markdown Generation**: Generate structured reports in standard format
4. **User Confirmation**: Display preview and ask if adjustments are needed
5. **Word Conversion**: Optional conversion to formal Word documents

### Scenario 2: Markdown to Word Conversion

1. **Confirm Requirements**: Confirm source Markdown file path
2. **Execute Conversion**: Generate well-formatted Word documents using templates
3. **Deliver Results**: Inform user of document save path

## Tool Scripts

| Script | Function |
|--------|----------|
| `read_reports.py` | Batch read .docx report files, return content in JSON format |
| `md_to_docx.py` | Convert Markdown reports to Word documents |
| `template.docx` | Word document format template |

## Dependencies

- `python-docx` - Read and generate Word documents
- `markdown` - Parse Markdown format
- `beautifulsoup4` - HTML processing

## Trigger Scenarios

- User mentions "weekly report", "summary", "consolidation", "report organization"
- Need to process .docx report files
- Generate team work summaries
- Convert Markdown to Word documents

## Installation & Support

Reports Summary supports the following AI editors and platforms:
- [Claude Code](../../claudecode/reports-summary/INSTALL-en.md)
- [Codex](../../codex/reports-summary/INSTALL-en.md)
- [Cursor](../../cursor/reports-summary/INSTALL-en.md)
- [OpenCode](../../opencode/reports-summary/INSTALL-en.md)
- [OpenClaw](../../openclaw/reports-summary/INSTALL-en.md)
- [Zerone](../../zerone/reports-summary/INSTALL-en.md)
- [Qoder](../../qoder/reports-summary/INSTALL-en.md)

---
For more information, visit: [GitHub - Zerone-Agent/agent-use-skills](https://github.com/Zerone-Agent/agent-use-skills)