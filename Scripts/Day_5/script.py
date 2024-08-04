import requests
import json

print("Importing Requests...")

response = requests.get('https://jsonplaceholder.typicode.com/posts')
print("Get reponse:")
print(f"Status code: {response.status_code}")


choice = input("Do you want to see the whole output? y/n").lower()
if choice == 'y':
    print(response.json())
elif choice == 'n':
    print("Ok by")
else: 
    print("Provide valid output")
    
    
new_post = {
    'title' : 'foo',
    'body' : 'bar',
    'userId' : 1
}

response = requests.post('https://jsonplaceholder.typicode.com/posts', json=new_post)
print("\nPost Request")

print(f"\nStatus code: {response.status_code}")
print(f"\nResponse headers:")
print(json.dumps(dict(response.headers), indent=4))

#Extracting the content type
content_type = response.headers.get('Content-Type')
print("\nContent-Type from Headers:")
print(content_type)