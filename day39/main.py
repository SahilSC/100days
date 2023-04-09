# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from day39.notification_manager import NotificationManager
from day39.flight_search import FlightSearch
from day39.flight_data import FlightData
from day39.data_manager import DataManager

def set_iata():
    for city_data in sheet_data:
        city = city_data['city']
        if city_data['iata'] == '':
            iata = flight_search.get_iata(city)
            data_manager.set_iata(iata, id)

def send_notif(sheet_data, city_data):
    notif = NotificationManager()
    for citydata in sheet_data:
        city = citydata['city']
        start_price = citydata['lowestPrice']
        if 'price' in city_data[city] and city_data[city]['price'] < start_price:
            notif.send_msg(city_data[city])

def get_citylist():
    citylist = {}
    f_data = FlightData()
    for city_data in sheet_data:
        city = city_data['city']
        citylist[city] = f_data.cityinfo(city_data['iata'])
    return citylist


data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

data_manager.retrieve_data()
sheet_data = data_manager.sheet_data['flightdeals']
# sheet_data = [{'city': 'Paris', 'iata': 'PAR', 'lowestPrice': 54, 'id': 2},
#               {'city': 'Berlin', 'iata': 'BER', 'lowestPrice': 42, 'id': 3},
#               {'city': 'Tokyo', 'iata': 'TYO', 'lowestPrice': 485, 'id': 4},
#               {'city': 'Sydney', 'iata': 'SYD', 'lowestPrice': 551, 'id': 5},
#               {'city': 'Istanbul', 'iata': 'IST', 'lowestPrice': 95, 'id': 6},
#               {'city': 'Kuala Lumpur', 'iata': 'KUL', 'lowestPrice': 414, 'id': 7},
#               {'city': 'New York', 'iata': 'NYC', 'lowestPrice': 240, 'id': 8},
#               {'city': 'San Francisco', 'iata': 'SFO', 'lowestPrice': 260, 'id': 9},
#               {'city': 'Cape Town', 'iata': 'CPT', 'lowestPrice': 378, 'id': 10}]

set_iata()
citylist = get_citylist()
print(citylist)
send_notif(sheet_data, citylist)

