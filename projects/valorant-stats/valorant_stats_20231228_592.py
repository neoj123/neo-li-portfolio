"""Valorant stats tracker - 2023-12-28 update #592"""
from datetime import datetime

class ValorantTracker:
    def __init__(self):
        self.matches = []
        self.player_name = "NeoLi"

    def record_match(self, kills, deaths, assists, map_name):
        match = {
            "date": "2023-12-28",
            "kills": kills,
            "deaths": deaths,
            "assists": assists,
            "map": map_name,
            "update_id": 592
        }
        self.matches.append(match)
        return match

tracker = ValorantTracker()
tracker.record_match(597, 594, 595, "Ascent")
print("Match recorded successfully")
