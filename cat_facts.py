import requests

url = "https://catfact.ninja/fact"
response = requests.get(url)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")
