# 在 Codex 中安装 Canvas Design

## 前置条件

- 已安装 [Codex](https://openai.com/index/codex/)
- 已安装 Git

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.codex/agent-use-skills
```

### 2. 创建符号链接

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/canvas-design
ln -s ~/.codex/agent-use-skills/awesome-skills/skills/canvas-design ~/.codex/skills/canvas-design
```

### 3. 验证安装

重启 Codex，然后尝试询问：

- "帮我设计一张极简主义的海报"
- "do you have canvas-design skill?"

## 更新

```bash
cd ~/.codex/agent-use-skills
git pull
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues
