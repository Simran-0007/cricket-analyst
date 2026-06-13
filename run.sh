#!/bin/bash
# Cricket Analytics Pro - Quick Start Script for Linux/Mac

echo ""
echo "============================================"
echo " 🏏 Cricket Analytics Pro - Setup & Run"
echo "============================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed"
    echo "Please install Python 3.8+ first"
    exit 1
fi

echo "✅ Python found"
python3 --version

# Check if pip is available
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not available"
    echo "Please reinstall Python with pip support"
    exit 1
fi

echo "✅ pip3 found"

# Install/upgrade dependencies
echo ""
echo "📦 Installing dependencies..."
pip3 install -q -r requirements.txt

if [ $? -ne 0 ]; then
    echo "⚠️  Some dependencies may need manual installation"
    echo "Attempting installation with --no-cache-dir flag..."
    pip3 install --no-cache-dir -r requirements.txt
fi

echo ""
echo "✨ Setup complete!"
echo ""
echo "🚀 Starting Cricket Analytics Pro..."
echo ""
echo "📱 The app will open in your browser at: http://localhost:8501"
echo ""
echo "💡 Tip: Press Ctrl+C to stop the server"
echo ""

# Run Streamlit app
streamlit run app.py
