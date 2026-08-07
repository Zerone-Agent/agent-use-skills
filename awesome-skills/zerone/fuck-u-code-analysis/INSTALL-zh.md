# 在 Zerone 中安装 Fuck-U-Code Analysis

## 前置条件

- [Zerone](https://github.com/zerone/zerone) 已安装
- [Node.js](https://nodejs.org/) >= 18.0.0 已安装
- Git 已安装

## 安装步骤

### 1. 安装 fuck-u-code CLI

```bash
npm install -g eff-u-code
```

### 2. 克隆 fuck-u-code 仓库

```bash
git clone https://github.com/Zerone-Agent/fuck-u-code.git ~/.agents/fuck-u-code
```

### 3. 创建技能软链接

```bash
mkdir -p ~/.agents/skills
rm -rf ~/.agents/skills/fuck-u-code-analysis
ln -s ~/.agents/fuck-u-code/skills/fuck-u-code-analysis ~/.agents/skills/fuck-u-code-analysis
```

### 4. 验证安装

重启 Zerone，然后尝试提问：
- "请用 fuck-u-code 分析当前项目的代码质量"

如果安装成功，Zerone 将自动识别并调用该技能。

## 更新

```bash
cd ~/.agents/fuck-u-code
git pull
```

## 卸载

```bash
rm -rf ~/.agents/skills/fuck-u-code-analysis
```

## 获取帮助

- GitHub：https://github.com/Zerone-Agent/fuck-u-code
- 问题反馈：https://github.com/Zerone-Agent/fuck-u-code/issues
