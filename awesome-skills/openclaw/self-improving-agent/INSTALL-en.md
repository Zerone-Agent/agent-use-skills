# Install Self-Improving Agent in OpenClaw

## Prerequisites

- [OpenClaw](https://github.com/nicepkg/openclaw) installed
- Git installed

## Installation Steps

### Method 1: Via ClawdHub (Recommended)

Run the following command in your terminal:

```bash
clawdhub install self-improving-agent
```

### Method 2: Manual Setup

1. **Clone agent-use-skills repository** (if not already cloned)

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

2. **Create symbolic link**

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/self-improving-agent
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/self-improving-agent ~/.openclaw/skills/self-improving-agent
```

3. **Create learning log files**

```bash
mkdir -p ~/.openclaw/workspace/.learnings
```

## Verify Installation

Restart OpenClaw and try asking:

- "Help me log a learning point"
- "do you have self-improvement skill?"

## Usage

### Enable Automatic Hooks (Optional)

If you want automatic reminders at session start or when commands fail, you can enable hooks:

```bash
# Copy hooks to OpenClaw hooks directory
cp -r ~/.openclaw/skills/self-improving-agent/hooks/openclaw ~/.openclaw/hooks/self-improvement

# Enable hooks
openclaw hooks enable self-improvement
```

## Update

```bash
cd ~/.openclaw/agent-use-skills && git pull
```

## Get Help

- File an issue: https://github.com/Zerone-Agent/agent-use-skills/issues
