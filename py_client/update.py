import requests


# for testing endpoint class ProductUpdateAPIView(generics.RetrieveAPIView)

endpoint = "http://localhost:8000/product/1/update/" 

data = {
    "name": "testing2",
    "price":23
}

get_response = requests.put(endpoint, json=data) #update methid put
print(get_response.json())