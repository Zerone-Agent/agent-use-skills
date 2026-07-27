# 在 Qoder 中安装 Impeccable

## 前置条件

- 已安装 [Qoder](https://qoder.com)
- 已安装 [Node.js](https://nodejs.org)（建议 v18+，用于 `npx`）
- 当前项目根目录可写

## 安装步骤

### 1. 在项目根目录运行官方安装器

```bash
cd /path/to/your/project
npx impeccable install
```

指定 Qoder 与范围：

```bash
npx impeccable install --providers=qoder --scope=project
```

Qoder 的技能目录为 `.qoder/skills/`（项目）或 `~/.qoder/skills/`（全局）。

### 2. 初始化项目设计上下文

在 Qoder 中打开项目，运行：

```
/impeccable init
```

它会询问界面是 brand 还是 product，然后写入 `PRODUCT.md` 和（可选）`DESIGN.md`。

### 3. 验证安装

输入：

```
/impeccable
```

应列出全部 23 个子命令。也可试：

```
/impeccable critique landing
```

## 更新

```bash
npx impeccable update
```

## 卸载

```bash
rm -rf .qoder/skills/impeccable
rm -rf .impeccable
# 若之前选择全局安装：
rm -rf ~/.qoder/skills/impeccable
```

## 获取帮助

- 文档：https://impeccable.style
- 提交问题：https://github.com/pbakaus/impeccable/issues
