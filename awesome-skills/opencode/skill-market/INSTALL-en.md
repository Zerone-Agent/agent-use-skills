# Installing Skill Market for OpenCode

## Prerequisites

- OpenCode installed
- Git installed
- Ensure you have Python installed (`uv` is recommended but optional)

## Installation Steps

### 1. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.config/opencode/agent-use-skills
```

### 2. Symlink Skills

Create a symlink so OpenCode discovers the skill-market skill:

```bash
mkdir -p ~/.config/opencode/skills
rm -rf ~/.config/opencode/skills/skill-market
ln -s ~/.config/opencode/agent-use-skills/awesome-skills/skills/skill-market ~/.config/opencode/skills/skill-market
```

### 3. Verify Installation

Run the following command or restart OpenCode and ask to verify:

```bash
~/.config/opencode/agent-use-skills/awesome-skills/skills/skill-market/scripts/market.py list
```

Or ask in OpenCode:
- "List all available skills on the skill market"
- "do you have skill-market?"

If successful, OpenCode will automatically recognize and invoke the Skill Market workflow.

## Updating

```bash
cd ~/.config/opencode/agent-use-skills
git pull
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues
