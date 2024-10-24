"""Valorant stats tracker - 2024-10-24 update #397"""
from datetime import datetime

class ValorantTracker:
    def __init__(self):
        self.matches = []
        self.player_name = "NeoLi"

    def record_match(self, kills, deaths, assists, map_name):
        match = {
            "date": "2024-10-24",
            "kills": kills,
            "deaths": deaths,
            "assists": assists,
            "map": map_name,
            "update_id": 397
        }
        self.matches.append(match)
        return match

tracker = ValorantTracker()
tracker.record_match(402, 399, 400, "Ascent")
print("Match recorded successfully")
