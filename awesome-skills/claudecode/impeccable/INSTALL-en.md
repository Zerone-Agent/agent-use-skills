# Installing Impeccable for Claude Code

## Prerequisites

- [Claude Code](https://claude.ai/code) installed
- [Node.js](https://nodejs.org) installed (v18+ recommended, for `npx`)
- Write access to your project root

## Installation Steps

### 1. Run the official installer from your project root

```bash
cd /path/to/your/project
npx impeccable install
```

The installer auto-detects Claude Code's harness folders and asks:
- **Scope**: current project (`--scope=project`) or global (`--scope=global`)
- **Whether to install the design hook**: defaults to yes (writes `.claude/settings.local.json` to detect anti-patterns on UI edits in real time)

To skip the prompts and target Claude Code explicitly:

```bash
npx impeccable install --providers=claude --scope=project
```

### 2. Initialize design context

Open the project in Claude Code and run:

```
/impeccable init
```

It asks whether the surface is brand (marketing/landing/portfolio) or product (app/dashboard/tool), then writes `PRODUCT.md` and (optionally) `DESIGN.md`. All later commands read this context.

### 3. Verify Installation

Type:

```
/impeccable
```

If the install succeeded, it lists all 23 sub-commands. You can also try:

```
/impeccable audit
```

## Updating

```bash
npx impeccable update
```

## Uninstallation

Remove the files Impeccable wrote:

```bash
rm -rf .claude/skills/impeccable
rm -rf .impeccable
# If you chose global install earlier:
rm -rf ~/.claude/skills/impeccable
```

Then manually remove the impeccable-related hook entries from `.claude/settings.local.json`.

## Getting Help

- Docs: https://impeccable.style
- Report issues: https://github.com/pbakaus/impeccable/issues
