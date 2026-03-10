# 在 OpenClaw 中安装 Content Research Writer

## 前置条件

- 已安装 [OpenClaw](https://github.com/nicepkg/openclaw)
- 已安装 Git

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 2. 创建符号链接

创建符号链接，使 OpenClaw 能够发现 content-research-writer 技能：

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/content-research-writer
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/content-research-writer ~/.openclaw/skills/content-research-writer
```

### 3. 验证安装

重启 OpenClaw，然后尝试询问：

- "帮我创建一篇关于 [主题] 的文章大纲"
- "do you have content-research-writer?"

如果安装成功，OpenClaw 会自动识别并调用 Content Research Writer 技能工作流。

## 更新

```bash
cd ~/.openclaw/agent-use-skills
git pull
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues
