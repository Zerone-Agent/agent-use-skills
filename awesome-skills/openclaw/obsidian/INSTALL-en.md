# Install Obsidian Skill in OpenClaw

## Prerequisites

- [OpenClaw](https://github.com/nicepkg/openclaw) installed
- [Obsidian Desktop App](https://obsidian.md/) installed
- Homebrew installed (macOS)
- Git installed

## Installation Steps

### 1. Install obsidian-cli

This skill depends on the `obsidian-cli` tool. Install it via Homebrew first:

```bash
brew tap yakitrak/yakitrak
brew install obsidian-cli
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
rm -rf ~/.openclaw/skills/obsidian
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/obsidian ~/.openclaw/skills/obsidian
```

### 4. Set Default Vault

Run the following command to set your primary vault as default:

```bash
obsidian-cli set-default "your-vault-folder-name"
```

## Verify Installation

Restart OpenClaw and try:

- "Where is my Obsidian vault located?"
- "Search my notes for 'AI' content"
- "do you have obsidian skill?"

## Update

1. **Update CLI**: `brew upgrade obsidian-cli`
2. **Update Skill Library**: `cd ~/.openclaw/agent-use-skills && git pull`

## Get Help

- Skill issues: https://github.com/Zerone-Agent/agent-use-skills/issues
- CLI tool issues: https://github.com/yakitrak/obsidian-cli/issues
