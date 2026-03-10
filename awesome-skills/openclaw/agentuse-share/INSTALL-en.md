# Install AgentUse Share in OpenClaw

## Prerequisites

- [OpenClaw](https://github.com/nicepkg/openclaw) installed
- Git installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 2. Create a symbolic link

Create a symbolic link so that OpenClaw can discover the agentuse-share skill:

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/agentuse-share
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/agentuse-share ~/.openclaw/skills/agentuse-share
```

### 3. Verify Installation

Restart OpenClaw and try asking:

- "Use agentuse-share skill to document a new skill"
- "do you have agentuse-share skill?"

If successful, OpenClaw will recognize and invoke the AgentUse Share skill workflow.

## Update

```bash
cd ~/.openclaw/agent-use-skills
git pull
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
