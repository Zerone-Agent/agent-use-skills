# Installing gstack for OpenCode

## Prerequisites

- [OpenCode](https://opencode.ai) installed
- [Git](https://git-scm.com/) installed
- [Bun](https://bun.sh/) v1.0+ installed

## Installation Steps

### 1. Clone and run setup with the opencode host

```bash
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/gstack
cd ~/gstack && ./setup --host opencode
```

setup distributes the gstack skills to `~/.config/opencode/skills/gstack-*/`, compiles TypeScript with Bun, installs the custom Chromium, and registers the MCP server.

### 2. Verify Installation

In OpenCode, type:

```
/office-hours
```

It should trigger the 6 YC-style product forcing questions. You can also run:

```
/hosts
```

to confirm the host is opencode and skills are loaded.

## Updating

```bash
cd ~/gstack && git pull && ./setup --host opencode
```

## Uninstallation

```bash
~/gstack/bin/gstack-uninstall
```

Or manually:

```bash
rm -rf ~/gstack ~/.gstack ~/.config/opencode/skills/gstack-*
```

## Getting Help

- Docs: https://github.com/garrytan/gstack/tree/main/docs
- Report issues: https://github.com/garrytan/gstack/issues
