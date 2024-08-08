"""LoL stats tracker - 2024-08-08 update #15"""
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
            "date": "2024-08-08",
            "game_id": 15
        }
        self.ranked_games.append(game)
        return game

tracker = LoLTracker()
tracker.record_game("MID", "Ahri", True, {"kills": 18, "deaths": 15, "assists": 17})
print(f"Game 15 recorded")
