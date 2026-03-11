# 在 Qoder 中安装 Twitter Algorithm Optimizer

## 安装步骤

### 1. 克隆仓库
```bash
git clone https://github.com/Zerone-Agent/agent-use-skills.git ~/.qoder/agent-use-skills
```

### 2. 创建符号链接
```bash
mkdir -p ~/.qoder/skills
ln -s ~/.qoder/agent-use-skills/awesome-skills/skills/twitter-algorithm-optimizer ~/.qoder/skills/twitter-algorithm-optimizer
```

## 验证安装

重启 Qoder，尝试提问：
- "我的推文算法评分是多少？[内容]"

## 更新
```bash
cd ~/.qoder/agent-use-skills && git pull
```
