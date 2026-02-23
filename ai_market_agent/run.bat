@echo off
REM AI Market Research Analyst - Windows Startup Script
REM This script sets up the environment and runs the application

echo ========================================
echo AI Market Research Analyst
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org
    pause
    exit /b 1
)

REM Check if .env file exists
if not exist ".env" (
    echo WARNING: .env file not found
    echo Creating .env from .env.example
    copy .env.example .env
    echo.
    echo IMPORTANT: Edit .env file and add your Gemini API key
    echo You can get it from: https://makersuite.google.com
    echo.
)

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating Python virtual environment...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo Installing dependencies...
    pip install -q -r backend\requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
) else (
    call venv\Scripts\activate.bat
)

REM Check for Gemini API key
for /f "delims==" %%A in ('findstr /r "^GEMINI_API_KEY" .env') do set "GEMINI_API_KEY=%%B"

if "%GEMINI_API_KEY%"=="" (
    echo ERROR: GEMINI_API_KEY not set in .env file
    echo.
    echo Steps to fix:
    echo 1. Go to https://makersuite.google.com
    echo 2. Click "Get API Key"
    echo 3. Copy your API key
    echo 4. Edit .env file and paste it
    echo 5. Run this script again
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo Starting AI Market Research Analyst
echo ========================================
echo.
echo Backend URL: http://localhost:5000
echo Dashboard URL: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.

cd backend
python app.py
