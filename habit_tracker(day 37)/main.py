import requests
import datetime as dt
import os

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = os.environ['TOKEN']
USERNAME = os.environ['NAME']

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# # response.text to check if it ran or not
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
ID = "graph1"
graphs_config = {
    "id": ID,
    "name": "Cycling graph",
    "unit": "km",
    "type": "float",
    "color": "momiji"
}
# color's value is in japanese. momiji = red

# have to pass a security key to make it work
headers = {
    "X-USER-TOKEN": TOKEN
}
pixel_url = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"
# response1 = requests.post(url=graph_endpoint, json=graphs_config, headers=headers)
# print(response1.text)

today = dt.datetime.now()
date = today.strftime("%Y%m%d")

pixel_params = {
    "date": date,
    # notes on day 37
    "quantity": "10",
}

# response3 = requests.post(url=pixel_url, json=pixel_params, headers=headers)
# print(response3.text)

updated_pixel_params = {
    "quantity": "4"
}
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{20240116}"

# response4 = requests.put(url=update_pixel_endpoint,json=updated_pixel_params, headers=headers)
# print(response4.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{20240116}"

response5 = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response5.text)
