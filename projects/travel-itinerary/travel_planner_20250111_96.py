"""Travel itinerary planner - 2025-01-11 update #96"""
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
            "date": "2025-01-11",
            "notes": notes,
            "entry_id": 96
        }
        self.itinerary.append(entry)
        return entry

trip = TravelItinerary("Tokyo")
trip.add_destination("Check-in", 6, "Exploring the area")
print("Itinerary updated")
