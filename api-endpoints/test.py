import requests

URL = 'http://api.open-notify.org/iss-now.json'

response = requests.get(url=URL)

data = response.json()['iss_position']

print(data)