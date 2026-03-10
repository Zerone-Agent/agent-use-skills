# Install Playwright Skill in OpenCode

## Prerequisites

- [OpenCode.ai](https://opencode.ai) installed
- Git installed
- Node.js installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.config/opencode/agent-use-skills
```

### 2. Create a symbolic link

```bash
mkdir -p ~/.config/opencode/skills
rm -rf ~/.config/opencode/skills/playwright-skill
ln -s ~/.config/opencode/agent-use-skills/awesome-skills/skills/playwright-skill ~/.config/opencode/skills/playwright-skill
```

### 3. Initialize Environment

```bash
cd ~/.config/opencode/skills/playwright-skill
npm run setup
```

### 4. Restart OpenCode

Restart OpenCode and verify by asking: "do you have playwright-skill?"

## Update

```bash
cd ~/.config/opencode/agent-use-skills
git pull
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
