# Installing Deep Research for OpenCode

## Prerequisites

- [OpenCode.ai](https://opencode.ai) installed
- Git installed
- Python 3.8+ installed
- A [Gemini API Key](https://aistudio.google.com/) from Google AI Studio

## Installation Steps

### 1. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.config/opencode/agent-use-skills
```

### 2. Install Python Dependencies

```bash
pip install -r ~/.config/opencode/agent-use-skills/awesome-skills/skills/deep-research/requirements.txt
```

### 3. Configure API Key

Set your Gemini API key as an environment variable:

```bash
export GEMINI_API_KEY=your-api-key-here
```

Or create a `.env` file in the skill directory:

```bash
cp ~/.config/opencode/agent-use-skills/awesome-skills/skills/deep-research/.env.example \
   ~/.config/opencode/agent-use-skills/awesome-skills/skills/deep-research/.env
# Edit the .env file and add your GEMINI_API_KEY
```

### 4. Symlink Skills

Create a symlink so OpenCode's native skill tool discovers the deep-research skill:

```bash
mkdir -p ~/.config/opencode/skills
rm -rf ~/.config/opencode/skills/deep-research
ln -s ~/.config/opencode/agent-use-skills/awesome-skills/skills/deep-research ~/.config/opencode/skills/deep-research
```

### 5. Restart OpenCode

Restart OpenCode. The plugin will automatically inject Deep Research context.

Verify by asking: "do you have deep-research?"

## Updating

```bash
cd ~/.config/opencode/agent-use-skills
git pull
pip install -r awesome-skills/skills/deep-research/requirements.txt
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues
