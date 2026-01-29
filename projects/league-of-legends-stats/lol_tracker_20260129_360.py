"""LoL stats tracker - 2026-01-29 update #360"""
class LoLTracker:
    def __init__(self):
        self.ranked_games = []
        self.summoner = "NeoLi123"

    def record_game(self, lane, champion, won, kda):
        game = {
            "lane": lane,
            "champion": champion,
            "won": won,
            "kda": kda,
            "date": "2026-01-29",
            "game_id": 360
        }
        self.ranked_games.append(game)
        return game

tracker = LoLTracker()
tracker.record_game("MID", "Ahri", True, {"kills": 363, "deaths": 360, "assists": 362})
print(f"Game 360 recorded")
