# 在 Cursor 中安装 Superpowers

要在 Cursor 的 Agent 模式下启用 Superpowers 技能框架，请按照以下简单步骤操作：

## 1. 使用插件添加命令
打开 Cursor 的 **Agent Chat**（确保处于 Agent 模式），然后直接输入以下命令：

```text
/plugin-add superpowers
```

## 2. 验证安装
安装完成后，你可以通过输入以下任何提示词来测试 Superpowers 是否已激活：

- "help me plan this feature"（触发 `brainstorming` 技能）
- "let's debug this issue"（触发 `systematic-debugging` 技能）

如果安装成功，Cursor Agent 会自动识别并根据 Superpowers 的技能规范开始执行任务。

## 3. 注意事项
- 确保你使用的是 Cursor 的最新版本，并且已开启 **Agent** 模式。
- Superpowers 技能是自动触发的，一旦安装完成，它们将作为 Agent 的扩展能力存在。

---
更多详情请参考：[Superpowers GitHub 仓库](https://github.com/obra/superpowers)
