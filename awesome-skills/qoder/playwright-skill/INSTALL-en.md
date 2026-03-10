# Install Playwright Skill in Qoder

## Prerequisites

- [Qoder](https://qoder.ai) installed
- Git installed
- Node.js installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.qoder/agent-use-skills
```

### 2. Create a symbolic link

```bash
mkdir -p ~/.qoder/skills
rm -rf ~/.qoder/skills/playwright-skill
ln -s ~/.qoder/agent-use-skills/awesome-skills/skills/playwright-skill ~/.qoder/skills/playwright-skill
```

### 3. Initialize Environment

```bash
cd ~/.qoder/skills/playwright-skill
npm run setup
```

### 4. Verify Installation

Restart Qoder and verify by asking: "do you have playwright-skill?"

## Update

```bash
cd ~/.qoder/agent-use-skills
git pull
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
