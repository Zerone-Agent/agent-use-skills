# Install Renovation Pitfall Avoidance Skills in Claude Code

## Prerequisites

- [Claude Code](https://github.com/claudecode) installed
- Git installed

## Installation Steps

### 1. Clone the repository

```bash
git clone https://github.com/zx029w/zhuangxiu-skills.git ~/.claude/zhuangxiu-skills
```

### 2. Create symbolic links

Link the 11 renovation skill subdirectories to Claude Code's skills directory:

```bash
mkdir -p ~/.claude/skills
for skill in quanwu-dingzhi-bucailei laofang-gaizao-bucailei zhuangxiu-hetong-shenhe zhuangxiu-baojia-shenhe zhuangxiu-fangan-zhenduan zhuangxiu-huanbao-bikeng zhuangxiu-liucheng-bucai zhuangxiu-fanche-jijiu zhuangxiu-bikeng-wenda zhuangxiu-zengxiang-bilei zhuangxiu-gongsi-bilei; do
  rm -rf ~/.claude/skills/$skill
  ln -s ~/.claude/zhuangxiu-skills/$skill ~/.claude/skills/$skill
done
```

### 3. Verify Installation

Restart Claude Code and try asking the following questions to verify the installation:

- "帮我审核这份装修合同" (triggers `zhuangxiu-hetong-shenhe`)
- "看一下这个装修报价有没有坑" (triggers `zhuangxiu-baojia-shenhe`)
- "do you have 装修避坑 skills?"

If installed successfully, Claude Code will automatically recognize and invoke the relevant renovation pitfall avoidance skill workflows.

## Update

```bash
cd ~/.claude/zhuangxiu-skills
git pull
```

## Uninstall

Delete the symbolic links to uninstall:

```bash
for skill in quanwu-dingzhi-bucailei laofang-gaizao-bucailei zhuangxiu-hetong-shenhe zhuangxiu-baojia-shenhe zhuangxiu-fangan-zhenduan zhuangxiu-huanbao-bikeng zhuangxiu-liucheng-bucai zhuangxiu-fanche-jijiu zhuangxiu-bikeng-wenda zhuangxiu-zengxiang-bilei zhuangxiu-gongsi-bilei; do
  rm -rf ~/.claude/skills/$skill
done
```

## Get Help

- GitHub: https://github.com/zx029w/zhuangxiu-skills
- Issues: https://github.com/zx029w/zhuangxiu-skills/issues
