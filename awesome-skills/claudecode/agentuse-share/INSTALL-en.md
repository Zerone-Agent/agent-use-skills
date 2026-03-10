# Install AgentUse Share in Claude Code

## Prerequisites

- [Claude Code](https://claude.ai/code) installed
- Git installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.claude/agent-use-skills
```

### 2. Create a symbolic link

Create a symbolic link so that Claude Code can discover the agentuse-share skill:

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/agentuse-share
ln -s ~/.claude/agent-use-skills/awesome-skills/skills/agentuse-share ~/.claude/skills/agentuse-share
```

### 3. Verify Installation

Restart Claude Code and try the following command to verify the installation:

- "Use agentuse-share skill to document a new skill"
- "do you have agentuse-share skill?"

If successful, Claude Code will recognize and invoke the AgentUse Share skill workflow.

## Update

```bash
cd ~/.claude/agent-use-skills
git pull
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
