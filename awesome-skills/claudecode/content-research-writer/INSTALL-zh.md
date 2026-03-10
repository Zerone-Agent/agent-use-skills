# 在 Claude Code 中安装 Content Research Writer

## 前置条件

- 已安装 [Claude Code](https://claude.ai/code)
- 已安装 Git

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.claude/agent-use-skills
```

### 2. 创建符号链接

创建符号链接，使 Claude Code 能够发现 content-research-writer 技能：

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/content-research-writer
ln -s ~/.claude/agent-use-skills/awesome-skills/skills/content-research-writer ~/.claude/skills/content-research-writer
```

### 3. 验证安装

重启 Claude Code，然后尝试询问以下问题来验证是否安装成功：

- "帮我创建一篇关于 [主题] 的文章大纲"
- "do you have content-research-writer?"

如果安装成功，Claude Code 会自动识别并调用 Content Research Writer 技能工作流。

## 更新

```bash
cd ~/.claude/agent-use-skills
git pull
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues
