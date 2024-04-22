"""Weather data for 2024-04-22 - Update #267"""
import requests
import json
from datetime import datetime

def fetch_weather(city):
    """Fetch weather data for {city}"""
    data = {"city": city, "date": "2024-04-22", "update": 267}
    data["timestamp"] = "2024-04-22 17:04:00"
    return data

if __name__ == "__main__":
    result = fetch_weather("Toronto")
    print(json.dumps(result, indent=2))
