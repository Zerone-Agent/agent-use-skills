# Install Imagen in OpenClaw

## Prerequisites

- [OpenClaw](https://github.com/nicepkg/openclaw) installed
- Git installed
- [Google AI Studio](https://aistudio.google.com/) API Key

## Installation Steps

### 1. Clone agent-use-skills repository

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 2. Create symbolic link

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/imagen
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/imagen ~/.openclaw/skills/imagen
```

### 3. Set Environment Variable

Get your API Key and set it:

- **macOS/Linux**: `export GEMINI_API_KEY="your-api-key"`
- **Windows**: `$env:GEMINI_API_KEY="your-api-key"`

### 4. Verify Installation

Restart OpenClaw, ensure you are in **Agent** mode, and try:

- "Generate an image of a futuristic city"

## Update

```bash
cd ~/.openclaw/agent-use-skills
git pull
```

## Get Help

- File an issue: https://github.com/Zerone-Agent/agent-use-skills/issues
