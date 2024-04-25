"""Weather data for 2024-04-25 - Update #973"""
import requests
import json
from datetime import datetime

def fetch_weather(city):
    """Fetch weather data for {city}"""
    data = {"city": city, "date": "2024-04-25", "update": 973}
    data["timestamp"] = "2024-04-25 11:52:00"
    return data

if __name__ == "__main__":
    result = fetch_weather("Toronto")
    print(json.dumps(result, indent=2))
