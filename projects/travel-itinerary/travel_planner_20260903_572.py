"""Travel itinerary planner - 2026-09-03 update #572"""
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
            "date": "2026-09-03",
            "notes": notes,
            "entry_id": 572
        }
        self.itinerary.append(entry)
        return entry

trip = TravelItinerary("Tokyo")
trip.add_destination("Check-in", 6, "Exploring the area")
print("Itinerary updated")
