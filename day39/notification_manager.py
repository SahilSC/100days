# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    pass
    def send_msg(self, city_dict):
        str = f"Low price alert! Only ${int(city_dict['price'])*1.26} to fly from {city_dict['cityFrom']}-{city_dict['flyFrom']} to {city_dict['cityTo']}-{city_dict['flyTo']}, from {city_dict['start_departure']} to {city_dict['end_departure']}."
        #print(str)
        account_sid = "AC2360754d765f11ade7826922e75f0656"
        auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=str,
            from_="+18885994465",
            to="+18323480147"
        )
        #print(message.sid)

# a = NotificationManager()
# a.send_msg({'price': 787, 'cityTo': 'Paris', 'flyTo': 'PAR', 'flyFrom': 'IAH', 'cityFrom': 'Houston', 'start_departure': '2023-09-21', 'end_departure': '2023-10-02'})