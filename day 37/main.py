import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "vishwanath"
TOKEN = "2jhhgrk2burjb3ulfgwkirh"
GRAPH_ID = "graph1"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

#response = requests.post(url=pixela_endpoint,json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id" : GRAPH_ID,
    "name" : "Cycling Graph",
    "unit" : "km",
    "type" : "float",
    "color" : "ajisai",
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

#response = requests.post(url=graph_endpoint,json=graph_params,headers=headers)
#print(response.text)

pixela_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "0.0",
 }

pixel_response = requests.post(url=pixela_creation_endpoint,json=pixel_data,headers=headers)
print(pixel_response.text)