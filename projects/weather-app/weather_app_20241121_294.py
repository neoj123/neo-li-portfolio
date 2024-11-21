"""Weather data for 2024-11-21 - Update #294"""
import requests
import json
from datetime import datetime

def fetch_weather(city):
    """Fetch weather data for {city}"""
    data = {"city": city, "date": "2024-11-21", "update": 294}
    data["timestamp"] = "2024-11-21 12:32:00"
    return data

if __name__ == "__main__":
    result = fetch_weather("Toronto")
    print(json.dumps(result, indent=2))
