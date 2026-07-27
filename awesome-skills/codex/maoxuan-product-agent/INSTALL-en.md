# Install Maoxuan Product Agent for Codex

## Prerequisites

- [Codex](https://github.com/openai/codex) installed
- Node.js and npm installed

## Installation Steps

### 1. Install the skill

```bash
npx skills add atdy/maoxuan-product-agent \
  --skill product-decision-agent \
  --agent codex \
  -g -y
```

### 2. Verify Installation

Restart Codex, then try:

```text
Use $product-decision-agent to decide whether to ship an A/B Test whose CTR rose 12% but orders did not.
```

If successful, Codex will diagnose the current bottleneck and return concrete next actions in Simplified Chinese.

## Updating

Re-run the installation command to fetch the latest version.

## Uninstallation

```bash
rm -rf ~/.agents/skills/product-decision-agent
```

## Getting Help

- GitHub: https://github.com/atdy/maoxuan-product-agent
- Report issues: https://github.com/atdy/maoxuan-product-agent/issues
