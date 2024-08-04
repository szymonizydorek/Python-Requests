import requests

print ("Importing requests...")

#Defing the ULR for the GET request
url = "https://postman-echo.com/get"

#Define the quert parameters
querystring = {"test":"123"}

#Define headers
headers = {}

#Send the GET request
response = requests.request("GET", url, headers=headers, params=querystring)

print("Response from the server: ")
print(response.text)