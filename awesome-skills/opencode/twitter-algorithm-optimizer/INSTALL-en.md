# Install Twitter Algorithm Optimizer in OpenCode

## Installation Steps

### 1. Clone repository
```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.config/opencode/agent-use-skills
```

### 2. Create symbolic link
```bash
mkdir -p ~/.config/opencode/skills
ln -s ~/.config/opencode/agent-use-skills/awesome-skills/skills/twitter-algorithm-optimizer ~/.config/opencode/skills/twitter-algorithm-optimizer
```

## Verify Installation

Restart OpenCode and try:
- "Analyze and optimize the algorithmic performance of this tweet: [Content]"

## Update
```bash
cd ~/.config/opencode/agent-use-skills && git pull
```
