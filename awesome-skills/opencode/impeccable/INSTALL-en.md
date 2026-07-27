# Installing Impeccable for OpenCode

## Prerequisites

- [OpenCode](https://opencode.ai) installed
- [Node.js](https://nodejs.org) installed (v18+ recommended, for `npx`)
- Write access to your project root

## Installation Steps

### 1. Run the official installer from your project root

```bash
cd /path/to/your/project
npx impeccable install
```

To target OpenCode explicitly:

```bash
npx impeccable install --providers=opencode --scope=project
```

OpenCode's skills directory is `.opencode/skills/` (project) or `~/.config/opencode/skills/` (global).

### 2. Initialize design context

Open the project in OpenCode and run:

```
/impeccable init
```

It asks whether the surface is brand or product, then writes `PRODUCT.md` and (optionally) `DESIGN.md`. All later commands read this context.

### 3. Verify Installation

Type:

```
/impeccable
```

You should see all 23 sub-commands. You can also try:

```
/impeccable audit
```

## Updating

```bash
npx impeccable update
```

## Uninstallation

```bash
rm -rf .opencode/skills/impeccable
rm -rf .impeccable
# If you chose global install earlier:
rm -rf ~/.config/opencode/skills/impeccable
```

## Getting Help

- Docs: https://impeccable.style
- Report issues: https://github.com/pbakaus/impeccable/issues
