# Installing gstack for Claude Code

## Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed
- [Git](https://git-scm.com/) installed
- [Bun](https://bun.sh/) v1.0+ installed

## Installation Steps

### 1. One-shot install (recommended)

Paste this into Claude Code (Claude will execute the rest):

> Install gstack: run **`git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup`** then add a "gstack" section to CLAUDE.md that says to use the /browse skill from gstack for all web browsing, never use mcp\_\_claude-in-chrome\_\_\* tools, and lists the available skills. Then ask the user if they also want to add gstack to the current project so teammates get it.

Or run it directly in your shell:

```bash
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack
cd ~/.claude/skills/gstack && ./setup
```

`./setup` automatically:
- Compiles TypeScript sources with Bun
- Installs the custom Chromium + Playwright dependencies
- Creates the global state directory `~/.gstack/`
- Registers the MCP server (e.g. `gbrain`)

### 2. Team mode (recommended for shared repos)

From your repo root:

```bash
(cd ~/.claude/skills/gstack && ./setup --team) && \
  ~/.claude/skills/gstack/bin/gstack-team-init required && \
  git add .claude/ CLAUDE.md && \
  git commit -m "require gstack for AI-assisted work"
```

Teammates get gstack automatically after pulling, with a silent hourly auto-update check. Swap `required` for `optional` if you'd rather nudge than block.

### 3. Verify Installation

In Claude Code, type:

```
/office-hours
```

Or the lighter check:

```
/hosts
```

You should see the current host info and loaded skills.

## Updating

```bash
cd ~/.claude/skills/gstack && ./gstack-upgrade
```

Or:

```bash
cd ~/.claude/skills/gstack && git pull && ./setup
```

In team mode, an auto-update check runs hourly (throttled, network-failure-safe, completely silent).

## Uninstallation

```bash
~/.claude/skills/gstack/bin/gstack-uninstall
```

Or manually:

```bash
rm -rf ~/.claude/skills/gstack ~/.gstack
```

## Getting Help

- Docs: https://github.com/garrytan/gstack/tree/main/docs
- Report issues: https://github.com/garrytan/gstack/issues
