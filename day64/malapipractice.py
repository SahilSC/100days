import os

import requests

endpoint = 'https://api.myanimelist.net/v2'
headers = {
    'X-MAL-CLIENT-ID':os.environ['CLIENT_ID']
}
params={
    'q':'attack on titan',
    'fields':'title,start_date,synopsis,main_picture'
}

ids= [ele['node'] for ele in requests.get(endpoint + "/anime",headers=headers,params=params).json()['data']]
print(ids)
# anime_details = requests.get(endpoint + '/anime/' + str(id), headers=headers,params=params).json()
# print(anime_details)