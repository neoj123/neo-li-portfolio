"""Weather data for 2024-01-20 - Update #247"""
import requests
import json
from datetime import datetime

def fetch_weather(city):
    """Fetch weather data for {city}"""
    data = {"city": city, "date": "2024-01-20", "update": 247}
    data["timestamp"] = "2024-01-20 10:32:00"
    return data

if __name__ == "__main__":
    result = fetch_weather("Toronto")
    print(json.dumps(result, indent=2))
