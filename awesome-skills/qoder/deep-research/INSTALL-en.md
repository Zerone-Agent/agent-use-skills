# Installing Deep Research for Qoder

## Prerequisites

- [Qoder](https://qoder.ai) installed
- Git installed
- Python 3.8+ installed
- A [Gemini API Key](https://aistudio.google.com/) from Google AI Studio

## Installation Steps

### 1. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.qoder/agent-use-skills
```

### 2. Install Python Dependencies

```bash
pip install -r ~/.qoder/agent-use-skills/awesome-skills/skills/deep-research/requirements.txt
```

### 3. Configure API Key

Set your Gemini API key as an environment variable:

```bash
export GEMINI_API_KEY=your-api-key-here
```

Or create a `.env` file in the skill directory:

```bash
cp ~/.qoder/agent-use-skills/awesome-skills/skills/deep-research/.env.example \
   ~/.qoder/agent-use-skills/awesome-skills/skills/deep-research/.env
# Edit the .env file and add your GEMINI_API_KEY
```

### 4. Symlink Skills

Create a symlink so Qoder discovers the deep-research skill:

```bash
mkdir -p ~/.qoder/skills
rm -rf ~/.qoder/skills/deep-research
ln -s ~/.qoder/agent-use-skills/awesome-skills/skills/deep-research ~/.qoder/skills/deep-research
```

### 5. Verify Installation

Restart Qoder, then try asking:

- "Research the competitive landscape of cloud providers"
- "do you have deep-research?"

If successful, Qoder will automatically recognize and invoke the Deep Research workflow.

## Updating

```bash
cd ~/.qoder/agent-use-skills
git pull
pip install -r awesome-skills/skills/deep-research/requirements.txt
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues
