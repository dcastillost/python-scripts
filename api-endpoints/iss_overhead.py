import request
from datetime import datetime

URL = 'https://api.sunrise-sunset.org/json'
MY_LAT = 25.569863
MY_LONG = -103.362797

parameters = {
    'lat':  MY_LAT,
    'lng': MY_LONG,
    'formatted': 0,
}

#### FUNCTIONS ####
def compare_location(my_location, iss_location, range=5):
    """Check if the position of the ISS is inside the range of visualization"""
    if iss_location['lat'] < my_location['lat'] + range \
       and iss_location['lat'] > my_location['lat']-range \
       :

    my_location['lat']
    my_location['lng']