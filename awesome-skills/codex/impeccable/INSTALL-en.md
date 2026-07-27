# Installing Impeccable for Codex

## Prerequisites

- [Codex CLI](https://openai.com/codex) installed
- [Node.js](https://nodejs.org) installed (v18+ recommended, for `npx`)
- Write access to your project root

## Installation Steps

### 1. Run the official installer from your project root

```bash
cd /path/to/your/project
npx impeccable install
```

To target Codex explicitly:

```bash
npx impeccable install --providers=codex --scope=project
```

This writes:
- `.agents/skills/impeccable/` (Codex auto-discovers this skills folder, including sub-agents)
- `.codex/hooks.json` (project-level hook config)

### 2. Trust the project hook (required by Codex)

Codex tracks trust by hook definition. Open `/hooks` and approve the impeccable hook when prompted.

To trust the entire project folder at once, use `/hooks-trust` or relaunch Codex with `--trust`.

### 3. Initialize design context

In a Codex session, run:

```
$impeccable init
```

(Note: Codex uses skills, not `/prompts:`. Type `$impeccable` or open `/skills` to see it.)

### 4. Verify Installation

Open `/skills` or type `$impeccable`, you should see all 23 sub-commands.

## Updating

```bash
npx impeccable update
# If .codex/hooks.json changed, open /hooks and approve again
```

## Uninstallation

```bash
rm -rf .agents/skills/impeccable
rm -rf .codex/hooks.json   # only if this file contains only impeccable config
rm -rf .impeccable
```

## Getting Help

- Docs: https://impeccable.style
- Report issues: https://github.com/pbakaus/impeccable/issues
