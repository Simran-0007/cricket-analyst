"""
Modern Cricket Analytics Web Application
A comprehensive Streamlit app for analyzing cricket players and performance.

Features:
- Player search and profiles
- Career statistics overview
- Format-wise analysis
- Recent form detection
- Interactive visualizations
- AI scouting reports
- Player comparison
- Fantasy insights
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import sys

# Import custom modules
from data_loader import CricketDataLoader
from analytics import CricketAnalytics
from visualizations import CricketVisualizations
from ai_report import AICricketAnalyst

# Configure Streamlit
st.set_page_config(
    page_title="Cricket Analytics Pro",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for dark mode and styling
st.markdown("""
<style>
    /* Main app styling */
    .main {
        background-color: #0f1419;
        color: #ffffff;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #1a1f2e;
    }
    
    /* Header styling */
    h1, h2, h3 {
        color: #00d4ff;
    }
    
    /* Card styling */
    .stat-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        color: white;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-weight: bold;
    }
    
    /* Input styling */
    .stTextInput input, .stSelectbox select {
        background-color: #1a1f2e;
        color: #ffffff;
        border: 1px solid #667eea;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)


# Initialize session state
@st.cache_resource
def initialize_app():
    """Initialize app resources"""
    return {
        "data_loader": CricketDataLoader(),
        "analytics": CricketAnalytics(),
        "visualizations": CricketVisualizations(),
        "ai_analyst": AICricketAnalyst(),
    }


def display_stat_box(label: str, value: str, color: str = "#667eea"):
    """Display a statistics box"""
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, {color} 0%, #764ba2 100%); 
                padding: 20px; border-radius: 10px; margin: 10px 0; text-align: center;">
        <h4 style="margin: 0; color: #cccccc;">{label}</h4>
        <h2 style="margin: 10px 0; color: white;">{value}</h2>
    </div>
    """, unsafe_allow_html=True)


def display_header():
    """Display app header"""
    col1, col2 = st.columns([1, 4])
    
    with col1:
        st.markdown("# 🏏")
    
    with col2:
        st.markdown("# Cricket Analytics Pro")
        st.markdown("*Advanced Cricket Player Analytics & Scouting Platform*")


def search_player_page(app_resources):
    """Player search and profile page"""
    st.header("🔍 Player Search & Profile")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        search_query = st.text_input(
            "Search for a cricket player:",
            placeholder="e.g., Virat Kohli, Steve Smith, etc."
        )
    
    with col2:
        st.write("")  # Spacing
        search_button = st.button("Search", use_container_width=True)
    
    if search_query or search_button:
        results = app_resources["data_loader"].search_players(search_query)
        
        if results:
            selected_player = st.selectbox(
                "Select a player:",
                results,
                key="player_search"
            )
            
            if selected_player:
                display_player_profile(selected_player, app_resources)
        else:
            st.warning("No players found. Try a different search term.")


def display_player_profile(player_name: str, app_resources):
    """Display comprehensive player profile"""
    
    overview = app_resources["analytics"].get_career_overview(player_name)
    
    if not overview:
        st.error("Player not found")
        return
    
    # Header with basic info
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        display_stat_box("Player", overview["name"], "#FF6B6B")
    
    with col2:
        display_stat_box("Role", overview["role"], "#4ECDC4")
    
    with col3:
        display_stat_box("Country", overview["country"], "#45B7D1")
    
    with col4:
        display_stat_box("Career Start", str(overview["career_start"]), "#FFA07A")
    
    st.markdown("---")
    
    # Career Statistics
    st.subheader("📊 Career Statistics Overview")
    
    if "batting" in overview:
        st.write("**Batting Statistics**")
        bat_col1, bat_col2, bat_col3 = st.columns(3)
        
        with bat_col1:
            total_runs = sum(stats.get("runs", 0) for stats in overview["batting"].values())
            display_stat_box("Total Runs", f"{total_runs:,}", "#FF6B6B")
        
        with bat_col2:
            total_centuries = sum(stats.get("hundreds", 0) for stats in overview["batting"].values())
            display_stat_box("Centuries", str(total_centuries), "#4ECDC4")
        
        with bat_col3:
            total_fifties = sum(stats.get("fifties", 0) for stats in overview["batting"].values())
            display_stat_box("Half-Centuries", str(total_fifties), "#45B7D1")
        
        # Batting table
        batting_data = []
        for format_name, stats in overview["batting"].items():
            batting_data.append({
                "Format": format_name,
                "Matches": stats.get("matches", 0),
                "Innings": stats.get("innings", 0),
                "Runs": stats.get("runs", 0),
                "Average": stats.get("average", 0),
                "Strike Rate": stats.get("strike_rate", 0),
                "Highest Score": stats.get("highest_score", 0),
            })
        
        if batting_data:
            st.dataframe(pd.DataFrame(batting_data), use_container_width=True)
    
    if "bowling" in overview:
        st.write("**Bowling Statistics**")
        bowl_col1, bowl_col2, bowl_col3 = st.columns(3)
        
        with bowl_col1:
            total_wickets = sum(stats.get("wickets", 0) for stats in overview["bowling"].values())
            display_stat_box("Total Wickets", str(total_wickets), "#9B59B6")
        
        with bowl_col2:
            avg_avg = sum(stats.get("average", 0) for stats in overview["bowling"].values()) / len(overview["bowling"])
            display_stat_box("Avg Bowling Avg", f"{avg_avg:.2f}", "#E74C3C")
        
        with bowl_col3:
            best_econ = min(stats.get("economy_rate", 100) for stats in overview["bowling"].values())
            display_stat_box("Best Economy", f"{best_econ:.2f}", "#3498DB")
        
        # Bowling table
        bowling_data = []
        for format_name, stats in overview["bowling"].items():
            bowling_data.append({
                "Format": format_name,
                "Matches": stats.get("matches", 0),
                "Wickets": stats.get("wickets", 0),
                "Average": stats.get("average", 0),
                "Economy Rate": stats.get("economy_rate", 0),
                "Best Figures": stats.get("best_figures", "N/A"),
            })
        
        if bowling_data:
            st.dataframe(pd.DataFrame(bowling_data), use_container_width=True)
    
    # IPL Stats if available
    if "ipl_stats" in overview:
        st.write("**IPL Statistics**")
        ipl_col1, ipl_col2, ipl_col3 = st.columns(3)
        
        with ipl_col1:
            display_stat_box("IPL Team", overview.get("ipl_team", "N/A"), "#FFA07A")
        
        if "batting" in overview["ipl_stats"]:
            ipl_runs = overview["ipl_stats"]["batting"].get("runs", 0)
            with ipl_col2:
                display_stat_box("IPL Runs", f"{ipl_runs:,}", "#FF6B6B")
            
            ipl_sr = overview["ipl_stats"]["batting"].get("strike_rate", 0)
            with ipl_col3:
                display_stat_box("IPL Strike Rate", f"{ipl_sr:.2f}", "#4ECDC4")


def format_analysis_page(app_resources):
    """Format-wise cricket analysis"""
    st.header("📈 Format Analysis")
    
    player_name = st.selectbox(
        "Select a player:",
        app_resources["data_loader"].get_all_players(),
        key="format_analysis_select"
    )
    
    if player_name:
        format_analysis = app_resources["analytics"].get_format_analysis(player_name)
        
        if not format_analysis:
            st.warning("No format data available for this player.")
            return
        
        # Create tabs for each format
        tabs = st.tabs(list(format_analysis.keys()))
        
        for idx, (format_name, tab) in enumerate(zip(format_analysis.keys(), tabs)):
            with tab:
                format_data = format_analysis[format_name]
                
                col1, col2, col3 = st.columns(3)
                
                if "batting" in format_data:
                    batting = format_data["batting"]
                    with col1:
                        display_stat_box("Matches", str(batting.get("matches", 0)), "#FF6B6B")
                    with col2:
                        display_stat_box("Total Runs", f"{batting.get('runs', 0):,}", "#4ECDC4")
                    with col3:
                        display_stat_box("Average", f"{batting.get('average', 0):.2f}", "#45B7D1")
                    
                    col4, col5, col6 = st.columns(3)
                    with col4:
                        display_stat_box("Centuries", str(batting.get("hundreds", 0)), "#FFA07A")
                    with col5:
                        display_stat_box("Half-Centuries", str(batting.get("fifties", 0)), "#95E1D3")
                    with col6:
                        display_stat_box("Strike Rate", f"{batting.get('strike_rate', 0):.2f}", "#FF8B94")
                
                if "bowling" in format_data:
                    st.write("---")
                    bowling = format_data["bowling"]
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        display_stat_box("Wickets", str(bowling.get("wickets", 0)), "#9B59B6")
                    with col2:
                        display_stat_box("Bowling Average", f"{bowling.get('average', 0):.2f}", "#E74C3C")
                    with col3:
                        display_stat_box("Economy Rate", f"{bowling.get('economy_rate', 0):.2f}", "#3498DB")


def recent_form_page(app_resources):
    """Recent form and trend analysis"""
    st.header("📊 Recent Form Analysis")
    
    player_name = st.selectbox(
        "Select a player:",
        app_resources["data_loader"].get_all_players(),
        key="form_select"
    )
    
    if not player_name:
        return
    
    # Get recent matches
    recent_matches = app_resources["data_loader"].get_recent_matches(player_name)
    
    if recent_matches.empty:
        st.warning("No recent match data available.")
        return
    
    col1, col2 = st.columns(2)
    
    with col1:
        num_matches = st.slider("Select number of matches to analyze:", 5, 20, 10)
    
    with col2:
        # Show recent form data
        trend = app_resources["analytics"].detect_performance_trend(player_name)
        st.metric("Current Trend", trend.get("trend", "N/A"), f"{trend.get('confidence', 0):.1f}% confidence")
    
    # Get recent form
    form_df = app_resources["analytics"].get_recent_form(player_name, num_matches)
    
    if not form_df.empty:
        # Display recent matches table
        st.subheader("Recent Matches")
        display_df = form_df[["date", "format", "opponent", "runs", "wickets", "venue"]].head(num_matches)
        st.dataframe(display_df, use_container_width=True)
        
        # Display visualizations
        st.subheader("Performance Visualizations")
        
        col1, col2 = st.columns(2)
        
        with col1:
            runs_fig = app_resources["visualizations"].plot_runs_by_match(
                form_df.head(num_matches), player_name
            )
            if runs_fig:
                st.plotly_chart(runs_fig, use_container_width=True)
        
        with col2:
            sr_fig = app_resources["visualizations"].plot_strike_rate_trend(
                form_df.head(num_matches), player_name
            )
            if sr_fig:
                st.plotly_chart(sr_fig, use_container_width=True)


def visualizations_page(app_resources):
    """Interactive visualizations"""
    st.header("📊 Advanced Visualizations")
    
    player_name = st.selectbox(
        "Select a player:",
        app_resources["data_loader"].get_all_players(),
        key="viz_select"
    )
    
    if not player_name:
        return
    
    format_analysis = app_resources["analytics"].get_format_analysis(player_name)
    
    if not format_analysis:
        st.warning("No data available for visualization.")
        return
    
    col1, col2 = st.columns(2)
    
    with col1:
        bat_fig = app_resources["visualizations"].plot_batting_comparison(format_analysis)
        if bat_fig:
            st.plotly_chart(bat_fig, use_container_width=True)
    
    with col2:
        runs_fig = app_resources["visualizations"].plot_runs_by_format(format_analysis)
        if runs_fig:
            st.plotly_chart(runs_fig, use_container_width=True)
    
    col3, col4 = st.columns(2)
    
    with col3:
        wickets_fig = app_resources["visualizations"].plot_wickets_by_format(format_analysis)
        if wickets_fig:
            st.plotly_chart(wickets_fig, use_container_width=True)
    
    with col4:
        st.write("### Format Analysis Summary")
        st.write(f"**Total Career Formats:** {len(format_analysis)}")
        
        total_matches = sum(
            stats.get("batting", {}).get("matches", 0) or stats.get("bowling", {}).get("matches", 0)
            for stats in format_analysis.values()
        )
        st.write(f"**Total Career Matches:** {total_matches}")


def ai_scouting_page(app_resources):
    """AI Scouting Report"""
    st.header("🤖 AI Cricket Analyst - Scouting Report")
    
    player_name = st.selectbox(
        "Select a player for analysis:",
        app_resources["data_loader"].get_all_players(),
        key="ai_select"
    )
    
    if not player_name:
        return
    
    if st.button("Generate Scouting Report", use_container_width=True):
        with st.spinner("Analyzing player data..."):
            report = app_resources["ai_analyst"].generate_scouting_report(player_name)
        
        if report:
            # Overall Rating
            rating = report["overall_rating"]
            st.metric("Overall Player Rating", f"{rating}/100")
            
            col1, col2 = st.columns(2)
            
            with col1:
                consistency = report["consistency_score"]
                st.metric("Consistency Score", f"{consistency:.1f}/100")
            
            with col2:
                recent_form = report["recent_form"]
                st.metric("Recent Form", recent_form.get("trend", "N/A"))
            
            st.markdown("---")
            
            # Strengths
            st.subheader("💪 Key Strengths")
            for strength in report["strengths"]:
                st.write(f"✅ {strength}")
            
            # Weaknesses
            st.subheader("⚠️ Areas for Improvement")
            for weakness in report["weaknesses"]:
                st.write(f"⚡ {weakness}")
            
            st.markdown("---")
            
            # Format Analysis
            st.subheader("📊 Format-wise Performance")
            st.write(report["format_analysis"])
            
            st.markdown("---")
            
            # Recommendation
            st.subheader("🎯 Scouting Recommendation")
            st.info(report["recommendation"])
            
            # Future Outlook
            st.subheader("🔮 Future Performance Outlook")
            st.write(report["future_outlook"])


def player_comparison_page(app_resources):
    """Compare two players"""
    st.header("⚖️ Player Comparison")
    
    col1, col2 = st.columns(2)
    
    all_players = app_resources["data_loader"].get_all_players()
    
    with col1:
        player1 = st.selectbox(
            "Select Player 1:",
            all_players,
            key="compare_1"
        )
    
    with col2:
        player2 = st.selectbox(
            "Select Player 2:",
            all_players,
            key="compare_2",
            index=1 if len(all_players) > 1 else 0
        )
    
    if player1 == player2:
        st.warning("Please select two different players for comparison.")
        return
    
    if st.button("Compare Players", use_container_width=True):
        comparison = app_resources["analytics"].compare_players(player1, player2)
        
        if comparison:
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                p1_rating = app_resources["ai_analyst"]._calculate_overall_rating(comparison["player1"])
                display_stat_box(player1, f"{p1_rating:.1f}/100", "#FF6B6B")
            
            with col2:
                p2_rating = app_resources["ai_analyst"]._calculate_overall_rating(comparison["player2"])
                display_stat_box(player2, f"{p2_rating:.1f}/100", "#4ECDC4")
            
            st.markdown("---")
            
            # Comparison table
            st.subheader("Career Statistics Comparison")
            
            if "odi_comparison" in comparison:
                comp_data = {
                    "Metric": ["ODI Runs", "ODI Average"],
                    player1: [
                        comparison["odi_comparison"]["runs"]["player1"],
                        f"{comparison['odi_comparison']['average']['player1']:.2f}"
                    ],
                    player2: [
                        comparison["odi_comparison"]["runs"]["player2"],
                        f"{comparison['odi_comparison']['average']['player2']:.2f}"
                    ],
                }
                st.dataframe(pd.DataFrame(comp_data), use_container_width=True)
            
            # Radar chart comparison
            comparison_fig = app_resources["visualizations"].plot_player_comparison(
                comparison["player1"],
                comparison["player2"]
            )
            if comparison_fig:
                st.plotly_chart(comparison_fig, use_container_width=True)


def main():
    """Main application"""
    
    # Initialize resources
    app_resources = initialize_app()
    
    # Display header
    display_header()
    
    st.markdown("---")
    
    # Sidebar navigation
    with st.sidebar:
        st.markdown("### 🗂️ Navigation")
        
        page = st.radio(
            "Select a page:",
            [
                "🔍 Player Search",
                "📈 Format Analysis",
                "📊 Recent Form",
                "📉 Visualizations",
                "🤖 AI Analyst",
                "⚖️ Compare Players",
                "ℹ️ About",
            ],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        st.markdown("### 📱 App Info")
        st.write("**Cricket Analytics Pro v1.0**")
        st.write("*Advanced cricket player analytics platform*")
        
        st.markdown("### 🎯 Features")
        st.write("""
        - Player Search & Profiles
        - Career Statistics
        - Format Analysis
        - Recent Form Tracking
        - AI Scouting Reports
        - Player Comparisons
        - Advanced Visualizations
        """)
    
    # Route to selected page
    if page == "🔍 Player Search":
        search_player_page(app_resources)
    
    elif page == "📈 Format Analysis":
        format_analysis_page(app_resources)
    
    elif page == "📊 Recent Form":
        recent_form_page(app_resources)
    
    elif page == "📉 Visualizations":
        visualizations_page(app_resources)
    
    elif page == "🤖 AI Analyst":
        ai_scouting_page(app_resources)
    
    elif page == "⚖️ Compare Players":
        player_comparison_page(app_resources)
    
    elif page == "ℹ️ About":
        st.markdown("""
        # About Cricket Analytics Pro
        
        ## Overview
        Cricket Analytics Pro is a comprehensive platform for analyzing cricket players and their performance across different formats.
        
        ## Features
        
        ### 1. Player Search & Profiles
        Search and view detailed player profiles with comprehensive statistics.
        
        ### 2. Format Analysis
        Analyze player performance across:
        - Test Cricket
        - ODI Cricket
        - T20 International
        - IPL Cricket
        
        ### 3. Recent Form Tracking
        Track recent matches and detect performance trends with moving averages.
        
        ### 4. AI Scouting Reports
        Get AI-generated scouting reports including:
        - Overall player rating
        - Key strengths and weaknesses
        - Consistency analysis
        - Future performance outlook
        - Peer comparison
        
        ### 5. Advanced Visualizations
        Interactive Plotly charts showing:
        - Runs by match
        - Strike rate trends
        - Batting average comparison
        - Format-wise distribution
        - Performance timelines
        
        ### 6. Player Comparison
        Compare two players side-by-side with detailed statistics and visual comparisons.
        
        ## Data Structure
        
        The application is built with modular architecture:
        - `data_loader.py`: Data management and player database
        - `analytics.py`: Statistical calculations
        - `visualizations.py`: Plotly chart generation
        - `ai_report.py`: AI analysis and scouting reports
        - `app.py`: Main Streamlit application
        
        ## Future Enhancements
        
        - Live match data integration
        - Real API integration (ESPN, Cricket API)
        - Fantasy cricket recommendations
        - Match prediction models
        - Historical trend analysis
        - Custom dashboards
        
        ## Technologies Used
        
        - **Framework**: Streamlit
        - **Data**: Pandas, NumPy
        - **Visualization**: Plotly
        - **Analysis**: Scikit-learn
        
        ---
        
        **Built with ❤️ for cricket analytics enthusiasts**
        """)


if __name__ == "__main__":
    main()
