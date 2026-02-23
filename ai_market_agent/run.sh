#!/bin/bash
# AI Market Research Analyst - Linux/Mac Startup Script
# This script sets up the environment and runs the application

echo "========================================"
echo "AI Market Research Analyst"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ from https://www.python.org"
    exit 1
fi

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "WARNING: .env file not found"
    echo "Creating .env from .env.example"
    cp .env.example .env
    echo ""
    echo "IMPORTANT: Edit .env file and add your Gemini API key"
    echo "You can get it from: https://makersuite.google.com"
    echo ""
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
    echo "Installing dependencies..."
    pip install -q -r backend/requirements.txt
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to install dependencies"
        exit 1
    fi
else
    source venv/bin/activate
fi

# Check for Gemini API key
GEMINI_API_KEY=$(grep "^GEMINI_API_KEY" .env | cut -d "=" -f 2 | xargs)

if [ -z "$GEMINI_API_KEY" ] || [ "$GEMINI_API_KEY" = "your_gemini_api_key_here" ]; then
    echo "ERROR: GEMINI_API_KEY not set in .env file"
    echo ""
    echo "Steps to fix:"
    echo "1. Go to https://makersuite.google.com"
    echo "2. Click 'Get API Key'"
    echo "3. Copy your API key"
    echo "4. Edit .env file and paste it"
    echo "5. Run this script again"
    echo ""
    exit 1
fi

echo ""
echo "========================================"
echo "Starting AI Market Research Analyst"
echo "========================================"
echo ""
echo "Backend URL: http://localhost:5000"
echo "Dashboard URL: http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

cd backend
python3 app.py
