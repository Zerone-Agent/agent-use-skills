# 在 Qoder 中安装 Canvas Design

## 前置条件

- 已安装 [Qoder](https://qoder.ai)
- 已安装 Git

## 安装步骤

### 1. 克隆 agent-use-skills 仓库

```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.qoder/agent-use-skills
```

### 2. 创建符号链接

```bash
mkdir -p ~/.qoder/skills
rm -rf ~/.qoder/skills/canvas-design
ln -s ~/.qoder/agent-use-skills/awesome-skills/skills/canvas-design ~/.qoder/skills/canvas-design
```

### 3. 验证安装

重启 Qoder，然后尝试询问：

- "帮我创作一张具备博物馆品质的海报"
- "do you have canvas-design skill?"

## 更新

```bash
cd ~/.qoder/agent-use-skills
git pull
```

## 获取帮助

- 提交问题：https://github.com/Zerone-Agent/agent-use-skills/issues
