"""Weather data for 2026-01-21 - Update #366"""
import requests
import json
from datetime import datetime

def fetch_weather(city):
    """Fetch weather data for {city}"""
    data = {"city": city, "date": "2026-01-21", "update": 366}
    data["timestamp"] = "2026-01-21 12:09:00"
    return data

if __name__ == "__main__":
    result = fetch_weather("Toronto")
    print(json.dumps(result, indent=2))
