import requests
from datetime import datetime

today = datetime.now()
TODAY = today.strftime('%Y%m%d')

TOKEN = "Welcome1"
USERNAME = "creative"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_config = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response_user_config = requests.post(url=pixela_endpoint, json=user_config)
#Creating the Graph URL https://pixe.la/v1/users/creative/graphs/graph1.html


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Working Graph",
    "unit": "hours",
    "type": "float",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

response_graph_config = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

graph_post_config = {
    "date":TODAY,
    "quantity": "3"
}

response_graph_post = requests.post(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}", headers=headers, json=graph_post_config)


graph_update_config = {
    "quantity": "1"
}

response_graph_post = requests.put(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}", headers=headers, json=graph_update_config)
