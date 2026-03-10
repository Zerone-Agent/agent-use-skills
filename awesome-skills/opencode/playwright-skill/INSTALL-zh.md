# 为 OpenCode 安装 Playwright Skill

## 前置条件

- 已安装 [OpenCode.ai](https://opencode.ai)
- 已安装 Git
- 已安装 Node.js

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.config/opencode/agent-use-skills
```

### 2. 创建符号链接

```bash
mkdir -p ~/.config/opencode/skills
rm -rf ~/.config/opencode/skills/playwright-skill
ln -s ~/.config/opencode/agent-use-skills/awesome-skills/skills/playwright-skill ~/.config/opencode/skills/playwright-skill
```

### 3. 初始化环境

```bash
cd ~/.config/opencode/skills/playwright-skill
npm run setup
```

### 4. 重启 OpenCode

重启 OpenCode，并通过询问验证是否安装成功："do you have playwright-skill?"

## 更新

```bash
cd ~/.config/opencode/agent-use-skills
git pull
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues
