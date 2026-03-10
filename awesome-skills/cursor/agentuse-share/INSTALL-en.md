# Install AgentUse Share in Cursor

## Prerequisites

- [Cursor](https://cursor.com) installed
- Git installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.cursor/agent-use-skills
```

### 2. Create a symbolic link

Create a symbolic link so that Cursor can discover the agentuse-share skill:

```bash
mkdir -p ~/.cursor/skills
rm -rf ~/.cursor/skills/agentuse-share
ln -s ~/.cursor/agent-use-skills/awesome-skills/skills/agentuse-share ~/.cursor/skills/agentuse-share
```

### 3. Verify Installation

Restart Cursor and ensure you are in **Agent** mode, then try asking:

- "Use agentuse-share skill to document a new skill"
- "do you have agentuse-share skill?"

If successful, Cursor Agent will recognize and invoke the AgentUse Share skill workflow.

## Update

```bash
cd ~/.cursor/agent-use-skills
git pull
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
