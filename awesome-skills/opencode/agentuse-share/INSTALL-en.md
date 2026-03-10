# Install AgentUse Share in OpenCode

## Prerequisites

- [OpenCode.ai](https://opencode.ai) installed
- Git installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.config/opencode/agent-use-skills
```

### 2. Create a symbolic link

Create a symbolic link so that OpenCode's native skill tools can discover the agentuse-share skill:

```bash
mkdir -p ~/.config/opencode/skills
rm -rf ~/.config/opencode/skills/agentuse-share
ln -s ~/.config/opencode/agent-use-skills/awesome-skills/skills/agentuse-share ~/.config/opencode/skills/agentuse-share
```

### 3. Restart OpenCode

Restart OpenCode, and the plugin will automatically inject the agentuse-share context.

Verify the installation by asking: "do you have agentuse-share?"

## Update

```bash
cd ~/.config/opencode/agent-use-skills
git pull
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
