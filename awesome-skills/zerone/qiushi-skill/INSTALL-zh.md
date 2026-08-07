# 在 Zerone 中安装求是 Skill

## 前置条件

- 已安装 Zerone
- 已安装 Git

## 安装步骤

### 1. 克隆 qiushi-skill 仓库

```bash
git clone https://github.com/HughYau/qiushi-skill.git ~/.agents/qiushi-skill
```

### 2. 创建符号链接

创建符号链接，使 Zerone 能够发现 qiushi-skill 技能：

```bash
mkdir -p ~/.agents/skills
for skill in arming-thought contradiction-analysis practice-cognition investigation-first mass-line criticism-self-criticism protracted-strategy concentrate-forces spark-prairie-fire overall-planning; do
  rm -rf ~/.agents/skills/$skill
  ln -s ~/.agents/qiushi-skill/skills/$skill ~/.agents/skills/$skill
done
```

### 3. 验证安装

重启 Zerone，尝试询问：
- "用实事求是的方法分析这个问题"
- "do you have qiushi-skill?"

如果安装成功，Zerone 会自动识别并调用求是 Skill 工作流。

## 更新

```bash
cd ~/.agents/qiushi-skill
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
for skill in arming-thought contradiction-analysis practice-cognition investigation-first mass-line criticism-self-criticism protracted-strategy concentrate-forces spark-prairie-fire overall-planning; do
  rm -rf ~/.agents/skills/$skill
done
```

## 获取帮助

- GitHub：https://github.com/HughYau/qiushi-skill