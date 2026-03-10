# Install AgentUse Share in Qoder

## Prerequisites

- [Qoder](https://qoder.ai) installed
- Git installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.qoder/agent-use-skills
```

### 2. Create a symbolic link

Create a symbolic link so that Qoder can discover the agentuse-share skill:

```bash
mkdir -p ~/.qoder/skills
rm -rf ~/.qoder/skills/agentuse-share
ln -s ~/.qoder/agent-use-skills/awesome-skills/skills/agentuse-share ~/.qoder/skills/agentuse-share
```

### 3. Verify Installation

Restart Qoder and try asking:

- "Use agentuse-share skill to document a new skill"
- "do you have agentuse-share skill?"

If successful, Qoder will recognize and invoke the AgentUse Share skill workflow.

## Update

```bash
cd ~/.qoder/agent-use-skills
git pull
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
