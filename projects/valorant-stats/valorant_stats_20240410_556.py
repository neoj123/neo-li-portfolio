"""Valorant stats tracker - 2024-04-10 update #556"""
from datetime import datetime

class ValorantTracker:
    def __init__(self):
        self.matches = []
        self.player_name = "NeoLi"

    def record_match(self, kills, deaths, assists, map_name):
        match = {
            "date": "2024-04-10",
            "kills": kills,
            "deaths": deaths,
            "assists": assists,
            "map": map_name,
            "update_id": 556
        }
        self.matches.append(match)
        return match

tracker = ValorantTracker()
tracker.record_match(561, 558, 559, "Ascent")
print("Match recorded successfully")
