# Summarize

**Summarize** is a powerful all-in-one content summary skill that supports fast distillation of URLs, local files (such as PDFs), audio, video, and YouTube links.

## Tags

Document & Office | Pending Verification

## Core Philosophy

- **Full Format Support**: Handles not just text-based web pages, but also PDFs, multimedia files, and YouTube videos.
- **Multi-Model Driven**: Supports major language models (Gemini, Claude, GPT, xAI) as backend inference engines.
- **Developer First**: Offers a concise CLI and optional JSON output, making it easy for Agents to invoke and analyze structured summaries.

## Key Features & Workflow

1. **Multi-dimensional Summary**: Quickly get the core content of a URL or local file via the `summarize` CLI.
2. **Smart YouTube Extraction**: Supports automatic content conversion and summarization for YouTube links (can be enhanced with Apify).
3. **Capture Enhancement**: Integrates with Firecrawl to bypass certain website anti-scraping limits for more complete raw data.
4. **Customizable Control**: Supports setting summary lengths (from short to xxl) and output formats.

## Skills Library Overview

- **Core Commands**: Encapsulated `summarize` command usage.
- **Configuration**: Configurable via `~/.summarize/config.json` or environment variables (e.g., `GEMINI_API_KEY`).
- **External Integration**: Supports extraction mode (`--extract-only`) to retrieve raw, unsummarized web data.

## Installation & Support

Summarize currently supports the following platform:

- [OpenClaw](../../openclaw/summarize/INSTALL-en.md)

---
For more information, visit: [Summarize Official Docs](https://summarize.sh)
