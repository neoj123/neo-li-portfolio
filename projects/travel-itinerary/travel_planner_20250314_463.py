"""Travel itinerary planner - 2025-03-14 update #463"""
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
            "date": "2025-03-14",
            "notes": notes,
            "entry_id": 463
        }
        self.itinerary.append(entry)
        return entry

trip = TravelItinerary("Bangkok")
trip.add_destination("Check-in", 2, "Exploring the area")
print("Itinerary updated")
