import requests

endpoint = "http://localhost:8000/product/" 

data = {
    "name":"Body creme",
    "description": "body creme ",
    "price":46,
}
get_response = requests.post(endpoint, json=data)
print(get_response.json())

