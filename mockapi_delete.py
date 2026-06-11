import requests 

base_url = 'https://6a15d51d91ff9a63de08dea8.mockapi.io/products'

id_product = 3

res_delete = requests.delete(
    
    base_url + '/' + str(id_product)
)

print(res_delete.status_code)