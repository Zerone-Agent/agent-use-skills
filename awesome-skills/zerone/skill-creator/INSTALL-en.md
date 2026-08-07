# Installing Skill Creator for Zerone

## Prerequisites

- Zerone installed
- Git installed
- Python installed

## Installation Steps

### 1. Clone agent-use-skills Repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.agents/agent-use-skills
```

### 2. Symlink Skills

Create a symlink so Zerone discovers the skill:

```bash
mkdir -p ~/.agents/skills
rm -rf ~/.agents/skills/skill-creator
ln -s ~/.agents/agent-use-skills/awesome-skills/skills/skill-creator ~/.agents/skills/skill-creator
```

### 3. Verify Installation

Restart Zerone and try asking:
- "Help me create a new skill"
- "do you have skill-creator?"

If successful, Zerone will automatically recognize and invoke the Skill Creator skill workflow.

## Updating

```bash
cd ~/.agents/agent-use-skills
git pull
```

## Uninstallation

Remove the symlink to uninstall:

```bash
rm -rf ~/.agents/skills/skill-creator
```

## Getting Help

- GitHub: https://github.com/Zerone-Agent/agent-use-skills