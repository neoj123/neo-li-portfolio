"""Travel itinerary planner - 2024-11-27 update #17"""
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
            "date": "2024-11-27",
            "notes": notes,
            "entry_id": 17
        }
        self.itinerary.append(entry)
        return entry

trip = TravelItinerary("Paris")
trip.add_destination("Check-in", 4, "Exploring the area")
print("Itinerary updated")
