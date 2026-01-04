"""Travel itinerary planner - 2026-01-04 update #151"""
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
            "date": "2026-01-04",
            "notes": notes,
            "entry_id": 151
        }
        self.itinerary.append(entry)
        return entry

trip = TravelItinerary("Bangkok")
trip.add_destination("Check-in", 5, "Exploring the area")
print("Itinerary updated")
