import requests
import os

BASE = os.getenv("API_BASE_URL")

r = requests.post(f"{BASE}/reset")
state = r.json()

action = {"type": "spam"}

r = requests.post(f"{BASE}/step", json=action)
print(r.json())