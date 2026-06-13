"""
Cricket Visualizations Module
Creates interactive charts and visualizations using Plotly.
"""

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from typing import Dict, List
import numpy as np


class CricketVisualizations:
    """Create cricket analytics visualizations"""
    
    @staticmethod
    def plot_runs_by_match(recent_matches: pd.DataFrame, player_name: str):
        """Plot runs scored in recent matches"""
        if recent_matches.empty:
            return None
        
        df = recent_matches.copy()
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values('date')
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=df['date'],
            y=df['runs'],
            mode='lines+markers',
            name='Runs',
            line=dict(color='#FF6B6B', width=2),
            marker=dict(size=8),
        ))
        
        # Add moving average
        df['runs_ma'] = df['runs'].rolling(window=3, min_periods=1).mean()
        fig.add_trace(go.Scatter(
            x=df['date'],
            y=df['runs_ma'],
            mode='lines',
            name='3-Match Average',
            line=dict(color='#4ECDC4', width=2, dash='dash'),
        ))
        
        fig.update_layout(
            title=f"Runs Trend - {player_name}",
            xaxis_title="Date",
            yaxis_title="Runs",
            hovermode='x unified',
            template='plotly_dark',
            height=400,
            margin=dict(l=40, r=40, t=40, b=40),
        )
        
        return fig
    
    @staticmethod
    def plot_strike_rate_trend(recent_matches: pd.DataFrame, player_name: str):
        """Plot strike rate trend"""
        if recent_matches.empty:
            return None
        
        df = recent_matches.copy()
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values('date')
        
        # Simulate strike rate (runs / balls * 100)
        df['strike_rate'] = (df['runs'] / np.maximum(df['runs'] / 0.5, 1)) * 100
        df['strike_rate'] = df['strike_rate'].rolling(window=3, min_periods=1).mean()
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=df['date'],
            y=df['strike_rate'],
            mode='lines+markers',
            name='Strike Rate',
            fill='tozeroy',
            line=dict(color='#95E1D3', width=2),
            marker=dict(size=8),
        ))
        
        fig.update_layout(
            title=f"Strike Rate Trend - {player_name}",
            xaxis_title="Date",
            yaxis_title="Strike Rate",
            hovermode='x unified',
            template='plotly_dark',
            height=400,
            margin=dict(l=40, r=40, t=40, b=40),
        )
        
        return fig
    
    @staticmethod
    def plot_batting_comparison(formats: Dict[str, Dict]) -> go.Figure:
        """Plot batting average comparison across formats"""
        if not formats:
            return None
        
        format_names = []
        averages = []
        
        for format_name, format_data in formats.items():
            if "batting" in format_data:
                format_names.append(format_name)
                averages.append(format_data["batting"].get("average", 0))
        
        fig = go.Figure(data=[
            go.Bar(
                x=format_names,
                y=averages,
                marker=dict(
                    color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A'],
                    line=dict(color='white', width=2),
                ),
                text=averages,
                textposition='outside',
            )
        ])
        
        fig.update_layout(
            title="Batting Average by Format",
            xaxis_title="Format",
            yaxis_title="Average",
            template='plotly_dark',
            height=400,
            showlegend=False,
            margin=dict(l=40, r=40, t=40, b=40),
        )
        
        return fig
    
    @staticmethod
    def plot_runs_by_format(formats: Dict[str, Dict]) -> go.Figure:
        """Plot total runs by format"""
        if not formats:
            return None
        
        format_names = []
        runs = []
        
        for format_name, format_data in formats.items():
            if "batting" in format_data:
                format_names.append(format_name)
                runs.append(format_data["batting"].get("runs", 0))
        
        fig = go.Figure(data=[
            go.Pie(
                labels=format_names,
                values=runs,
                marker=dict(colors=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']),
                hovertemplate='<b>%{label}</b><br>Runs: %{value:,.0f}<br>%{percent}<extra></extra>',
            )
        ])
        
        fig.update_layout(
            title="Total Runs Distribution by Format",
            template='plotly_dark',
            height=400,
            margin=dict(l=40, r=40, t=40, b=40),
        )
        
        return fig
    
    @staticmethod
    def plot_wickets_by_format(formats: Dict[str, Dict]) -> go.Figure:
        """Plot wickets by format"""
        if not formats:
            return None
        
        format_names = []
        wickets = []
        
        for format_name, format_data in formats.items():
            if "bowling" in format_data:
                format_names.append(format_name)
                wickets.append(format_data["bowling"].get("wickets", 0))
        
        fig = go.Figure(data=[
            go.Bar(
                x=format_names,
                y=wickets,
                marker=dict(
                    color=['#9B59B6', '#E74C3C', '#3498DB', '#F39C12'],
                    line=dict(color='white', width=2),
                ),
                text=wickets,
                textposition='outside',
            )
        ])
        
        fig.update_layout(
            title="Wickets by Format",
            xaxis_title="Format",
            yaxis_title="Wickets",
            template='plotly_dark',
            height=400,
            showlegend=False,
            margin=dict(l=40, r=40, t=40, b=40),
        )
        
        return fig
    
    @staticmethod
    def plot_player_comparison(player1_stats: Dict, player2_stats: Dict) -> go.Figure:
        """Compare two players with radar chart"""
        
        # Extract comparable stats
        metrics = []
        p1_values = []
        p2_values = []
        
        if "batting" in player1_stats and "batting" in player2_stats:
            for format_name in player1_stats["batting"]:
                if format_name in player2_stats["batting"]:
                    metrics.append(f"{format_name} Avg")
                    p1_values.append(player1_stats["batting"][format_name].get("average", 0))
                    p2_values.append(player2_stats["batting"][format_name].get("average", 0))
        
        # Normalize values for better visualization
        if metrics:
            max_val = max(max(p1_values), max(p2_values))
            if max_val > 0:
                p1_values = [v / max_val * 100 for v in p1_values]
                p2_values = [v / max_val * 100 for v in p2_values]
        else:
            metrics = ["Stat1", "Stat2"]
            p1_values = [50, 50]
            p2_values = [50, 50]
        
        fig = go.Figure(data=[
            go.Scatterpolar(
                r=p1_values,
                theta=metrics,
                fill='toself',
                name=player1_stats["name"],
                line=dict(color='#FF6B6B'),
            ),
            go.Scatterpolar(
                r=p2_values,
                theta=metrics,
                fill='toself',
                name=player2_stats["name"],
                line=dict(color='#4ECDC4'),
            ),
        ])
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100],
                ),
            ),
            title="Player Comparison",
            template='plotly_dark',
            height=500,
            margin=dict(l=40, r=40, t=40, b=40),
        )
        
        return fig
    
    @staticmethod
    def plot_performance_timeline(recent_matches: pd.DataFrame) -> go.Figure:
        """Plot performance timeline with multiple metrics"""
        if recent_matches.empty:
            return None
        
        df = recent_matches.copy()
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values('date')
        
        fig = make_subplots(
            rows=2, cols=1,
            shared_xaxes=True,
            vertical_spacing=0.1,
            subplot_titles=("Runs Scored", "Wickets Taken"),
        )
        
        fig.add_trace(
            go.Bar(x=df['date'], y=df['runs'], name='Runs', marker=dict(color='#FF6B6B')),
            row=1, col=1,
        )
        
        fig.add_trace(
            go.Bar(x=df['date'], y=df['wickets'], name='Wickets', marker=dict(color='#9B59B6')),
            row=2, col=1,
        )
        
        fig.update_layout(
            template='plotly_dark',
            height=600,
            hovermode='x unified',
            margin=dict(l=40, r=40, t=60, b=40),
        )
        
        return fig


# Global visualizations instance
def get_visualizations():
    """Get visualizations module"""
    return CricketVisualizations()
