# 在 Codex 中安装装修避坑技能集

## 前置条件

- 已安装 [Codex](https://github.com/codex)
- 已安装 Git

## 安装步骤

### 1. 克隆仓库

```bash
git clone https://github.com/zx029w/zhuangxiu-skills.git ~/.codex/zhuangxiu-skills
```

### 2. 创建符号链接

将 11 个装修技能子目录链接到 Codex 的 skills 目录：

```bash
mkdir -p ~/.codex/skills
for skill in quanwu-dingzhi-bucailei laofang-gaizao-bucailei zhuangxiu-hetong-shenhe zhuangxiu-baojia-shenhe zhuangxiu-fangan-zhenduan zhuangxiu-huanbao-bikeng zhuangxiu-liucheng-bucai zhuangxiu-fanche-jijiu zhuangxiu-bikeng-wenda zhuangxiu-zengxiang-bilei zhuangxiu-gongsi-bilei; do
  rm -rf ~/.codex/skills/$skill
  ln -s ~/.codex/zhuangxiu-skills/$skill ~/.codex/skills/$skill
done
```

### 3. 验证安装

重启 Codex，然后尝试询问以下问题来验证是否安装成功：

- "帮我审核这份装修合同"（触发 `zhuangxiu-hetong-shenhe`）
- "看一下这个装修报价有没有坑"（触发 `zhuangxiu-baojia-shenhe`）
- "do you have 装修避坑 skills?"

如果安装成功，Codex 会自动识别并调用相关的装修避坑技能工作流。

## 更新

```bash
cd ~/.codex/zhuangxiu-skills
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
for skill in quanwu-dingzhi-bucailei laofang-gaizao-bucailei zhuangxiu-hetong-shenhe zhuangxiu-baojia-shenhe zhuangxiu-fangan-zhenduan zhuangxiu-huanbao-bikeng zhuangxiu-liucheng-bucai zhuangxiu-fanche-jijiu zhuangxiu-bikeng-wenda zhuangxiu-zengxiang-bilei zhuangxiu-gongsi-bilei; do
  rm -rf ~/.codex/skills/$skill
done
```

## 获取帮助

- GitHub: https://github.com/zx029w/zhuangxiu-skills
- 提交问题: https://github.com/zx029w/zhuangxiu-skills/issues
