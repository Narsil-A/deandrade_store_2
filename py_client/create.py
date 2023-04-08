import requests
from getpass import getpass 



auth_endpoint = "http://localhost:8000/product/auth/"

username = input("What is your username?\n")
password = getpass("What is your password ?\n")

auth_reponse = requests.post(auth_endpoint, json={'username':username, 'password':password})

print(auth_reponse.json())

if auth_reponse.status_code == 200:
    token = auth_reponse.json()['token']
    headers = {
        "authorization": f"Bearer {token}"
    }
    endpoint = "http://localhost:8000/product/"

data = {
        "url":'', 
        "pk":'',
        "name":"Labial",
        "get_absolute_url":'',
        "description":"Labial mate",
        "price":5,
        "get_image":'',
        "get_thumbnail":''
    }
get_response = requests.post(endpoint, json=data)
print(get_response.json())




