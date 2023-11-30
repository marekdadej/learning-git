import logging

def dodawanie(*args):
    result = sum(args)
    return result

def odejmowanie(a, b):
    result = a - b
    return result

def mnozenie(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

def dzielenie(a, b):
    result = a / b
    return result

logging.basicConfig(level=logging.INFO)

print("Podaj działanie, posługując się odpowiednią liczbą:")
print("1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")

operacja = int(input())

if operacja in [1, 2, 3, 4]:
    if operacja in [1, 3]:
        print(f"Podaj składniki, oddzielone spacją:")
        skladniki = list(map(float, input().split()))
        logging.info(f'Wybrane działanie: {operacja}')
        if operacja == 1:
            logging.info(f'Dodaję {", ".join(map(str, skladniki))}')
            print(f'Wynik to {sum(skladniki):.2f}')
        elif operacja == 3:
            logging.info(f'Mnożę {", ".join(map(str, skladniki))}')
            print(f'Wynik to {mnozenie(*skladniki):.2f}')
    else:
        print("Podaj pierwszą liczbę:")
        liczba1 = float(input())
        print("Podaj drugą liczbę:")
        liczba2 = float(input())
        logging.info(f'Wybrane działanie: {operacja}')
        if operacja == 2:
            logging.info(f'Odejmuję {liczba1} i {liczba2}')
            print(f'Wynik to {odejmowanie(liczba1, liczba2):.2f}')
        elif operacja == 4:
            if liczba2 == 0:
                print("Nie można dzielić przez zero.")
            else:
                logging.info(f'Dzielę {liczba1} przez {liczba2}')
                print(f'Wynik to {dzielenie(liczba1, liczba2):.2f}')
else:
    print("Niepoprawny wybór działania.")
