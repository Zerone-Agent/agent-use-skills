# 在 OpenClaw 中安装 GitHub 技能

## 前置条件

- 已安装 [OpenClaw](https://github.com/nicepkg/openclaw)
- 已安装 [GitHub CLI (gh)](https://cli.github.com/)
- 已配置 GitHub 认证 (`gh auth login`)
- 已安装 Git

## 安装步骤

### 1. 安装 GitHub CLI (如果尚未安装)

macOS 用户可通过 Homebrew 快速安装：

```bash
brew install gh
```

完成安装后请运行 `gh auth login` 进行登录授权。

### 2. 克隆 agent-use-skills 仓库

将技能库克隆到本地（如果尚未克隆）：

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 3. 在 OpenClaw 中配置技能

创建符号链接，使 OpenClaw 能够调用该技能：

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/github
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/github ~/.openclaw/skills/github
```

## 验证安装

重启 OpenClaw，尝试提问：

- "帮我检查一下最近 5 个 PR 的 CI 状态"
- "列出本项目所有开启的 Issue"
- "do you have github skill?"

## 更新

1. **更新 CLI**: `brew upgrade gh`
2. **更新技能库**: `cd ~/.openclaw/agent-use-skills && git pull`

## 获取帮助

- 技能逻辑问题：https://github.com/Zerone-Agent/agent-use-skills/issues
- CLI 工具问题：https://github.com/cli/cli/issues
