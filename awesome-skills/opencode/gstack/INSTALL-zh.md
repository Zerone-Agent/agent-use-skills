# 在 OpenCode 中安装 gstack

## 前置条件

- 已安装 [OpenCode](https://opencode.ai)
- 已安装 [Git](https://git-scm.com/)
- 已安装 [Bun](https://bun.sh/) v1.0+

## 安装步骤

### 1. 克隆并按 OpenCode host 运行 setup

```bash
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/gstack
cd ~/gstack && ./setup --host opencode
```

setup 会把 gstack 技能分发到 `~/.config/opencode/skills/gstack-*/`，并完成 Bun 编译、定制 Chromium 安装、MCP server 注册等。

### 2. 验证安装

在 OpenCode 中输入：

```
/office-hours
```

应触发 YC 风格的 6 个产品盘问。也可先跑：

```
/hosts
```

确认 host 为 opencode 且技能已加载。

## 更新

```bash
cd ~/gstack && git pull && ./setup --host opencode
```

## 卸载

```bash
~/gstack/bin/gstack-uninstall
```

或手动：

```bash
rm -rf ~/gstack ~/.gstack ~/.config/opencode/skills/gstack-*
```

## 获取帮助

- 文档：https://github.com/garrytan/gstack/tree/main/docs
- 提交问题：https://github.com/garrytan/gstack/issues
