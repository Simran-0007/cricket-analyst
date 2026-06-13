"""
AI Cricket Analyst Module
Generates detailed scouting reports and performance analysis.
"""

from typing import Dict, List
import random
from analytics import CricketAnalytics
from data_loader import CricketDataLoader


class AICricketAnalyst:
    """Generate AI-powered cricket analysis and scouting reports"""
    
    def __init__(self):
        self.analytics = CricketAnalytics()
        self.data_loader = CricketDataLoader()
    
    def generate_scouting_report(self, player_name: str) -> Dict:
        """Generate comprehensive scouting report for a player"""
        player = self.data_loader.get_player(player_name)
        
        if not player:
            return None
        
        overview = self.analytics.get_career_overview(player_name)
        strengths = self.analytics.get_player_strengths(player_name)
        weaknesses = self.analytics.get_player_weaknesses(player_name)
        trend = self.analytics.detect_performance_trend(player_name)
        format_analysis = self.analytics.get_format_analysis(player_name)
        
        report = {
            "player_name": player_name,
            "role": player["role"],
            "country": player["country"],
            "career_start": player.get("career_start", 2010),
            "overall_rating": self._calculate_overall_rating(overview),
            "strengths": strengths,
            "weaknesses": weaknesses,
            "recent_form": trend,
            "format_analysis": self._format_analysis_summary(format_analysis),
            "consistency_score": self._calculate_consistency(format_analysis),
            "recommendation": self._generate_recommendation(overview, strengths, weaknesses, trend),
            "future_outlook": self._generate_future_outlook(player, trend),
        }
        
        return report
    
    def _calculate_overall_rating(self, overview: Dict) -> float:
        """Calculate overall player rating (0-100)"""
        rating = 50.0  # Base rating
        
        # Batting component
        if "batting" in overview:
            batting_data = overview["batting"]
            for format_name, stats in batting_data.items():
                rating += stats.get("average", 0) / 2
                rating += stats.get("strike_rate", 0) / 5
                rating += min(stats.get("hundreds", 0) * 3, 30)
        
        # Bowling component
        if "bowling" in overview:
            bowling_data = overview["bowling"]
            for format_name, stats in bowling_data.items():
                avg = stats.get("average", 50)
                rating += max(50 - avg, 0)  # Lower average is better
                rating += max(10 - stats.get("economy_rate", 10), 0)
        
        return min(round(rating / 2, 1), 100)
    
    def _format_analysis_summary(self, format_analysis: Dict) -> str:
        """Summarize format-wise performance"""
        if not format_analysis:
            return "Limited format data available"
        
        summary_parts = []
        
        for format_name in ["Test", "ODI", "T20I", "IPL"]:
            if format_name in format_analysis:
                format_data = format_analysis[format_name]
                if "batting" in format_data:
                    avg = format_data["batting"].get("average", 0)
                    matches = format_data["batting"].get("matches", 0)
                    summary_parts.append(f"{format_name}: {matches} matches, Avg {avg}")
                elif "bowling" in format_data:
                    avg = format_data["bowling"].get("average", 0)
                    wickets = format_data["bowling"].get("wickets", 0)
                    summary_parts.append(f"{format_name}: {wickets} wickets, Avg {avg}")
        
        return " | ".join(summary_parts) if summary_parts else "Incomplete format data"
    
    def _calculate_consistency(self, format_analysis: Dict) -> float:
        """Calculate consistency score based on format performance"""
        if not format_analysis:
            return 0.0
        
        averages = []
        
        for format_name, format_data in format_analysis.items():
            if "batting" in format_data:
                averages.append(format_data["batting"].get("average", 0))
            elif "bowling" in format_data:
                avg = format_data["bowling"].get("average", 50)
                averages.append(50 - min(avg, 50))  # Invert: lower average is better for bowlers
        
        if not averages:
            return 50.0
        
        # Calculate coefficient of variation
        mean = sum(averages) / len(averages)
        if mean == 0:
            return 0.0
        
        variance = sum((x - mean) ** 2 for x in averages) / len(averages)
        std_dev = variance ** 0.5
        cv = (std_dev / mean) * 100 if mean != 0 else 0
        
        # Lower CV means more consistent
        consistency = max(100 - cv, 0)
        return round(consistency, 1)
    
    def _generate_recommendation(self, overview: Dict, strengths: List[str], 
                                weaknesses: List[str], trend: Dict) -> str:
        """Generate scouting recommendation"""
        
        trend_status = trend.get("trend", "Inconsistent")
        
        if trend_status == "Improving Form ↗":
            return "RECOMMENDED: Player is in excellent form. Strong performance metrics and upward trajectory indicate readiness for selection."
        elif trend_status == "Declining Form ↘":
            return "CAUTION: Player is experiencing a form slump. Monitor recent performances and consider alternative options."
        else:
            if len(strengths) > len(weaknesses):
                return "RECOMMENDED: Consistent performer with strong fundamentals. Suitable for squad selection."
            else:
                return "WATCH: Monitor player development. Notable strengths but areas for improvement noted."
    
    def _generate_future_outlook(self, player: Dict, trend: Dict) -> str:
        """Generate future performance outlook"""
        
        career_start = player.get("career_start", 2010)
        current_year = 2024
        years_active = current_year - career_start
        
        trend_status = trend.get("trend", "Consistent")
        
        outlook_parts = []
        
        # Age and experience factor
        if years_active < 5:
            outlook_parts.append("Early career stage with growth potential")
        elif years_active < 10:
            outlook_parts.append("Peak performance years ahead")
        else:
            outlook_parts.append("Experienced player approaching twilight years")
        
        # Form factor
        if trend_status == "Improving Form ↗":
            outlook_parts.append("Positive trajectory suggests sustained performance")
        elif trend_status == "Declining Form ↘":
            outlook_parts.append("May face challenges in competitive fixtures")
        else:
            outlook_parts.append("Expected to maintain current performance levels")
        
        return ". ".join(outlook_parts) + "."
    
    def compare_with_peers(self, player_name: str) -> Dict:
        """Compare player performance with peers"""
        player = self.data_loader.get_player(player_name)
        
        if not player:
            return None
        
        # Get all players for comparison
        all_players = self.data_loader.get_all_players()
        
        # Filter peers (same role and country if possible)
        peers = [p for p in all_players if p != player_name]
        
        player_rating = self._calculate_overall_rating(
            self.analytics.get_career_overview(player_name)
        )
        
        peer_ratings = []
        for peer in peers[:5]:  # Top 5 peers
            peer_rating = self._calculate_overall_rating(
                self.analytics.get_career_overview(peer)
            )
            peer_ratings.append({"name": peer, "rating": peer_rating})
        
        # Sort by rating
        peer_ratings.sort(key=lambda x: x["rating"], reverse=True)
        
        rank = 1
        for idx, peer in enumerate(peer_ratings):
            if peer["rating"] > player_rating:
                rank += 1
        
        return {
            "player_name": player_name,
            "rating": player_rating,
            "rank": rank,
            "total_peers": len(peers),
            "top_peers": peer_ratings[:5],
        }


# Global AI analyst instance
def get_ai_analyst():
    """Get or create AI analyst instance"""
    return AICricketAnalyst()
