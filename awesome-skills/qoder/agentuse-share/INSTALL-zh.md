# 在 Qoder 中安装 AgentUse Share

## 前置条件

- 已安装 [Qoder](https://qoder.ai)
- 已安装 Git

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.qoder/agent-use-skills
```

### 2. 创建符号链接

创建符号链接，使 Qoder 能够发现 agentuse-share 技能：

```bash
mkdir -p ~/.qoder/skills
rm -rf ~/.qoder/skills/agentuse-share
ln -s ~/.qoder/agent-use-skills/awesome-skills/skills/agentuse-share ~/.qoder/skills/agentuse-share
```

### 3. 验证安装

重启 Qoder，然后尝试询问：

- "使用 agentuse-share 技能为一个新技能写文档"
- "do you have agentuse-share skill?"

如果安装成功，Qoder 会自动识别并调用 AgentUse Share 技能工作流。

## 更新

```bash
cd ~/.qoder/agent-use-skills
git pull
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues
