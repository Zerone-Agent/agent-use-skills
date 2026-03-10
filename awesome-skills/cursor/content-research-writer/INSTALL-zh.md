# 在 Cursor 中安装 Content Research Writer

## 前置条件

- 已安装 [Cursor](https://cursor.com)
- 已安装 Git

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.cursor/agent-use-skills
```

### 2. 创建符号链接

创建符号链接，使 Cursor 能够发现 content-research-writer 技能：

```bash
mkdir -p ~/.cursor/skills
rm -rf ~/.cursor/skills/content-research-writer
ln -s ~/.cursor/agent-use-skills/awesome-skills/skills/content-research-writer ~/.cursor/skills/content-research-writer
```

### 3. 验证安装

重启 Cursor 并确保处于 **Agent** 模式，然后尝试询问：

- "帮我创建一篇关于 [主题] 的文章大纲"
- "do you have content-research-writer?"

如果安装成功，Cursor Agent 会自动识别并调用 Content Research Writer 技能工作流。

## 更新

```bash
cd ~/.cursor/agent-use-skills
git pull
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues
