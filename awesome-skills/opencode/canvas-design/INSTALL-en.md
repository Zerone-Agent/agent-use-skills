# Install Canvas Design in OpenCode

## Prerequisites

- [OpenCode.ai](https://opencode.ai) installed
- Git installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.config/opencode/agent-use-skills
```

### 2. Create a symbolic link

```bash
mkdir -p ~/.config/opencode/skills
rm -rf ~/.config/opencode/skills/canvas-design
ln -s ~/.config/opencode/agent-use-skills/awesome-skills/skills/canvas-design ~/.config/opencode/skills/canvas-design
```

### 3. Restart OpenCode

Restart OpenCode and verify by asking: "do you have canvas-design?"

## Update

```bash
cd ~/.config/opencode/agent-use-skills
git pull
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
