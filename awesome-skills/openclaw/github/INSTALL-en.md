# Install GitHub Skill in OpenClaw

## Prerequisites

- [OpenClaw](https://github.com/nicepkg/openclaw) installed
- [GitHub CLI (gh)](https://cli.github.com/) installed
- GitHub authenticated (`gh auth login`)
- Git installed

## Installation Steps

### 1. Install GitHub CLI (if not already installed)

macOS users can install it via Homebrew:

```bash
brew install gh
```

After installation, run `gh auth login` to authorize your account.

### 2. Clone agent-use-skills repository

Clone the skills library to your local machine (if not already done):

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 3. Configure Skill in OpenClaw

Create a symbolic link so OpenClaw can find and use the skill:

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/github
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/github ~/.openclaw/skills/github
```

## Verify Installation

Restart OpenClaw and try:

- "Check the CI status of the last 5 pull requests"
- "List all open issues in this repository"
- "do you have github skill?"

## Update

1. **Update CLI**: `brew upgrade gh`
2. **Update Skill Library**: `cd ~/.openclaw/agent-use-skills && git pull`

## Get Help

- Skill issues: https://github.com/Zerone-Agent/agent-use-skills/issues
- CLI tool issues: https://github.com/cli/cli/issues
