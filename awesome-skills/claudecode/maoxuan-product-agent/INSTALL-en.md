# Install Maoxuan Product Agent for Claude Code

## Prerequisites

- [Claude Code](https://claude.ai/code) installed
- Node.js and npm installed

## Installation Steps

### 1. Install the skill

```bash
npx skills add atdy/maoxuan-product-agent \
  --skill product-decision-agent \
  --agent claude-code \
  -g -y
```

### 2. Verify Installation

Restart Claude Code, then try:

```text
/product-decision-agent We have 20 requests competing for two engineers. What should the next version include?
```

If successful, Claude Code will diagnose the current bottleneck and return concrete next actions in Simplified Chinese.

## Updating

Re-run the installation command to fetch the latest version.

## Uninstallation

```bash
rm -rf ~/.claude/skills/product-decision-agent
```

## Getting Help

- GitHub: https://github.com/atdy/maoxuan-product-agent
- Report issues: https://github.com/atdy/maoxuan-product-agent/issues
