# Huashu Design - Zerone 安装指南

## 前置条件

- Zerone 已安装
- Git 已安装

## 安装步骤

### 1. 克隆仓库

```bash
git clone https://github.com/alchaincyf/huashu-design.git ~/.agents/huashu-design
```

### 2. 创建符号链接

```bash
mkdir -p ~/.agents/skills
ln -sf ~/.agents/huashu-design ~/.agents/skills/huashu-design
```

### 3. 验证安装

重启 Zerone，然后尝试以下对话：

```
帮我对这个设计做一个 5 维度评审
```

如果技能正确加载，AI 将自动识别并调用 Huashu Design 的工作流。

## 更新方法

```bash
cd ~/.agents/huashu-design && git pull
```

## 卸载

```bash
rm ~/.agents/skills/huashu-design
```

## 获取帮助

- GitHub 仓库：https://github.com/alchaincyf/huashu-design
- 问题反馈：https://github.com/alchaincyf/huashu-design/issues
