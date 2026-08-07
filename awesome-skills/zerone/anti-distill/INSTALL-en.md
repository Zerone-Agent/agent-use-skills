# Installing Anti-Distill for Zerone

## Prerequisites

- Zerone installed
- Git installed

## Installation Steps

### 1. Clone anti-distill

```bash
git clone https://github.com/leilei926524-tech/anti-distill.git ~/.agents/anti-distill
```

### 2. Symlink Skills

Create a symlink so Zerone discovers the skill:

```bash
mkdir -p ~/.agents/skills
rm -rf ~/.agents/skills/anti-distill
ln -s ~/.agents/anti-distill/skills/anti-distill ~/.agents/skills/anti-distill
```

### 3. Verify Installation

Restart Zerone and try asking:
- "Help me clean this Skill file"
- "do you have anti-distill?"

If successful, Zerone will automatically recognize and invoke the Anti-Distill skill workflow.

## Updating

```bash
cd ~/.agents/anti-distill
git pull
```

## Uninstallation

Remove the symlink to uninstall:

```bash
rm -rf ~/.agents/skills/anti-distill
```

## Getting Help

- GitHub: https://github.com/leilei926524-tech/anti-distill