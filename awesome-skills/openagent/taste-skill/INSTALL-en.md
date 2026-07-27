# Installing Taste Skill for OpenAgent

## Prerequisites

- OpenAgent installed
- Git installed

## Installation Steps

### 1. Clone the taste-skill repository

```bash
git clone https://github.com/Leonxlnx/taste-skill.git ~/.openagent/taste-skill
```

### 2. Symlink the skills

Link all 13 sub-skill folders into OpenAgent's skills directory:

```bash
mkdir -p ~/.openagent/skills
for skill in ~/.openagent/taste-skill/skills/*/; do
  skill_name=$(basename "$skill")
  rm -rf ~/.openagent/skills/$skill_name
  ln -s "$skill" ~/.openagent/skills/$skill_name
done
```

### 3. Verify Installation

Restart OpenAgent, then try asking:

- "do you have taste-skill?"
- "use taste-skill to design a soft, premium brand site"

If successful, OpenAgent will automatically pick the right taste-skill sub-skill based on your brief.

## Updating

```bash
cd ~/.openagent/taste-skill
git pull
```

## Uninstallation

```bash
for skill in ~/.openagent/taste-skill/skills/*/; do
  rm -rf ~/.openagent/skills/$(basename "$skill")
done
```

## Getting Help

- Report issues: https://github.com/Leonxlnx/taste-skill/issues
