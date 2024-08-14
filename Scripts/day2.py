import requests

print("Testing JSON capabilities")


data = {
    'key': 'value'
}

response = requests.get('https://api.github.com', json=data)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")
