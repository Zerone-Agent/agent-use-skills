# Installing LJG Skills for Zerone

## Prerequisites

- Zerone installed
- Git installed

## Installation Steps

### 1. Clone LJG Skills

```bash
git clone https://github.com/lijigang/ljg-skills.git ~/.agents/ljg-skills
```

### 2. Symlink Skills

Create symlinks so Zerone discovers all the LJG skills:

```bash
mkdir -p ~/.agents/skills
for skill in $(ls ~/.agents/ljg-skills/skills); do
  rm -rf ~/.agents/skills/$skill
  ln -s ~/.agents/ljg-skills/skills/$skill ~/.agents/skills/$skill
done
```

### 3. Install ljg-card Dependencies (if using the card casting feature)

`ljg-card` requires Playwright for screenshot capture:

```bash
cd ~/.agents/skills/ljg-card && npm install && npx playwright install chromium
```

### 4. Verify Installation

Restart Zerone, then try asking:

- "do you have ljg-card?"
- "do you have ljg-learn?"

If successful, Zerone will automatically recognize and invoke the relevant skill.

## Updating

```bash
cd ~/.agents/ljg-skills
git pull
```

## Uninstallation

```bash
for skill in $(ls ~/.agents/ljg-skills/skills); do
  rm -rf ~/.agents/skills/$skill
done
rm -rf ~/.agents/ljg-skills
```

## Getting Help

- GitHub: https://github.com/lijigang/ljg-skills
- Report issues: https://github.com/lijigang/ljg-skills/issues
