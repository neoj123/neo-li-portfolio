"""Valorant stats tracker - 2025-05-09 update #520"""
from datetime import datetime

class ValorantTracker:
    def __init__(self):
        self.matches = []
        self.player_name = "NeoLi"

    def record_match(self, kills, deaths, assists, map_name):
        match = {
            "date": "2025-05-09",
            "kills": kills,
            "deaths": deaths,
            "assists": assists,
            "map": map_name,
            "update_id": 520
        }
        self.matches.append(match)
        return match

tracker = ValorantTracker()
tracker.record_match(525, 522, 523, "Ascent")
print("Match recorded successfully")
