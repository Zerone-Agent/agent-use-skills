# Installing Taste Skill for Zerone

## Prerequisites

- Zerone installed
- Git installed

## Installation Steps

### 1. Clone the taste-skill repository

```bash
git clone https://github.com/Leonxlnx/taste-skill.git ~/.agents/taste-skill
```

### 2. Symlink the skills

Link all 13 sub-skill folders into Zerone's skills directory:

```bash
mkdir -p ~/.agents/skills
for skill in ~/.agents/taste-skill/skills/*/; do
  skill_name=$(basename "$skill")
  rm -rf ~/.agents/skills/$skill_name
  ln -s "$skill" ~/.agents/skills/$skill_name
done
```

### 3. Verify Installation

Restart Zerone, then try asking:

- "do you have taste-skill?"
- "use taste-skill to design a soft, premium brand site"

If successful, Zerone will automatically pick the right taste-skill sub-skill based on your brief.

## Updating

```bash
cd ~/.agents/taste-skill
git pull
```

## Uninstallation

```bash
for skill in ~/.agents/taste-skill/skills/*/; do
  rm -rf ~/.agents/skills/$(basename "$skill")
done
```

## Getting Help

- Report issues: https://github.com/Leonxlnx/taste-skill/issues
