"""
Cricket Analytics Module
Performs various statistical analyses on cricket player data.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple
from datetime import datetime, timedelta
from data_loader import CricketDataLoader


class CricketAnalytics:
    """Perform cricket analytics calculations"""
    
    def __init__(self):
        self.data_loader = CricketDataLoader()
    
    def get_career_overview(self, player_name: str) -> Dict:
        """Get comprehensive career overview for a player"""
        player = self.data_loader.get_player(player_name)
        
        if not player:
            return None
        
        overview = {
            "name": player["name"],
            "role": player["role"],
            "country": player["country"],
            "career_start": player.get("career_start", 2010),
            "types": ["International"],
        }
        
        # Aggregate batting stats
        batting_stats = {}
        for format_key in ["test_batting", "odi_batting", "t20i_batting"]:
            if format_key in player:
                format_name = format_key.split("_")[0].upper()
                batting_stats[format_name] = player[format_key]
        
        if batting_stats:
            overview["batting"] = batting_stats
        
        # Aggregate bowling stats
        bowling_stats = {}
        for format_key in ["test_bowling", "odi_bowling", "t20i_bowling"]:
            if format_key in player:
                format_name = format_key.split("_")[0].upper()
                bowling_stats[format_name] = player[format_key]
        
        if bowling_stats:
            overview["bowling"] = bowling_stats
        
        # IPL stats
        if "ipl_stats" in player:
            overview["types"].append("IPL")
            overview["ipl_team"] = player.get("ipl_team", "Unknown")
            overview["ipl_stats"] = player["ipl_stats"]
        
        return overview
    
    def calculate_batting_average(self, runs: int, innings: int) -> float:
        """Calculate batting average (runs / innings)"""
        return round(runs / max(innings, 1), 2)
    
    def calculate_strike_rate(self, runs: int, balls: int) -> float:
        """Calculate strike rate (runs / balls * 100)"""
        return round((runs / max(balls, 1)) * 100, 2)
    
    def calculate_economy_rate(self, runs_conceded: int, overs: float) -> float:
        """Calculate economy rate (runs conceded / overs)"""
        return round(runs_conceded / max(overs, 1), 2)
    
    def calculate_bowling_average(self, runs_conceded: int, wickets: int) -> float:
        """Calculate bowling average (runs conceded / wickets)"""
        return round(runs_conceded / max(wickets, 1), 2)
    
    def get_format_analysis(self, player_name: str) -> Dict:
        """Analyze player performance across different formats"""
        player = self.data_loader.get_player(player_name)
        
        if not player:
            return None
        
        analysis = {}
        
        # Test Cricket
        if "test_batting" in player or "test_bowling" in player:
            analysis["Test"] = {}
            if "test_batting" in player:
                analysis["Test"]["batting"] = player["test_batting"]
            if "test_bowling" in player:
                analysis["Test"]["bowling"] = player["test_bowling"]
        
        # ODI Cricket
        if "odi_batting" in player or "odi_bowling" in player:
            analysis["ODI"] = {}
            if "odi_batting" in player:
                analysis["ODI"]["batting"] = player["odi_batting"]
            if "odi_bowling" in player:
                analysis["ODI"]["bowling"] = player["odi_bowling"]
        
        # T20 International
        if "t20i_batting" in player or "t20i_bowling" in player:
            analysis["T20I"] = {}
            if "t20i_batting" in player:
                analysis["T20I"]["batting"] = player["t20i_batting"]
            if "t20i_bowling" in player:
                analysis["T20I"]["bowling"] = player["t20i_bowling"]
        
        # IPL
        if "ipl_stats" in player:
            analysis["IPL"] = player["ipl_stats"]
        
        return analysis
    
    def get_recent_form(self, player_name: str, matches: int = 5) -> pd.DataFrame:
        """Get recent form analysis"""
        recent_matches = self.data_loader.get_recent_matches(player_name)
        
        if recent_matches.empty:
            return pd.DataFrame()
        
        # Get most recent matches
        df = recent_matches.head(matches).copy()
        
        # Calculate rolling averages
        df["runs_ma"] = df["runs"].rolling(window=3, min_periods=1).mean()
        df["wickets_ma"] = df["wickets"].rolling(window=3, min_periods=1).mean()
        
        return df
    
    def detect_performance_trend(self, player_name: str) -> Dict:
        """Detect performance trends from recent matches"""
        recent_matches = self.data_loader.get_recent_matches(player_name)
        
        if recent_matches.empty or len(recent_matches) < 3:
            return {"trend": "Insufficient data", "confidence": 0}
        
        # Analyze runs trend
        runs_values = recent_matches["runs"].head(10).values
        if len(runs_values) > 0:
            recent_avg = np.mean(runs_values[:5])
            older_avg = np.mean(runs_values[5:])
            
            if recent_avg > older_avg * 1.2:
                trend = "Improving Form ↗"
            elif recent_avg < older_avg * 0.8:
                trend = "Declining Form ↘"
            else:
                trend = "Consistent Form →"
            
            confidence = min(abs((recent_avg - older_avg) / max(older_avg, 1)) * 100, 100)
            
            return {
                "trend": trend,
                "confidence": round(confidence, 1),
                "recent_average": round(recent_avg, 2),
                "older_average": round(older_avg, 2),
            }
        
        return {"trend": "Insufficient data", "confidence": 0}
    
    def compare_players(self, player1_name: str, player2_name: str) -> Dict:
        """Compare two players side by side"""
        player1 = self.data_loader.get_player(player1_name)
        player2 = self.data_loader.get_player(player2_name)
        
        if not player1 or not player2:
            return None
        
        comparison = {
            "player1": self.get_career_overview(player1_name),
            "player2": self.get_career_overview(player2_name),
        }
        
        # Calculate head-to-head stats if applicable
        if "odi_batting" in player1 and "odi_batting" in player2:
            comp_odi_runs = {
                "player1": player1["odi_batting"]["runs"],
                "player2": player2["odi_batting"]["runs"],
            }
            comp_odi_avg = {
                "player1": player1["odi_batting"]["average"],
                "player2": player2["odi_batting"]["average"],
            }
            comparison["odi_comparison"] = {
                "runs": comp_odi_runs,
                "average": comp_odi_avg,
            }
        
        return comparison
    
    def get_player_strengths(self, player_name: str) -> List[str]:
        """Identify key strengths of a player"""
        player = self.data_loader.get_player(player_name)
        
        if not player:
            return []
        
        strengths = []
        
        # Check batting strengths
        for format_key in ["test_batting", "odi_batting", "t20i_batting"]:
            if format_key in player:
                stats = player[format_key]
                if stats.get("average", 0) > 40:
                    strengths.append(f"Strong batting average in {format_key.split('_')[0].upper()}: {stats['average']}")
                if stats.get("strike_rate", 0) > 130:
                    strengths.append(f"High strike rate in {format_key.split('_')[0].upper()}: {stats['strike_rate']}")
                if stats.get("hundreds", 0) >= 5:
                    strengths.append(f"Multiple centuries ({stats['hundreds']}) in {format_key.split('_')[0].upper()}")
        
        # Check bowling strengths
        for format_key in ["test_bowling", "odi_bowling", "t20i_bowling"]:
            if format_key in player:
                stats = player[format_key]
                if stats.get("average", 100) < 30:
                    strengths.append(f"Excellent bowling average in {format_key.split('_')[0].upper()}: {stats['average']}")
                if stats.get("economy_rate", 10) < 7:
                    strengths.append(f"Tight economy rate in {format_key.split('_')[0].upper()}: {stats['economy_rate']}")
        
        return strengths if strengths else ["Consistent performer", "Versatile across formats"]
    
    def get_player_weaknesses(self, player_name: str) -> List[str]:
        """Identify potential weaknesses of a player"""
        player = self.data_loader.get_player(player_name)
        
        if not player:
            return []
        
        weaknesses = []
        
        # Check batting weaknesses
        for format_key in ["test_batting", "odi_batting", "t20i_batting"]:
            if format_key in player:
                stats = player[format_key]
                if stats.get("average", 0) < 25:
                    weaknesses.append(f"Lower batting average in {format_key.split('_')[0].upper()}: {stats['average']}")
                if stats.get("hundreds", 0) == 0 and stats.get("matches", 0) > 20:
                    weaknesses.append(f"Limited centuries in {format_key.split('_')[0].upper()} ({stats['matches']} matches)")
        
        # Check bowling weaknesses
        for format_key in ["test_bowling", "odi_bowling", "t20i_bowling"]:
            if format_key in player:
                stats = player[format_key]
                if stats.get("economy_rate", 0) > 8:
                    weaknesses.append(f"High economy rate in {format_key.split('_')[0].upper()}: {stats['economy_rate']}")
        
        return weaknesses if weaknesses else ["Consistent performer"]


# Global analytics instance
def get_analytics():
    """Get or create analytics instance"""
    return CricketAnalytics()
