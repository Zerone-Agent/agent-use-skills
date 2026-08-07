# 在 Zerone 中安装 Anti-Distill

## 前置条件

- 已安装 Zerone
- 已安装 Git

## 安装步骤

### 1. 克隆 anti-distill 仓库

```bash
git clone https://github.com/leilei926524-tech/anti-distill.git ~/.agents/anti-distill
```

### 2. 创建符号链接

创建符号链接，使 Zerone 能够发现 anti-distill 技能：

```bash
mkdir -p ~/.agents/skills
rm -rf ~/.agents/skills/anti-distill
ln -s ~/.agents/anti-distill/skills/anti-distill ~/.agents/skills/anti-distill
```

### 3. 验证安装

重启 Zerone，尝试询问：
- "帮我清洗这个 Skill 文件"
- "do you have anti-distill?"

如果安装成功，Zerone 会自动识别并调用 Anti-Distill 技能工作流。

## 更新

```bash
cd ~/.agents/anti-distill
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.agents/skills/anti-distill
```

## 获取帮助

- GitHub：https://github.com/leilei926524-tech/anti-distill