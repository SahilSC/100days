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
#key = '4865dd8e5aed494080023524231403'
api_key = os.environ.get("AUTH_TOKEN")
location = (29.6186, -95.5377)
#location = (-11.67, -50.25)

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
  account_sid = "AC2360754d765f11ade7826922e75f0656"
  auth_token = "cd7d10819f1b02d6ad032475e1dace7c"
  client = Client(account_sid, auth_token)
  message = client.messages.create(
    body="BRING UMBRELLAA ne wmsg!!",
    from_="+18885994465",
    to="+18323480147"
  )
  print(message.sid)