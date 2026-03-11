# Install Summarize in OpenClaw

## Prerequisites

- [OpenClaw](https://github.com/nicepkg/openclaw) installed
- Homebrew installed (macOS)
- [Gemini API Key](https://aistudio.google.com/app/apikey) (Recommended) or other supported model Keys

## Installation Steps

### 1. Install summarize CLI

This skill depends on the `summarize` CLI tool. Install it via Homebrew first:

```bash
brew tap steipete/tap
brew install summarize
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
rm -rf ~/.openclaw/skills/summarize
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/summarize ~/.openclaw/skills/summarize
```

### 4. Set Environment Variables

Set the API key for your chosen model:

```bash
export GEMINI_API_KEY="your-api-key"
# OR
export ANTHROPIC_API_KEY="your-api-key"
```

## Verify Installation

Restart OpenClaw and try:

- "Summarize this webpage: https://example.com"
- "Summarize this local PDF: /path/to/document.pdf"

## Update

1. **Update CLI**: `brew upgrade summarize`
2. **Update Skill Library**: `cd ~/.openclaw/agent-use-skills && git pull`

## Get Help

- Skill issues: https://github.com/Zerone-Agent/agent-use-skills/issues
- CLI tool issues: https://github.com/steipete/summarize/issues
