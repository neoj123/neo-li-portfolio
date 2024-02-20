"""Travel itinerary planner - 2024-02-20 update #579"""
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
            "date": "2024-02-20",
            "notes": notes,
            "entry_id": 579
        }
        self.itinerary.append(entry)
        return entry

trip = TravelItinerary("Bangkok")
trip.add_destination("Check-in", 6, "Exploring the area")
print("Itinerary updated")
