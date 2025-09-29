import requests
import json
api_key = '756d78a664c5adbe666ff998200e85a7'
city_name = 'Seoul'

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

data = requests.get(url)

#print(data.text)

data_dict = json.loads(data.text)
print(data_dict['name'])