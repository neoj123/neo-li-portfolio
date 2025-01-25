"""LoL stats tracker - 2025-01-25 update #885"""
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
            "date": "2025-01-25",
            "game_id": 885
        }
        self.ranked_games.append(game)
        return game

tracker = LoLTracker()
tracker.record_game("MID", "Ahri", True, {"kills": 888, "deaths": 885, "assists": 887})
print(f"Game 885 recorded")
