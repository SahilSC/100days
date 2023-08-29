import smtplib
import datetime as dt
import random as rd
import os

now = dt.datetime.now()
my_email = "pythonchowdhury@gmail.com"
password = os.environ['APP_PASSWORD']
to_email = "sahilschowdhury@gmail.com"
if now.weekday() == 6:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user = my_email, password = password)
        with open(file="quotes.txt") as quote_file:
            allquotes = quote_file.readlines()
            quote = rd.choice(allquotes)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                            msg=f"Subject: Happy Monday\n\n{quote}")





























# # import smtplib
# #
# # my_email = "pythonchowdhury@gmail.com"
# # password = "seovethvpbswzgzm"
# # to_addrs = "pythonchowdhury@yahoo.com"
# # with smtplib.SMTP("smtp.gmail.com", 587) as connection:
# #     connection.starttls()
# #     connection.login(user = my_email, password = password)
# #     connection.sendmail(from_addr = my_email,
# #                         to_addrs = to_addrs,
# #                         msg = "Subject: Sneding sus\n\n Lmaooo has a header now ! 2")
#
# import datetime as dt
#
# now = dt.datetime.now()
# dow = now.we
# print()