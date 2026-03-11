# 在 OpenClaw 中安装 Humanizer

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
rm -rf ~/.openclaw/skills/humanizer
ln -s ~/.openclaw/agent-use-skills/awesome-skills/skills/humanizer ~/.openclaw/skills/humanizer
```

## 验证安装

重启 OpenClaw，尝试提问：

- "帮我检查这段文案是否有 AI 生成的痕迹，并给出润色方案：[文案内容]"
- "do you have humanizer skill?"

## 使用建议

Humanizer 技能在处理以下场景时效果最佳：
- 博客文章和社交媒体帖子润色
- 避免 AI 摘要中出现常见的过度概括词汇
- 提升 Agent 自动回复的真实感与亲和力

## 更新

```bash
cd ~/.openclaw/agent-use-skills && git pull
```

## 获取帮助

- 技能逻辑问题：https://github.com/Zerone-Agent/agent-use-skills/issues
- 参考指南：[Wikipedia - Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
