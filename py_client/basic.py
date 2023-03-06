import requests 

# endpoint = "https://httpbin.org/status200/"

# endpoint = "https://httpbin.org/anything"

endpoint = "http://localhost:8000/product"

# requests.get() 

get_response = requests.get(endpoint, json={"query":"Hello world"}) # HTTP request

print(get_response.json()['messege']) # print raw text response 

print(get_response.text)

print(get_response.status_code)