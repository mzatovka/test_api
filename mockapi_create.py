import requests

base_url = 'https://6a15d51d91ff9a63de08dea8.mockapi.io/products'

new_product = {
    
    "title": "Apple",
    "description": "tasty apple",
    "price": "3.6",
    "count": 12
    
    
}

responce_create = requests.post(
    
    base_url,
    json=new_product
    
)

print(responce_create.status_code)


