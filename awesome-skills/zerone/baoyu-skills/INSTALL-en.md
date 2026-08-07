# Installing Baoyu Skills for Zerone

## Prerequisites

- Zerone installed
- Git installed

## Installation Steps

### 1. Clone Baoyu Skills

```bash
git clone https://github.com/JimLiu/baoyu-skills.git ~/.agents/baoyu-skills
```

### 2. Symlink Skills

Create symlinks so Zerone discovers the Baoyu skills:

```bash
mkdir -p ~/.agents/skills
for skill in $(ls ~/.agents/baoyu-skills/skills); do
  rm -rf ~/.agents/skills/$skill
  ln -s ~/.agents/baoyu-skills/skills/$skill ~/.agents/skills/$skill
done
```

### 3. Verify Installation

Restart Zerone, then try asking:

- "do you have baoyu-imagine?"

If successful, Zerone will automatically recognize and invoke the relevant Baoyu skill.

## Updating

```bash
cd ~/.agents/baoyu-skills
git pull
```

## Uninstallation

```bash
for skill in $(ls ~/.agents/baoyu-skills/skills); do
  rm -rf ~/.agents/skills/$skill
done
```

## Getting Help

- GitHub: https://github.com/JimLiu/baoyu-skills
- Report issues: https://github.com/JimLiu/baoyu-skills/issues