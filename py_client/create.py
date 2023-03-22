import requests

headers = {'Authorization': 'Token a4ab5f80e4608500a5720d8f0c0de663432ec06b'}


endpoint = "http://localhost:8000/product/" 

data = {
    "name":"nedwh1",
    "description": "newhas2",
    "price":23,
}
get_response = requests.post(endpoint, json=data)
print(get_response.json())

