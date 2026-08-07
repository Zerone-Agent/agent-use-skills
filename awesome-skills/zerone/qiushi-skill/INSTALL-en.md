# Installing Qiushi Skill for Zerone

## Prerequisites

- Zerone installed
- Git installed

## Installation Steps

### 1. Clone qiushi-skill

```bash
git clone https://github.com/HughYau/qiushi-skill.git ~/.agents/qiushi-skill
```

### 2. Symlink Skills

Create symlinks so Zerone discovers the skills:

```bash
mkdir -p ~/.agents/skills
for skill in arming-thought contradiction-analysis practice-cognition investigation-first mass-line criticism-self-criticism protracted-strategy concentrate-forces spark-prairie-fire overall-planning; do
  rm -rf ~/.agents/skills/$skill
  ln -s ~/.agents/qiushi-skill/skills/$skill ~/.agents/skills/$skill
done
```

### 3. Verify Installation

Restart Zerone and try asking:
- "Use seeking truth from facts to analyze this problem"
- "do you have qiushi-skill?"

If successful, Zerone will automatically recognize and invoke Qiushi Skill workflow.

## Updating

```bash
cd ~/.agents/qiushi-skill
git pull
```

## Uninstallation

Remove the symlinks to uninstall:

```bash
for skill in arming-thought contradiction-analysis practice-cognition investigation-first mass-line criticism-self-criticism protracted-strategy concentrate-forces spark-prairie-fire overall-planning; do
  rm -rf ~/.agents/skills/$skill
done
```

## Getting Help

- GitHub: https://github.com/HughYau/qiushi-skill