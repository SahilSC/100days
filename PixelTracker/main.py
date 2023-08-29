import requests
import datetime as dt
from datetime import datetime
import os
pixela_endpoint = 'https://pixe.la/v1/users'
TOKEN = os.environ.get("TOKEN")
USERNAME = "imajinary"
ID = "codinggraph"
users_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url = pixela_endpoint, json=users_params)
# print(response.text)

graph_path = f"{pixela_endpoint}/{USERNAME}/graphs"
header = {
    "X-USER-TOKEN": TOKEN,
}

graph_config = {
    "id": ID,
    "name": "codingtime",
    "unit": "commits",
    "type": "int",
    "color": "sora",
}
# graph_response = requests.post(url=graph_path, json=graph_config, headers=header)
# print(graph_response.text)

pixel_path = f"{graph_path}/{ID}"
now = datetime.now()
date = now.strftime("%Y%m%d")
print(date)
pixel_param = {
    "date": date,
    "quantity": input("How many git commits BRAH: "),
}
pixel_response = requests.post(url=pixel_path, json=pixel_param,headers=header)
print(pixel_response.text)

# update_path = f"{pixel_path}/{date}"
# update_param = {
#     "quantity" : "0",
# }
# update_response = requests.put(url=update_path, json=update_param, headers = header)
# print(update_response.text + " sda")

# delete_response = requests.delete(url=update_path,headers=header)
# print(delete_response)