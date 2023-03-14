import requests

def willrain(data):
    for hour in data:
        if hour["will_it_rain"]==1 or 1==hour["will_it_snow"]:
            return True
    return False

api_key = '4865dd8e5aed494080023524231403'
location = (29.6186, -95.5377)
params = {
    "q": location,
    "days": 1,
    "key": api_key,
}
request = requests.get(url='http://api.weatherapi.com/v1/forecast.json'
                       , params=params)
request.raise_for_status()

data = request.json()['forecast']['forecastday'][0]['hour'][7:20]
print(willrain(data))
print(data)


