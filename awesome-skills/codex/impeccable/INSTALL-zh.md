# 在 Codex 中安装 Impeccable

## 前置条件

- 已安装 [Codex CLI](https://openai.com/codex)
- 已安装 [Node.js](https://nodejs.org)（建议 v18+，用于 `npx`）
- 当前项目根目录可写

## 安装步骤

### 1. 在项目根目录运行官方安装器

```bash
cd /path/to/your/project
npx impeccable install
```

指定 Codex 与范围：

```bash
npx impeccable install --providers=codex --scope=project
```

安装会写入：
- `.agents/skills/impeccable/`（Codex 自动发现的技能目录，含子 agent）
- `.codex/hooks.json`（项目级 hook 配置）

### 2. 信任项目 hook（Codex 必须）

Codex 按 hook 定义跟踪信任。打开 `/hooks`，根据提示批准 impeccable hook。

如需批量信任整个项目目录，使用 `/hooks-trust` 或重启 Codex 时加 `--trust`。

### 3. 初始化项目设计上下文

在 Codex 会话中运行：

```
$impeccable init
```

（注：Codex 用 skills 而非 `/prompts:`，输入 `$impeccable` 或打开 `/skills` 可见。）

### 4. 验证安装

打开 `/skills` 或输入 `$impeccable`，应列出全部 23 个子命令。

## 更新

```bash
npx impeccable update
# 若 .codex/hooks.json 有变化，需再次打开 /hooks 批准
```

## 卸载

```bash
rm -rf .agents/skills/impeccable
rm -rf .codex/hooks.json   # 仅当该文件只有 impeccable 配置时
rm -rf .impeccable
```

## 获取帮助

- 文档：https://impeccable.style
- 提交问题：https://github.com/pbakaus/impeccable/issues
