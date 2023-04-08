import requests
from pprint import pprint
class FlightSearch:
    API_KEY = "bmcL2MjZRvtX2gHNvjPip2ZKzsgg_jca"
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
