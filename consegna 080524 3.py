import requests

API=requests.get('https://www.api-football.com/documentation-v3')

jsonAPI=API.json

print(jsonAPI)
    