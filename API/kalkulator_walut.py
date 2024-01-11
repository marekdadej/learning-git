import requests
import csv

# Pobieranie danych z API
response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

# Zapis do pliku CSV
with open('kursy_walut.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['currency', 'code', 'bid', 'ask'])  # Nagłówki

    for rate in data[0]['rates']:
        writer.writerow([rate['currency'], rate['code'], rate['bid'], rate['ask']])
