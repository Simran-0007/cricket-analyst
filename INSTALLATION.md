# 🚀 Cricket Analytics Pro - Installation Guide

## 📋 Table of Contents
1. [Prerequisites](#prerequisites)
2. [Windows Installation](#windows-installation-step-by-step)
3. [macOS Installation](#macos-installation-step-by-step)
4. [Linux Installation](#linux-installation-step-by-step)
5. [Verify Installation](#verify-installation)
6. [Troubleshooting](#troubleshooting)
7. [First Time Usage](#first-time-usage)

---

## ✅ Prerequisites

Before you start, ensure you have:
- **Internet Connection** (required for downloading packages)
- **~500 MB Free Disk Space**
- **Administrator Access** (for some installations)

---

## 🪟 Windows Installation (Step-by-Step)

### Step 1: Check if Python is Installed

Open **Command Prompt** (Win + R, type `cmd`)

```cmd
python --version
```

**Expected output:** Python 3.8.0 or higher

If you see "python is not recognized", go to [Step 1B: Install Python](#step-1b-install-python-windows)

### Step 1B: Install Python (Windows)

1. Visit **https://www.python.org/downloads/**
2. Click **"Download Python 3.11.x"** (latest version)
3. Run the installer file
4. ✅ **IMPORTANT**: Check **"Add Python to PATH"** at the bottom
5. Click **"Install Now"**
6. Wait for installation to complete
7. Close the installer

**Verify:** Open Command Prompt and run:
```cmd
python --version
```

### Step 2: Navigate to Project Directory

Open **Command Prompt** and run:

```cmd
cd C:\Users\simra\.vscode-shared\cricket_analytics
```

You should see the folder path in the command prompt.

### Step 3: Create Virtual Environment (Recommended)

```cmd
python -m venv venv
```

Wait for completion (30-60 seconds).

### Step 4: Activate Virtual Environment

```cmd
venv\Scripts\activate
```

You should see `(venv)` at the beginning of the command line.

### Step 5: Install Dependencies

```cmd
pip install -r requirements.txt
```

**Expected time:** 2-5 minutes
**Watch for:** "Successfully installed" messages

If you encounter errors, try:
```cmd
pip install --upgrade pip setuptools wheel
pip install --no-cache-dir -r requirements.txt
```

### Step 6: Run the Application

```cmd
streamlit run app.py
```

The app will start and automatically open in your browser.
**Browser URL:** `http://localhost:8501`

---

## 🍎 macOS Installation (Step-by-Step)

### Step 1: Install Python (if not installed)

Open **Terminal** and run:

```bash
# Check if Python is installed
python3 --version

# If not installed, install via Homebrew
brew install python3
```

### Step 2: Navigate to Project Directory

```bash
cd ~/.vscode-shared/cricket_analytics
```

### Step 3: Create Virtual Environment

```bash
python3 -m venv venv
```

### Step 4: Activate Virtual Environment

```bash
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run the Application

```bash
streamlit run app.py
```

The app will open in your default browser.

---

## 🐧 Linux Installation (Step-by-Step)

### Step 1: Install Python and pip

Open **Terminal** and run:

```bash
# Update package manager
sudo apt-get update

# Install Python
sudo apt-get install python3 python3-pip python3-venv

# Verify
python3 --version
pip3 --version
```

### Step 2: Navigate to Project Directory

```bash
cd ~/.vscode-shared/cricket_analytics
```

### Step 3: Create Virtual Environment

```bash
python3 -m venv venv
```

### Step 4: Activate Virtual Environment

```bash
source venv/bin/activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run the Application

```bash
streamlit run app.py
```

---

## ⚡ Quick Start Using Batch/Shell Script

### Windows: Using run.bat

Simply double-click:
```
C:\Users\simra\.vscode-shared\cricket_analytics\run.bat
```

Or in Command Prompt:
```cmd
cd C:\Users\simra\.vscode-shared\cricket_analytics
run.bat
```

### macOS/Linux: Using run.sh

In Terminal:
```bash
cd ~/.vscode-shared/cricket_analytics
chmod +x run.sh
./run.sh
```

---

## ✔️ Verify Installation

After installation, verify everything works:

### Option 1: Quick Test

```bash
python -c "
import streamlit
import pandas
import plotly
print('✅ All packages installed correctly!')
"
```

### Option 2: Test Individual Modules

```bash
python -c "
from data_loader import CricketDataLoader
from analytics import CricketAnalytics
from visualizations import CricketVisualizations
from ai_report import AICricketAnalyst
print('✅ All modules loaded successfully!')
"
```

---

## 🌐 Access the Application

### First Time

1. After running `streamlit run app.py`, the browser opens automatically
2. If not, manually open: **http://localhost:8501**

### Browser Recommendation

- Chrome (Recommended)
- Firefox
- Edge
- Safari

### What You Should See

- Header: "🏏 Cricket Analytics Pro"
- Sidebar: Navigation menu with 7 options
- Main area: Welcome message or selected page

---

## 🔧 Troubleshooting

### Problem: "Python not found"

**Solution:**
1. Install Python from https://www.python.org/downloads/
2. ✅ Check "Add Python to PATH" during installation
3. Restart Command Prompt/Terminal
4. Verify: `python --version`

### Problem: "pip install fails"

**Solution:**
```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Try installation again
pip install -r requirements.txt --upgrade

# If still fails, try without cache
pip install --no-cache-dir -r requirements.txt
```

### Problem: "ModuleNotFoundError: No module named 'streamlit'"

**Solution:**
```bash
# Activate virtual environment (if using one)
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

# Install again
pip install -r requirements.txt
```

### Problem: "Port 8501 already in use"

**Solution:**
```bash
# Use different port
streamlit run app.py --server.port 8502
```

### Problem: "Permission denied" (Mac/Linux)

**Solution:**
```bash
# Make script executable
chmod +x run.sh

# Then run
./run.sh
```

### Problem: Slow startup

**Solution:**
- First run: Takes 30-60 seconds (normal)
- Subsequent runs: 5-10 seconds
- Be patient!

---

## 🎯 First Time Usage

### After Installation

1. ✅ App is running at `http://localhost:8501`
2. ✅ You see the Cricket Analytics Pro homepage

### Try This First

1. Click **"🔍 Player Search"** in sidebar
2. Type **"virat"** in search box
3. Click search button
4. Select **"Virat Kohli"**
5. Scroll through the profile

### Then Explore

- **📈 Format Analysis** - Compare formats
- **📊 Recent Form** - View trends
- **📉 Visualizations** - See charts
- **🤖 AI Analyst** - Get insights
- **⚖️ Compare Players** - Compare players
- **ℹ️ About** - Learn more

---

## 📁 Installation Folder Structure

After successful installation, your folder should look like:

```
C:\Users\simra\.vscode-shared\cricket_analytics\
├── venv/                          (if using virtual env)
├── app.py                         ✅
├── data_loader.py                 ✅
├── analytics.py                   ✅
├── visualizations.py              ✅
├── ai_report.py                   ✅
├── requirements.txt               ✅
├── README.md                      ✅
├── SETUP_GUIDE.md                 ✅
├── SUMMARY.md                      ✅
├── PROJECT_INDEX.md               ✅
├── QUICK_REFERENCE.md             ✅
├── run.bat                        ✅
└── run.sh                         ✅
```

All ✅ files should be present.

---

## 🔄 Uninstall / Clean Up

### Deactivate Virtual Environment

```bash
# Windows
deactivate

# Mac/Linux
deactivate
```

### Delete Virtual Environment

```bash
# Windows (Command Prompt as Admin)
rmdir /s venv

# Mac/Linux
rm -rf venv
```

### Keep Project Files

The Python files (.py) and documentation (.md) remain.

---

## ⬆️ Update Installation

### Get Latest Version

```bash
# Activate virtual environment first
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

# Update packages
pip install -r requirements.txt --upgrade
```

---

## 💻 System Requirements Summary

| Requirement | Minimum | Recommended |
|-------------|---------|------------|
| Python | 3.8 | 3.10+ |
| RAM | 2 GB | 4 GB+ |
| Disk Space | 500 MB | 1 GB |
| Internet | Required | For setup only |
| OS | Windows/Mac/Linux | Any |

---

## 📞 Getting Help

### Check Documentation

1. **README.md** - Feature guide
2. **SETUP_GUIDE.md** - Detailed setup
3. **PROJECT_INDEX.md** - Complete index
4. **QUICK_REFERENCE.md** - Commands

### Common Questions

**Q: Do I need admin access?**
A: Not always, but recommended for initial setup.

**Q: Can I use Python 3.7?**
A: Technically yes, but 3.8+ is recommended.

**Q: How much internet do I need?**
A: ~500 MB for initial package download only.

**Q: Can I run this on a Mac?**
A: Yes! Follow the macOS instructions.

**Q: Can I run on Linux?**
A: Yes! Follow the Linux instructions.

---

## ✨ Success Indicators

After installation, you should see:

✅ Command prompt shows `(venv)` when activated
✅ `pip install` completes without errors
✅ `streamlit run app.py` starts without errors
✅ Browser opens to `http://localhost:8501`
✅ You see the Cricket Analytics Pro interface
✅ You can search for players
✅ Charts and data display correctly

---

## 🎉 Installation Complete!

If you've reached this point:
- ✅ Python is installed
- ✅ Dependencies are installed
- ✅ Application is running
- ✅ You can access it in browser

**Congratulations! You're ready to analyze cricket! 🏏**

---

**Need More Help?**
- Windows issues? Check SETUP_GUIDE.md
- Command help? Check QUICK_REFERENCE.md
- Code help? Check PROJECT_INDEX.md

**Happy analyzing!**
