# Installing Humanizer-zh for Zerone

## Prerequisites

- Zerone installed
- Git installed

## Installation Steps

### 1. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.agents/agent-use-skills
```

### 2. Symlink Skills

Create a symlink so Zerone discovers the skill:

```bash
mkdir -p ~/.agents/skills
rm -rf ~/.agents/skills/humanizer-zh
ln -s ~/.agents/agent-use-skills/awesome-skills/skills/humanizer-zh ~/.agents/skills/humanizer-zh
```

### 3. Verify Installation

Restart Zerone and try asking:
- "Help me remove AI writing traces from this text"
- "do you have humanizer-zh?"

If successful, Zerone will automatically recognize and invoke the Humanizer-zh skill workflow.

## Updating

```bash
cd ~/.agents/agent-use-skills
git pull
```

## Uninstallation

Remove the symlink to uninstall:

```bash
rm -rf ~/.agents/skills/humanizer-zh
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues