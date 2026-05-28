"""Valorant stats tracker - 2026-05-28 update #122"""
from datetime import datetime

class ValorantTracker:
    def __init__(self):
        self.matches = []
        self.player_name = "NeoLi"

    def record_match(self, kills, deaths, assists, map_name):
        match = {
            "date": "2026-05-28",
            "kills": kills,
            "deaths": deaths,
            "assists": assists,
            "map": map_name,
            "update_id": 122
        }
        self.matches.append(match)
        return match

tracker = ValorantTracker()
tracker.record_match(127, 124, 125, "Ascent")
print("Match recorded successfully")
