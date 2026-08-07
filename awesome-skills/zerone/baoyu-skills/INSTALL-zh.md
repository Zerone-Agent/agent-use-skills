# 为 Zerone 安装 Baoyu Skills

## 前提条件

- 已安装 Zerone
- 已安装 Git

## 安装步骤

### 1. 克隆 Baoyu Skills 仓库

```bash
git clone https://github.com/JimLiu/baoyu-skills.git ~/.agents/baoyu-skills
```

### 2. 创建符号链接

创建符号链接，使 Zerone 能够发现 Baoyu 技能：

```bash
mkdir -p ~/.agents/skills
for skill in $(ls ~/.agents/baoyu-skills/skills); do
  rm -rf ~/.agents/skills/$skill
  ln -s ~/.agents/baoyu-skills/skills/$skill ~/.agents/skills/$skill
done
```

### 3. 验证安装

重启 Zerone 后，尝试询问：

- "do you have baoyu-imagine?"

如果安装成功，Zerone 将自动识别并调用相应的 Baoyu 技能。

## 更新

```bash
cd ~/.agents/baoyu-skills
git pull
```

## 卸载

```bash
for skill in $(ls ~/.agents/baoyu-skills/skills); do
  rm -rf ~/.agents/skills/$skill
done
```

## 获取帮助

- GitHub: https://github.com/JimLiu/baoyu-skills
- 提交问题: https://github.com/JimLiu/baoyu-skills/issues