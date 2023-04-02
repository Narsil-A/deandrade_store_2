import requests
import stripe 

# stripe api key globally

stripe.api_key = 'sk_test_51LD9B4Hg5MZzC85xuF8GZjWf2cBnETEGqfLH7M5DMGTP74TmV0Z3psIfSVnlp8VPSC2V2SAuWq4bE1ZTVY7SRM3g00HvcTyfkA'

# account_id
# account_id = 'account_id'

# request

# print(stripe.Customer.list(stripe_account=account_id))

# CRUD operation stripe customer
# create customer 
# customer = (stripe.Customer.create())
# print(customer)

# retrive customer 

customer = (stripe.Customer.retrieve('cus_NdaEqkpcGa17ht'))
print(customer)
