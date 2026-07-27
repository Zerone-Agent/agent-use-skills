# Installing gstack for Cursor

## Prerequisites

- [Cursor](https://cursor.com) installed
- [Git](https://git-scm.com/) installed
- [Bun](https://bun.sh/) v1.0+ installed

## Installation Steps

### 1. Clone and run setup with the cursor host

```bash
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/gstack
cd ~/gstack && ./setup --host cursor
```

setup distributes the gstack skills to `~/.cursor/skills/gstack-*/`, compiles TypeScript with Bun, installs the custom Chromium, and registers the MCP server.

### 2. Verify Installation

In Cursor Agent mode, type:

```
/office-hours
```

It should trigger the 6 YC-style product forcing questions. You can also run:

```
/hosts
```

to confirm the host is cursor and skills are loaded.

## Updating

```bash
cd ~/gstack && git pull && ./setup --host cursor
```

## Uninstallation

```bash
~/gstack/bin/gstack-uninstall
```

Or manually:

```bash
rm -rf ~/gstack ~/.gstack ~/.cursor/skills/gstack-*
```

## Getting Help

- Docs: https://github.com/garrytan/gstack/tree/main/docs
- Report issues: https://github.com/garrytan/gstack/issues
