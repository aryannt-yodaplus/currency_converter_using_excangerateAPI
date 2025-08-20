import requests
import os


amt = float(input('Enter Amout: '))
from_currency = input('Source Currency: ').upper()
to_currency = input('Converted Currency: ').upper()

url = F'https://v6.exchangerate-api.com/v6/742e36dd1fe17d038c4c3e19/latest/{from_currency}'
response = requests.get(url)
data = response.json()

rate = data['conversion_rates'][to_currency]

converted_amt = amt * rate

print(f'Converted {amt} from {from_currency} to {converted_amt} {to_currency}')