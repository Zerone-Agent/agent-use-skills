# Installing Taste Skill for Codex

## Prerequisites

- [Codex](https://openai.com/index/codex/) installed
- Git installed

## Installation Steps

### 1. Clone the taste-skill repository

```bash
git clone https://github.com/Leonxlnx/taste-skill.git ~/.codex/taste-skill
```

### 2. Symlink the skills

Link all 13 sub-skill folders into Codex's skills directory:

```bash
mkdir -p ~/.codex/skills
for skill in ~/.codex/taste-skill/skills/*/; do
  skill_name=$(basename "$skill")
  rm -rf ~/.codex/skills/$skill_name
  ln -s "$skill" ~/.codex/skills/$skill_name
done
```

### 3. Verify Installation

Restart Codex, then try asking:

- "do you have taste-skill?"
- "use taste-skill to design a brutalist portfolio"

If successful, Codex will automatically pick the right taste-skill sub-skill based on your brief (`gpt-taste` is a stricter variant specifically tuned for GPT/Codex).

## Updating

```bash
cd ~/.codex/taste-skill
git pull
```

## Uninstallation

```bash
for skill in ~/.codex/taste-skill/skills/*/; do
  rm -rf ~/.codex/skills/$(basename "$skill")
done
```

## Getting Help

- Report issues: https://github.com/Leonxlnx/taste-skill/issues
