# 在 Codex 中安装 Taste Skill

## 前置条件

- 已安装 [Codex](https://openai.com/index/codex/)
- 已安装 Git

## 安装步骤

### 1. 克隆 taste-skill 仓库

```bash
git clone https://github.com/Leonxlnx/taste-skill.git ~/.codex/taste-skill
```

### 2. 创建符号链接

将 13 个子技能目录链接到 Codex 的技能目录：

```bash
mkdir -p ~/.codex/skills
for skill in ~/.codex/taste-skill/skills/*/; do
  skill_name=$(basename "$skill")
  rm -rf ~/.codex/skills/$skill_name
  ln -s "$skill" ~/.codex/skills/$skill_name
done
```

### 3. 验证安装

重启 Codex，然后尝试询问：

- "do you have taste-skill?"
- "用 taste-skill 帮我设计一个 brutalist 风格的 portfolio"

如果安装成功，Codex 会根据 brief 自动识别并调用对应的 taste-skill 子技能工作流（特别是 `gpt-taste`，它是面向 GPT/Codex 的更严格变体）。

## 更新

```bash
cd ~/.codex/taste-skill
git pull
```

## 卸载

```bash
for skill in ~/.codex/taste-skill/skills/*/; do
  rm -rf ~/.codex/skills/$(basename "$skill")
done
```

## 获取帮助

- 提交问题：https://github.com/Leonxlnx/taste-skill/issues
