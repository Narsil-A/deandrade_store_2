import requests

endpoint = "http://localhost:8000/product/" 

data = {
    "name",
    "description",
    "price",
}
get_response = requests.post(endpoint, json=data)
print(get_response.json())

