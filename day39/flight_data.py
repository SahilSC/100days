from datetime import datetime, timedelta
import requests
import os

class FlightData:
    API_KEY = os.environ["FLIGHT_DATA_KEY"]
    API_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
    departure_city = "city:HOU"
    header = {
        "apikey":API_KEY,
        "Content-Encoding":"gzip",
        "Content-Type":"application/json"
    }

    start = datetime.now()
    end = start + timedelta(days=180)
    from_date = start.strftime("%d/%m/%Y")
    to_date = end.strftime("%d/%m/%Y")
    min_nights = 7
    max_nights = 28
    params = {
        "fly_from": departure_city,
        "date_from":from_date,
        "date_to": to_date,
        "max_stopovers": "0",
        "nights_in_dst_from": min_nights,
        "nights_in_dst_to": max_nights,
        "sort": "price",
        "currency": "GBP",
        "limit": 1
    }
    def cityinfo(self, to_iata):
        self.params["fly_to"]=to_iata
        response = requests.get(url = self.API_ENDPOINT, params = self.params, headers = self.header)
        response.raise_for_status()
        data = response.json()['data']
        citydict = {}
        for cityinfo in data:
            citydict['price'] = cityinfo['price']
            citydict['cityTo'] = cityinfo['cityTo']
            citydict['flyTo'] = to_iata
            citydict['flyFrom'] = cityinfo['flyFrom']
            citydict['cityFrom'] = cityinfo['cityFrom']
            citydict['start_departure'] = cityinfo['route'][0]['local_departure'].split('T')[0]
            citydict['end_departure'] = cityinfo['route'][1]['local_departure'].split('T')[0]
        return citydict
        #print(citydict)

        # with open('output.txt','w') as f:
        #     f.write(str(response.json()))
