import requests
import json

#currency_shortcut = input('Enter currency shortcut: ')
url = f'https://api.nbp.pl/api/exchangerates/rates/c/eur/last/5/?format=json'
response = requests.get(url)
json_data = json.loads(response.text)
#data = json.loads(text)

for rate in json_data['rates']:
    print(rate)
print(len(json_data['rates']))