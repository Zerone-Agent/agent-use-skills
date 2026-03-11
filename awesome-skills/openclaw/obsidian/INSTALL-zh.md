# 在 OpenClaw 中安装 Obsidian 技能

## 前置条件

- 已安装 [OpenClaw](https://github.com/nicepkg/openclaw)
- 已安装 [Obsidian 桌面客户端](https://obsidian.md/)
- 已安装 Homebrew (macOS)
- 已安装 Git

## 安装步骤

### 1. 安装 obsidian-cli

该技能依赖于 `obsidian-cli` 工具，请先通过 Homebrew 安装：

```bash
brew tap yakitrak/yakitrak
brew install obsidian-cli
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
rm -rf ~/.openclaw/skills/obsidian
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/obsidian ~/.openclaw/skills/obsidian
```

### 4. 设置默认仓库 (Vault)

运行以下命令，将您常用的文件夹设置为默认仓库：

```bash
obsidian-cli set-default "您的仓库文件夹名称"
```

## 验证安装

重启 OpenClaw，尝试提问：

- "我的 Obsidian 仓库在哪里？"
- "在我的笔记里搜索关于 'AI' 的内容"
- "do you have obsidian skill?"

## 更新

1. **更新 CLI**: `brew upgrade obsidian-cli`
2. **更新技能库**: `cd ~/.openclaw/agent-use-skills && git pull`

## 获取帮助

- 技能逻辑问题：https://github.com/Zerone-Agent/agent-use-skills/issues
- CLI 工具问题：https://github.com/yakitrak/obsidian-cli/issues
