import requests

# for testing endpoint class ProductDetailAPIView(generics.RetrieveAPIView)
endpoint = "http://localhost:8000/product/1/" 

get_response = requests.get(endpoint) 
print(get_response.json())