# 在 Qoder 中安装 Skill Market

## 前置条件

- 已安装 Qoder
- 已安装 Git
- 确保已安装 Python（推荐使用 `uv`，但非必须）

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.qoder/agent-use-skills
```

### 2. 创建符号链接

创建符号链接，使 Qoder 能够发现 skill-market 技能：

```bash
mkdir -p ~/.qoder/skills
rm -rf ~/.qoder/skills/skill-market
ln -s ~/.qoder/agent-use-skills/awesome-skills/skills/skill-market ~/.qoder/skills/skill-market
```

### 3. 验证安装

执行以下命令或重启 Qoder 后询问以验证是否安装成功：

```bash
~/.qoder/agent-use-skills/awesome-skills/skills/skill-market/scripts/market.py list
```

或者在 Qoder 中尝试询问：
- "列出 skill market 上的所有可用技能"
- "do you have skill-market?"

如果安装成功，Qoder 会自动识别并调用 Skill Market 技能工作流。

## 更新

```bash
cd ~/.qoder/agent-use-skills
git pull
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues
