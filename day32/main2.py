##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import smtplib
import random
import pandas as pd
import os

now = dt.datetime.now()
day = now.day
month = now.month


my_email = "pythonchowdhury@gmail.com"
password = os.environ['APP_PASSWORD']
to_email = "lintukjoshi@gmail.com"

files = [f"letter_templates/letter_{_}.txt" for _ in range(1, 4)]
letters = []
for file in files:
    with open(file) as _:
        letter = _.readlines()
        full = ""
        for _1 in letter:
            full= full + _1
        letters.append(full)


df = pd.read_csv("birthdays.csv")
for _ in range(0, len(df)):
    personday = df['day'][_]
    personmonth = df['month'][_]
    personname = df['name'][_]
    personemail = df['email'][_]
    if day == personday and personmonth == month:
        randomletter = random.choice(letters)
        randomletter = randomletter.replace('[NAME]', personname)
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=my_email, password = password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=personemail,
                            msg = f"Subject: HAPPY BIRTHDAY!!!\n\n{randomletter}")






