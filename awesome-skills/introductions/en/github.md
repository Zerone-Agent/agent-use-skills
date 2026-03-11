# GitHub

The **GitHub** skill enables AI agents to interact directly with GitHub using the official `gh` CLI. It covers everything from project management (Issues/PRs) to automation or maintenance (Actions/Runs), making development workflows more intelligent.

## Core Philosophy

- **Official Integration**: Built on the official GitHub CLI to ensure stability and security.
- **Deep Visibility**: Monitor CI/CD status via `gh run` and extract detailed logs for failed steps.
- **Structured Queries**: Supports JSON output and `jq` filtering, allowing Agents to quickly extract core data like PR status or issue numbers.
- **Limitless Access**: Built-in `gh api` support to call any GitHub REST API, covering all advanced scenarios.

## Key Features & Workflow

1. **Pull Request Management**: Check PR status, CI checks, and details.
2. **Action Automation**: List workflow runs, view run details, and retrieve failure logs (`log-failed`).
3. **Issue Tracking**: List and filter project tasks with structured output.
4. **Repository Interaction**: Supports cross-project operations using the `--repo` flag even outside of git directories.

## Skills Library Overview

- **Core Tool**: Encapsulates the `gh` command-line tool.
- **CI/CD Integration**: Emphasizes monitoring capabilities for GitHub Actions.
- **API Extensibility**: Provides infinite expansion possibilities via `gh api`.

## Installation & Support

The GitHub skill currently supports the following platform:

- [OpenClaw](../../openclaw/github/INSTALL-en.md)

---
For more information, visit: [GitHub CLI Official Manual](https://cli.github.com/manual/)
