import requests

endpoint = "http://localhost:8000/product/" 

data = {
    "name":"new1",
    "description": "new2",
    "price":23,
}
get_response = requests.post(endpoint, json=data)
print(get_response.json())

