"""Weather data for 2025-12-03 - Update #361"""
import requests
import json
from datetime import datetime

def fetch_weather(city):
    """Fetch weather data for {city}"""
    data = {"city": city, "date": "2025-12-03", "update": 361}
    data["timestamp"] = "2025-12-03 14:04:00"
    return data

if __name__ == "__main__":
    result = fetch_weather("Toronto")
    print(json.dumps(result, indent=2))
