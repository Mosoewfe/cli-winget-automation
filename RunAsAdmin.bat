@echo off
:: Check for administrative rights
net session >nul 2>&1
if %errorLevel% == 0 (
    goto :adminTasks
) else (
    echo Requesting administrative privileges...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)
:adminTasks
:: Change directory to where the batch file is located
cd /d "%~dp0"
:: ---- PASTE YOUR ACTUAL COMMANDS BELOW THIS LINE ----
py script.py
pause
