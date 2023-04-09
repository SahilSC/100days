import requests
from pprint import pprint
import os
class FlightSearch:
    API_KEY = os.environ['FLIGHT_SEARCH_KEY']
    headers = {
        "apikey":API_KEY,
        "Content-Encoding": "gzip"
    }
    kiwi_endpoint = "https://api.tequila.kiwi.com/locations/query"
    params = {
        "term":"London"
    }

    def get_iata(self, place):
        response = requests.get(url=FlightSearch.kiwi_endpoint,
                                params ={"term":place},
                                headers = FlightSearch.headers)
        response.raise_for_status()
        data = response.json()
        return data["locations"][0]["code"]
