# Installing Matt Pocock Skills for Claude Code

## Prerequisites

- [Claude Code](https://claude.ai/code) installed
- Git installed

## Installation Steps

### 1. Clone the mattpocock-skills repository

```bash
git clone https://github.com/mattpocock/skills.git ~/.claude/mattpocock-skills
```

### 2. Symlink the skills

Link all skills under `engineering/` and `productivity/` into Claude Code's skills directory:

```bash
mkdir -p ~/.claude/skills
for category in engineering productivity; do
  for skill in ~/.claude/mattpocock-skills/skills/$category/*/; do
    skill_name=$(basename "$skill")
    rm -rf ~/.claude/skills/$skill_name
    ln -s "$skill" ~/.claude/skills/$skill_name
  done
done
```

### 3. Run the one-time setup per repo

Open your project in Claude Code and run:

```
/setup-matt-pocock-skills
```

It asks about:
- **Issue tracker**: GitHub / Linear / local markdown
- **Triage labels**: which labels you apply to issues
- **Docs location**: where generated docs should live

### 4. Verify Installation

Type:

```
/ask-matt
```

You should see all user-invoked skills, with a recommendation for the current situation. You can also try:

```
/grill-me
```

## Updating

```bash
cd ~/.claude/mattpocock-skills
git pull
```

## Uninstallation

```bash
for category in engineering productivity; do
  for skill in ~/.claude/mattpocock-skills/skills/$category/*/; do
    rm -rf ~/.claude/skills/$(basename "$skill")
  done
done
```

## Getting Help

- Report issues: https://github.com/mattpocock/skills/issues
