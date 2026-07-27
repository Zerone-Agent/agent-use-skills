# 在 Cursor 中安装 Impeccable

## 前置条件

- 已安装 [Cursor](https://cursor.com)
- 已安装 [Node.js](https://nodejs.org)（建议 v18+，用于 `npx`）
- Cursor 已启用 Agent Skills：Settings → Rules → Agent Skills（Nightly 频道）

## 安装步骤

### 1. 在项目根目录运行官方安装器

```bash
cd /path/to/your/project
npx impeccable install
```

安装器会自动检测 Cursor 的 harness 目录（项目本地 `.cursor/` 或全局 `~/.cursor/`），并询问安装范围与是否启用 hook。

指定 Cursor 与范围：

```bash
npx impeccable install --providers=cursor --scope=project
```

### 2. 启用 Agent Skills（首次需手动）

打开 Cursor → Settings → Beta → 切到 Nightly；再 Settings → Rules → 勾选 **Agent Skills**。

### 3. 初始化项目设计上下文

在 Cursor Agent 模式中运行：

```
/impeccable init
```

### 4. 验证安装

输入 `/impeccable`，应列出 23 个子命令。也可试：

```
/impeccable audit
```

## 更新

```bash
npx impeccable update
```

## 卸载

```bash
rm -rf .cursor/skills/impeccable
rm -rf .impeccable
```

并从 `.cursor/hooks.json` 中移除 impeccable 相关 hook 配置。

## 获取帮助

- 文档：https://impeccable.style
- 提交问题：https://github.com/pbakaus/impeccable/issues
