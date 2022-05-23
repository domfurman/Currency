import requests
from pprint import pprint

API_key = '5d54440abaa032b7a65ea578b2a3bfe0'
city = input('enter')
url = f'https://api.openweathermap.org/data/2.5/weather?lat=250&lon=250&appid={API_key}'
response = requests.get(url).json()
print(response)
