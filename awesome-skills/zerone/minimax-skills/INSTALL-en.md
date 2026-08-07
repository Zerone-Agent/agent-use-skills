# Installing MiniMax Skills for Zerone

## Prerequisites

- Zerone installed
- Git installed

## Installation Steps

### 1. Clone MiniMax Skills

```bash
git clone https://github.com/MiniMax-AI/skills.git ~/.agents/minimax-skills
```

### 2. Symlink Skills

Create symlinks so Zerone discovers the skills:

```bash
mkdir -p ~/.agents/skills
for skill in android-native-dev ios-application-dev flutter-dev react-native-dev frontend-dev fullstack-dev shader-dev gif-sticker-maker vision-analysis minimax-pdf pptx-generator minimax-xlsx minimax-docx minimax-multimodal-toolkit; do
  rm -rf ~/.agents/skills/$skill
  ln -s ~/.agents/minimax-skills/skills/$skill ~/.agents/skills/$skill
done
```

### 3. Verify Installation

Restart Zerone and try asking:
- "Help me create a PowerPoint presentation"
- "do you have minimax skills?"

If successful, Zerone will automatically recognize and invoke MiniMax Skills workflow.

## Updating

```bash
cd ~/.agents/minimax-skills
git pull
```

## Uninstallation

Remove the symlinks to uninstall:

```bash
for skill in android-native-dev ios-application-dev flutter-dev react-native-dev frontend-dev fullstack-dev shader-dev gif-sticker-maker vision-analysis minimax-pdf pptx-generator minimax-xlsx minimax-docx minimax-multimodal-toolkit; do
  rm -rf ~/.agents/skills/$skill
done
```

## Getting Help

- GitHub: https://github.com/MiniMax-AI/skills