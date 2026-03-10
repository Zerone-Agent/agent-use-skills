# 为 OpenCode 安装 AgentUse Share

## 前置条件

- 已安装 [OpenCode.ai](https://opencode.ai)
- 已安装 Git

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.config/opencode/agent-use-skills
```

### 2. 创建符号链接

创建符号链接，使 OpenCode 的原生技能工具能够发现 agentuse-share 技能：

```bash
mkdir -p ~/.config/opencode/skills
rm -rf ~/.config/opencode/skills/agentuse-share
ln -s ~/.config/opencode/agent-use-skills/awesome-skills/skills/agentuse-share ~/.config/opencode/skills/agentuse-share
```

### 3. 重启 OpenCode

重启 OpenCode，插件将自动注入 agentuse-share 上下文。

通过询问以下问题来验证是否安装成功："do you have agentuse-share?"

## 更新

```bash
cd ~/.config/opencode/agent-use-skills
git pull
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues
