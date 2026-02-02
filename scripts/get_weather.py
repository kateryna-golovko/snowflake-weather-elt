import requests
import json
from datetime import datetime
import urllib.parse

API_KEY = "API_KEY"  # Replace with the API key
CITY = "Melbourne,AU"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"

response = requests.get(URL)
data = response.json()

timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
filename = f"data/raw/weather_{CITY}_{timestamp}.json"

with open(filename, "w") as f:
    json.dump(data, f, indent=2)

print(f"Saved {filename}")
