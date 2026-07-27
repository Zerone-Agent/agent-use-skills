# 在 Claude Code 中安装 Matt Pocock Skills

## 前置条件

- 已安装 [Claude Code](https://claude.ai/code)
- 已安装 Git

## 安装步骤

### 1. 克隆 mattpocock-skills 仓库

```bash
git clone https://github.com/mattpocock/skills.git ~/.claude/mattpocock-skills
```

### 2. 创建符号链接

把 `engineering/` 与 `productivity/` 两个分类下的全部技能目录链接到 Claude Code 的技能目录：

```bash
mkdir -p ~/.claude/skills
for category in engineering productivity; do
  for skill in ~/.claude/mattpocock-skills/skills/$category/*/; do
    skill_name=$(basename "$skill")
    rm -rf ~/.claude/skills/$skill_name
    ln -s "$skill" ~/.claude/skills/$skill_name
  done
done
```

### 3. 在每个仓库内运行一次性配置

在 Claude Code 中打开你的项目目录，运行：

```
/setup-matt-pocock-skills
```

它会询问：
- **Issue tracker**：GitHub / Linear / 本地 markdown
- **Triage 标签**：你给 issue 打哪些标签
- **文档位置**：生成的文档放到哪里

### 4. 验证安装

输入：

```
/ask-matt
```

应列出全部用户调用技能，并按当前情境推荐合适的入口。也可单独试：

```
/grill-me
```

## 更新

```bash
cd ~/.claude/mattpocock-skills
git pull
```

## 卸载

```bash
for category in engineering productivity; do
  for skill in ~/.claude/mattpocock-skills/skills/$category/*/; do
    rm -rf ~/.claude/skills/$(basename "$skill")
  done
done
```

## 获取帮助

- 提交问题：https://github.com/mattpocock/skills/issues
