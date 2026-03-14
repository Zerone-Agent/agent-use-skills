# Install Multi Search Engine in OpenClaw

## Prerequisites

- OpenClaw platform installed
- Git installed

## Installation Steps

### 1. Clone the agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 2. Create a symbolic link

Create a symbolic link so that OpenClaw can discover the multi-search-engine skill:

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/multi-search-engine
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/multi-search-engine ~/.openclaw/skills/multi-search-engine
```

### 3. Verify Installation

Restart OpenClaw and try the following command to verify the installation:

- "Search for python tutorials using google"
- "do you have the multi-search-engine skill?"

If successful, OpenClaw will recognize and invoke the Multi Search Engine skill workflow.

## Update

```bash
cd ~/.openclaw/agent-use-skills
git pull
```

## Get Help

- Submit issues: https://github.com/Zerone-Agent/agent-use-skills/issues
