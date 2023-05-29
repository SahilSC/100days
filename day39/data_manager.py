import requests
import pprint
import os
class DataManager:
    API_KEY = os.environ["DATA_MANAGER_KEY"]
    SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
    USER_SHEETY_ENDPOINT = "https://api.sheety.co/533c6cd46d1fb3fe1daab6928e0cd70a/flights/users"

    HEADER = {
        "Content-Type":"application/json",
        "Authorization":API_KEY
    }

    # sheet_param = {
    #     "flightdeal":{
    #         "iata":1,
    #     }
    # }
    #response = requests.put(url=f"{sheety_endpoint}/2", headers = header, json = sheet_param)
    def __init__(self):
        self.sheet_data = None

    def retrieve_data(self):
        response = requests.get(url=DataManager.SHEETY_ENDPOINT, headers=DataManager.HEADER)
        response.raise_for_status()
        self.sheet_data = response.json()

    def set_iata(self, iata, id):
        json = {
            "flightdeal":{
                "iata":iata
            }
        }
        response = requests.post(url=f"{DataManager.SHEETY_ENDPOINT}/{id}",
                                json = json,
                                headers = DataManager.HEADER)

    def get_mail(self):
        response = requests.get(url=DataManager.USER_SHEETY_ENDPOINT, headers=DataManager.HEADER)
        response.raise_for_status()
        self.personinfo = response.json()['users']
        mails = []
        for row in self.personinfo:
            mails.append(row['email'])
        return mails



