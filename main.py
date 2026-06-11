import requests 

args = {
    
    'name': 'monitor',
    'size': 25
    


# выполнение запроса get с параметрами args
# метод get позволяет получить информацию с ссылки      
}

response = requests.get("https://httpbin.org/get", params=args)

# json метод , который позволяет извлечь данные из ответа response 
# в примере получаем данные args(ключ) 
print(response.status_code)

#print(response.json()["args"])


# запрос post нужен для создания новых обЪектов 
client_body = {
    
    'title': 'наушники',
    'price': 150
    
}

res_post = requests.post(
    
    'https://httpbin.org/post',
    json=client_body 
    
)

#print(res_post.json())

# запросы put нужны для изменения всего объекта 
# patch частично изменяет объекты 
change_id = {
    
    'id':'1',
    
}

change_data = {
    
    'title':'наушники',
    'price': 200
    
}


res_put = requests.put(
    
    'https://httpbin.org/put',
    params=args,
    json=change_data
    
)

print(res_put.json())

# delete используется для удаления объектов
res_del = requests.delete(
    
    
    'https://httpbin.org/delete',
    params={
        'id': 2
    }
    
    )


print(res_del.json())


