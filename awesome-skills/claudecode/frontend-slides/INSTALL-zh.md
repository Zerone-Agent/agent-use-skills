# 在 Claude Code 中安装 Frontend Slides

## 前置条件

- 已安装 [Claude Code](https://claude.ai/code)
- 已安装 Git
- （PPT 转换功能需要）Python 3 及 `python-pptx` 库

## 安装步骤

### 方式一：直接克隆（推荐）

将 Frontend Slides 仓库直接克隆到 Claude Code 技能目录：

```bash
git clone https://github.com/zarazhangrui/frontend-slides.git ~/.claude/skills/frontend-slides
```

### 方式二：手动复制

```bash
# 创建技能目录
mkdir -p ~/.claude/skills/frontend-slides/scripts

# 克隆仓库到临时目录
git clone https://github.com/zarazhangrui/frontend-slides.git /tmp/frontend-slides

# 复制核心文件
cp /tmp/frontend-slides/SKILL.md ~/.claude/skills/frontend-slides/
cp /tmp/frontend-slides/STYLE_PRESETS.md ~/.claude/skills/frontend-slides/
cp /tmp/frontend-slides/viewport-base.css ~/.claude/skills/frontend-slides/
cp /tmp/frontend-slides/html-template.md ~/.claude/skills/frontend-slides/
cp /tmp/frontend-slides/animation-patterns.md ~/.claude/skills/frontend-slides/
cp /tmp/frontend-slides/scripts/extract-pptx.py ~/.claude/skills/frontend-slides/scripts/

# 清理临时目录
rm -rf /tmp/frontend-slides
```

### 安装 PPT 转换依赖（可选）

如果你需要将 PowerPoint 文件转换为网页演示，需要安装 `python-pptx`：

```bash
pip install python-pptx
```

## 验证安装

重启 Claude Code，然后通过以下方式验证安装是否成功：

```
/frontend-slides
```

或者直接尝试：

- "帮我创建一个关于 [主题] 的演示文稿"
- "把我的 presentation.pptx 转换为网页幻灯片"

如果安装成功，Claude Code 会自动识别并调用 Frontend Slides 技能工作流，引导你完成风格选择和演示文稿创建。

## 更新

```bash
cd ~/.claude/skills/frontend-slides
git pull
```

## 获取帮助

- 提交问题：https://github.com/zarazhangrui/frontend-slides/issues
