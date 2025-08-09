@echo off
REM scripts\bootstrap.bat - Bootstrap script for Windows

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed. Attempting to install...
    REM Try to use winget if available
    where winget >nul 2>nul
    if %errorlevel% equ 0 (
        winget install -e --id Python.Python.3
    ) else (
        echo Please install Python manually from https://www.python.org/downloads/
        exit /b 1
    )
)

REM Run the main Python CLI
python -m envgen.cli %*
