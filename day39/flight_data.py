from datetime import datetime, timedelta
import requests

class FlightData:
    API_KEY = "Nn7I_zQQzMIcfFKqkHuxWsDNEeSswrWD"
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
    def __init__(self, to_iata):
        params = {
            "fly_from":self.departure_city,
            "date_from":self.from_date,
            "date_to":self.to_date,
            "max_stopovers":"0",
            "nights_in_dst_from":self.min_nights,
            "nights_in_dst_to":self.max_nights,
            "sort":"price",
            "fly_to":to_iata,
            "currency":"GBP",
            "limit":1
        }

        response = requests.get(url = self.API_ENDPOINT, params = params, headers = self.header)
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
        self.citydict = citydict
        #print(citydict)

        # with open('output.txt','w') as f:
        #     f.write(str(response.json()))
