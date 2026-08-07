# 在 Zerone 中安装 Content Research Writer

## 前置条件

- 已安装 Zerone
- 已安装 Git

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.agents/agent-use-skills
```

### 2. 创建符号链接

创建符号链接，使 Zerone 能够发现 content-research-writer 技能：

```bash
mkdir -p ~/.agents/skills
rm -rf ~/.agents/skills/content-research-writer
ln -s ~/.agents/agent-use-skills/awesome-skills/skills/content-research-writer ~/.agents/skills/content-research-writer
```

### 3. 验证安装

重启 Zerone，尝试询问：
- "帮我写一篇关于 AI 发展的博客文章"
- "do you have content-research-writer?"

如果安装成功，Zerone 会自动识别并调用 Content Research Writer 技能工作流。

## 更新

```bash
cd ~/.agents/agent-use-skills
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.agents/skills/content-research-writer
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues