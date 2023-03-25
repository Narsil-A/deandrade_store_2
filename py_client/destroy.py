import requests

product_id = input("What is the product id you want to use?\n")

try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} not a valid id')

if product_id:    

    # for testing endpoint class ProductDestroyAPIView(generics.DestroyAPIView)
    endpoint = f"http://localhost:8000/product/{product_id}/destroy/" 

    # pk = > 4 not exist 
    get_response = requests.delete(endpoint) 
    print(get_response.status_code, get_response.status_code==204)