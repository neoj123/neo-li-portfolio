"""Valorant stats tracker - 2025-08-01 update #591"""
from datetime import datetime

class ValorantTracker:
    def __init__(self):
        self.matches = []
        self.player_name = "NeoLi"

    def record_match(self, kills, deaths, assists, map_name):
        match = {
            "date": "2025-08-01",
            "kills": kills,
            "deaths": deaths,
            "assists": assists,
            "map": map_name,
            "update_id": 591
        }
        self.matches.append(match)
        return match

tracker = ValorantTracker()
tracker.record_match(596, 593, 594, "Ascent")
print("Match recorded successfully")
