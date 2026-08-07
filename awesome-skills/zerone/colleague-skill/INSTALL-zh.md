# 在 Zerone 中安装 Colleague Skill

## 前置条件

- 已安装 Zerone
- 已安装 Git

## 安装步骤

### 1. 克隆 colleague-skill 仓库

```bash
git clone https://github.com/titanwings/colleague-skill.git ~/.agents/colleague-skill
```

### 2. 创建符号链接

创建符号链接，使 Zerone 能够发现 colleague-skill 技能：

```bash
mkdir -p ~/.agents/skills
rm -rf ~/.agents/skills/colleague-skill
ln -s ~/.agents/colleague-skill/skills/colleague-skill ~/.agents/skills/colleague-skill
```

### 3. 验证安装

重启 Zerone，尝试询问：
- "帮我创建一个同事数字人"
- "do you have colleague-skill?"

如果安装成功，Zerone 会自动识别并调用 Colleague Skill 工作流。

## 更新

```bash
cd ~/.agents/colleague-skill
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.agents/skills/colleague-skill
```

## 获取帮助

- GitHub：https://github.com/titanwings/colleague-skill