# Install Prompt Engineering in Qoder

## Installation Steps

### 1. Clone repository
```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.qoder/agent-use-skills
```

### 2. Create symbolic link
```bash
mkdir -p ~/.qoder/skills
ln -s ~/.qoder/agent-use-skills/awesome-skills/skills/prompt-engineering ~/.qoder/skills/prompt-engineering
```

## Verify Installation

Restart Qoder and try:
- "How can I reduce token consumption in my prompts?"

## Update
```bash
cd ~/.qoder/agent-use-skills && git pull
```
