# Installing gstack for Codex

## Prerequisites

- [Codex CLI](https://openai.com/codex) installed
- [Git](https://git-scm.com/) installed
- [Bun](https://bun.sh/) v1.0+ installed

## Installation Steps

### 1. Clone and run setup with the codex host

```bash
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/gstack
cd ~/gstack && ./setup --host codex
```

setup distributes the gstack skills to `~/.codex/skills/gstack-*/`, compiles TypeScript with Bun, installs the custom Chromium, and registers the MCP server.

### 2. Verify Installation

In a Codex session, type:

```
$office-hours
```

Or:

```
/hosts
```

to confirm the host is codex and skills are loaded.

## Updating

```bash
cd ~/gstack && git pull && ./setup --host codex
```

## Uninstallation

```bash
~/gstack/bin/gstack-uninstall
```

Or manually:

```bash
rm -rf ~/gstack ~/.gstack ~/.codex/skills/gstack-*
```

## Getting Help

- Docs: https://github.com/garrytan/gstack/tree/main/docs
- Report issues: https://github.com/garrytan/gstack/issues
