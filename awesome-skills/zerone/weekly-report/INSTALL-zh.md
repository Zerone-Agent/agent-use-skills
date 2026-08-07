# 在 Zerone 中安装 Weekly Report

## 前置条件

- 已安装 Zerone
- 已安装 Git
- 确保已安装 Python 和 pip

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.agents/agent-use-skills
```

### 2. 创建符号链接

创建符号链接，使 Zerone 能够发现 weekly-report 技能：

```bash
mkdir -p ~/.agents/skills
rm -rf ~/.agents/skills/weekly-report
ln -s ~/.agents/agent-use-skills/awesome-skills/skills/weekly-report ~/.agents/skills/weekly-report
```

### 3. 安装 Python 依赖

```bash
pip install python-docx markdown beautifulsoup4
```

### 4. 验证安装

重启 Zerone，尝试询问：
- "帮我生成这周的周报"
- "do you have weekly-report?"

如果安装成功，Zerone 会自动识别并调用 Weekly Report 技能工作流。

## 更新

```bash
cd ~/.agents/agent-use-skills
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.agents/skills/weekly-report
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues