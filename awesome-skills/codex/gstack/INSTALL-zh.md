# 在 Codex 中安装 gstack

## 前置条件

- 已安装 [Codex CLI](https://openai.com/codex)
- 已安装 [Git](https://git-scm.com/)
- 已安装 [Bun](https://bun.sh/) v1.0+

## 安装步骤

### 1. 克隆并按 Codex host 运行 setup

```bash
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/gstack
cd ~/gstack && ./setup --host codex
```

setup 会把 gstack 技能分发到 `~/.codex/skills/gstack-*/`，并完成 Bun 编译、定制 Chromium 安装、MCP server 注册等。

### 2. 验证安装

在 Codex 会话中输入：

```
$office-hours
```

或：

```
/hosts
```

确认 host 为 codex 且技能已加载。

## 更新

```bash
cd ~/gstack && git pull && ./setup --host codex
```

## 卸载

```bash
~/gstack/bin/gstack-uninstall
```

或手动：

```bash
rm -rf ~/gstack ~/.gstack ~/.codex/skills/gstack-*
```

## 获取帮助

- 文档：https://github.com/garrytan/gstack/tree/main/docs
- 提交问题：https://github.com/garrytan/gstack/issues
