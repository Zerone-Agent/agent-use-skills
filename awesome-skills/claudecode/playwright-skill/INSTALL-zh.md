# 在 Claude Code 中安装 Playwright Skill

## 前置条件

- 已安装 [Claude Code](https://claude.ai/code)
- 已安装 Git
- 已安装 Node.js (建议 v18+)

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.claude/agent-use-skills
```

### 2. 创建符号链接

创建符号链接，使 Claude Code 能够发现 playwright-skill 技能：

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/playwright-skill
ln -s ~/.claude/agent-use-skills/awesome-skills/skills/playwright-skill ~/.claude/skills/playwright-skill
```

### 3. 初始化技能环境

Playwright 需要安装浏览器驱动和依赖包，请在技能目录下运行初始化：

```bash
cd ~/.claude/skills/playwright-skill
npm run setup
```

### 4. 验证安装

重启 Claude Code，然后尝试输入以下指令来验证是否安装成功：

- "帮我截一张 http://localhost:3000 的全屏图"
- "do you have playwright-skill?"

如果安装成功，Claude Code 会自动识别并调用 Playwright Skill 技能工作流，并在浏览器中执行操作。

## 更新

```bash
cd ~/.claude/agent-use-skills
git pull
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues
