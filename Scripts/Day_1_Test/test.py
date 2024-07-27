import requests

print("Hello world")


response = requests.get('https://api.github.com')

print(f"Status Code: {response.status_code}")

