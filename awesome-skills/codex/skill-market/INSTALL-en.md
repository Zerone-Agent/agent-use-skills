# Installing Skill Market for Codex

## Prerequisites

- Codex installed
- Git installed
- Ensure you have Python installed (`uv` is recommended but optional)

## Installation Steps

### 1. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.codex/agent-use-skills
```

### 2. Symlink Skills

Create a symlink so Codex discovers the skill-market skill:

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/skill-market
ln -s ~/.codex/agent-use-skills/awesome-skills/skills/skill-market ~/.codex/skills/skill-market
```

### 3. Verify Installation

Run the following command or restart Codex and ask to verify:

```bash
~/.codex/agent-use-skills/awesome-skills/skills/skill-market/scripts/market.py list
```

Or ask in Codex:
- "List all available skills on the skill market"
- "do you have skill-market?"

If successful, Codex will automatically recognize and invoke the Skill Market workflow.

## Updating

```bash
cd ~/.codex/agent-use-skills
git pull
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues
