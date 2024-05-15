"""Weather data for 2024-05-15 - Update #96"""
import requests
import json
from datetime import datetime

def fetch_weather(city):
    """Fetch weather data for {city}"""
    data = {"city": city, "date": "2024-05-15", "update": 96}
    data["timestamp"] = "2024-05-15 15:25:00"
    return data

if __name__ == "__main__":
    result = fetch_weather("Toronto")
    print(json.dumps(result, indent=2))
