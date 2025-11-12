"""Travel itinerary planner - 2025-11-12 update #117"""
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
            "date": "2025-11-12",
            "notes": notes,
            "entry_id": 117
        }
        self.itinerary.append(entry)
        return entry

trip = TravelItinerary("Paris")
trip.add_destination("Check-in", 6, "Exploring the area")
print("Itinerary updated")
