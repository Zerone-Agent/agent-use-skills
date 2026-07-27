# Installing Matt Pocock Skills for Cursor

## Prerequisites

- [Cursor](https://cursor.com) installed
- Git installed

## Installation Steps

### 1. Clone the mattpocock-skills repository

```bash
git clone https://github.com/mattpocock/skills.git ~/.cursor/mattpocock-skills
```

### 2. Symlink the skills

Link all skills under `engineering/` and `productivity/` into Cursor's skills directory:

```bash
mkdir -p ~/.cursor/skills
for category in engineering productivity; do
  for skill in ~/.cursor/mattpocock-skills/skills/$category/*/; do
    skill_name=$(basename "$skill")
    rm -rf ~/.cursor/skills/$skill_name
    ln -s "$skill" ~/.cursor/skills/$skill_name
  done
done
```

### 3. Run the one-time setup per repo

Open your project in Cursor Agent mode and run:

```
/setup-matt-pocock-skills
```

It asks about issue tracker, triage labels, and docs location.

### 4. Verify Installation

Type:

```
/ask-matt
```

You should see all user-invoked skills.

## Updating

```bash
cd ~/.cursor/mattpocock-skills
git pull
```

## Uninstallation

```bash
for category in engineering productivity; do
  for skill in ~/.cursor/mattpocock-skills/skills/$category/*/; do
    rm -rf ~/.cursor/skills/$(basename "$skill")
  done
done
```

## Getting Help

- Report issues: https://github.com/mattpocock/skills/issues
