# Aplikacja Domowe Wydatki

Aplikacja Domowe Wydatki to prosty system do zarządzania osobistymi wydatkami, stworzony z użyciem Flask, Flask-WTF.

## Instalacja

Aby zainstalować i uruchomić aplikację lokalnie, wykonaj następujące kroki:

1. Sklonuj repozytorium:
git clone [URL_REPOZYTORIUM]

2. Przejdź do katalogu projektu:
cd domowe_wydatki

3. Utwórz środowisko wirtualne:
python -m venv venv
lub
python3 -m venv venv

4. Aktywuj środowisko wirtualne:
- Na Windows:
  ```
  venv\Scripts\activate
  ```
- Na MacOS/Linux:
  ```
  source venv/bin/activate
  ```
5. Zainstaluj wymagane zależności:
pip install -r requirements.txt
lub
pip3 install -r requirements.txt

6. Uruchom aplikację:
python app.py
lub
python3 app.py


## Użycie

Po uruchomieniu aplikacji, odwiedź `http://127.0.0.1:5000` w swojej przeglądarce.

- Na stronie głównej możesz zobaczyć listę wszystkich wydatków oraz dodać nowy wydatek.
- Aby edytować istniejący wydatek, kliknij na link 'Edytuj' obok wydatku.

## Rozwój

Aplikacja jest prostym projektem, który może być rozwijany w różnych kierunkach, w zależności od potrzeb użytkownika.
