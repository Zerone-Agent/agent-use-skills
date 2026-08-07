# 在 Zerone 中安装 Self-Improving Agent

## 前置条件

- 已安装 Zerone
- 已安装 Git

## 安装步骤

### 1. 克隆 self-improving-agent 仓库

```bash
git clone https://github.com/peterskoett/self-improving-agent.git ~/.agents/self-improving-agent
```

### 2. 创建符号链接

创建符号链接，使 Zerone 能够发现 self-improving-agent 技能：

```bash
mkdir -p ~/.agents/skills
rm -rf ~/.agents/skills/self-improving-agent
ln -s ~/.agents/self-improving-agent/skills/self-improving-agent ~/.agents/skills/self-improving-agent
```

### 3. 验证安装

重启 Zerone，尝试询问：
- "帮我记录这次学习的经验"
- "do you have self-improving-agent?"

如果安装成功，Zerone 会自动识别并调用 Self-Improving Agent 技能工作流。

## 更新

```bash
cd ~/.agents/self-improving-agent
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.agents/skills/self-improving-agent
```

## 获取帮助

- GitHub：https://github.com/peterskoett/self-improving-agent