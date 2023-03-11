import requests

endpoint = "http://localhost:8000/product/" 

data = {
    "name":"facial creme",
    "description":"creme for face",
    "price":55,
}
get_response = requests.post(endpoint, json=data)
print(get_response.json())

