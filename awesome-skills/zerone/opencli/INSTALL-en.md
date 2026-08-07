# Installing OpenCLI for Zerone

## Prerequisites

- Zerone installed
- Git installed
- Node.js >= 21.0.0 (or Bun >= 1.0) installed

## Installation Steps

### 1. Clone OpenCLI Repository

```bash
git clone https://github.com/jackwener/OpenCLI.git ~/.agents/opencli
```

### 2. Symlink Skills

Create symlinks so Zerone discovers the OpenCLI skills:

```bash
mkdir -p ~/.agents/skills
for skill in $(ls ~/.agents/opencli/skills); do
  rm -rf ~/.agents/skills/$skill
  ln -s ~/.agents/opencli/skills/$skill ~/.agents/skills/$skill
done
```

### 3. Install OpenCLI npm Package

```bash
npm install -g @jackwener/opencli
```

### 4. Install Browser Extension

OpenCLI connects to Chrome/Chromium through a Browser Bridge extension:

1. Download the latest `opencli-extension-v{version}.zip` from the [Releases page](https://github.com/jackwener/OpenCLI/releases)
2. Unzip it, open `chrome://extensions`, and enable **Developer mode**
3. Click **Load unpacked** and select the unzipped folder

### 5. Verify Installation

Restart Zerone, then run:

```bash
opencli doctor
opencli list
```

Try asking Zerone:
- "do you have opencli-browser?"
- "do you have opencli-explorer?"

If successful, Zerone will automatically recognize and invoke the relevant OpenCLI skill.

## Updating

```bash
cd ~/.agents/opencli
git pull
npm update -g @jackwener/opencli
```

## Uninstallation

Remove the symlinks and repository:

```bash
for skill in $(ls ~/.agents/opencli/skills); do
  rm -rf ~/.agents/skills/$skill
done
rm -rf ~/.agents/opencli
npm uninstall -g @jackwener/opencli
```

## Getting Help

- GitHub: https://github.com/jackwener/OpenCLI
- Report issues: https://github.com/jackwener/OpenCLI/issues