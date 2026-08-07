# Installing Guizang PPT Skill for Zerone

## Prerequisites

- Zerone installed
- Git installed

## Installation Steps

### 1. Clone repository

```bash
git clone https://github.com/op7418/guizang-ppt-skill.git ~/.agents/guizang-ppt-skill
```

### 2. Symlink Skill

Create a symlink so Zerone discovers the skill:

```bash
mkdir -p ~/.agents/skills
rm -rf ~/.agents/skills/guizang-ppt-skill
ln -s ~/.agents/guizang-ppt-skill ~/.agents/skills/guizang-ppt-skill
```

### 3. Verify Installation

Restart Zerone, then try asking:
- "Make me a magazine-style deck"
- "Make me a Swiss-style deck"

If successful, Zerone will automatically recognize and invoke the skill.

## Updating

```bash
cd ~/.agents/guizang-ppt-skill
git pull
```

## Uninstallation

```bash
rm -rf ~/.agents/skills/guizang-ppt-skill
```

## Getting Help

- GitHub: https://github.com/op7418/guizang-ppt-skill
- Report issues: https://github.com/op7418/guizang-ppt-skill/issues
