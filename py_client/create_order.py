import requests
from getpass import getpass 



auth_endpoint = "http://localhost:8000/auth/checkout/"

username = input("What is your username?\n")
password = getpass("What is your password ?\n")

auth_reponse = requests.post(auth_endpoint, json={'username':username, 'password':password})

print(auth_reponse.json())

if auth_reponse.status_code == 200:
    token = auth_reponse.json()['token']
    headers = {
        "authorization": f"Token {token}"
    }
    endpoint = "http://localhost:8000/order/checkout/"

data = {
        "id":1,
        "first_name":"Andrea",
        "last_name":"Camargo",
        "email":"andrea@django.com",
        "address":"san antonio",
        "zipcode":"2010",
        "place":"Caracas",
        "phone":"04241170505",
        "stripe_token":'',
        "items":'',
    }
get_response = requests.post(endpoint, json=data)
print(get_response.json())

