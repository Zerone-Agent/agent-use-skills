# Installing Skill Market for OpenClaw

## Prerequisites

- OpenClaw installed
- Git installed
- Ensure you have Python installed (`uv` is recommended but optional)

## Installation Steps

### 1. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 2. Symlink Skills

Create a symlink so OpenClaw discovers the skill-market skill:

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/skill-market
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/skill-market ~/.openclaw/skills/skill-market
```

### 3. Verify Installation

Run the following command or restart OpenClaw and ask to verify:

```bash
~/.openclaw/agent-use-skills/awesome-skills/skills/skill-market/scripts/market.py list
```

Or ask in OpenClaw:
- "List all available skills on the skill market"
- "do you have skill-market?"

If successful, OpenClaw will automatically recognize and invoke the Skill Market workflow.

## Updating

```bash
cd ~/.openclaw/agent-use-skills
git pull
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues
