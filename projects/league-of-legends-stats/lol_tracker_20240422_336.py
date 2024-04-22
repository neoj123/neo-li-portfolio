"""LoL stats tracker - 2024-04-22 update #336"""
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
            "date": "2024-04-22",
            "game_id": 336
        }
        self.ranked_games.append(game)
        return game

tracker = LoLTracker()
tracker.record_game("MID", "Ahri", True, {"kills": 339, "deaths": 336, "assists": 338})
print(f"Game 336 recorded")
