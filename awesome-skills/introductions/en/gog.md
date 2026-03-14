# Gog (Google Workspace CLI)

**Gog** is a powerful command-line interface (CLI) used to manage and interact with core Google Workspace services, including Gmail, Calendar, Drive, Contacts, Sheets, and Docs.

## Tags

🗂️ Document & Office | 🔍 Pending Verification

## Core Philosophy

- **Unified Management**: Manage the entire Google ecosystem through a single `gog` command.
- **Agent-Friendly**: Supports JSON output (`--json`), allowing AI Agents to easily extract and process email content, calendar events, or spreadsheet data.
- **Security First**: Based on the OAuth authentication flow, ensuring that the Agent only performs operations within the scope authorized by the user.

## Key Features & Workflow

1. **Gmail Operations**: Supports email search (consistent with web search syntax) and sending emails.
2. **Drive Management**: Supports searching and listing files, making it easy for Agents to find reference documents.
3. **Sheets Data Interaction**: Supports reading (`get`), updating (`update`), and appending (`append`) spreadsheet data—ideal for automated record-keeping or report generation.
4. **Calendar & Contacts**: Supports viewing schedules and managing contact information.
5. **Docs Export**: Supports exporting Google Docs to formats like plain text for easy reading by the Agent.

## Skills Library Overview

- **Core Commands**: Encapsulated `gog` CLI usage covering various sub-services.
- **Authentication**: OAuth credential configuration via `gog auth`.
- **Environment Support**: Supports the `GOG_ACCOUNT` variable to simplify command calls.

## Installation & Support

Gog currently supports the following platform:

- [OpenClaw](../../openclaw/gog/INSTALL-en.md)

---
For more information, visit: [Gog Official website](https://gogcli.sh)
