"""Valorant stats tracker - 2024-08-26 update #17"""
from datetime import datetime

class ValorantTracker:
    def __init__(self):
        self.matches = []
        self.player_name = "NeoLi"

    def record_match(self, kills, deaths, assists, map_name):
        match = {
            "date": "2024-08-26",
            "kills": kills,
            "deaths": deaths,
            "assists": assists,
            "map": map_name,
            "update_id": 17
        }
        self.matches.append(match)
        return match

tracker = ValorantTracker()
tracker.record_match(22, 19, 20, "Ascent")
print("Match recorded successfully")
