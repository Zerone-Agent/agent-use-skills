# 在 Claude Code 中安装 Taste Skill

## 前置条件

- 已安装 [Claude Code](https://claude.ai/code)
- 已安装 Git

## 安装步骤

### 1. 克隆 taste-skill 仓库

```bash
git clone https://github.com/Leonxlnx/taste-skill.git ~/.claude/taste-skill
```

### 2. 创建符号链接

将 13 个子技能目录链接到 Claude Code 的技能目录：

```bash
mkdir -p ~/.claude/skills
for skill in ~/.claude/taste-skill/skills/*/; do
  skill_name=$(basename "$skill")
  rm -rf ~/.claude/skills/$skill_name
  ln -s "$skill" ~/.claude/skills/$skill_name
done
```

### 3. 验证安装

重启 Claude Code，然后尝试询问：

- "do you have taste-skill?"
- "用 taste-skill 帮我设计一个极简风格的 landing page"

如果安装成功，Claude Code 会根据 brief 自动识别并调用对应的 taste-skill 子技能工作流。

## 更新

```bash
cd ~/.claude/taste-skill
git pull
```

## 卸载

```bash
for skill in ~/.claude/taste-skill/skills/*/; do
  rm -rf ~/.claude/skills/$(basename "$skill")
done
```

## 获取帮助

- 提交问题：https://github.com/Leonxlnx/taste-skill/issues
