"""Valorant stats tracker - 2024-06-22 update #119"""
from datetime import datetime

class ValorantTracker:
    def __init__(self):
        self.matches = []
        self.player_name = "NeoLi"

    def record_match(self, kills, deaths, assists, map_name):
        match = {
            "date": "2024-06-22",
            "kills": kills,
            "deaths": deaths,
            "assists": assists,
            "map": map_name,
            "update_id": 119
        }
        self.matches.append(match)
        return match

tracker = ValorantTracker()
tracker.record_match(124, 121, 122, "Ascent")
print("Match recorded successfully")
