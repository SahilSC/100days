import requests
import os
from datetime import datetime

APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")
nutrition_endpoint = os.environ.get("nutrition_endpoint")
sheety_endpoint = os.environ.get("sheety_endpoint")


headers = {
    "x-app-id":APP_ID,
    "x-app-key":APP_KEY,
    "Authorization": BEARER_TOKEN,
    #"Content-Type":'exercise/json',
}

sentence = input("Tell me what exercise you did: ")
#sentence = "ran for 3 miles for 20 mins"
exercise_params = {
    "query":sentence,
    "gender":"male",
    "weight_kg":52.16,
    "height_cm":167.64,
    "age":18
}
response = requests.post(url=nutrition_endpoint, json=exercise_params, headers=headers)
response.raise_for_status()
data = response.json()
now = datetime.now()
date = now.strftime("%m/%d/%Y")
time = now.strftime("%I:%M:%S")
exercise = data['exercises'][0]['name'].title()

duration = data['exercises'][0]['duration_min']
calories = data['exercises'][0]['nf_calories']

sheety_params = {
    "workout":{
        "date":date,
        "time":time,
        "exercise":exercise,
        "duration":duration,
        "calories":calories
    }
}
sheety_response =requests.post(url=sheety_endpoint, json = sheety_params,headers=headers)









