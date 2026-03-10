# Install Canvas Design in Qoder

## Prerequisites

- [Qoder](https://qoder.ai) installed
- Git installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.qoder/agent-use-skills
```

### 2. Create a symbolic link

```bash
mkdir -p ~/.qoder/skills
rm -rf ~/.qoder/skills/canvas-design
ln -s ~/.qoder/agent-use-skills/awesome-skills/skills/canvas-design ~/.qoder/skills/canvas-design
```

### 3. Verify Installation

Restart Qoder and verify by asking: "do you have canvas-design skill?"

## Update

```bash
cd ~/.qoder/agent-use-skills
git pull
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
