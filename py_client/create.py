import requests

endpoint = "http://localhost:8000/product/" 

data = {
    "name":"new",
    "description": "new",
    "price":8,
}
get_response = requests.post(endpoint, json=data)
print(get_response.json())

