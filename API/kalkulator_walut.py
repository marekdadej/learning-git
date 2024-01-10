import requests
import csv

# Funkcja do pobierania kursów walut z API NBP
def pobierz_kursy_walut():
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    data = response.json()
    return data[0]['rates']

# Funkcja do przeliczania waluty
def przelicz_walute(rates, kod_waluty, ilosc):
    for rate in rates:
        if rate['code'] == kod_waluty:
            return ilosc * rate['ask']
    return None

# Pobranie kursów walut
rates = pobierz_kursy_walut()

# Przygotowanie danych do zapisu w formacie CSV
csv_data = [["currency", "code", "bid", "ask"]]

for rate in rates:
    csv_data.append([rate['currency'], rate['code'], rate['bid'], rate['ask']])

# Zapis do pliku CSV
with open('kursy_walut.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(csv_data)

print("Plik CSV został utworzony.")

# Interfejs użytkownika dla kalkulatora walut
kod_waluty = input("Podaj kod waluty (USD, AUD, CAD, EUR, HUF, CHF, GBP, JPY, CZK, DKK, NOK, SEK, XDR): ")
ilosc = float(input("Podaj ilość waluty do przeliczenia: "))

wynik = przelicz_walute(rates, kod_waluty, ilosc)
if wynik is not None:
    print(f"Koszt {ilosc} {kod_waluty} w PLN to {wynik:.2f}")
else:
    print("Nie znaleziono podanej waluty.")