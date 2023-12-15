"""Weather data for 2023-12-15 - Update #997"""
import requests
import json
from datetime import datetime

def fetch_weather(city):
    """Fetch weather data for {city}"""
    data = {"city": city, "date": "2023-12-15", "update": 997}
    data["timestamp"] = "2023-12-15 13:59:00"
    return data

if __name__ == "__main__":
    result = fetch_weather("Toronto")
    print(json.dumps(result, indent=2))
