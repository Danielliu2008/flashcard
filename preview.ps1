# 记忆辅助 App - Windows 极速桌面预览启动脚本
$OutputEncoding = [System.Text.Encoding]::UTF8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "   🚀 记忆辅助 App - Windows 极速桌面预览服务启动中...    " -ForegroundColor Green
Write-Host "========================================================" -ForegroundColor Cyan

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "[错误] 未在系统 PATH 中找到 Python，请确保已安装 Python 3！" -ForegroundColor Red
    exit 1
}

python preview\server.py
