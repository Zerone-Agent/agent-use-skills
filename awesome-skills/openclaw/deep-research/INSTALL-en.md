# Installing Deep Research for OpenClaw

## Prerequisites

- [OpenClaw](https://github.com/nicepkg/openclaw) installed
- Git installed
- Python 3.8+ installed
- A [Gemini API Key](https://aistudio.google.com/) from Google AI Studio

## Installation Steps

### 1. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 2. Install Python Dependencies

```bash
pip install -r ~/.openclaw/agent-use-skills/awesome-skills/skills/deep-research/requirements.txt
```

### 3. Configure API Key

Set your Gemini API key as an environment variable:

```bash
export GEMINI_API_KEY=your-api-key-here
```

Or create a `.env` file in the skill directory:

```bash
cp ~/.openclaw/agent-use-skills/awesome-skills/skills/deep-research/.env.example \
   ~/.openclaw/agent-use-skills/awesome-skills/skills/deep-research/.env
# Edit the .env file and add your GEMINI_API_KEY
```

### 4. Symlink Skills

Create a symlink so OpenClaw discovers the deep-research skill:

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/deep-research
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/deep-research ~/.openclaw/skills/deep-research
```

### 5. Verify Installation

Restart OpenClaw, then try asking:

- "Research the competitive landscape of cloud providers"
- "do you have deep-research?"

If successful, OpenClaw will automatically recognize and invoke the Deep Research workflow.

## Updating

```bash
cd ~/.openclaw/agent-use-skills
git pull
pip install -r awesome-skills/skills/deep-research/requirements.txt
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues
