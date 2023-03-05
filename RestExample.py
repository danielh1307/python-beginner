import requests

response = requests.get("http://localhost:8080/stars")
print(response)
print(response.json())
print(response.json()[0])
print(response.json()[0]['name'])

# create a new resource
headers = {'Content-Type': 'application/json'}
response = requests.post("http://localhost:8080/stars", json = {'name': 'Antares', 'constellation': 'Scorpion'}, headers = headers)
print(response)