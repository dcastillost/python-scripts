import requests
from datetime import datetime


URL = 'https://api.sunrise-sunset.org/json'
MY_LAT = 25.569863
MY_LONG = -103.362797

parameters = {
    'lat':  MY_LAT,
    'lng': MY_LONG,
    'formatted': 0,
}

response = requests.get(URL, params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise']
sunrise_time = sunrise.split('T')[1]
print(sunrise_time)