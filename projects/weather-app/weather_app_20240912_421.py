"""Weather data for 2024-09-12 - Update #421"""
import requests
import json
from datetime import datetime

def fetch_weather(city):
    """Fetch weather data for {city}"""
    data = {"city": city, "date": "2024-09-12", "update": 421}
    data["timestamp"] = "2024-09-12 17:56:00"
    return data

if __name__ == "__main__":
    result = fetch_weather("Toronto")
    print(json.dumps(result, indent=2))
