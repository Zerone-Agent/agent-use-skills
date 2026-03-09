# UI UX Pro Max - Claude Code 安装指南

## 安装步骤

### 方法一：使用 Claude Marketplace（推荐）

在 Claude Code 中执行以下两条命令：

```
/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill
/plugin install ui-ux-pro-max@ui-ux-pro-max-skill
```

### 方法二：使用 CLI 工具

1. **安装 CLI 工具**

```bash
npm install -g uipro-cli
```

2. **初始化项目**

```bash
cd /path/to/your/project
uipro init --ai claude
```

## 验证安装

安装完成后，在 Claude Code 中尝试以下对话：

```
Build a landing page for my SaaS product
```

如果技能正确加载，AI 将自动生成设计系统并开始实现 UI。

## 使用方法

### 技能模式（自动激活）

直接在对话中描述 UI/UX 任务，技能将自动激活：

```
为我的美容水疗中心构建落地页
创建一个暗黑模式的仪表板
设计一个电商移动应用界面
```

### 高级用法：持久化设计系统

生成并保存设计系统到文件：

```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "SaaS dashboard" --design-system --persist -p "MyApp"
```

这将创建 `design-system/` 文件夹结构：
- `MASTER.md` - 全局设计系统（颜色、字体、间距、组件）
- `pages/` - 页面特定的覆盖规则

## 更新方法

```bash
npm update -g uipro-cli
uipro init --ai claude
```

## 详细文档

- [GitHub 仓库](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
- [官方网站](https://uupm.cc)
