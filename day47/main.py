import requests
from bs4 import BeautifulSoup
import smtplib
import os

URL="https://www.amazon.com/Apple-2022-10-9-inch-iPad-Wi-Fi/dp/B0BJLXMVMV/ref=sr_1_1?keywords=ipad+10th&qid=1685550679&sr=8-1&ufe=app_do%3Aamzn1.fos.c3015c4a-46bb-44b9-81a4-dc28e6d374b3"
minprice = 440

def get_content():
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
    headers = {
        "User-Agent":user_agent,
        "Accept-Language":"en-US,en;q=0.9",
    }
    response = requests.get(URL, headers=headers)
    content = response.text
    soup = BeautifulSoup(content, "html.parser")
    item_name = soup.find(name="span",id = "productTitle").getText().encode('utf8')
    price = float(soup.find(name="span", class_="a-offscreen").getText()[1:])
    if price <= minprice:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user="pythonchowdhury@gmail.com",
                             password=os.environ["APP_PASSWORD"])
            connection.sendmail(from_addr="pythonchowdhury@gmail.com",
                                to_addrs="sahilschowdhury@gmail.com",
                                msg=f"Subject: Cheap {item_name}!\n\nCurrent price is {price}, lower than {minprice} by {minprice-price}.\n{URL}")

get_content()