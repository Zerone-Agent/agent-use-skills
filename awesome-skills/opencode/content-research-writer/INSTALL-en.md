# Installing content-research-writer for OpenCode

## Prerequisites

- [OpenCode.ai](https://opencode.ai) installed
- Git installed

## Installation Steps

### 1. Clone agent-use-skills

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.config/opencode/agent-use-skills
```

### 2. Symlink Skills

Create a symlink so OpenCode's native skill tool discovers content-research-writer skills:

```bash
mkdir -p ~/.config/opencode/skills
rm -rf ~/.config/opencode/skills/content-research-writer
ln -s ~/.config/opencode/agent-use-skills/awesome-skills/skills/content-research-writer ~/.config/opencode/skills/content-research-writer
```

### 3. Restart OpenCode

Restart OpenCode. The plugin will automatically inject content-research-writer context.

Verify by asking: "do you have content-research-writer?"

## Updating

```bash
cd ~/.config/opencode/agent-use-skills
git pull
```

## Getting Help

- Report issues: https://github.com/Zerone-Agent/agent-use-skills/issues
