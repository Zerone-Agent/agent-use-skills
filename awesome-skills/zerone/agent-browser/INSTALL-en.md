# Install Agent Browser in Zerone

## Prerequisites

- Zerone installed
- Node.js and npm installed
- Git installed

## Installation Steps

### 1. Install Core CLI

Agent Browser is a global CLI tool. Install it via npm first:

```bash
npm install -g agent-browser
agent-browser install --with-deps
```

### 2. Clone agent-browser repository

Clone the skills library to your local machine:

```bash
git clone https://github.com/vercel-labs/agent-browser.git ~/.agents/agent-browser
```

### 3. Configure Skill in Zerone

Create a symbolic link so Zerone can find and use the skill:

```bash
mkdir -p ~/.agents/skills
rm -rf ~/.agents/skills/agent-browser
ln -s ~/.agents/agent-browser/skills/agent-browser ~/.agents/skills/agent-browser
```

## Verify Installation

Restart Zerone and try:

- "Open google.com and tell me the reference ID of the search box"
- "do you have agent-browser skill?"

## Update

1. **Update CLI**: `npm update -g agent-browser`
2. **Update Skill Library**: `cd ~/.agents/agent-browser && git pull`

## Uninstallation

Just remove the symbolic link to uninstall:

```bash
rm -rf ~/.agents/skills/agent-browser
```

## Get Help

- Skill issues: https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser
- CLI issues: https://github.com/vercel-labs/agent-browser/issues
