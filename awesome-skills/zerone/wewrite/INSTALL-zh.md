# 在 Zerone 中安装 WeWrite

## 前置条件

- 已安装 Zerone
- 已安装 Git
- 已安装 Node.js 和 npm

## 安装步骤

### 1. 克隆 wewrite 仓库

```bash
git clone https://github.com/oaker-io/wewrite.git ~/.agents/wewrite
```

### 2. 创建符号链接

创建符号链接，使 Zerone 能够发现 wewrite 技能：

```bash
mkdir -p ~/.agents/skills
rm -rf ~/.agents/skills/wewrite
ln -s ~/.agents/wewrite/skills/wewrite ~/.agents/skills/wewrite
```

### 3. 安装依赖（可选）

如需使用完整功能，安装依赖：

```bash
cd ~/.agents/wewrite
npm install
pip install -r requirements.txt  # Python 脚本依赖
```

### 4. 验证安装

重启 Zerone，尝试询问：
- "帮我写一篇公众号文章"
- "do you have wewrite?"

如果安装成功，Zerone 会自动识别并调用 WeWrite 技能工作流。

## 更新

```bash
cd ~/.agents/wewrite
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.agents/skills/wewrite
```

## 获取帮助

- GitHub：https://github.com/oaker-io/wewrite