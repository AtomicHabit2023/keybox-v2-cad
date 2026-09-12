# KeyBox Git Bridge MCP

A deliberately restricted local MCP server that lets Codex perform the Git operations needed for the KeyBox V2 CAD review loop **without giving the Codex sandbox direct access to the owner's SSH private key or unrestricted filesystem**.

The bridge is intended to run as the normal Windows user. It is hard-scoped to one repository and exposes only a small allowlist of Git operations.

## Allowed repository

Default:

`C:\Users\wirat\Documents\Codex\keybox-v2-cad`

Override only when deliberately relocating the repo:

`KEYBOX_REPO=<absolute path>`

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
- all commands run only inside the configured KeyBox repository.

## Install

Python 3.10+ is required. The official MCP Python SDK v2 is used.

From a normal Windows PowerShell, not inside the Codex sandbox:

```powershell
cd C:\Users\wirat\Documents\Codex\keybox-v2-cad\tools\keybox_git_bridge
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install "mcp>=2,<3"
```

The MCP Python SDK's CLI can run this server over stdio. A simple development test is:

```powershell
.\.venv\Scripts\Activate.ps1
mcp dev server.py
```

For Codex, configure the bridge as a local stdio MCP server using the Python/MCP environment above. Exact Codex UI/config placement can vary by version; the important runtime command is equivalent to:

```powershell
mcp run server.py
```

and the working directory should be this `tools\keybox_git_bridge` folder.

## First connection test

After adding the bridge to Codex, ask Codex to call only:

`git_status`

Expected result: it reports the KeyBox repository path, current branch and status without attempting to access `.ssh` from inside the Codex sandbox.

Then test:

1. `git_fetch_origin`
2. `git_create_or_switch_branch("cad/CAD-TEST")`
3. `git_status`

Do not push the test branch unless needed. Delete/cleanup can be done manually afterward because destructive cleanup is intentionally not exposed by this bridge.

## Why this solves the earlier failure

Codex's normal sandbox could edit the repository but could not read the user's `C:\Users\wirat\.ssh` credential files. This bridge runs in the normal Windows user context, so Git can use the already-configured SSH/ssh-agent environment while Codex sees only narrow Git tools, never the private key itself.

## Operational rule

From CAD-002 onward Codex should use the bridge for all network Git operations and should work on `cad/CAD-###` branches. Direct pushes to `main` remain a design-authority action only.
