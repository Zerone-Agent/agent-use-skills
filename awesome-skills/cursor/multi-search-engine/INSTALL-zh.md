# 在 Cursor 中安装 Multi Search Engine

## 前置条件

- 已安装 [Cursor](https://cursor.com)
- 已安装 Git

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.cursor/agent-use-skills
```

### 2. 创建符号链接

创建符号链接，使 Cursor 能够发现 multi-search-engine 技能：

```bash
mkdir -p ~/.cursor/skills
rm -rf ~/.cursor/skills/multi-search-engine
ln -s ~/.cursor/agent-use-skills/awesome-skills/skills/multi-search-engine ~/.cursor/skills/multi-search-engine
```

### 3. 验证安装

重启 Cursor 并在 **Agent** 模式尝试以下命令验证安装：

- "使用 google 搜索关于 python 的教程"
- "do you have the multi-search-engine skill?"

如果成功，Cursor Agent 会自动识别并调用 Multi Search Engine 技能。

## 更新

```bash
cd ~/.cursor/agent-use-skills
git pull
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues
