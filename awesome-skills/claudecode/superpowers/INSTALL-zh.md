# 在 Claude Code 中安装 Superpowers

要在 Claude Code 环境中安装并启用 Superpowers 技能框架，请按照以下步骤操作：

## 1. 注册插件市场
首先，你需要将 Superpowers 的 marketplace 添加到你的 Claude Code 中。在 Claude Code 的对话界面输入：

```bash
/plugin marketplace add obra/superpowers-marketplace
```

## 2. 安装 Superpowers 插件
注册好市场后，运行以下命令完成插件安装：

```bash
/plugin install superpowers@superpowers-marketplace
```

## 3. 验证安装
安装完成后，你可以通过开启一个新会话并尝试触发某个技能来验证是否成功。例如，你可以尝试输入：

- "帮我规划一个新功能" (triggering `brainstorming`)
- "让我们调试一下这个错误" (triggering `systematic-debugging`)

如果安装成功，Claude 会自动识别并调用相关的 Superpowers 技能工作流。

## 4. 后续更新
如果需要更新插件到最新版本，可以使用：

```bash
/plugin update superpowers
```

---
更多详情请参考：[Superpowers GitHub 仓库](https://github.com/obra/superpowers)
