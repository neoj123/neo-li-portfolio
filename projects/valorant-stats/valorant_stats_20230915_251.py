"""Valorant stats tracker - 2023-09-15 update #251"""
from datetime import datetime

class ValorantTracker:
    def __init__(self):
        self.matches = []
        self.player_name = "NeoLi"

    def record_match(self, kills, deaths, assists, map_name):
        match = {
            "date": "2023-09-15",
            "kills": kills,
            "deaths": deaths,
            "assists": assists,
            "map": map_name,
            "update_id": 251
        }
        self.matches.append(match)
        return match

tracker = ValorantTracker()
tracker.record_match(256, 253, 254, "Ascent")
print("Match recorded successfully")
