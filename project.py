import requests
from bs4 import BeautifulSoup

url = 'https://api.nbp.pl/api/exchangerates/rates/a/eur/'
response = requests.get(url)

print(response)