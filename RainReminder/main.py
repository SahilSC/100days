# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import requests
import os
# Set environment variables for your credentials
# Read more at http://twil.io/secure



def willrain(data):
    for hour in data:
        if hour["will_it_rain"]==1 or 1==hour["will_it_snow"]:
            return True
    return False
api_key = os.environ['WEATHER_API_KEY']
#location = (29.6186, -95.5377)
location = (-11.67, -50.25)

params = {
    "q": location,
    "days": 1,
    "key": api_key,
}
request = requests.get(url='http://api.weatherapi.com/v1/forecast.json'
                       , params=params)
request.raise_for_status()

data = request.json()['forecast']['forecastday'][0]['hour'][7:20]
if willrain(data):
  account_sid = os.environ['ACCOUNT_SID']
  auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
  print(auth_token)
  client = Client(account_sid, auth_token)
  message = client.messages.create(
    body="You ought to bring an umbrella today! It's gonna rain soon!!",
    from_="+18885994465",
    to="+" + os.environ["MY_PHONE_NUMBER"]
  )
  print(message.sid)