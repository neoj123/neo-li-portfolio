"""Travel itinerary planner - 2026-04-19 update #246"""
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
            "date": "2026-04-19",
            "notes": notes,
            "entry_id": 246
        }
        self.itinerary.append(entry)
        return entry

trip = TravelItinerary("New York")
trip.add_destination("Check-in", 2, "Exploring the area")
print("Itinerary updated")
