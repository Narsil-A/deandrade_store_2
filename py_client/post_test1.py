import requests


headers = {'Authorization': 'Bearer 01c61e4d32583048b62c110e75fac70f5d9431e8'}
endpoint = "http://localhost:8000/product/" 

data = {
    "name":"skin care",
    "get_absolute_url":"",
    "products":""
    }
get_response = requests.post(endpoint, json=data, headers=headers) 
print(get_response.json())