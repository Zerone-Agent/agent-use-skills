# 在 Claude Code 中安装 Impeccable

## 前置条件

- 已安装 [Claude Code](https://claude.ai/code)
- 已安装 [Node.js](https://nodejs.org)（建议 v18+，用于 `npx`）
- 当前项目根目录可写

## 安装步骤

### 1. 在项目根目录运行官方安装器

```bash
cd /path/to/your/project
npx impeccable install
```

安装器会自动检测 Claude Code 的 harness 目录，并询问：
- **安装范围**：当前项目（`--scope=project`）还是全局（`--scope=global`）
- **是否安装设计 hook**：默认 yes（写入 `.claude/settings.local.json`，对 UI 编辑实时检测反模式）

如需跳过交互、指定 Claude Code：

```bash
npx impeccable install --providers=claude --scope=project
```

### 2. 初始化项目设计上下文

在 Claude Code 中打开项目，运行：

```
/impeccable init
```

它会询问你的界面是 brand（营销/落地页/作品集）还是 product（应用/仪表盘/工具），然后写入 `PRODUCT.md` 和（可选）`DESIGN.md`，后续命令都会读取这些上下文。

### 3. 验证安装

在 Claude Code 中输入：

```
/impeccable
```

如果安装成功，会列出全部 23 个子命令。也可单独试：

```
/impeccable audit
```

## 更新

```bash
npx impeccable update
```

## 卸载

删除 Impeccable 写入的文件即可：

```bash
rm -rf .claude/skills/impeccable
rm -rf .impeccable
# 若之前选择全局安装：
rm -rf ~/.claude/skills/impeccable
```

并从 `.claude/settings.local.json` 中手动移除 impeccable 相关 hook 配置。

## 获取帮助

- 文档：https://impeccable.style
- 提交问题：https://github.com/pbakaus/impeccable/issues
