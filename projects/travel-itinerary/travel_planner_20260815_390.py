"""Travel itinerary planner - 2026-08-15 update #390"""
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
            "date": "2026-08-15",
            "notes": notes,
            "entry_id": 390
        }
        self.itinerary.append(entry)
        return entry

trip = TravelItinerary("New York")
trip.add_destination("Check-in", 6, "Exploring the area")
print("Itinerary updated")
