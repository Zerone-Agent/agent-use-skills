# 在 Codex 中安装毛选产品决策 Agent

## 前置条件

- [Codex](https://github.com/openai/codex) 已安装
- Node.js 与 npm 已安装

## 安装步骤

### 1. 安装 Skill

```bash
npx skills add atdy/maoxuan-product-agent \
  --skill product-decision-agent \
  --agent codex \
  -g -y
```

### 2. 验证安装

重启 Codex，然后尝试：

```text
使用 $product-decision-agent 帮我判断：A/B Test 点击率涨了 12%，但订单没涨，要不要全量？
```

如果安装成功，Codex 会用简体中文定位当前核心阻塞，并给出明确的下一步行动。

## 更新

重新运行安装命令即可获取最新版本。

## 卸载

```bash
rm -rf ~/.agents/skills/product-decision-agent
```

## 获取帮助

- GitHub: https://github.com/atdy/maoxuan-product-agent
- 提交问题: https://github.com/atdy/maoxuan-product-agent/issues
