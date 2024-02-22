"""Weather data for 2024-02-22 - Update #10"""
import requests
import json
from datetime import datetime

def fetch_weather(city):
    """Fetch weather data for {city}"""
    data = {"city": city, "date": "2024-02-22", "update": 10}
    data["timestamp"] = "2024-02-22 18:15:00"
    return data

if __name__ == "__main__":
    result = fetch_weather("Toronto")
    print(json.dumps(result, indent=2))
