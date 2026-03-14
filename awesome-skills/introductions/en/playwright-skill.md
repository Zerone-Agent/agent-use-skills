# Playwright Skill

**Playwright Skill** is a full-featured browser automation tool based on [Playwright](https://playwright.dev/). It is designed to help developers and AI Agents automate a wide variety of browser tasks, including web testing, form filling, screenshot capturing, responsive design checks, UX validation, and complex login flow automation.

## Tags

Dev & Testing | Pending Verification

## Core Philosophy

- **Automation & Intelligent Detection**: Capable of automatically detecting running local development servers, eliminating the need to manually input URLs.
- **Ephemeral & Clean**: All generated test scripts are stored in the `/tmp` directory and are automatically cleaned up by the system after execution, preventing any clutter in your project codebase.
- **Visible Debugging**: Operates in non-headless mode (`headless: false`) by default, allowing users to visually monitor the browser's automated actions in real-time.
- **Highly Extensible**: Not limited to pre-built scripts; it can dynamically write any complex Playwright automation code based on specific user requirements.

## Key Features & Workflow

1. **Dev Server Detection**: Automatically scans and identifies running ports before testing local projects.
2. **Dynamic Scripting**: Real-time generation of custom Playwright scripts based on user-described tasks (e.g., "test login flow" or "check mobile layout").
3. **Cross-Platform Execution**: Safely executes scripts within the designated skill directory using a unified executor.
4. **Multi-Dimensional Validation**:
    - **Screenshots & Comparisons**: Automatically saves full-page or specific element screenshots.
    - **Responsive Testing**: Validates page layouts across various resolutions (Desktop, Tablet, Mobile).
    - **Link Checking**: Automatically scans and verifies the validity of all links on a page.
5. **Real-Time Feedback**: Outputs execution logs in real-time and presents test results alongside artifacts like screenshots.

## Skills Library Overview

The skill consists of the following core components:
- **Core Executor (`run.js`)**: Responsible for loading the environment and safely executing test code.
- **Helper Library (`lib/helpers.js`)**: Provides utility functions for server detection, safe clicking, form filling, and more.
- **API Reference (`API_REFERENCE.md`)**: A detailed Playwright operation guide for advanced tasks.

## Installation & Support

Playwright Skill supports the following AI editors and platforms:
- [Claude Code](../../claudecode/playwright-skill/INSTALL-en.md)
- [Cursor](../../cursor/playwright-skill/INSTALL-en.md)
- [Codex](../../codex/playwright-skill/INSTALL-en.md)
- [OpenCode](../../opencode/playwright-skill/INSTALL-en.md)
- [OpenClaw](../../openclaw/playwright-skill/INSTALL-en.md)
- [Qoder](../../qoder/playwright-skill/INSTALL-en.md)

---
For more information, visit: [GitHub - Zerone-Agent/agent-use-skills](https://github.com/Zerone-Agent/agent-use-skills)
