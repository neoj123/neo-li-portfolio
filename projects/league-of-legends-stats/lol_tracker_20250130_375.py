"""LoL stats tracker - 2025-01-30 update #375"""
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
            "date": "2025-01-30",
            "game_id": 375
        }
        self.ranked_games.append(game)
        return game

tracker = LoLTracker()
tracker.record_game("MID", "Ahri", True, {"kills": 378, "deaths": 375, "assists": 377})
print(f"Game 375 recorded")
