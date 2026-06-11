import requests

base_url = 'https://6a15d51d91ff9a63de08dea8.mockapi.io/products'


new_data_product = {
    
    "title": "Apple",
    "description": "tasty apple",
    "price": "3.99",
    "count": 100
    
    
}

responce_update = requests.put(
    
    base_url + '/12',   # указываем точно какой конкретно id мы изменяем 
    json=new_data_product
    
    
)

print(responce_update.status_code)




