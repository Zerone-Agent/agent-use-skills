# Install Humanizer in OpenClaw

## Prerequisites

- [OpenClaw](https://github.com/nicepkg/openclaw) installed
- Git installed

## Installation Steps

### 1. Clone agent-use-skills repository

Clone the skills library to your local machine (if not already done):

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 2. Configure Skill in OpenClaw

Create a symbolic link so OpenClaw can find and use the skill:

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/humanizer
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/humanizer ~/.openclaw/skills/humanizer
```

## Verify Installation

Restart OpenClaw and try:

- "Check this copy for AI-generated patterns and provide a humanized version: [Content]"
- "do you have humanizer skill?"

## Usage Tips

Humanizer works best for:
- Polishing blog posts and social media content
- Avoiding common AI generalizations in summaries
- Increasing the authenticity and relatability of automated Agent responses

## Update

```bash
cd ~/.openclaw/agent-use-skills && git pull
```

## Get Help

- Skill issues: https://github.com/Zerone-Agent/agent-use-skills/issues
- Reference: [Wikipedia - Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
