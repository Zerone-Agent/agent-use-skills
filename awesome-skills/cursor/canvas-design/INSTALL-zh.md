# 在 Cursor 中安装 Canvas Design

## 前置条件

- 已安装 [Cursor](https://cursor.com)
- 已安装 Git

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.cursor/agent-use-skills
```

### 2. 创建符号链接

创建符号链接，使 Cursor 能够发现 canvas-design 技能：

```bash
mkdir -p ~/.cursor/skills
rm -rf ~/.cursor/skills/canvas-design
ln -s ~/.cursor/agent-use-skills/awesome-skills/skills/canvas-design ~/.cursor/skills/canvas-design
```

### 3. 验证安装

重启 Cursor 并确保处于 **Agent** 模式，然后尝试询问：

- "帮我根据 [主题] 创作艺术作品"
- "do you have canvas-design skill?"

如果安装成功，Cursor Agent 会自动识别并调用 Canvas Design 技能。

## 更新

```bash
cd ~/.cursor/agent-use-skills
git pull
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues
