from twilio.rest import Client
import requests
import datetime as dt
from datetime import datetime
import time
import os


# NEWS_API_KEY = tradingview.com
# ALPHA_KEY = https://www.alphavantage.co/documentation/#daily
# TWILIO_AUTH_TOKEN = Twilio console

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
THRESHOLD = 0


def get_json():
    params = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": STOCK,
        "apikey": os.environ.get("ALPHA_KEY"),
        "outputsize": "compact",
    }

    request = requests.get(url="https://www.alphavantage.co/query", params=params)
    request.raise_for_status()
    return request.json()['Time Series (Daily)']


def get_dates():
    now = datetime.now()
    dates = [
        str(datetime.now() - dt.timedelta(days=1))[:10],
        str(datetime.now() - dt.timedelta(days=2))[:10],
        str(datetime.now() - dt.timedelta(days=3))[:10],
        str(datetime.now() - dt.timedelta(days=4))[:10]]
    times = 0
    for date in dates:
        if times == 0 and date in data:
            times += 1
            curdate = date
        elif times == 1 and date in data:
            prevdate = date
            break
    return (curdate, prevdate)

def get_news(percent):

    curdate, prevdate = get_dates()
    numarticles = 3
    params={
        "q":COMPANY_NAME,
        "from":prevdate,
        "to":curdate,
        "sortBy":"popularity",
        "pageSize":numarticles,
        "apiKey":os.environ.get("NEWS_API_KEY"),
    }
    request = requests.get(url = 'https://newsapi.org/v2/everything', params = params)
    articles = request.json()['articles']
    msg = []
    for ind in range(0, numarticles):
        msg.append(make_msg(articles[ind], percent))
    return msg

def make_msg(dict, percent):
    emoji = "Down" if percent < 0 else "Up"
    header = f"{STOCK} {emoji} {abs(percent)}%\n"
    author = dict['author']
    title = dict['title']
    content = dict['content']
    #url = dict['url']
    url = ""
    contentsplit = content.split('[+')[0][:-1]
    msg = f"{author}: {title}\nBrief:{contentsplit}\n{url}"
    #msg = emoji + f"\nBrief: {contentsplit}"
    #msg = emoji + f"\nTitle: {title}"
    return msg

def send_text(msg):
    account_sid = "AC2360754d765f11ade7826922e75f0656"
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=msg,
        from_="+18885994465",
        to="+18323480147"
    )
    print(message.sid)
    time.sleep(5)

data = get_json()
curdate, prevdate = get_dates()
stockdif = float(data[curdate]['4. close']) - float(data[prevdate]['4. close'])
percent = round(stockdif / float(data[curdate]['4. close']) * 100)

if abs(percent) >= THRESHOLD:
    news = get_news(percent)
    for article in news:
        send_text(article)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
