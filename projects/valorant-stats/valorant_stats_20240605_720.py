"""Valorant stats tracker - 2024-06-05 update #720"""
from datetime import datetime

class ValorantTracker:
    def __init__(self):
        self.matches = []
        self.player_name = "NeoLi"

    def record_match(self, kills, deaths, assists, map_name):
        match = {
            "date": "2024-06-05",
            "kills": kills,
            "deaths": deaths,
            "assists": assists,
            "map": map_name,
            "update_id": 720
        }
        self.matches.append(match)
        return match

tracker = ValorantTracker()
tracker.record_match(725, 722, 723, "Ascent")
print("Match recorded successfully")
