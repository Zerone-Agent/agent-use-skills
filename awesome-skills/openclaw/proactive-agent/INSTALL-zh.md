# 在 OpenClaw 中安装 Proactive Agent 技能

## 前置条件

- 已安装 [OpenClaw](https://github.com/nicepkg/openclaw)
- 已安装 Git

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

将技能库克隆到本地（如果尚未克隆）：

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.openclaw/agent-use-skills
```

### 2. 在 OpenClaw 中配置技能

创建符号链接，使 OpenClaw 能够调用该技能：

```bash
mkdir -p ~/.openclaw/skills
rm -rf ~/.openclaw/skills/proactive-agent
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/proactive-agent ~/.openclaw/skills/proactive-agent
```

### 3. 初始化工作空间资产

Proactive Agent 需要一些核心 Markdown 文件来维护内存和身份。执行以下脚本或手动拷贝：

```bash
# 拷贝模板资产到您的 OpenClaw 工作空间
cp -r ~/.openclaw/skills/proactive-agent/assets/*.md ~/.openclaw/workspace/
```

## 验证安装

重启 OpenClaw，它将检测到 `ONBOARDING.md` 并可能开始引导流程。您可以尝试提问：

- "开始引导流程 (Start onboarding)"
- "do you have proactive-agent skill?"

## 核心建议

为了发挥该技能的最佳效果，建议：
1. **遵循 WAL 协议**：当您对 Agent 做出更正时，确认它已更新 `SESSION-STATE.md`。
2. **定期清理缓冲区**：Agent 会自动管理 `working-buffer.md`，但在关键任务交接时可以手动查看该文件。

## 更新

```bash
cd ~/.openclaw/agent-use-skills && git pull
```

## 获取帮助

- 技能逻辑问题：https://github.com/Zerone-Agent/agent-use-skills/issues
- 参考指南：[Hal Stack 🦞](https://github.com/halthelobster/hal-stack)
