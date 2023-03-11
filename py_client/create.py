import requests

endpoint = "http://localhost:8000/product/" 

data = {
    "name":"facial",
    "description": "face",
    "price":78,
}
get_response = requests.post(endpoint, json=data)
print(get_response.json())

