import requests


base_url = 'https://reqres.in/api/collections/todos/records'

project_id = {
    
    'project_id' : 26590
    
}

# Создание заголовка в котором сохранён токен авторизации 
header_auth = {
    
   'x-api-key' : 'pro_4299c0733dac257311a8c9e1412f1f7905abdf538d224b661be17fe08d740f56' 
    
}


res = requests.get(
    
    base_url,
    # передача заголовка с токеном
    headers=header_auth,
    params=project_id
    
)


info = requests.get(
    
    base_url + '/d3bef05a-355f-446a-8c8d-61bdf2318f75',
    headers = {'x-api-key': 'pro_4299c0733dac257311a8c9e1412f1f7905abdf538d224b661be17fe08d740f56'},
    params=project_id
    
    
)

to_do_dict = {
    
    
  "data": {
    "title": "buy milk",
    'priority' : 0,
    'completed': False
  }
}
    


to_do = requests.post(
    
    base_url,
    headers = {'x-api-key': 'pro_4299c0733dac257311a8c9e1412f1f7905abdf538d224b661be17fe08d740f56'},
    params=project_id,
    # сервер понимает что какая-то информация хранится в параметре json и мы помещаем новую информацию в параметр json
    json=to_do_dict

    
    
)    
    
print(info.status_code)
print(res.status_code)
print(to_do.status_code)