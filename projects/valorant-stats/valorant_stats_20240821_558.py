"""Valorant stats tracker - 2024-08-21 update #558"""
from datetime import datetime

class ValorantTracker:
    def __init__(self):
        self.matches = []
        self.player_name = "NeoLi"

    def record_match(self, kills, deaths, assists, map_name):
        match = {
            "date": "2024-08-21",
            "kills": kills,
            "deaths": deaths,
            "assists": assists,
            "map": map_name,
            "update_id": 558
        }
        self.matches.append(match)
        return match

tracker = ValorantTracker()
tracker.record_match(563, 560, 561, "Ascent")
print("Match recorded successfully")
