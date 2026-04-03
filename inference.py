import requests

BASE_URL = "http://localhost:8000"

requests.post(f"{BASE_URL}/reset")

action = {
    "type": "security",
    "priority": "high",
    "route": "security_team"
}

result = requests.post(f"{BASE_URL}/step", json=action).json()

print(result)