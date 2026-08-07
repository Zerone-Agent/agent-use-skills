# 在 Zerone 中安装人味儿写作

## 前置条件

- [Zerone](https://www.zerone.run/) 已安装
- Git 已安装

## 安装步骤

### 1. 克隆 renwei-writing 仓库

```bash
git clone https://github.com/orange2ai/renwei-writing.git ~/.agents/skills/renwei-writing
```

### 2. 验证安装

重启 Zerone，然后尝试询问：
- “你会用人味儿写作吗？”
- “帮我润色这段文字”

如果安装成功，Zerone 会自动识别并调用人味儿写作技能。

## 更新

```bash
cd ~/.agents/skills/renwei-writing
git pull
```

## 卸载

```bash
rm -rf ~/.agents/skills/renwei-writing
```

## 获取帮助

- GitHub: https://github.com/orange2ai/renwei-writing
- 提交问题: https://github.com/orange2ai/renwei-writing/issues
