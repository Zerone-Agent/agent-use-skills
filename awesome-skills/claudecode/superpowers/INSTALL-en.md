# Installing Superpowers in Claude Code

Follow these steps to install and enable the Superpowers skills framework in your Claude Code environment:

## 1. Register the Marketplace
First, add the Superpowers marketplace to your Claude Code. Run the following command in the Claude Code chat:

```bash
/plugin marketplace add obra/superpowers-marketplace
```

## 2. Install the Superpowers Plugin
Once the marketplace is registered, run this command to install the plugin:

```bash
/plugin install superpowers@superpowers-marketplace
```

## 3. Verify Installation
To verify, start a new session and try to trigger a skill. For example, you can say:

- "Help me plan this feature" (triggers `brainstorming`)
- "Let's debug this issue" (triggers `systematic-debugging`)

If successful, Claude will automatically recognize and invoke the relevant Superpowers workflow.

## 4. Updates
To update the plugin to the latest version, use:

```bash
/plugin update superpowers
```

---
For more details, visit: [Superpowers GitHub Repository](https://github.com/obra/superpowers)
