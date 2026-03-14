# 在 Claude Code 中安装 Humanizer-zh

## 前置条件

- 已安装 [Claude Code](https://claude.ai/code)
- 已安装 Git

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.claude/agent-use-skills
```

### 2. 创建符号链接

创建符号链接，使 Claude Code 能够发现 humanizer-zh 技能：

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/humanizer-zh
ln -s ~/.claude/agent-use-skills/awesome-skills/skills/humanizer-zh ~/.claude/skills/humanizer-zh
```

### 3. 验证安装

重启 Claude Code，然后尝试输入以下指令来验证是否安装成功：

- "使用 humanizer-zh 技能优化这段文字"
- "do you have humanizer-zh skill?"

如果安装成功，Claude Code 会自动识别并调用 Humanizer-zh 技能工作流。

## 更新

```bash
cd ~/.claude/agent-use-skills
git pull
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues
