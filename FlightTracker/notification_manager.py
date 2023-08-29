# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
import smtplib
import os

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def send_msg(self, city_dict):
        str = self.create_msg(city_dict)
        print(str)
        account_sid = os.environ['ACCOUNT_SID']
        auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=str,
            from_="+18885994465",
            to="+" + os.environ['MY_PHONE_NUMBER']
        )
        #print(message.sid)

    def create_msg(self, city_dict):
        str = f"Low price alert! Only ${round(int(city_dict['price']) * 1.26, 2)}/{round(int(city_dict['price']))} sterling  to fly from {city_dict['cityFrom']}-{city_dict['flyFrom']} to {city_dict['cityTo']}-{city_dict['flyTo']}, from {city_dict['start_departure']} to {city_dict['end_departure']}."
        if city_dict['stop_over'] is not None:
            str = str + f"\nFlight has 1 stop over, via {city_dict['stop_over']}."
        return str

    def send_mails(self, mails, msg="No deals today :("):
        from_email = 'pythonchowdhury@gmail.com'
        password = os.environ['APP_PASSWORD']
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(password=password, user=from_email)
            for mail in mails:
                connection.sendmail(from_addr=from_email,
                                    to_addrs=mail,
                                    msg=f'Subject: Cheap Flights\n\n{msg}')



# a = NotificationManager()
# a.send_mails(msg = "s", mails = ['sahilschowdhury@gmail.com'])

# a.send_msg({'price': 787, 'cityTo': 'Paris', 'flyTo': 'PAR', 'flyFrom': 'IAH', 'cityFrom': 'Houston', 'start_departure': '2023-09-21', 'end_departure': '2023-10-02'})