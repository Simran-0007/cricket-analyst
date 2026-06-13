# 🚀 Cricket Analytics Pro - Quick Reference

## ⚡ Quick Commands

### Start Application
```bash
streamlit run app.py
```

### With Options
```bash
# Different port
streamlit run app.py --server.port 8000

# Headless mode
streamlit run app.py --server.headless true

# Debug mode
streamlit run app.py --logger.level=debug
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Update Dependencies
```bash
pip install --upgrade -r requirements.txt
```

### Virtual Environment (Windows)
```bash
# Create
python -m venv venv

# Activate
venv\Scripts\activate

# Deactivate
deactivate
```

### Virtual Environment (Mac/Linux)
```bash
# Create
python3 -m venv venv

# Activate
source venv/bin/activate

# Deactivate
deactivate
```

---

## 🎯 Key URLs

- **Local App**: `http://localhost:8501`
- **Streamlit Docs**: https://docs.streamlit.io
- **Plotly Docs**: https://plotly.com/python/

---

## 📚 File Reference

### Python Modules
| File | Size | Purpose |
|------|------|---------|
| app.py | 23KB | Main application |
| data_loader.py | 12KB | Data management |
| analytics.py | 10KB | Analysis engine |
| visualizations.py | 10KB | Chart creation |
| ai_report.py | 9KB | AI analysis |

### Documentation
| File | Purpose |
|------|---------|
| README.md | Complete guide |
| SETUP_GUIDE.md | Installation |
| SUMMARY.md | Overview |
| PROJECT_INDEX.md | Full index |
| requirements.txt | Dependencies |

---

## 🎓 Sample Code Usage

### Import Modules
```python
from data_loader import CricketDataLoader
from analytics import CricketAnalytics
from visualizations import CricketVisualizations
from ai_report import AICricketAnalyst
```

### Load Data
```python
loader = CricketDataLoader()
player = loader.get_player("Virat Kohli")
```

### Get Analytics
```python
analytics = CricketAnalytics()
overview = analytics.get_career_overview("Virat Kohli")
```

### Generate Report
```python
analyst = AICricketAnalyst()
report = analyst.generate_scouting_report("Virat Kohli")
```

### Create Visualizations
```python
viz = CricketVisualizations()
fig = viz.plot_runs_by_match(matches_df, "Virat Kohli")
```

---

## 🔍 Troubleshooting

### Port Already in Use
```bash
streamlit run app.py --server.port 8502
```

### Module Not Found
```bash
pip install --force-reinstall -r requirements.txt
```

### Slow Startup
- First run: 30-60 seconds (normal)
- Subsequent: 5-10 seconds

### Browser Won't Open
- Manually open: `http://localhost:8501`

---

## 💡 Tips & Tricks

### Development Mode
```bash
streamlit run app.py --logger.level=debug
```

### Configuration File
Create `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#667eea"
backgroundColor = "#0f1419"

[server]
headless = false
```

### Test Individual Module
```bash
python -c "from data_loader import CricketDataLoader; loader = CricketDataLoader(); print(loader.get_all_players())"
```

---

## 📱 Navigation Guide

**Main Pages:**
1. 🔍 Player Search - Find and view players
2. 📈 Format Analysis - Compare formats
3. 📊 Recent Form - Track recent matches
4. 📉 Visualizations - View charts
5. 🤖 AI Analyst - Get insights
6. ⚖️ Compare Players - Compare two players
7. ℹ️ About - App information

---

## ✨ Feature Highlights

- 🏏 17 Sample Players
- 📊 40+ Statistics per Player
- 📈 4 Cricket Formats
- 🤖 AI-Generated Reports
- 📉 Interactive Charts
- 🎨 Modern Dark Theme
- 💻 Fully Responsive
- ⚡ Fast Performance

---

## 🔗 Related Files

```
C:\Users\simra\.vscode-shared\cricket_analytics\
├── app.py                    ← Start here
├── README.md                 ← Read this
├── SETUP_GUIDE.md           ← Installation help
├── PROJECT_INDEX.md         ← Full index
└── requirements.txt         ← Dependencies
```

---

## 🎯 Next Steps

1. ✅ Install dependencies: `pip install -r requirements.txt`
2. ✅ Run app: `streamlit run app.py`
3. ✅ Open browser: `http://localhost:8501`
4. ✅ Search a player: Type "Virat"
5. ✅ Explore features: Click sidebar options

---

## 📞 Support

- Docs: README.md
- Setup: SETUP_GUIDE.md
- Overview: SUMMARY.md
- Index: PROJECT_INDEX.md

---

**Cricket Analytics Pro v1.0** - Ready to Analyze! 🏏
