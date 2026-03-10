# Install AgentUse Share in Codex

## Prerequisites

- [Codex](https://openai.com/index/codex/) installed
- Git installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.codex/agent-use-skills
```

### 2. Create a symbolic link

Create a symbolic link so that Codex can discover the agentuse-share skill:

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/agentuse-share
ln -s ~/.codex/agent-use-skills/awesome-skills/skills/agentuse-share ~/.codex/skills/agentuse-share
```

### 3. Verify Installation

Restart Codex and try asking:

- "Use agentuse-share skill to document a new skill"
- "do you have agentuse-share skill?"

If successful, Codex will recognize and invoke the AgentUse Share skill workflow.

## Update

```bash
cd ~/.codex/agent-use-skills
git pull
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
