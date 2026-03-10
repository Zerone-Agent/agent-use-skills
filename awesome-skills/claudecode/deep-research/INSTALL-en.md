# Installing Deep Research for Claude Code

## Prerequisites

- [Claude Code](https://claude.ai/code) installed
- Git installed
- Python 3.8+ installed
- A [Gemini API Key](https://aistudio.google.com/) from Google AI Studio

## Installation Steps

### 1. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.claude/agent-use-skills
```

### 2. Install Python Dependencies

```bash
pip install -r ~/.claude/agent-use-skills/awesome-skills/skills/deep-research/requirements.txt
```

### 3. Configure API Key

Set your Gemini API key as an environment variable:

```bash
export GEMINI_API_KEY=your-api-key-here
```

Or create a `.env` file in the skill directory:

```bash
cp ~/.claude/agent-use-skills/awesome-skills/skills/deep-research/.env.example \
   ~/.claude/agent-use-skills/awesome-skills/skills/deep-research/.env
# Edit the .env file and add your GEMINI_API_KEY
```

### 4. Symlink Skills

Create a symlink so Claude Code discovers the deep-research skill:

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/deep-research
ln -s ~/.claude/agent-use-skills/awesome-skills/skills/deep-research ~/.claude/skills/deep-research
```

### 5. Verify Installation

Restart Claude Code, then try asking the following to verify the installation:

- "Research the competitive landscape of cloud providers"
- "do you have deep-research?"

If successful, Claude Code will automatically recognize and invoke the Deep Research workflow.

## Updating

```bash
cd ~/.claude/agent-use-skills
git pull
pip install -r awesome-skills/skills/deep-research/requirements.txt
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues
