# Installing Skill Market for Qoder

## Prerequisites

- Qoder installed
- Git installed
- Ensure you have Python installed (`uv` is recommended but optional)

## Installation Steps

### 1. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.qoder/agent-use-skills
```

### 2. Symlink Skills

Create a symlink so Qoder discovers the skill-market skill:

```bash
mkdir -p ~/.qoder/skills
rm -rf ~/.qoder/skills/skill-market
ln -s ~/.qoder/agent-use-skills/awesome-skills/skills/skill-market ~/.qoder/skills/skill-market
```

### 3. Verify Installation

Run the following command or restart Qoder and ask to verify:

```bash
~/.qoder/agent-use-skills/awesome-skills/skills/skill-market/scripts/market.py list
```

Or ask in Qoder:
- "List all available skills on the skill market"
- "do you have skill-market?"

If successful, Qoder will automatically recognize and invoke the Skill Market workflow.

## Updating

```bash
cd ~/.qoder/agent-use-skills
git pull
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues
