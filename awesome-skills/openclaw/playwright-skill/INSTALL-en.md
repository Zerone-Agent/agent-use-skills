# Install Playwright Skill in OpenClaw

## Prerequisites

- [OpenClaw](https://github.com/nicepkg/openclaw) installed
- Git installed
- Node.js installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 2. Create a symbolic link

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/playwright-skill
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/playwright-skill ~/.openclaw/skills/playwright-skill
```

### 3. Initialize Environment

```bash
cd ~/.openclaw/skills/playwright-skill
npm run setup
```

### 4. Verify Installation

Restart OpenClaw and verify by asking: "do you have playwright-skill?"

## Update

```bash
cd ~/.openclaw/agent-use-skills
git pull
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
