from __future__ import annotations

import os
import re
import subprocess
from pathlib import Path
from typing import Any

from mcp.server import MCPServer

mcp = MCPServer("KeyBox Git Bridge")

DEFAULT_REPO = r"C:\Users\wirat\Documents\Codex\keybox-v2-cad"
REPO = Path(os.environ.get("KEYBOX_REPO", DEFAULT_REPO)).expanduser().resolve()

_BRANCH_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._/-]{0,119}$")


def _ensure_repo() -> None:
    if not REPO.exists():
        raise RuntimeError(f"Allowed repository does not exist: {REPO}")
    if not (REPO / ".git").exists():
        raise RuntimeError(f"Allowed path is not a Git repository: {REPO}")


def _git(*args: str, timeout: int = 120) -> dict[str, Any]:
    _ensure_repo()
    cp = subprocess.run(
        ["git", "-C", str(REPO), *args],
        capture_output=True,
        text=True,
        timeout=timeout,
        shell=False,
        check=False,
    )
    return {
        "ok": cp.returncode == 0,
        "returncode": cp.returncode,
        "stdout": cp.stdout.strip(),
        "stderr": cp.stderr.strip(),
        "repo": str(REPO),
        "command": ["git", *args],
    }


def _validate_branch(branch: str) -> str:
    branch = branch.strip()
    if not _BRANCH_RE.fullmatch(branch):
        raise ValueError("Invalid branch name")
    if ".." in branch or branch.startswith("-") or branch.endswith("/") or "//" in branch:
        raise ValueError("Unsafe branch name")
    return branch


def _validate_relpath(path_text: str) -> str:
    raw = path_text.replace("\\", "/").strip()
    if not raw or raw.startswith("/") or raw.startswith("-"):
        raise ValueError(f"Unsafe path: {path_text!r}")
    parts = Path(raw).parts
    if ".." in parts:
        raise ValueError(f"Parent traversal is not allowed: {path_text!r}")
    candidate = (REPO / Path(*parts)).resolve()
    try:
        candidate.relative_to(REPO)
    except ValueError as exc:
        raise ValueError(f"Path escapes allowed repository: {path_text!r}") from exc
    return raw


@mcp.tool()
def git_status() -> dict[str, Any]:
    """Return branch, concise status, and remotes for the one allowed KeyBox repository."""
    return {
        "branch": _git("branch", "--show-current"),
        "status": _git("status", "--short"),
        "remote": _git("remote", "-v"),
    }


@mcp.tool()
def git_log(limit: int = 8) -> dict[str, Any]:
    """Return recent local commits. Limit is clamped to 1..30."""
    limit = max(1, min(int(limit), 30))
    return _git("log", f"-{limit}", "--oneline", "--decorate")


@mcp.tool()
def git_diff_summary() -> dict[str, Any]:
    """Return changed filenames and diff statistics for review preparation."""
    return {
        "unstaged": _git("diff", "--name-status"),
        "staged": _git("diff", "--cached", "--name-status"),
        "unstaged_stat": _git("diff", "--stat"),
        "staged_stat": _git("diff", "--cached", "--stat"),
    }


@mcp.tool()
def git_fetch_origin() -> dict[str, Any]:
    """Fetch origin. Non-destructive; does not merge or modify working files."""
    return _git("fetch", "--prune", "origin", timeout=180)


@mcp.tool()
def git_pull_ff_only() -> dict[str, Any]:
    """Pull the current branch using fast-forward only. No merge commits are allowed."""
    return _git("pull", "--ff-only", "origin", timeout=180)


@mcp.tool()
def git_create_or_switch_branch(branch: str) -> dict[str, Any]:
    """Create or switch to a safe task branch. Intended form: cad/CAD-002."""
    branch = _validate_branch(branch)
    exists = _git("show-ref", "--verify", "--quiet", f"refs/heads/{branch}")
    if exists["returncode"] == 0:
        return _git("switch", branch)
    return _git("switch", "-c", branch)


@mcp.tool()
def git_stage(paths: list[str]) -> dict[str, Any]:
    """Stage only explicitly listed repository-relative paths. Wildcards and parent traversal are disallowed."""
    if not paths:
        raise ValueError("At least one path is required")
    safe = [_validate_relpath(p) for p in paths]
    return _git("add", "--", *safe)


@mcp.tool()
def git_commit(message: str) -> dict[str, Any]:
    """Create a local commit from files that are already staged. This tool never stages automatically."""
    message = message.strip()
    if not message or len(message) > 240 or "\x00" in message:
        raise ValueError("Commit message must be 1..240 characters")
    return _git("commit", "-m", message)


@mcp.tool()
def git_push_head() -> dict[str, Any]:
    """Push the current task branch and set upstream. Direct pushes to main are intentionally blocked."""
    branch_result = _git("branch", "--show-current")
    if not branch_result["ok"] or not branch_result["stdout"]:
        return {"ok": False, "error": "Could not determine current branch", "detail": branch_result}

    current = _validate_branch(branch_result["stdout"])
    if current == "main":
        return {
            "ok": False,
            "error": "Direct pushes to main are intentionally blocked by KeyBox Git Bridge. Use cad/CAD-###.",
        }

    return _git("push", "-u", "origin", "HEAD", timeout=240)
