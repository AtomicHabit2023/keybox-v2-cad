# KeyBox Git Bridge MCP

A deliberately restricted local MCP server that lets Codex perform the Git operations needed for the KeyBox V2 CAD review loop **without giving the Codex sandbox direct access to the owner's SSH private key or unrestricted filesystem**.

The bridge runs as the normal Windows user, listens only on localhost, is hard-scoped to one repository, and exposes only a small allowlist of Git operations.

## Allowed repository

Default:

`C:\Users\wirat\Documents\Codex\keybox-v2-cad`

Override only when deliberately relocating the repo:

`KEYBOX_REPO=<absolute path>`

Default MCP endpoint:

`http://127.0.0.1:8765/mcp`

## Exposed tools

- `git_status`
- `git_log`
- `git_diff_summary`
- `git_fetch_origin`
- `git_pull_ff_only`
- `git_create_or_switch_branch`
- `git_stage`
- `git_commit`
- `git_push_head`

Safety behavior:

- no arbitrary shell command tool;
- no delete/reset/clean/rebase/force-push tool;
- `git_stage` accepts only explicit repository-relative paths;
- branch names are validated;
- `git_push_head` refuses to push `main`;
- subprocesses use `shell=False`;
- all commands run only inside the configured KeyBox repository;
- HTTP transport binds to `127.0.0.1`, not the LAN.

## One-time install

Python 3.10+ is required. The official MCP Python SDK v2 is used.

Run from a **normal Windows PowerShell**, not inside the Codex sandbox:

```powershell
cd C:\Users\wirat\Documents\Codex\keybox-v2-cad\tools\keybox_git_bridge
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install "mcp>=2,<3"
```

## Start the bridge

From the same normal Windows account:

```powershell
cd C:\Users\wirat\Documents\Codex\keybox-v2-cad\tools\keybox_git_bridge
.\.venv\Scripts\Activate.ps1
python server.py
```

Leave that small PowerShell window running while Codex is doing CAD work. The bridge should listen at:

`http://127.0.0.1:8765/mcp`

The server code uses MCP Streamable HTTP. The official MCP Python SDK v2 supports this transport; the server is intentionally local-only.

## Add to Codex

Add a custom HTTP MCP server named something like:

`keybox-git`

with URL:

`http://127.0.0.1:8765/mcp`

Exact UI placement can vary by Codex version. After adding it, ask Codex to list/use the `keybox-git` tools.

## First connection test

Ask Codex to call only:

`git_status`

Expected result: it reports the KeyBox repository path, current branch and status **without trying to read `.ssh` from inside the Codex sandbox**.

Then test:

1. `git_fetch_origin`
2. `git_status`

For real CAD work, create branches only when a task is released, e.g. `git_create_or_switch_branch("cad/CAD-002")`.

## Why this solves the earlier failure

Codex's normal sandbox could edit the repository but could not read the user's `C:\Users\wirat\.ssh` credential files. This bridge runs in the normal Windows user context, so Git can use the already-configured SSH/ssh-agent environment while Codex sees only narrow Git tools, never the private key itself.

## Operational rule

From CAD-002 onward Codex should use the bridge for all network Git operations and work on `cad/CAD-###` branches. Direct pushes to `main` remain blocked by the bridge.
