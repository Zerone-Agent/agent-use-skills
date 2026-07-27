# 在 Cursor 中安装 Taste Skill

## 前置条件

- 已安装 [Cursor](https://cursor.com)
- 已安装 Git

## 安装步骤

### 1. 克隆 taste-skill 仓库

```bash
git clone https://github.com/Leonxlnx/taste-skill.git ~/.cursor/taste-skill
```

### 2. 创建符号链接

将 13 个子技能目录链接到 Cursor 的技能目录：

```bash
mkdir -p ~/.cursor/skills
for skill in ~/.cursor/taste-skill/skills/*/; do
  skill_name=$(basename "$skill")
  rm -rf ~/.cursor/skills/$skill_name
  ln -s "$skill" ~/.cursor/skills/$skill_name
done
```

### 3. 验证安装

重启 Cursor 并切换到 **Agent** 模式，然后尝试询问：

- "do you have taste-skill?"
- "用 taste-skill 帮我设计一个极简风格的 landing page"

如果安装成功，Cursor Agent 会根据 brief 自动识别并调用对应的 taste-skill 子技能工作流。

## 更新

```bash
cd ~/.cursor/taste-skill
git pull
```

## 卸载

```bash
for skill in ~/.cursor/taste-skill/skills/*/; do
  rm -rf ~/.cursor/skills/$(basename "$skill")
done
```

## 获取帮助

- 提交问题：https://github.com/Leonxlnx/taste-skill/issues
