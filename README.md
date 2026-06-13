# 🏏 Cricket Analytics Pro

A modern, comprehensive cricket analytics web application built with Python and Streamlit. Analyze international and IPL cricket players with advanced statistics, AI-powered scouting reports, and interactive visualizations.

## ✨ Features

### 1. **Player Search & Profiles** 🔍
- Search any cricket player by name
- Support for international and IPL players
- Comprehensive career statistics overview
- Multiple formats: Test, ODI, T20I, IPL

### 2. **Career Overview** 📊
- Matches, Innings, Runs
- Batting Average, Strike Rate
- Highest Score, Centuries, Half-Centuries
- Wickets, Bowling Average, Economy Rate
- Format-wise breakdowns

### 3. **Format Analysis** 📈
Analyze player performance across:
- **Test Cricket** - The longest format with detailed statistics
- **ODI Cricket** - 50-over international matches
- **T20 International** - 20-over international cricket
- **IPL** - Indian Premier League statistics

### 4. **Recent Form Analysis** 📊
- Track last 5, 10, or 20 matches
- Automatic performance trend detection
- Moving averages for trend identification
- Form indicators (Improving ↗, Declining ↘, Consistent →)

### 5. **Interactive Visualizations** 📉
- Runs scored by match with trend lines
- Strike rate trends over time
- Batting average comparison by format
- Runs distribution by format (pie chart)
- Wickets by format (bar chart)
- Performance comparison radar charts

### 6. **AI Cricket Analyst** 🤖
Generate detailed scouting reports including:
- Overall player rating (0-100)
- Key strengths and weaknesses
- Consistency analysis across formats
- Recent form assessment
- Peer comparison and ranking
- Future performance outlook

### 7. **Player Comparison** ⚖️
- Side-by-side comparison of two players
- Career statistics comparison
- Visual comparison charts
- Head-to-head analysis
- Performance metrics comparison

### 8. **Modern Dashboard Design** 🎨
- Dark mode interface for comfortable viewing
- Responsive layout for all devices
- Professional sports analytics appearance
- Smooth animations and transitions
- Color-coded statistics cards
- Intuitive navigation

## 🏗️ Project Architecture

```
cricket_analytics/
├── app.py                 # Main Streamlit application
├── data_loader.py         # Cricket data management and player database
├── analytics.py           # Statistical calculations and analysis
├── visualizations.py      # Plotly charts and visualizations
├── ai_report.py          # AI analyst and scouting reports
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

### Module Breakdown

#### `app.py` - Main Application
- Streamlit UI and page routing
- All user-facing features
- Navigation and layout management
- Result display and formatting

#### `data_loader.py` - Data Management
- Generates realistic mock cricket data
- Player database with statistics
- Recent match data generation
- Search functionality
- Extensible for API integration

#### `analytics.py` - Analytics Engine
- Career overview calculations
- Format-wise analysis
- Recent form analysis
- Performance trend detection
- Player comparison logic
- Strengths/weaknesses identification

#### `visualizations.py` - Visualization Module
- Plotly-based interactive charts
- Runs trend visualization
- Strike rate trends
- Format comparison charts
- Player comparison radar charts
- Performance timeline plots

#### `ai_report.py` - AI Analysis
- Scouting report generation
- Overall player ratings
- Consistency scoring
- Performance recommendations
- Peer comparison analysis
- Future outlook prediction

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone or navigate to the project directory**
```bash
cd cricket_analytics
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
streamlit run app.py
```

4. **Access the app**
- Open your browser and navigate to: `http://localhost:8501`

## 📖 Usage Guide

### Player Search
1. Click on "🔍 Player Search" in the sidebar
2. Enter a player name in the search box
3. Select from suggestions
4. View comprehensive player profile with statistics

### Format Analysis
1. Select "📈 Format Analysis"
2. Choose a player from the dropdown
3. View tabs for each format (Test, ODI, T20I, IPL)
4. Compare statistics across formats

### Recent Form
1. Navigate to "📊 Recent Form"
2. Select a player
3. Choose number of matches (5-20)
4. View trend analysis and visualizations

### AI Scouting Report
1. Go to "🤖 AI Analyst"
2. Select a player
3. Click "Generate Scouting Report"
4. Review comprehensive analysis including:
   - Player rating
   - Strengths and weaknesses
   - Consistency score
   - Recommendation for selection
   - Future performance outlook

### Player Comparison
1. Select "⚖️ Compare Players"
2. Choose two different players
3. Click "Compare Players"
4. View side-by-side comparison with visualizations

## 🔄 Data Structure

### Player Statistics Include:
```
{
    "name": "Player Name",
    "role": "Batsman|Bowler|All-rounder",
    "country": "Country",
    "career_start": 2010,
    "test_batting": { matches, innings, runs, average, highest_score, hundreds, fifties, strike_rate },
    "test_bowling": { matches, wickets, runs_conceded, average, economy_rate, best_figures },
    "odi_batting": { matches, innings, runs, average, highest_score, hundreds, fifties, strike_rate },
    "odi_bowling": { matches, wickets, runs_conceded, average, economy_rate, best_figures },
    "t20i_batting": { matches, innings, runs, average, highest_score, hundreds, fifties, strike_rate },
    "t20i_bowling": { matches, wickets, runs_conceded, average, economy_rate, best_figures },
    "ipl_stats": { batting: {...}, bowling: {...} }
}
```

## 🔮 Future Expansion

The architecture is designed for easy extension:

### 1. **Live Match Data Integration**
- Real-time match updates
- Live score tracking
- In-match performance analysis

### 2. **Real API Integration**
- Cricket API (cricketapi.com)
- ESPN Cricinfo data
- Official ICC/IPL statistics
- Historical data archives

### 3. **Fantasy Cricket Recommendations**
- Dream11/MyTeam11 recommendations
- Optimal team selection
- Budget optimization
- Injury impact analysis

### 4. **Match Prediction Models**
- ML-based match outcome prediction
- Player performance prediction
- Team strength analysis
- Win probability models

### 5. **Advanced Analytics**
- Head-to-head statistics
- Venue-specific performance
- Opposition-specific statistics
- Historical trend analysis

### 6. **Custom Dashboards**
- Personalized player tracking
- Custom analytics workflows
- Export capabilities
- Comparison history

## 💡 Key Features Explained

### Performance Trend Detection
Analyzes recent 10 matches to detect trends:
- **Improving Form ↗**: Recent average > older average (20% improvement)
- **Declining Form ↘**: Recent average < older average (20% decline)
- **Consistent Form →**: Stable performance

### Consistency Score
Calculates coefficient of variation across formats:
- Lower variation = higher consistency score
- Scores range from 0-100
- Helps identify reliable performers

### Overall Player Rating
Composite score considering:
- Batting average (higher is better)
- Strike rate (format-dependent)
- Number of centuries
- Bowling average (lower is better)
- Economy rate (lower is better)
- Range: 0-100

### Fantasy Cricket Score
Predicts fantasy cricket points based on:
- Batting contributions
- Strike rate bonus
- Bowling performance
- Wickets taken
- Consistency factor

## 🎯 Technical Stack

| Component | Technology |
|-----------|-----------|
| Framework | Streamlit 1.28+ |
| Data Processing | Pandas, NumPy |
| Visualizations | Plotly |
| Analysis | NumPy, SciPy |
| API Requests | Requests |
| Date Handling | python-dateutil |

## 📊 Sample Players Included

### International Players
- Virat Kohli (India)
- Steve Smith (Australia)
- Kane Williamson (New Zealand)
- Pat Cummins (Australia)
- Ben Stokes (England)
- Jasprit Bumrah (India)
- Rashid Khan (Afghanistan)
- And more...

### IPL Players
- All international players plus
- MS Dhoni (CSK)
- David Warner (DC)
- AB de Villiers (RCB)
- Yuzvendra Chahal (RR)
- And more...

## ⚙️ Configuration

### Customizing Data
Edit `data_loader.py` to:
- Add more players
- Modify statistics generation
- Connect to real APIs
- Import historical data

### Customizing Visualizations
Edit `visualizations.py` to:
- Change color schemes
- Add new chart types
- Modify chart layouts
- Add custom filters

### Extending Analytics
Edit `analytics.py` to:
- Add new metrics
- Modify calculations
- Create custom comparisons
- Implement new algorithms

## 🐛 Troubleshooting

### App won't start
```bash
# Verify Python installation
python --version

# Reinstall dependencies
pip install --force-reinstall -r requirements.txt

# Run with verbose output
streamlit run app.py --logger.level=debug
```

### Missing players
- Check `data_loader.py` contains player data
- Verify database initialization
- Check search functionality

### Visualization errors
- Ensure Plotly is installed: `pip install --upgrade plotly`
- Check data format in `visualizations.py`
- Verify enough data points for charts

## 📝 Code Comments

The codebase is well-documented with:
- Module docstrings explaining functionality
- Function docstrings with parameter descriptions
- Inline comments for complex logic
- Type hints for better code understanding

## 🤝 Contributing

To extend this project:

1. **Add new players**: Edit `data_loader.py`
2. **Add new analysis**: Extend `analytics.py`
3. **Add new visualizations**: Update `visualizations.py`
4. **Add new features**: Extend `app.py`

## 📄 License

This project is provided as-is for educational and analytical purposes.

## 🙏 Acknowledgments

- Built with Streamlit for rapid web development
- Uses Plotly for interactive visualizations
- Inspired by professional cricket analytics platforms

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review code comments and docstrings
3. Verify data in sample files
4. Check Streamlit documentation

---

**Cricket Analytics Pro v1.0** - *Empowering Cricket Analytics*

Built with ❤️ for cricket enthusiasts and analysts worldwide.
