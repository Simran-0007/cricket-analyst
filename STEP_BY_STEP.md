# 📖 Cricket Analytics Pro - Complete Installation Steps

## 🪟 FOR WINDOWS USERS

### **STEP 1: Install Python** (Skip if already installed)

1. Go to: https://www.python.org/downloads/
2. Click blue **"Download Python 3.11"** button
3. Run the downloaded file
4. **IMPORTANT**: Check ☑️ "Add Python to PATH" at bottom
5. Click **"Install Now"**
6. Wait for completion (~2 minutes)
7. Click **"Close"**

✅ **Verify Python installed:**
- Press `Win + R`
- Type `cmd` and press Enter
- Type: `python --version`
- Should show: `Python 3.11.x` or higher

---

### **STEP 2: Open Command Prompt**

- Press `Win + R`
- Type: `cmd`
- Press Enter

You should see:
```
C:\Users\YourUsername>
```

---

### **STEP 3: Navigate to Project**

In Command Prompt, type:
```cmd
cd C:\Users\simra\.vscode-shared\cricket_analytics
```

Press Enter. You should see:
```
C:\Users\simra\.vscode-shared\cricket_analytics>
```

---

### **STEP 4: Create Virtual Environment** (Optional but Recommended)

In Command Prompt, type:
```cmd
python -m venv venv
```

Press Enter. Wait 30-60 seconds.

---

### **STEP 5: Activate Virtual Environment**

In Command Prompt, type:
```cmd
venv\Scripts\activate
```

Press Enter. You should see:
```
(venv) C:\Users\simra\.vscode-shared\cricket_analytics>
```

Note the `(venv)` at the start - this means it's activated! ✅

---

### **STEP 6: Install Dependencies**

In Command Prompt, type:
```cmd
pip install -r requirements.txt
```

Press Enter. Watch for messages like:
```
Collecting streamlit
Downloading streamlit-1.28.1-py2.py3-none-win_amd64.whl (...KB)
Successfully installed streamlit-1.28.1
```

**This may take 2-5 minutes.** Be patient!

---

### **STEP 7: Run the Application**

In Command Prompt, type:
```cmd
streamlit run app.py
```

Press Enter. You should see:
```
Collecting usage statistics...
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://XXX.XXX.X.X:8501
```

✅ Your browser should automatically open!

---

### **STEP 8: Verify It Works**

1. Look for the heading: **"🏏 Cricket Analytics Pro"**
2. Look for sidebar with options:
   - 🔍 Player Search
   - 📈 Format Analysis
   - 📊 Recent Form
   - etc.
3. Type "virat" in Player Search
4. Click search

✅ **If you see all this, Installation is SUCCESSFUL!**

---

## 🍎 FOR MACOS USERS

### **STEP 1: Install Python** (Skip if already installed)

1. Open **Terminal** (Command + Space, type "terminal")
2. Install Homebrew first:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
3. Press Enter and follow instructions
4. Then install Python:
```bash
brew install python3
```
5. Verify:
```bash
python3 --version
```

---

### **STEP 2: Navigate to Project**

In Terminal, type:
```bash
cd ~/.vscode-shared/cricket_analytics
```

Press Enter.

---

### **STEP 3: Create Virtual Environment** (Optional)

```bash
python3 -m venv venv
```

Wait 30-60 seconds.

---

### **STEP 4: Activate Virtual Environment**

```bash
source venv/bin/activate
```

You should see `(venv)` at the start of your prompt.

---

### **STEP 5: Install Dependencies**

```bash
pip install -r requirements.txt
```

Wait 2-5 minutes for installation.

---

### **STEP 6: Run Application**

```bash
streamlit run app.py
```

Your browser should open automatically!

---

### **STEP 7: Verify**

Look for Cricket Analytics Pro heading and sidebar options.

✅ **You're done!**

---

## 🐧 FOR LINUX USERS

### **STEP 1: Install Python**

Open Terminal and run:
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv
```

Verify:
```bash
python3 --version
```

---

### **STEP 2: Navigate to Project**

```bash
cd ~/.vscode-shared/cricket_analytics
```

---

### **STEP 3: Create Virtual Environment**

```bash
python3 -m venv venv
```

---

### **STEP 4: Activate Virtual Environment**

```bash
source venv/bin/activate
```

---

### **STEP 5: Install Dependencies**

```bash
pip install -r requirements.txt
```

---

### **STEP 6: Run Application**

```bash
streamlit run app.py
```

---

### **STEP 7: Verify**

Application should open in browser!

✅ **Installation Complete!**

---

## ⚡ EASIEST METHOD: Use Quick Start Script

### **Windows Only:**

Simply double-click:
```
run.bat
```

This script will:
1. ✅ Check Python installation
2. ✅ Install dependencies
3. ✅ Start the application

Done!

---

## ✔️ VERIFY INSTALLATION

### Check Python is Installed

**Windows:**
```cmd
python --version
```

**Mac/Linux:**
```bash
python3 --version
```

Should show: `Python 3.8.0` or higher

---

### Check Dependencies are Installed

**Windows:**
```cmd
pip list
```

**Mac/Linux:**
```bash
pip list
```

Should show:
```
streamlit    1.28.1
pandas       2.0.3
plotly       5.17.0
numpy        1.24.3
requests     2.31.0
```

---

### Test Application Start

**All platforms:**
```bash
streamlit run app.py
```

Should display:
```
Local URL: http://localhost:8501
```

---

## 🆘 COMMON ISSUES & SOLUTIONS

### Issue: "python is not recognized"

**Solution:**
1. Install Python from python.org
2. **CHECK** "Add Python to PATH" during install
3. Restart Command Prompt
4. Try again

---

### Issue: "pip install fails"

**Solution:**
```cmd
# Upgrade pip first
python -m pip install --upgrade pip

# Try again
pip install -r requirements.txt
```

---

### Issue: "ModuleNotFoundError: No module named 'streamlit'"

**Solution:**
```bash
# Activate virtual environment first
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

### Issue: "Port 8501 already in use"

**Solution:**
```bash
streamlit run app.py --server.port 8502
```

---

### Issue: "Permission denied" (Mac/Linux)

**Solution:**
```bash
chmod +x run.sh
./run.sh
```

---

## 📋 CHECKLIST

Before and after installation:

**Before Installation:**
- [ ] Operating System: Windows / macOS / Linux
- [ ] Internet connection available
- [ ] ~500 MB free disk space
- [ ] Administrator access (recommended)

**After Installation:**
- [ ] Python installed (python --version shows 3.8+)
- [ ] Project folder accessible
- [ ] Virtual environment created
- [ ] Dependencies installed (pip list shows packages)
- [ ] Application starts (streamlit run app.py works)
- [ ] Browser opens to http://localhost:8501
- [ ] Cricket Analytics Pro interface visible
- [ ] Can search for players (try "virat")

✅ **All checked? You're ready!**

---

## 🎯 NEXT STEPS AFTER INSTALLATION

1. **Search for a player**
   - Click "🔍 Player Search"
   - Type "virat" or any player name
   - Click Search
   - View the player profile

2. **Explore features**
   - Try "📈 Format Analysis"
   - Try "📊 Recent Form"
   - Try "🤖 AI Analyst"
   - Try "⚖️ Compare Players"

3. **Read documentation**
   - README.md - Complete guide
   - QUICK_REFERENCE.md - Commands
   - PROJECT_INDEX.md - Full index

4. **Customize**
   - Edit data_loader.py to add players
   - Edit app.py to change UI
   - Edit visualizations.py for new charts

---

## 📞 NEED HELP?

**Check these files:**
1. **INSTALLATION.md** (this file)
2. **SETUP_GUIDE.md** - Detailed setup
3. **README.md** - Feature guide
4. **QUICK_REFERENCE.md** - Commands

**Common Problems:**
- Python not found? → Install Python, add to PATH
- pip fails? → Upgrade pip: `python -m pip install --upgrade pip`
- Modules missing? → Reinstall: `pip install -r requirements.txt --force-reinstall`
- Port in use? → Use different port: `streamlit run app.py --server.port 8502`

---

## 🎉 INSTALLATION SUCCESSFUL!

If you can see:
- ✅ Cricket Analytics Pro heading
- ✅ Sidebar with navigation
- ✅ Can search for players
- ✅ Charts display correctly

**Congratulations! Your installation is complete! 🏏**

---

**Questions?** Read the documentation files or check the QUICK_REFERENCE.md

**Ready to analyze cricket!** 📊
