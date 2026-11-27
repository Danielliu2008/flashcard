@echo off
chcp 65001 >nul


where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo error
    pause
    exit /b 1
)

python preview\server.py
pause
