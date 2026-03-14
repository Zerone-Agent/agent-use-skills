# Install Humanizer-zh in OpenClaw

## Prerequisites

- [OpenClaw](https://github.com/nicepkg/openclaw) installed
- Git installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 2. Create a symbolic link

Create a symbolic link so that OpenClaw can discover the humanizer-zh skill:

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/humanizer-zh
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/humanizer-zh ~/.openclaw/skills/humanizer-zh
```

### 3. Verify Installation

Restart OpenClaw and try asking:

- "Use humanizer-zh skill to optimize this text"
- "do you have humanizer-zh skill?"

If successful, OpenClaw will automatically recognize and invoke the Humanizer-zh skill workflow.

## Update

```bash
cd ~/.openclaw/agent-use-skills
git pull
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
