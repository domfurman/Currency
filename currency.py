import requests
import json

option_choose = input('''
Choose operation you want to do, type:
1 to check rates
2 to convert one currency to another
3 to chech the average rates for some amount of days
''')

def rate_check():
    currency = input('Enter currency you want to check (GBP, PLN, EUR etc.): ')
    url = f'https://api.nbp.pl/api/exchangerates/rates/c/{currency}/today/?format=json'
    response = requests.get(url)
    json_data = json.loads(response.text)
    return round(json_data['rates'][0]['bid'], 2) 
#print(rate_check())
def converter():
    source_currency = input('Enter currency you want to convert (EUR, GBP etc,): ')
    source_currency_amount = int(input('Enter amount of currency you want to convert: '))
    target_currency = input('Enter currency in which you want the result (GBP, EUR etc.): ')

    source_url = f'https://api.nbp.pl/api/exchangerates/rates/c/{source_currency}/today/?format=json'
    source_response = requests.get(source_url)
    source_json_data = json.loads(source_response.text)

    target_currency_url = f'https://api.nbp.pl/api/exchangerates/rates/c/{target_currency}/today/?format=json'
    target_response = requests.get(target_currency_url)
    target_json_data = json.loads(target_response.text)

    scaler = source_json_data['rates'][0]['ask']/target_json_data['rates'][0]['ask']
    return round(source_currency_amount * scaler, 2)
#print(converter())


#ask_sum = 0
#bid_sum = 0
#for value in json_data['rates']:
#    ask_sum += value['ask']
#   bid_sum += value['bid']
#print(round(ask_sum/5, 2))
#print(json_data['rates'])