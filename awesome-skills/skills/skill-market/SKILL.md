---
name: skill-market
description: Use this skill to find, explore, and install new skills from the Zerone Skill Market (https://api.zerone.market/api). Trigger this when the user asks to "add a skill", "install a skill", "browse skills", or mentions a skill name that is not currently installed.
---

# Skill Market

This skill enables the automated discovery and installation of specialized agent skills from the Zerone Skill Market.

## Workflow

Follow these steps to find and install a skill:

### 1. Browse and Discover
Run the listing script to see available skills. This provides names, descriptions, and supported frameworks.

```bash
scripts/market.py list
```

### 2. Identify the Target Skill
Search the list for a skill that matches the user's request. Identify the exact `name` of the skill (e.g., `agent-browser`, `imagen`).

### 3. Check Compatibility
Get detailed information about the skill to see which frameworks it supports.

```bash
scripts/market.py info <skill-name>
```

**Framework Matching:**
- Check if the current agent framework (e.g., `Antigravity`, `Claude Code`, `OpenCode`) is in the `frameworks` list.
- **If the current framework is NOT supported:**
  1. STOP and inform the user that the skill does not explicitly support the current framework.
  2. List the available frameworks from the `info` command.
  3. Suggest the most similar/compatible framework (typically `OpenCode` for Antigravity-like environments).
  4. **Ask the user for permission** to proceed with the suggested framework or if they would like to pick another one.

### 4. Get Installation Instructions
Fetch the specific installation tutorial for the chosen skill and framework.

```bash
scripts/market.py install <skill-name> <framework>
```

### 5. Execute Installation

**SECURITY WARNING: DO NOT AUTO-RUN COMMANDS.**

The installation tutorial will contain a set of steps or commands. Before executing any instructions:
1. **Require explicit user confirmation** before any install action. Show the commands to the user and ask for permission.
2. **Verify Integrity**: If the marketplace response provides signed packages or checksums, verify them.
3. **Review Manually/Sandbox**: Review the install tutorial text manually before execution or run installs in a sandbox.
4. **Restrict Privileges**: Restrict the installation from performing privileged filesystem or network actions unless you trust the marketplace maintainer.

Only after explicit user approval, execute the instructions to install the skill into the `.agent/skills/` directory.

## Current Environment Context
- **Market Endpoint:** `https://api.zerone.market/api`
- **Default Language:** `en` (English is used for API requests as per instructions)
- **Local Skills path:** `.agent/skills/`

## Example Usage

**User:** "Can you help me install the imagen skill from the market?"

1. **Agent:** Runs `scripts/market.py list`
2. **Agent:** Finds `imagen` in the list.
3. **Agent:** Runs `scripts/market.py info imagen`
4. **Agent:** Note that `Claude Code` is supported.
5. **Agent:** Runs `scripts/market.py install imagen "Claude Code"`
6. **Agent:** Follows the returned tutorial steps (usually involves downloading a `.skill` file or cloning a repo into `.agent/skills/`).
