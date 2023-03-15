import requests
import os
from datetime import datetime

APP_ID = "7f01390e"
APP_KEY = "0029430fcd8e1abac17aa58aa9303ae8"
BEARER_TOKEN = "Bearer Sussbuss"
nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/533c6cd46d1fb3fe1daab6928e0cd70a/sahil'sWorkouts/workouts"


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









