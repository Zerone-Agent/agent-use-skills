# Installing Matt Pocock Skills for Qoder

## Prerequisites

- [Qoder](https://qoder.com) installed
- Git installed

## Installation Steps

### 1. Clone the mattpocock-skills repository

```bash
git clone https://github.com/mattpocock/skills.git ~/.qoder/mattpocock-skills
```

### 2. Symlink the skills

Link all skills under `engineering/` and `productivity/` into Qoder's skills directory:

```bash
mkdir -p ~/.qoder/skills
for category in engineering productivity; do
  for skill in ~/.qoder/mattpocock-skills/skills/$category/*/; do
    skill_name=$(basename "$skill")
    rm -rf ~/.qoder/skills/$skill_name
    ln -s "$skill" ~/.qoder/skills/$skill_name
  done
done
```

### 3. Run the one-time setup per repo

Open your project in Qoder and run:

```
/setup-matt-pocock-skills
```

It asks about issue tracker, triage labels, and docs location.

### 4. Verify Installation

Type `/ask-matt`, you should see all user-invoked skills.

## Updating

```bash
cd ~/.qoder/mattpocock-skills
git pull
```

## Uninstallation

```bash
for category in engineering productivity; do
  for skill in ~/.qoder/mattpocock-skills/skills/$category/*/; do
    rm -rf ~/.qoder/skills/$(basename "$skill")
  done
done
```

## Getting Help

- Report issues: https://github.com/mattpocock/skills/issues
