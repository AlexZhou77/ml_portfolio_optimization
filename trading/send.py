import requests
import json
import os

with open("payloads/weights.json","r") as f:
    weights_data = json.load(f)

with open("payloads/directions.json","r") as f:
    directions_data = json.load(f)

# Merge into one payload
payloads = {
    "weights": weights_data,
    "directions": directions_data
}

url = "https://webhook.site/8d16ac62-58f2-4295-a0d2-9f4c6c087deb"
response = requests.post(url, json = payloads)

print("Status Code:", response.status_code)
print("Response:", response.text)