# Installing Skill Market for Zerone

## Prerequisites

- Zerone installed
- Git installed
- Python installed (recommended: `uv`, but not required)

## Installation Steps

### 1. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.agents/agent-use-skills
```

### 2. Symlink Skills

Create a symlink so Zerone discovers the skill:

```bash
mkdir -p ~/.agents/skills
rm -rf ~/.agents/skills/skill-market
ln -s ~/.agents/agent-use-skills/awesome-skills/skills/skill-market ~/.agents/skills/skill-market
```

### 3. Verify Installation

Run the following command or restart Zerone and try asking:

```bash
~/.agents/agent-use-skills/awesome-skills/skills/skill-market/scripts/market.py list
```

Or in Zerone, try asking:
- "List all available skills in the skill market"
- "do you have skill-market?"

If successful, Zerone will automatically recognize and invoke the Skill Market skill workflow.

## Updating

```bash
cd ~/.agents/agent-use-skills
git pull
```

## Uninstallation

Remove the symlink to uninstall:

```bash
rm -rf ~/.agents/skills/skill-market
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues