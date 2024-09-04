"""Weather data for 2024-09-04 - Update #503"""
import requests
import json
from datetime import datetime

def fetch_weather(city):
    """Fetch weather data for {city}"""
    data = {"city": city, "date": "2024-09-04", "update": 503}
    data["timestamp"] = "2024-09-04 15:06:00"
    return data

if __name__ == "__main__":
    result = fetch_weather("Toronto")
    print(json.dumps(result, indent=2))
