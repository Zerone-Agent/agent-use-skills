# Installing Impeccable for Cursor

## Prerequisites

- [Cursor](https://cursor.com) installed
- [Node.js](https://nodejs.org) installed (v18+ recommended, for `npx`)
- Cursor Agent Skills enabled: Settings → Rules → Agent Skills (Nightly channel)

## Installation Steps

### 1. Run the official installer from your project root

```bash
cd /path/to/your/project
npx impeccable install
```

The installer auto-detects Cursor's harness folders (project-local `.cursor/` or global `~/.cursor/`) and asks about scope and hook installation.

To target Cursor explicitly:

```bash
npx impeccable install --providers=cursor --scope=project
```

### 2. Enable Agent Skills (first-time only)

Open Cursor → Settings → Beta → switch to Nightly; then Settings → Rules → enable **Agent Skills**.

### 3. Initialize design context

In Cursor Agent mode, run:

```
/impeccable init
```

### 4. Verify Installation

Type `/impeccable`, you should see all 23 sub-commands. You can also try:

```
/impeccable audit
```

## Updating

```bash
npx impeccable update
```

## Uninstallation

```bash
rm -rf .cursor/skills/impeccable
rm -rf .impeccable
```

Then remove the impeccable-related hook entries from `.cursor/hooks.json`.

## Getting Help

- Docs: https://impeccable.style
- Report issues: https://github.com/pbakaus/impeccable/issues
