import requests

base_url = 'https://6a15d51d91ff9a63de08dea8.mockapi.io/products'

all_products = requests.get(base_url)

#print(all_products.status_code) 

#if all_products.status_code == 200:
    #print(all_products.json()[0]['title'])    
    #print('title' in all_products.json()[0])

args_product = {
    
    'title':'Computer',
    'count': 39
    
    
}
    
responce_computer = requests.get(base_url,
                                 params=args_product)

print(responce_computer.status_code)
print(responce_computer.json())

id_product = 3

res_one_product = requests.get(f'{base_url}/{id_product}')

print(res_one_product.json())





    
    
