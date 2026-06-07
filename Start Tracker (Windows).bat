@echo off
echo Starting Yield Portfolio Tracker...
echo.
python server.py
if errorlevel 1 (
    echo.
    echo Python not found. Please install Python from https://python.org
    echo Make sure to check "Add Python to PATH" during installation.
    pause
)
