# Deep Research

**Deep Research** is an autonomous multi-step research skill powered by Google's Gemini Deep Research Agent. Unlike standard LLM queries that respond in seconds, Deep Research is an "analyst-in-a-box" that plans, searches, reads, and synthesizes information into comprehensive, cited reports.

## Core Philosophy
- **Autonomous Research**: The agent automatically plans research strategies and completes multiple rounds of searching and analysis without human intervention.
- **Deep Synthesis**: Goes beyond simple information retrieval to perform in-depth analysis and synthesis across multiple sources.
- **Cited Output**: All research results include source citations, ensuring traceability and verifiability.
- **Flexible Interaction**: Supports multiple interaction modes including real-time streaming, async polling, history queries, and follow-up questions.

## Key Features & Workflow

1. **Research Task Launch**: Start a deep research task with a natural language query — the agent autonomously plans the search strategy.
2. **Real-Time Streaming**: Stream research progress in real-time, showing thinking steps and building the report as it's generated.
3. **Async Research**: Start a research task without waiting for completion, then retrieve results later via status polling.
4. **Continue Conversations**: Ask follow-up questions based on previous research results for deeper exploration.
5. **Structured Output Formats**: Specify custom output formats like "Executive Summary → Comparison Table → Recommendations."
6. **History Management**: Automatically caches research history, supporting browsing and reviewing past research tasks.
7. **Multiple Output Modes**: Supports human-readable Markdown reports, structured JSON data, and raw API responses.

## Use Cases

- Market analysis and competitive landscaping
- Technical literature reviews and surveys
- Due diligence research
- Historical research and timeline construction
- Comparative analysis of frameworks, products, and technologies

## Cost & Performance

| Metric | Value |
|--------|-------|
| Time | 2-10 minutes per task |
| Cost | $2-5 per task (varies by complexity) |
| Token Usage | ~250k-900k input, ~60k-80k output |

## Installation & Support

Deep Research supports the following AI editors and platforms:
- [Claude Code](../../claudecode/deep-research/INSTALL-en.md)
- [Cursor](../../cursor/deep-research/INSTALL-en.md)
- [Codex](../../codex/deep-research/INSTALL-en.md)
- [OpenCode](../../opencode/deep-research/INSTALL-en.md)
- [OpenClaw](../../openclaw/deep-research/INSTALL-en.md)
- [Qoder](../../qoder/deep-research/INSTALL-en.md)

---
For more information, visit: [GitHub - Zerone-Agent/agent-use-skills](https://github.com/Zerone-Agent/agent-use-skills)
