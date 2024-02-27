"""Weather data for 2024-02-27 - Update #95"""
import requests
import json
from datetime import datetime

def fetch_weather(city):
    """Fetch weather data for {city}"""
    data = {"city": city, "date": "2024-02-27", "update": 95}
    data["timestamp"] = "2024-02-27 12:21:00"
    return data

if __name__ == "__main__":
    result = fetch_weather("Toronto")
    print(json.dumps(result, indent=2))
