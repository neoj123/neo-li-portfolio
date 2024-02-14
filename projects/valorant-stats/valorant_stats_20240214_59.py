"""Valorant stats tracker - 2024-02-14 update #59"""
from datetime import datetime

class ValorantTracker:
    def __init__(self):
        self.matches = []
        self.player_name = "NeoLi"

    def record_match(self, kills, deaths, assists, map_name):
        match = {
            "date": "2024-02-14",
            "kills": kills,
            "deaths": deaths,
            "assists": assists,
            "map": map_name,
            "update_id": 59
        }
        self.matches.append(match)
        return match

tracker = ValorantTracker()
tracker.record_match(64, 61, 62, "Ascent")
print("Match recorded successfully")
