# Install Prompt Engineering in Codex

## Installation Steps

### 1. Clone repository
```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.codex/agent-use-skills
```

### 2. Create symbolic link
```bash
mkdir -p ~/.codex/skills
ln -s ~/.codex/agent-use-skills/awesome-skills/skills/prompt-engineering ~/.codex/skills/prompt-engineering
```

## Verify Installation

Restart Codex and try:
- "Analyze this logic using Chain-of-Thought (CoT) pattern."

## Update
```bash
cd ~/.codex/agent-use-skills && git pull
```
