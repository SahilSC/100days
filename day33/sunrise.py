import requests
from datetime import datetime
LAT = 51.507351
LONG = -0.1277
# request = requests.get("http://api.open-notify.org/iss-now.json")
# request.raise_for_status()
# location = (request.json()['iss_position']['latitude'], request.json()['iss_position']['longitude'])
# print(location)

parameters = {
    "lat": LAT,
    "lng": LONG,
    "formatted": 0
}

response = requests.get(url = 'https://api.sunrise-sunset.org/json', params = parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split('+')[0][0:2]
sunset = data['results']['sunset'].split('T')[1].split('+')[0][0:2]

time_now = datetime.now()
print(sunrise)
print(sunset)
print(time_now.hour)