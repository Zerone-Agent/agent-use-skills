# 在 OpenClaw 中安装 Agent Browser

## 前置条件

- 已安装 [OpenClaw](https://github.com/nicepkg/openclaw)
- 已安装 Node.js 和 npm
- 已安装 Git

## 安装步骤

### 1. 安装核心 CLI

Agent Browser 是一个全局命令行工具，首先需要通过 npm 安装：

```bash
npm install -g agent-browser
agent-browser install --with-deps
```

### 2. 克隆 agent-use-skills 仓库

将技能库克隆到本地（如果尚未克隆）：

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 3. 在 OpenClaw 中配置技能

创建符号链接，使 OpenClaw 能够调用该技能：

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/agent-browser
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/agent-browser ~/.openclaw/skills/agent-browser
```

## 验证安装

重启 OpenClaw，尝试提问：

- "打开 google.com 并告诉我搜索框的引用 ID"
- "do you have agent-browser skill?"

## 更新

1. **更新 CLI**: `npm update -g agent-browser`
2. **更新技能库**: `cd ~/.openclaw/agent-use-skills && git pull`

## 获取帮助

- 技能逻辑问题：https://github.com/Zerone-Agent/agent-use-skills/issues
- CLI 工具问题：https://github.com/vercel-labs/agent-browser/issues
