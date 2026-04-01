import requests

# If running locally, use this URL:
url = "http://127.0.0"

try:
    response = requests.get(url)
    data = response.json()
    for user in data:
        print(f"User: {user['name']} lives in {user['city']}")
except Exception as e:
    print(f"Error fetching data: {e}")
