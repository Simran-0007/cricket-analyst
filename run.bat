@echo off
REM Cricket Analytics Pro - Quick Start Script for Windows

echo.
echo ============================================
echo  🏏 Cricket Analytics Pro - Setup & Run
echo ============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.8+ and add it to PATH
    pause
    exit /b 1
)

echo ✅ Python found
python --version

REM Check if pip is available
pip --version >nul 2>&1
if errorlevel 1 (
    echo ❌ pip is not available
    echo Please reinstall Python with pip support
    pause
    exit /b 1
)

echo ✅ pip found

REM Install/upgrade dependencies
echo.
echo 📦 Installing dependencies...
pip install -q -r requirements.txt
if errorlevel 1 (
    echo ⚠️  Some dependencies may need manual installation
    echo Attempting installation with --no-cache-dir flag...
    pip install --no-cache-dir -r requirements.txt
)

echo.
echo ✨ Setup complete!
echo.
echo 🚀 Starting Cricket Analytics Pro...
echo.
echo 📱 The app will open in your browser at: http://localhost:8501
echo.
echo 💡 Tip: Press Ctrl+C to stop the server
echo.

REM Run Streamlit app
streamlit run app.py

pause
