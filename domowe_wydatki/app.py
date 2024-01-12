from flask import Flask, render_template, redirect, url_for, request
from forms import ExpenseForm
from models import Expenses

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TwojTajnyKlucz'

expenses = Expenses()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ExpenseForm()
    if form.validate_on_submit():
        expenses.add({'title': form.title.data, 'amount': str(form.amount.data)})
        return redirect(url_for('index'))
    return render_template('index.html', form=form, expenses=expenses.get_all())

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    expense = expenses.get(id)
    if 'amount' in expense and expense['amount']:
        expense['amount'] = float(expense['amount'])
    form = ExpenseForm(data=expense)
    if form.validate_on_submit():
        updated_expense = {'title': form.title.data, 'amount': str(form.amount.data)}
        expenses.update(id, updated_expense)
        return redirect(url_for('index'))

    return render_template('edit.html', form=form, id=id)

if __name__ == '__main__':
    app.run(debug=True)
