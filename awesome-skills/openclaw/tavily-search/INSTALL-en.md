# Install Tavily Search in OpenClaw

## Prerequisites

- [OpenClaw](https://github.com/nicepkg/openclaw) installed
- Git installed
- Node.js installed
- [Tavily API Key](https://tavily.com)

## Installation Steps

### 1. Clone agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 2. Create symbolic link

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/tavily-search
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/tavily-search ~/.openclaw/skills/tavily-search
```

### 3. Set Environment Variable

Get your API Key and set it:

- **macOS/Linux**: `export TAVILY_API_KEY="your-api-key"`
- **Windows**: `$env:TAVILY_API_KEY="your-api-key"`

### 4. Verify Installation

Restart OpenClaw and try:

- "Search for the latest trends in [topic] and provide a deep analysis"
- "do you have tavily-search skill?"

## Update

```bash
cd ~/.openclaw/agent-use-skills && git pull
```

## Get Help

- File an issue: https://github.com/Zerone-Agent/agent-use-skills/issues
