import requests

# for testing endpoint class ProductDetailAPIView(generics.RetrieveAPIView)
endpoint = "http://localhost:8000/product/2/" 

# pk = > 4 not exist 

get_response = requests.get(endpoint)

print(get_response.json())