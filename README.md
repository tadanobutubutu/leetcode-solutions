# LeetCode Solutions

My LeetCode solutions, auto-synced to this repository via GitHub Actions.

## Setup

This repo uses [joshcai/leetcode-sync](https://github.com/joshcai/leetcode-sync) to automatically sync accepted submissions from LeetCode.

### Required Secrets

Add the following secrets to **Settings > Secrets and variables > Actions**:

| Secret | Description |
|---|---|
| `LEETCODE_CSRF_TOKEN` | `csrftoken` cookie from leetcode.com |
| `LEETCODE_SESSION` | `LEETCODE_SESSION` cookie from leetcode.com |

### How to get cookies

1. Log in to [leetcode.com](https://leetcode.com)
2. Open DevTools → Application → Cookies → `https://leetcode.com`
3. Copy the values of `csrftoken` and `LEETCODE_SESSION`

### Workflow Permissions

Enable write access: **Settings > Actions > General > Workflow permissions > Read and write permissions**

## Sync Schedule

Runs automatically every day at **5:00 AM JST**. Manual trigger is also available via `workflow_dispatch`.
