# Installing Skill Market for Claude Code

## Prerequisites

- Claude Code installed
- Git installed
- Ensure you have Python installed (`uv` is recommended but optional)

## Installation Steps

### 1. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.claude/agent-use-skills
```

### 2. Symlink Skills

Create a symlink so Claude Code discovers the skill-market skill:

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/skill-market
ln -s ~/.claude/agent-use-skills/awesome-skills/skills/skill-market ~/.claude/skills/skill-market
```

### 3. Verify Installation

Run the following command or restart Claude Code and ask to verify:

```bash
~/.claude/agent-use-skills/awesome-skills/skills/skill-market/scripts/market.py list
```

Or ask in Claude Code:
- "List all available skills on the skill market"
- "do you have skill-market?"

If successful, Claude Code will automatically recognize and invoke the Skill Market workflow.

## Updating

```bash
cd ~/.claude/agent-use-skills
git pull
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues
