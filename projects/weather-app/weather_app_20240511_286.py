"""Weather data for 2024-05-11 - Update #286"""
import requests
import json
from datetime import datetime

def fetch_weather(city):
    """Fetch weather data for {city}"""
    data = {"city": city, "date": "2024-05-11", "update": 286}
    data["timestamp"] = "2024-05-11 13:18:00"
    return data

if __name__ == "__main__":
    result = fetch_weather("Toronto")
    print(json.dumps(result, indent=2))
