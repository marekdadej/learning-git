from flask import Flask, render_template, url_for, request, redirect
import time

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/o_mnie')
def o_mnie():
    return render_template('o_mnie.html')

@app.route('/kontakt', methods=['GET'])
def kontakt():
    return render_template('kontakt.html')

@app.route('/kontakt', methods=['POST'])
def send():
    if request.method == 'POST':
        name = request.form['name']
        lastname = request.form['lastname']
        email = request.form['email']
        phone = request.form['tel']
        message = request.form['wiadomość']
        
        # Dane do zapisania w pliku
        data = f"Dane otrzymane od: {name} {lastname}, Email: {email}, Telefon: {phone}, Wiadomość: {message}\n"
        
        # Zapis do pliku save.txt
        with open('save.txt', 'a') as file:
            file.write(data)
    
        time.sleep(3)  # Oczekiwanie 3 sekund
        return redirect('/kontakt')  # Przekierowanie na stronę home po 3 sekundach
        

if __name__ == '__main__':
    app.run(debug=True)