"""Travel itinerary planner - 2024-05-17 update #974"""
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
            "date": "2024-05-17",
            "notes": notes,
            "entry_id": 974
        }
        self.itinerary.append(entry)
        return entry

trip = TravelItinerary("New York")
trip.add_destination("Check-in", 2, "Exploring the area")
print("Itinerary updated")
