# 在 Codex 中安装 Playwright Skill

## 前置条件

- 已安装 [Codex](https://openai.com/index/codex/)
- 已安装 Git
- 已安装 Node.js

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.codex/agent-use-skills
```

### 2. 创建符号链接

创建符号链接，使 Codex 能够发现 playwright-skill 技能：

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/playwright-skill
ln -s ~/.codex/agent-use-skills/awesome-skills/skills/playwright-skill ~/.codex/skills/playwright-skill
```

### 3. 初始化环境

```bash
cd ~/.codex/skills/playwright-skill
npm run setup
```

### 4. 验证安装

重启 Codex，然后尝试询问：

- "帮我截一张 http://localhost:3000 的全屏图"
- "do you have playwright-skill?"

如果安装成功，Codex 会自动识别并调用 Playwright Skill 技能工作流。

## 更新

```bash
cd ~/.codex/agent-use-skills
git pull
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues
