# 在 Claude Code 中安装 Canvas Design

## 前置条件

- 已安装 [Claude Code](https://claude.ai/code)
- 已安装 Git

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.claude/agent-use-skills
```

### 2. 创建符号链接

创建符号链接，使 Claude Code 能够发现 canvas-design 技能（包含其专属字体库）：

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/canvas-design
ln -s ~/.claude/agent-use-skills/awesome-skills/skills/canvas-design ~/.claude/skills/canvas-design
```

### 3. 验证安装

重启 Claude Code，然后尝试输入以下指令来验证是否安装成功：

- "帮我根据 [某个主题] 创作一张海报"
- "do you have canvas-design skill?"

如果安装成功，Claude Code 会自动识别并调用 Canvas Design 技能的工作流，首先生成设计哲学。

## 更新

```bash
cd ~/.claude/agent-use-skills
git pull
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues
