"""Travel itinerary planner - 2026-03-06 update #346"""
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
            "date": "2026-03-06",
            "notes": notes,
            "entry_id": 346
        }
        self.itinerary.append(entry)
        return entry

trip = TravelItinerary("New York")
trip.add_destination("Check-in", 4, "Exploring the area")
print("Itinerary updated")
