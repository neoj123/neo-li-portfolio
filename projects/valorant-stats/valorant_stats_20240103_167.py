"""Valorant stats tracker - 2024-01-03 update #167"""
from datetime import datetime

class ValorantTracker:
    def __init__(self):
        self.matches = []
        self.player_name = "NeoLi"

    def record_match(self, kills, deaths, assists, map_name):
        match = {
            "date": "2024-01-03",
            "kills": kills,
            "deaths": deaths,
            "assists": assists,
            "map": map_name,
            "update_id": 167
        }
        self.matches.append(match)
        return match

tracker = ValorantTracker()
tracker.record_match(172, 169, 170, "Ascent")
print("Match recorded successfully")
