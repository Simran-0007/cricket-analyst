"""
Cricket Analytics Data Loader
Generates mock cricket player data for international and IPL players.
Can be extended to fetch real data from APIs.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
import random

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)


class CricketDataLoader:
    """Load and manage cricket player data"""
    
    def __init__(self):
        self.players_db = {}
        self.load_sample_data()
    
    def load_sample_data(self):
        """Load sample cricket data for demonstration"""
        
        # International players
        international_players = [
            {"name": "Virat Kohli", "type": "International", "role": "Batsman", "country": "India"},
            {"name": "Steve Smith", "type": "International", "role": "Batsman", "country": "Australia"},
            {"name": "Babar Azam", "type": "International", "role": "Batsman", "country": "Pakistan"},
            {"name": "Pat Cummins", "type": "International", "role": "Bowler", "country": "Australia"},
            {"name": "Jasprit Bumrah", "type": "International", "role": "Bowler", "country": "India"},
            {"name": "Kane Williamson", "type": "International", "role": "Batsman", "country": "New Zealand"},
            {"name": "Ben Stokes", "type": "International", "role": "All-rounder", "country": "England"},
            {"name": "Rashid Khan", "type": "International", "role": "Bowler", "country": "Afghanistan"},
            {"name": "KL Rahul", "type": "International", "role": "Batsman", "country": "India"},
            {"name": "Rohit Sharma", "type": "International", "role": "Batsman", "country": "India"},
        ]
        
        # IPL players (with international players + IPL-specific)
        ipl_players = [
            {"name": "Virat Kohli", "type": "IPL", "role": "Batsman", "country": "India", "team": "Royal Challengers Bangalore"},
            {"name": "Rohit Sharma", "type": "IPL", "role": "Batsman", "country": "India", "team": "Mumbai Indians"},
            {"name": "MS Dhoni", "type": "IPL", "role": "Batsman", "country": "India", "team": "Chennai Super Kings"},
            {"name": "Suresh Raina", "type": "IPL", "role": "Batsman", "country": "India", "team": "Chennai Super Kings"},
            {"name": "Hardik Pandya", "type": "IPL", "role": "All-rounder", "country": "India", "team": "Mumbai Indians"},
            {"name": "Rishabh Pant", "type": "IPL", "role": "Batsman", "country": "India", "team": "Delhi Capitals"},
            {"name": "KL Rahul", "type": "IPL", "role": "Batsman", "country": "India", "team": "Lucknow Super Giants"},
            {"name": "David Warner", "type": "IPL", "role": "Batsman", "country": "Australia", "team": "Delhi Capitals"},
            {"name": "AB de Villiers", "type": "IPL", "role": "Batsman", "country": "South Africa", "team": "Royal Challengers Bangalore"},
            {"name": "Yuzvendra Chahal", "type": "IPL", "role": "Bowler", "country": "India", "team": "Rajasthan Royals"},
        ]
        
        # Create player profiles
        for player in international_players:
            self.players_db[player["name"]] = self._generate_player_stats(player)
        
        for player in ipl_players:
            if player["name"] in self.players_db:
                # Add IPL stats to existing international player
                self.players_db[player["name"]]["ipl_stats"] = self._generate_ipl_stats(player)
                self.players_db[player["name"]]["ipl_team"] = player["team"]
            else:
                self.players_db[player["name"]] = self._generate_player_stats(player)
                self.players_db[player["name"]]["ipl_stats"] = self._generate_ipl_stats(player)
                self.players_db[player["name"]]["ipl_team"] = player["team"]
    
    def _generate_player_stats(self, player: Dict) -> Dict:
        """Generate realistic cricket statistics for a player"""
        
        role = player["role"]
        is_batsman = role in ["Batsman", "All-rounder"]
        is_bowler = role in ["Bowler", "All-rounder"]
        
        stats = {
            "name": player["name"],
            "type": player["type"],
            "role": role,
            "country": player["country"],
            "career_start": 2010 + random.randint(-5, 5),
        }
        
        # Test Cricket Stats (if applicable)
        if is_batsman:
            test_matches = random.randint(20, 100)
            test_runs = random.randint(2000, 12000)
            test_avg = round(test_runs / max(test_matches, 1), 2)
            stats["test_batting"] = {
                "matches": test_matches,
                "innings": random.randint(test_matches - 5, test_matches),
                "runs": test_runs,
                "average": test_avg,
                "highest_score": random.randint(100, 300),
                "hundreds": random.randint(0, test_matches // 8),
                "fifties": random.randint(0, test_matches // 5),
                "strike_rate": round(random.uniform(50, 80), 2),
            }
        
        if is_bowler:
            test_matches = random.randint(15, 80)
            test_wickets = random.randint(50, 600)
            test_avg = round(random.uniform(20, 40), 2)
            stats["test_bowling"] = {
                "matches": test_matches,
                "wickets": test_wickets,
                "runs_conceded": test_wickets * test_avg * 1.2,
                "average": test_avg,
                "economy_rate": round(random.uniform(2.5, 3.5), 2),
                "best_figures": f"{random.randint(3, 8)}/{random.randint(20, 60)}",
            }
        
        # ODI Stats
        if is_batsman:
            odi_matches = random.randint(50, 200)
            odi_runs = random.randint(2000, 13000)
            odi_avg = round(odi_runs / max(odi_matches, 1), 2)
            stats["odi_batting"] = {
                "matches": odi_matches,
                "innings": random.randint(odi_matches - 10, odi_matches),
                "runs": odi_runs,
                "average": odi_avg,
                "highest_score": random.randint(100, 200),
                "hundreds": random.randint(0, odi_matches // 10),
                "fifties": random.randint(0, odi_matches // 5),
                "strike_rate": round(random.uniform(85, 105), 2),
            }
        
        if is_bowler:
            odi_matches = random.randint(40, 150)
            odi_wickets = random.randint(80, 500)
            stats["odi_bowling"] = {
                "matches": odi_matches,
                "wickets": odi_wickets,
                "runs_conceded": odi_wickets * 25,
                "average": round(random.uniform(23, 35), 2),
                "economy_rate": round(random.uniform(4.0, 5.5), 2),
                "best_figures": f"{random.randint(3, 7)}/{random.randint(25, 50)}",
            }
        
        # T20I Stats
        if is_batsman:
            t20i_matches = random.randint(40, 150)
            t20i_runs = random.randint(1000, 4000)
            t20i_avg = round(t20i_runs / max(t20i_matches, 1), 2)
            stats["t20i_batting"] = {
                "matches": t20i_matches,
                "innings": random.randint(t20i_matches - 8, t20i_matches),
                "runs": t20i_runs,
                "average": t20i_avg,
                "highest_score": random.randint(50, 120),
                "hundreds": random.randint(0, 2),
                "fifties": random.randint(0, t20i_matches // 8),
                "strike_rate": round(random.uniform(130, 160), 2),
            }
        
        if is_bowler:
            t20i_matches = random.randint(30, 100)
            t20i_wickets = random.randint(40, 200)
            stats["t20i_bowling"] = {
                "matches": t20i_matches,
                "wickets": t20i_wickets,
                "runs_conceded": t20i_wickets * 18,
                "average": round(random.uniform(18, 30), 2),
                "economy_rate": round(random.uniform(6.0, 8.5), 2),
                "best_figures": f"{random.randint(2, 5)}/{random.randint(15, 35)}",
            }
        
        return stats
    
    def _generate_ipl_stats(self, player: Dict) -> Dict:
        """Generate IPL-specific statistics"""
        
        role = player["role"]
        is_batsman = role in ["Batsman", "All-rounder"]
        is_bowler = role in ["Bowler", "All-rounder"]
        
        stats = {}
        
        if is_batsman:
            ipl_matches = random.randint(30, 200)
            ipl_runs = random.randint(800, 7000)
            stats["batting"] = {
                "matches": ipl_matches,
                "innings": random.randint(ipl_matches - 5, ipl_matches),
                "runs": ipl_runs,
                "average": round(ipl_runs / max(ipl_matches, 1), 2),
                "highest_score": random.randint(50, 120),
                "hundreds": random.randint(0, 3),
                "fifties": random.randint(0, ipl_matches // 6),
                "strike_rate": round(random.uniform(125, 155), 2),
            }
        
        if is_bowler:
            ipl_matches = random.randint(25, 150)
            ipl_wickets = random.randint(30, 180)
            stats["bowling"] = {
                "matches": ipl_matches,
                "wickets": ipl_wickets,
                "runs_conceded": ipl_wickets * 22,
                "average": round(random.uniform(22, 35), 2),
                "economy_rate": round(random.uniform(7.0, 9.5), 2),
                "best_figures": f"{random.randint(2, 5)}/{random.randint(20, 40)}",
            }
        
        return stats
    
    def _generate_recent_matches(self, num_matches: int = 20) -> pd.DataFrame:
        """Generate recent match data"""
        matches = []
        for i in range(num_matches):
            date = datetime.now() - timedelta(days=i*7)
            if np.random.random() > 0.4:  # 60% of matches have runs
                runs = random.randint(0, 150)
            else:
                runs = 0
            
            if np.random.random() > 0.5:  # 50% of matches have wickets
                wickets = random.randint(0, 5)
            else:
                wickets = 0
            
            matches.append({
                "date": date.strftime("%Y-%m-%d"),
                "format": random.choice(["Test", "ODI", "T20I", "IPL"]),
                "opponent": random.choice(["India", "Australia", "Pakistan", "England", "West Indies", "RCB", "MI", "CSK"]),
                "runs": runs,
                "wickets": wickets,
                "venue": random.choice(["Lords", "MCG", "Eden Gardens", "SCG", "Wankhede", "Arun Jaitley"]),
            })
        
        return pd.DataFrame(matches)
    
    def get_player(self, name: str) -> Dict:
        """Get player statistics by name"""
        for player_name in self.players_db:
            if player_name.lower() == name.lower():
                return self.players_db[player_name]
        return None
    
    def search_players(self, query: str) -> List[str]:
        """Search players by partial name match"""
        query_lower = query.lower()
        return [name for name in self.players_db.keys() 
                if query_lower in name.lower()]
    
    def get_all_players(self) -> List[str]:
        """Get list of all players"""
        return sorted(list(self.players_db.keys()))
    
    def get_recent_matches(self, player_name: str) -> pd.DataFrame:
        """Get recent matches for a player"""
        if player_name in self.players_db:
            return self._generate_recent_matches(20)
        return pd.DataFrame()


# Global data loader instance
@staticmethod
def get_data_loader():
    """Get or create data loader instance"""
    return CricketDataLoader()
