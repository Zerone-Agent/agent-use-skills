# Installing Video Summarizer for Zerone

## Prerequisites

- Zerone installed
- Git installed
- yt-dlp, ffmpeg, and OpenAI Whisper installed

## Installation Steps

### 1. Install Tool Dependencies

```bash
pip install yt-dlp openai-whisper
brew install ffmpeg  # macOS
# or apt install ffmpeg  # Linux
```

### 2. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.agents/agent-use-skills
```

### 3. Symlink Skills

Create a symlink so Zerone discovers the skill:

```bash
mkdir -p ~/.agents/skills
rm -rf ~/.agents/skills/video-summarizer
ln -s ~/.agents/agent-use-skills/awesome-skills/skills/video-summarizer ~/.agents/skills/video-summarizer
```

### 4. Verify Installation

Restart Zerone and try asking:
- "Help me summarize this video https://www.youtube.com/watch?v=xxx"
- "do you have video-summarizer?"

If successful, Zerone will automatically recognize and invoke the Video Summarizer skill workflow.

## Updating

```bash
cd ~/.agents/agent-use-skills
git pull
```

## Uninstallation

Remove the symlink to uninstall:

```bash
rm -rf ~/.agents/skills/video-summarizer
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues