"""Weather data for 2025-05-13 - Update #291"""
import requests
import json
from datetime import datetime

def fetch_weather(city):
    """Fetch weather data for {city}"""
    data = {"city": city, "date": "2025-05-13", "update": 291}
    data["timestamp"] = "2025-05-13 11:42:00"
    return data

if __name__ == "__main__":
    result = fetch_weather("Toronto")
    print(json.dumps(result, indent=2))
