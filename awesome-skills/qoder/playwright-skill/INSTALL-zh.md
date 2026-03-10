# 在 Qoder 中安装 Playwright Skill

## 前置条件

- 已安装 [Qoder](https://qoder.ai)
- 已安装 Git
- 已安装 Node.js

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.qoder/agent-use-skills
```

### 2. 创建符号链接

```bash
mkdir -p ~/.qoder/skills
rm -rf ~/.qoder/skills/playwright-skill
ln -s ~/.qoder/agent-use-skills/awesome-skills/skills/playwright-skill ~/.qoder/skills/playwright-skill
```

### 3. 初始化环境

```bash
cd ~/.qoder/skills/playwright-skill
npm run setup
```

### 4. 验证安装

重启 Qoder，然后尝试询问：

- "帮我截一张 http://localhost:3000 的全屏图"
- "do you have playwright-skill?"

## 更新

```bash
cd ~/.qoder/agent-use-skills
git pull
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues
