"""Travel itinerary planner - 2024-10-22 update #520"""
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
            "date": "2024-10-22",
            "notes": notes,
            "entry_id": 520
        }
        self.itinerary.append(entry)
        return entry

trip = TravelItinerary("Tokyo")
trip.add_destination("Check-in", 3, "Exploring the area")
print("Itinerary updated")
