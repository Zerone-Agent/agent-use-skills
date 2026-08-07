# Installing Colleague Skill for Zerone

## Prerequisites

- Zerone installed
- Git installed

## Installation Steps

### 1. Clone colleague-skill

```bash
git clone https://github.com/titanwings/colleague-skill.git ~/.agents/colleague-skill
```

### 2. Symlink Skills

Create a symlink so Zerone discovers the skill:

```bash
mkdir -p ~/.agents/skills
rm -rf ~/.agents/skills/colleague-skill
ln -s ~/.agents/colleague-skill/skills/colleague-skill ~/.agents/skills/colleague-skill
```

### 3. Verify Installation

Restart Zerone and try asking:
- "Help me create a digital colleague"
- "do you have colleague-skill?"

If successful, Zerone will automatically recognize and invoke the Colleague Skill workflow.

## Updating

```bash
cd ~/.agents/colleague-skill
git pull
```

## Uninstallation

Remove the symlink to uninstall:

```bash
rm -rf ~/.agents/skills/colleague-skill
```

## Getting Help

- GitHub: https://github.com/titanwings/colleague-skill