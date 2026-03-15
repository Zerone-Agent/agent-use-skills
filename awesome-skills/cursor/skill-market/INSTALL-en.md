# Installing Skill Market for Cursor

## Prerequisites

- Cursor installed
- Git installed
- Ensure you have Python installed (`uv` is recommended but optional)

## Installation Steps

### 1. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.cursor/agent-use-skills
```

### 2. Symlink Skills

Create a symlink so Cursor discovers the skill-market skill:

```bash
mkdir -p ~/.cursor/skills
rm -rf ~/.cursor/skills/skill-market
ln -s ~/.cursor/agent-use-skills/awesome-skills/skills/skill-market ~/.cursor/skills/skill-market
```

### 3. Verify Installation

Run the following command or restart Cursor and ask to verify:

```bash
~/.cursor/agent-use-skills/awesome-skills/skills/skill-market/scripts/market.py list
```

Or ask in Cursor:
- "List all available skills on the skill market"
- "do you have skill-market?"

If successful, Cursor will automatically recognize and invoke the Skill Market workflow.

## Updating

```bash
cd ~/.cursor/agent-use-skills
git pull
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues
