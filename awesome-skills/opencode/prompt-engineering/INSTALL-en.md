# Install Prompt Engineering in OpenCode

## Installation Steps

### 1. Clone repository
```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.config/opencode/agent-use-skills
```

### 2. Create symbolic link
```bash
mkdir -p ~/.config/opencode/skills
ln -s ~/.config/opencode/agent-use-skills/awesome-skills/skills/prompt-engineering ~/.config/opencode/skills/prompt-engineering
```

## Verify Installation

Restart OpenCode and try:
- "How can I use persuasion principles in this skill?"

## Update
```bash
cd ~/.config/opencode/agent-use-skills && git pull
```
