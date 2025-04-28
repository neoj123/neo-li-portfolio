"""Valorant stats tracker - 2025-04-28 update #286"""
from datetime import datetime

class ValorantTracker:
    def __init__(self):
        self.matches = []
        self.player_name = "NeoLi"

    def record_match(self, kills, deaths, assists, map_name):
        match = {
            "date": "2025-04-28",
            "kills": kills,
            "deaths": deaths,
            "assists": assists,
            "map": map_name,
            "update_id": 286
        }
        self.matches.append(match)
        return match

tracker = ValorantTracker()
tracker.record_match(291, 288, 289, "Ascent")
print("Match recorded successfully")
