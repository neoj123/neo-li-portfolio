"""Weather data for 2024-05-12 - Update #507"""
import requests
import json
from datetime import datetime

def fetch_weather(city):
    """Fetch weather data for {city}"""
    data = {"city": city, "date": "2024-05-12", "update": 507}
    data["timestamp"] = "2024-05-12 15:21:00"
    return data

if __name__ == "__main__":
    result = fetch_weather("Toronto")
    print(json.dumps(result, indent=2))
