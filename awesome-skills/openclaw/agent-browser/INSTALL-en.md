# Install Agent Browser in OpenClaw

## Prerequisites

- [OpenClaw](https://github.com/nicepkg/openclaw) installed
- Node.js and npm installed
- Git installed

## Installation Steps

### 1. Install Core CLI

Agent Browser is a global CLI tool. Install it via npm first:

```bash
npm install -g agent-browser
agent-browser install --with-deps
```

### 2. Clone agent-use-skills repository

Clone the skills library to your local machine (if not already done):

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 3. Configure Skill in OpenClaw

Create a symbolic link so OpenClaw can find and use the skill:

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/agent-browser
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/agent-browser ~/.openclaw/skills/agent-browser
```

## Verify Installation

Restart OpenClaw and try:

- "Open google.com and tell me the reference ID of the search box"
- "do you have agent-browser skill?"

## Update

1. **Update CLI**: `npm update -g agent-browser`
2. **Update Skill Library**: `cd ~/.openclaw/agent-use-skills && git pull`

## Get Help

- Skill issues: https://github.com/Zerone-Agent/agent-use-skills/issues
- CLI issues: https://github.com/vercel-labs/agent-browser/issues
