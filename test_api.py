
import requests 

# так как это пайтест все функции должы начинаться со слова test 
def test_get_all_products():
    res = requests.get(
        
        'https://6a15d51d91ff9a63de08dea8.mockapi.io/products'
        
    )

    assert res.status_code == 200
    # для того чтобы достать информацию из res применяем .json
    assert len(res.json()) > 0 
    
    
def test_get_one_product():
    res = requests.get(
        
        'https://6a15d51d91ff9a63de08dea8.mockapi.io/products/1'
        
    )
    
    product_data = res.json()
    
    assert res.status_code == 200 
    
    assert "title" in product_data
    assert 'price' in product_data
    
    
    
def test_create_product():
    
    res = requests.post(            
        'https://6a15d51d91ff9a63de08dea8.mockapi.io/products',

        
    
        json = {
        
            "title": "Phone",
            "description": "smart device",
            "price": "999",
            "count": 5
        
        }
    )
    

    assert res.status_code in [200,201]
    
    
    id_new_product = res.json()['id']
    
    res_get = requests.get(
        
        'https://6a15d51d91ff9a63de08dea8.mockapi.io/products/'+id_new_product
        
    )
    
    assert res_get.status_code == 200
    assert 'title' in res_get.json()
    
    
    
def test_delete_one_product():
    res_add = requests.post(
        
        'https://6a15d51d91ff9a63de08dea8.mockapi.io/products',
        json = {
            
            "title": "Phone",
            "description": "smart device",
            "price": "999",
            "count": 5
            
         
        }
        
    )
    
    id_added_product = res_add.json()['id']
    
    
    res = requests.delete(
        
        'https://6a15d51d91ff9a63de08dea8.mockapi.io/products/'+id_added_product
        
    )
    
    assert res.status_code == 200
    
    res_get = requests.get(
        
        
        'https://6a15d51d91ff9a63de08dea8.mockapi.io/products/'+id_added_product

        
    )
    
    assert res_get.status_code == 404