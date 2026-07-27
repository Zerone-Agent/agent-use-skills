# Installing Impeccable for Qoder

## Prerequisites

- [Qoder](https://qoder.com) installed
- [Node.js](https://nodejs.org) installed (v18+ recommended, for `npx`)
- Write access to your project root

## Installation Steps

### 1. Run the official installer from your project root

```bash
cd /path/to/your/project
npx impeccable install
```

To target Qoder explicitly:

```bash
npx impeccable install --providers=qoder --scope=project
```

Qoder's skills directory is `.qoder/skills/` (project) or `~/.qoder/skills/` (global).

### 2. Initialize design context

Open the project in Qoder and run:

```
/impeccable init
```

It asks whether the surface is brand or product, then writes `PRODUCT.md` and (optionally) `DESIGN.md`.

### 3. Verify Installation

Type:

```
/impeccable
```

You should see all 23 sub-commands. You can also try:

```
/impeccable critique landing
```

## Updating

```bash
npx impeccable update
```

## Uninstallation

```bash
rm -rf .qoder/skills/impeccable
rm -rf .impeccable
# If you chose global install earlier:
rm -rf ~/.qoder/skills/impeccable
```

## Getting Help

- Docs: https://impeccable.style
- Report issues: https://github.com/pbakaus/impeccable/issues
