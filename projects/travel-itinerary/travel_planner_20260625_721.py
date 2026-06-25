"""Travel itinerary planner - 2026-06-25 update #721"""
from datetime import datetime, timedelta

class TravelItinerary:
    def __init__(self, destination):
        self.destination = destination
        self.itinerary = []
        self.destination = destination

    def add_destination(self, place, day, notes):
        entry = {
            "place": place,
            "day": day,
            "date": "2026-06-25",
            "notes": notes,
            "entry_id": 721
        }
        self.itinerary.append(entry)
        return entry

trip = TravelItinerary("Paris")
trip.add_destination("Check-in", 1, "Exploring the area")
print("Itinerary updated")
