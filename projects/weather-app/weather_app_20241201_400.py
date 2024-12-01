"""Weather data for 2024-12-01 - Update #400"""
import requests
import json
from datetime import datetime

def fetch_weather(city):
    """Fetch weather data for {city}"""
    data = {"city": city, "date": "2024-12-01", "update": 400}
    data["timestamp"] = "2024-12-01 11:27:00"
    return data

if __name__ == "__main__":
    result = fetch_weather("Toronto")
    print(json.dumps(result, indent=2))
