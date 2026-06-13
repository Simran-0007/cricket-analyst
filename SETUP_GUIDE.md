# 🚀 Cricket Analytics Pro - Setup Guide

## System Requirements

- **Operating System**: Windows, macOS, or Linux
- **Python Version**: 3.8 or higher
- **RAM**: Minimum 2GB (4GB recommended)
- **Disk Space**: 500MB for installation and data
- **Internet**: Required for initial setup

## Installation Steps

### 1. **Install Python** (if not already installed)

#### Windows
- Download from [python.org](https://www.python.org/downloads/)
- Run installer
- ✅ **Important**: Check "Add Python to PATH" during installation
- Click "Install Now"

#### macOS
```bash
brew install python3
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip
```

### 2. **Navigate to Project Directory**

#### Windows
```cmd
cd C:\Users\YourUsername\.vscode-shared\cricket_analytics
```

#### macOS/Linux
```bash
cd ~/.vscode-shared/cricket_analytics
```

### 3. **Create Virtual Environment (Optional but Recommended)**

#### Windows
```cmd
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. **Install Dependencies**

```bash
pip install -r requirements.txt
```

If you encounter issues, try:
```bash
pip install --upgrade pip setuptools wheel
pip install --no-cache-dir -r requirements.txt
```

### 5. **Run the Application**

#### Option A: Direct Command

```bash
streamlit run app.py
```

#### Option B: Using Run Script

**Windows:**
```cmd
run.bat
```

**macOS/Linux:**
```bash
chmod +x run.sh
./run.sh
```

### 6. **Access the Application**

- Default URL: `http://localhost:8501`
- The app should automatically open in your browser
- If not, manually navigate to the URL above

## Troubleshooting

### Issue: "Python not found"
**Solution:**
- Ensure Python is installed and added to PATH
- Restart terminal/command prompt after installation
- Verify: `python --version`

### Issue: "pip install fails"
**Solution:**
- Upgrade pip: `python -m pip install --upgrade pip`
- Try with no-cache: `pip install --no-cache-dir -r requirements.txt`
- Use specific versions: `pip install streamlit==1.28.1`

### Issue: "Module not found" error
**Solution:**
- Ensure virtual environment is activated
- Reinstall all dependencies: `pip install -r requirements.txt --force-reinstall`
- Check that all files are in the same directory

### Issue: "Port 8501 already in use"
**Solution:**
```bash
# Use different port
streamlit run app.py --server.port 8502
```

### Issue: "Slow startup"
**Solution:**
- First run takes longer due to caching
- Subsequent runs will be faster
- Check internet connection for package download

## First-Time Usage

1. **Launch the app** and wait for it to load (30-60 seconds first time)
2. **Navigate to Player Search** using sidebar
3. **Search for "Virat"** to find Virat Kohli
4. **Select the player** to view the profile
5. **Explore different sections** using the sidebar navigation

## Verify Installation

Run this command to verify all modules are working:

```python
python -c "
import streamlit as st
from data_loader import CricketDataLoader
from analytics import CricketAnalytics
from visualizations import CricketVisualizations
from ai_report import AICricketAnalyst
print('✅ All imports successful!')
"
```

## Windows-Specific Setup

### Using Command Prompt

```cmd
# Navigate to project
cd C:\Users\YourUsername\.vscode-shared\cricket_analytics

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
```

### Using PowerShell

```powershell
# Navigate to project
cd "C:\Users\YourUsername\.vscode-shared\cricket_analytics"

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
```

## macOS/Linux Setup

```bash
# Navigate to project
cd ~/.vscode-shared/cricket_analytics

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
```

## Dependencies Explained

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | >=1.28.0 | Web framework |
| pandas | >=2.0.0 | Data processing |
| plotly | >=5.17.0 | Visualizations |
| numpy | >=1.24.0 | Numerical computing |
| requests | >=2.31.0 | HTTP requests |
| python-dateutil | >=2.8.0 | Date utilities |

## Performance Tips

1. **First Run**: May take 2-5 minutes to compile all packages
2. **Subsequent Runs**: Should start in 10-30 seconds
3. **Memory**: Close other applications for better performance
4. **Network**: Use stable internet for first-time setup

## Advanced Configuration

### Custom Port
```bash
streamlit run app.py --server.port 8000
```

### Disable Browser Auto-open
```bash
streamlit run app.py --server.headless true
```

### Logging
```bash
streamlit run app.py --logger.level=debug
```

### Configuration File
Create `~/.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#667eea"
backgroundColor = "#0f1419"
secondaryBackgroundColor = "#1a1f2e"
textColor = "#ffffff"

[server]
headless = false
```

## Uninstall

To remove the application:

```bash
# Deactivate virtual environment (if using one)
deactivate

# Delete the project directory
# Windows: del /s C:\Users\YourUsername\.vscode-shared\cricket_analytics
# macOS/Linux: rm -rf ~/.vscode-shared/cricket_analytics
```

## Update Application

To update to the latest version:

```bash
# Pull latest changes
git pull  # if using git

# Reinstall dependencies
pip install -r requirements.txt --upgrade

# Restart application
streamlit run app.py
```

## Getting Help

### Check Logs
1. Streamlit logs appear in the terminal
2. Look for specific error messages
3. Note the error line and module name

### Common Error Messages

**"ModuleNotFoundError: No module named 'streamlit'"**
- Solution: `pip install streamlit`

**"ConnectionError: HTTPConnectionPool"**
- Solution: Check internet connection or use offline mode

**"FileNotFoundError"**
- Solution: Verify working directory and file paths

## Next Steps

1. ✅ Installation complete
2. ✅ App is running
3. 📖 Read README.md for feature documentation
4. 🎯 Start exploring cricket analytics!

## Support Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Plotly Documentation](https://plotly.com/python/)
- [Python Documentation](https://docs.python.org/)

---

**Happy cricket analytics! 🏏**
