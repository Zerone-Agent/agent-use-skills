# 在 OpenCode 中安装 Impeccable

## 前置条件

- 已安装 [OpenCode](https://opencode.ai)
- 已安装 [Node.js](https://nodejs.org)（建议 v18+，用于 `npx`）
- 当前项目根目录可写

## 安装步骤

### 1. 在项目根目录运行官方安装器

```bash
cd /path/to/your/project
npx impeccable install
```

指定 OpenCode 与范围：

```bash
npx impeccable install --providers=opencode --scope=project
```

OpenCode 的技能目录为 `.opencode/skills/`（项目）或 `~/.config/opencode/skills/`（全局）。

### 2. 初始化项目设计上下文

在 OpenCode 中打开项目，运行：

```
/impeccable init
```

它会询问界面是 brand 还是 product，然后写入 `PRODUCT.md` 和（可选）`DESIGN.md`，后续命令都会读取这些上下文。

### 3. 验证安装

在 OpenCode 中输入：

```
/impeccable
```

应列出全部 23 个子命令。也可单独试：

```
/impeccable audit
```

## 更新

```bash
npx impeccable update
```

## 卸载

```bash
rm -rf .opencode/skills/impeccable
rm -rf .impeccable
# 若之前选择全局安装：
rm -rf ~/.config/opencode/skills/impeccable
```

## 获取帮助

- 文档：https://impeccable.style
- 提交问题：https://github.com/pbakaus/impeccable/issues
