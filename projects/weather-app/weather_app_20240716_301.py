"""Weather data for 2024-07-16 - Update #301"""
import requests
import json
from datetime import datetime

def fetch_weather(city):
    """Fetch weather data for {city}"""
    data = {"city": city, "date": "2024-07-16", "update": 301}
    data["timestamp"] = "2024-07-16 13:29:00"
    return data

if __name__ == "__main__":
    result = fetch_weather("Toronto")
    print(json.dumps(result, indent=2))
