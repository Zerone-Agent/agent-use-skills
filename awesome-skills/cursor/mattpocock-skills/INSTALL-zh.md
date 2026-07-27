# 在 Cursor 中安装 Matt Pocock Skills

## 前置条件

- 已安装 [Cursor](https://cursor.com)
- 已安装 Git

## 安装步骤

### 1. 克隆 mattpocock-skills 仓库

```bash
git clone https://github.com/mattpocock/skills.git ~/.cursor/mattpocock-skills
```

### 2. 创建符号链接

把 `engineering/` 与 `productivity/` 两个分类下的全部技能目录链接到 Cursor 的技能目录：

```bash
mkdir -p ~/.cursor/skills
for category in engineering productivity; do
  for skill in ~/.cursor/mattpocock-skills/skills/$category/*/; do
    skill_name=$(basename "$skill")
    rm -rf ~/.cursor/skills/$skill_name
    ln -s "$skill" ~/.cursor/skills/$skill_name
  done
done
```

### 3. 在每个仓库内运行一次性配置

在 Cursor Agent 模式中打开你的项目目录，运行：

```
/setup-matt-pocock-skills
```

它会询问 issue tracker、triage 标签、文档位置等配置。

### 4. 验证安装

输入：

```
/ask-matt
```

应列出全部用户调用技能。

## 更新

```bash
cd ~/.cursor/mattpocock-skills
git pull
```

## 卸载

```bash
for category in engineering productivity; do
  for skill in ~/.cursor/mattpocock-skills/skills/$category/*/; do
    rm -rf ~/.cursor/skills/$(basename "$skill")
  done
done
```

## 获取帮助

- 提交问题：https://github.com/mattpocock/skills/issues
