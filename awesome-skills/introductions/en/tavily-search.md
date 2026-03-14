# Tavily Search

**Tavily Search** is a web search skill optimized for AI Agents using the Tavily API. It is designed to provide clean, relevant, and non-scraper-aware search results, perfectly suited for direct consumption by AI agents.

## Tags

🗂️ Document & Office | ✅ Verified

## Core Philosophy

- **AI-Optimized**: Unlike traditional search engines, Tavily is purpose-built for AI training and agents, returning results that better fit large language models' processing needs.
- **Deep Research Capability**: Supports a deep research (--deep) mode to gather more comprehensive information across multiple sources.
- **Content Extraction**: In addition to searching, it features built-in web content extraction for agents to read target pages directly.

## Key Features & Workflow

1. **Smart Search**: Supports general search and specialized news search (--topic news), with customizable result counts.
2. **Deep Research**: Activate advanced search mode via the `--deep` parameter for complex research questions.
3. **Web Extraction**: Extract clean text content directly from a URL.
4. **Lightweight Output**: Returns concise, relevant snippets to minimize the agent's context window burden.

## Skills Library Overview

- **Search Script**: `search.mjs` - Core search logic handling queries and parameters.
- **Extraction Script**: `extract.mjs` - Web text extraction tool.
- **Configuration**: Requires the `TAVILY_API_KEY` environment variable.

## Installation & Support

Tavily Search currently supports the following platform:

- [OpenClaw](../../openclaw/tavily-search/INSTALL-en.md)

---
For more information, visit: [Tavily Homepage](https://tavily.com)
