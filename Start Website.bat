@echo off
title Bottle2Filament - Starting...
color 0a
echo.
echo ================================================
echo     BOTTLE2FILAMENT - Starting Website
echo     Wait a few seconds then open browser!
echo ================================================
echo.

:: Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Python not found!
    echo Please install from: https://www.python.org/downloads/
    echo and TICK "Add Python to PATH"
    echo.
    pause
    exit /b 1
)

:: Create venv if missing
if not exist "venv" (
    echo.
    echo First time setup: Creating virtual environment...
    python -m venv venv
)

:: Activate venv
call venv\Scripts\activate.bat || (
    echo.
    echo [ERROR] Failed to activate virtual environment
    pause
    exit /b 1
)

:: Install packages if needed
if not exist "venv\installed.flag" (
    echo.
    echo Installing required packages... (only happens once)
    pip install Flask Flask-Login flask-wtf python-dotenv
    echo installed > venv\installed.flag
    echo.
    echo Packages installed successfully!
)

:: Start the website
echo.
echo ================================================
echo   Website is starting...
echo   Open your browser and go to:
echo        http://127.0.0.1:5000
echo ================================================
echo.
python run.py

pause