import requests
from pprint import pprint

API_key = '5d54440abaa032b7a65ea578b2a3bfe0'
city = input('Enter city name: ')
url = f'https://api.openweathermap.org/data/2.5/weather?q=London&APPID={API_key}&units=metric'
response = requests.get(url).json()
print(response)
