# 在 Claude Code 中安装毛选产品决策 Agent

## 前置条件

- [Claude Code](https://claude.ai/code) 已安装
- Node.js 与 npm 已安装

## 安装步骤

### 1. 安装 Skill

```bash
npx skills add atdy/maoxuan-product-agent \
  --skill product-decision-agent \
  --agent claude-code \
  -g -y
```

### 2. 验证安装

重启 Claude Code，然后尝试：

```text
/product-decision-agent 我们有 20 个需求抢两个研发，下一版该怎么排？
```

如果安装成功，Claude Code 会用简体中文定位当前核心阻塞，并给出明确的下一步行动。

## 更新

重新运行安装命令即可获取最新版本。

## 卸载

```bash
rm -rf ~/.claude/skills/product-decision-agent
```

## 获取帮助

- GitHub: https://github.com/atdy/maoxuan-product-agent
- 提交问题: https://github.com/atdy/maoxuan-product-agent/issues
