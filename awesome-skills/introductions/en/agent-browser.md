# Agent Browser

**Agent Browser** is a Rust-based high-performance headless browser automation CLI with Node.js fallback. It enables AI agents to navigate, click, type, and snapshot pages via structured commands.

## Tags

Document & Office | Pending Verification

## Core Philosophy

- **Agent-Friendly**: Provides a list of interactive elements with simplified references (e.g., `@e1`, `@e2`) via `snapshot -i`, significantly reducing the complexity for Agents to parse the DOM.
- **High Performance**: Built with Rust (supporting Playwright/Puppeteer protocols) to ensure lightning-fast startup and execution.
- **Structured Interaction**: All actions (clicking, filling, getting text) are performed through a consistent CLI interface, making it easy to integrate into automation workflows.

## Key Features & Workflow

1.  **Page Snapshot**: Use `snapshot -i` to get the current interactive elements and their references for subsequent commands.
2.  **Interaction**: Supports all standard browser actions like `click`, `fill`, `hover`, `scroll`, etc., using `@ref` directly from the snapshot.
3.  **State Management**: Supports `state save/load` to persist and restore session states (Cookies, localStorage), useful for bypassing login flows.
4.  **Media Capture**: Provides features for screenshots, PDF generation, and video recording for verification or demonstrations.

## Skills Library Overview

- **Core Commands**: The `agent-browser` CLI offers four categories of instructions: navigation, analysis, interaction, and information retrieval.
- **Session Isolation**: Supports the `--session` parameter to maintain multiple independent browser contexts simultaneously.
- **Advanced Debugging**: Supports `--headed` mode to show the browser window, along with console and error log inspection.

## Installation & Support

Agent Browser currently supports the following platform:

- [OpenClaw](../../openclaw/agent-browser/INSTALL-en.md)

---
For more information, visit: [Agent Browser GitHub](https://github.com/vercel-labs/agent-browser)
