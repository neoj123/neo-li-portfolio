"""Travel itinerary planner - 2025-06-23 update #794"""
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
            "date": "2025-06-23",
            "notes": notes,
            "entry_id": 794
        }
        self.itinerary.append(entry)
        return entry

trip = TravelItinerary("New York")
trip.add_destination("Check-in", 4, "Exploring the area")
print("Itinerary updated")
