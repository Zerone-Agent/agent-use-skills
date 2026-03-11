# 在 OpenClaw 中安装 Self-Improving Agent

## 前置条件

- 已安装 [OpenClaw](https://github.com/nicepkg/openclaw)
- 已安装 Git

## 安装步骤

### 方法一：使用 ClawdHub（推荐）

在终端中执行以下命令：

```bash
clawdhub install self-improving-agent
```

### 方法二：手动安装

1. **克隆 agent-use-skills 仓库**（如果尚未克隆）

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

2. **创建符号链接**

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/self-improving-agent
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/self-improving-agent ~/.openclaw/skills/self-improving-agent
```

3. **创建学习日志文件**

```bash
mkdir -p ~/.openclaw/workspace/.learnings
```

## 验证安装

重启 OpenClaw，然后尝试询问：

- "帮我记录一个学习点"
- "do you have self-improvement skill?"

## 使用方法

### 启用自动钩子（可选）

如果您希望在会话开始或命令出错时自动触发提醒，可以启用钩子：

```bash
# 拷贝钩子到 OpenClaw 钩子目录
cp -r ~/.openclaw/skills/self-improving-agent/hooks/openclaw ~/.openclaw/hooks/self-improvement

# 启用钩子
openclaw hooks enable self-improvement
```

## 更新

```bash
cd ~/.openclaw/agent-use-skills && git pull
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues
