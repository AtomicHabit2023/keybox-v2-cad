$ErrorActionPreference = "Stop"

$Here = Split-Path -Parent $MyInvocation.MyCommand.Path
$Venv = Join-Path $Here ".venv"
$Python = Join-Path $Venv "Scripts\python.exe"

if (-not (Test-Path $Python)) {
    Write-Host "Creating KeyBox Git Bridge virtual environment..."
    py -m venv $Venv
    & $Python -m pip install --upgrade pip
    & $Python -m pip install "mcp>=2,<3"
}

$env:KEYBOX_REPO = "C:\Users\wirat\Documents\Codex\keybox-v2-cad"
$env:KEYBOX_BRIDGE_HOST = "127.0.0.1"
$env:KEYBOX_BRIDGE_PORT = "8765"

Write-Host "Starting KeyBox Git Bridge at http://127.0.0.1:8765/mcp"
Write-Host "Leave this window open while Codex is working."
& $Python (Join-Path $Here "server.py")
