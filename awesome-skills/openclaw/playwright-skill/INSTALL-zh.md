# 在 OpenClaw 中安装 Playwright Skill

## 前置条件

- 已安装 [OpenClaw](https://github.com/nicepkg/openclaw)
- 已安装 Git
- 已安装 Node.js

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 2. 创建符号链接

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/playwright-skill
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/playwright-skill ~/.openclaw/skills/playwright-skill
```

### 3. 初始化环境

```bash
cd ~/.openclaw/skills/playwright-skill
npm run setup
```

### 4. 验证安装

重启 OpenClaw，然后尝试询问：

- "帮我截一张 http://localhost:3000 的全屏图"
- "do you have playwright-skill?"

## 更新

```bash
cd ~/.openclaw/agent-use-skills
git pull
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues
