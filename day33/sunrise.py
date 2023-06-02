import requests
from datetime import datetime
import smtplib
import time
import os

def night(sunrise, sunset, now):
    # if sunrise < sunset:
    #     return !(now < sunset and now > sunrise)
    # else:
    #     return now < sunset and now > sunrise
    night = sunrise < now < sunset
    return not night if sunrise < sunset else sunrise > now > sunset

def close(location):
    return abs(LAT-location[0]) <= 5 and abs(LONG - location[1]) <= 5

LAT = 29.6
LONG = -95

request = requests.get("http://api.open-notify.org/iss-now.json")
request.raise_for_status()
location = (float(request.json()['iss_position']['latitude']), float(request.json()['iss_position']['longitude']))


parameters = {
    "lat": LAT,
    "lng": LONG,
    "formatted": 0
}

response = requests.get(url = 'https://api.sunrise-sunset.org/json', params = parameters)
response.raise_for_status()
data = response.json()

sunrise = int(data['results']['sunrise'].split('T')[1].split('+')[0][0:2])
sunset = int(data['results']['sunset'].split('T')[1].split('+')[0][0:2])

time_now = int(datetime.utcnow().hour)

while True:
    time.sleep(60)
    if night(sunrise, sunset, time_now) and close(location):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user="pythonchowdhury@gmail.com", password=os.environ['APP_PASSWORD'])
            connection.sendmail(from_addr="pythonchowdhury@gmail.com",
                                to_addrs="sahilschowdhury@gmail.com",
                                msg="Subject: ISS Space Station Near You!\n\nLook in the night sky! The ISS is coming!!")



