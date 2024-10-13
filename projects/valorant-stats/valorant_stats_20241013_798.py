"""Valorant stats tracker - 2024-10-13 update #798"""
from datetime import datetime

class ValorantTracker:
    def __init__(self):
        self.matches = []
        self.player_name = "NeoLi"

    def record_match(self, kills, deaths, assists, map_name):
        match = {
            "date": "2024-10-13",
            "kills": kills,
            "deaths": deaths,
            "assists": assists,
            "map": map_name,
            "update_id": 798
        }
        self.matches.append(match)
        return match

tracker = ValorantTracker()
tracker.record_match(803, 800, 801, "Ascent")
print("Match recorded successfully")
