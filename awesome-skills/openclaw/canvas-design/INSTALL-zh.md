# 在 OpenClaw 中安装 Canvas Design

## 前置条件

- 已安装 [OpenClaw](https://github.com/nicepkg/openclaw)
- 已安装 Git

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 2. 创建符号链接

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/canvas-design
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/canvas-design ~/.openclaw/skills/canvas-design
```

### 3. 验证安装

重启 OpenClaw，然后尝试询问：

- "帮我设计一个视觉哲学并将其表达为海报"
- "do you have canvas-design skill?"

## 更新

```bash
cd ~/.openclaw/agent-use-skills
git pull
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues
