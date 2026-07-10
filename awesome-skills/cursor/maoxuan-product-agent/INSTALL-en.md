# Install Maoxuan Product Agent for Cursor

## Prerequisites

- [Cursor](https://cursor.com) installed
- Node.js and npm installed

## Installation Steps

### 1. Install the skill

```bash
npx skills add atdy/maoxuan-product-agent \
  --skill product-decision-agent \
  --agent cursor \
  -g -y
```

### 2. Verify Installation

Restart Cursor, then try in Agent mode:

```text
/product-decision-agent Our community DAU fell 15% for two weeks. Should we launch a campaign?
```

If successful, Cursor will diagnose the current bottleneck and return concrete next actions in Simplified Chinese.

## Updating

Re-run the installation command to fetch the latest version.

## Uninstallation

```bash
rm -rf ~/.cursor/skills/product-decision-agent
```

## Getting Help

- GitHub: https://github.com/atdy/maoxuan-product-agent
- Report issues: https://github.com/atdy/maoxuan-product-agent/issues
