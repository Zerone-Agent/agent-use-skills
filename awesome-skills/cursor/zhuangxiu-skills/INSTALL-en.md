# Install Renovation Pitfall Avoidance Skills in Cursor

## Prerequisites

- [Cursor](https://github.com/cursor) installed
- Git installed

## Installation Steps

### 1. Clone the repository

```bash
git clone https://github.com/zx029w/zhuangxiu-skills.git ~/.cursor/zhuangxiu-skills
```

### 2. Create symbolic links

Link the 11 renovation skill subdirectories to Cursor's skills directory:

```bash
mkdir -p ~/.cursor/skills
for skill in quanwu-dingzhi-bucailei laofang-gaizao-bucailei zhuangxiu-hetong-shenhe zhuangxiu-baojia-shenhe zhuangxiu-fangan-zhenduan zhuangxiu-huanbao-bikeng zhuangxiu-liucheng-bucai zhuangxiu-fanche-jijiu zhuangxiu-bikeng-wenda zhuangxiu-zengxiang-bilei zhuangxiu-gongsi-bilei; do
  rm -rf ~/.cursor/skills/$skill
  ln -s ~/.cursor/zhuangxiu-skills/$skill ~/.cursor/skills/$skill
done
```

### 3. Verify Installation

Restart Cursor and try asking the following questions to verify the installation:

- "帮我审核这份装修合同" (triggers `zhuangxiu-hetong-shenhe`)
- "看一下这个装修报价有没有坑" (triggers `zhuangxiu-baojia-shenhe`)
- "do you have 装修避坑 skills?"

If installed successfully, Cursor will automatically recognize and invoke the relevant renovation pitfall avoidance skill workflows.

## Update

```bash
cd ~/.cursor/zhuangxiu-skills
git pull
```

## Uninstall

Delete the symbolic links to uninstall:

```bash
for skill in quanwu-dingzhi-bucailei laofang-gaizao-bucailei zhuangxiu-hetong-shenhe zhuangxiu-baojia-shenhe zhuangxiu-fangan-zhenduan zhuangxiu-huanbao-bikeng zhuangxiu-liucheng-bucai zhuangxiu-fanche-jijiu zhuangxiu-bikeng-wenda zhuangxiu-zengxiang-bilei zhuangxiu-gongsi-bilei; do
  rm -rf ~/.cursor/skills/$skill
done
```

## Get Help

- GitHub: https://github.com/zx029w/zhuangxiu-skills
- Issues: https://github.com/zx029w/zhuangxiu-skills/issues
