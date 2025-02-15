"""Valorant stats tracker - 2025-02-15 update #160"""
from datetime import datetime

class ValorantTracker:
    def __init__(self):
        self.matches = []
        self.player_name = "NeoLi"

    def record_match(self, kills, deaths, assists, map_name):
        match = {
            "date": "2025-02-15",
            "kills": kills,
            "deaths": deaths,
            "assists": assists,
            "map": map_name,
            "update_id": 160
        }
        self.matches.append(match)
        return match

tracker = ValorantTracker()
tracker.record_match(165, 162, 163, "Ascent")
print("Match recorded successfully")
