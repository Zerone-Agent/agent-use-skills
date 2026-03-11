# Install Gog (Google Workspace CLI) in OpenClaw

## Prerequisites

- [OpenClaw](https://github.com/nicepkg/openclaw) installed
- Homebrew installed (macOS)
- A Google account and OAuth credentials (client_secret.json) created in the Google Cloud Console

## Installation Steps

### 1. Install gog CLI

This skill depends on the `gog` CLI tool. Install it via Homebrew:

```bash
brew tap steipete/tap
brew install gogcli
```

### 2. Initialize Authentication

You need to provide your Google Cloud OAuth credentials file:

```bash
# Import credentials
gog auth credentials /path/to/your/client_secret.json

# Add account and authorize services
gog auth add your-email@gmail.com --services gmail,calendar,drive,contacts,sheets,docs
```

### 3. Clone agent-use-skills repository

Clone the skills library to your local machine (if not already done):

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 4. Configure Skill in OpenClaw

Create a symbolic link:

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/gog
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/gog ~/.openclaw/skills/gog
```

### 5. Set Environment Variable (Optional)

To simplify usage, it's recommended to set a default account:

```bash
export GOG_ACCOUNT="your-email@gmail.com"
```

## Verify Installation

Restart OpenClaw and try asking:

- "Search for Gmail messages from the last 7 days with the subject 'Invoice'"
- "Check my calendar events for today"
- "do you have gog skill?"

## Update

1. **Update CLI**: `brew upgrade gogcli`
2. **Update Skill Library**: `cd ~/.openclaw/agent-use-skills && git pull`

## Get Help

- Skill issues: https://github.com/Zerone-Agent/agent-use-skills/issues
- CLI tool issues: https://github.com/steipete/gog/issues
