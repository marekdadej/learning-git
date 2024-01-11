from flask import Flask, render_template, request, url_for
import csv

app = Flask(__name__)

@app.route('/kalkulator', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        currency_code = request.form['currency']
        amount = float(request.form['amount'])
        cost = calculate_cost(currency_code, amount)
        return render_template('index.html', rates=get_rates(), cost=cost)
    return render_template('index.html', rates=get_rates(), cost=None)  # None, jeśli jeszcze nie obliczono kosztu

def get_rates():
    rates = []
    with open('kursy_walut.csv', newline='', encoding='utf-8') as file:
        csvreader = csv.DictReader(file, delimiter=';')
        for row in csvreader:
            rates.append(row)
    return rates

def calculate_cost(code, amount):
    rates = get_rates()
    for rate in rates:
        if rate['code'] == code:
            return amount * float(rate['ask'])
    return 0

if __name__ == '__main__':
    app.run(debug=True)
