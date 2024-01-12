from flask import Flask, jsonify, request, abort, render_template, redirect, url_for
from forms import ExpenseForm
from models import Expenses

app = Flask(__name__)
app.config['SECRET_KEY'] = 'l1hunti'

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

# Endpointy API
@app.route('/api/expenses', methods=['GET'])
def api_get_expenses():
    return jsonify(expenses.get_all())

@app.route('/api/expenses', methods=['POST'])
def api_create_expense():
    form = ExpenseForm(request.form)
    if form.validate():
        expenses.add({'title': form.title.data, 'amount': str(form.amount.data)})
        return jsonify({"message": "Expense added"}), 201
    else:
        return jsonify(form.errors), 400

@app.route('/api/expenses/<int:id>', methods=['GET'])
def api_get_expense(id):
    try:
        expense = expenses.get(id)
        return jsonify(expense)
    except IndexError:
        abort(404)

@app.route('/api/expenses/<int:id>', methods=['PUT'])
def api_update_expense(id):
    try:
        expense = expenses.get(id)
        form = ExpenseForm(request.form)
        if form.validate():
            expenses.update(id, {'title': form.title.data, 'amount': str(form.amount.data)})
            return jsonify({"message": "Expense updated"}), 200
        else:
            return jsonify(form.errors), 400
    except IndexError:
        abort(404)

@app.route('/api/expenses/<int:id>', methods=['DELETE'])
def api_delete_expense(id):
    try:
        expenses.delete(id)
        return jsonify({"message": "Expense deleted"}), 200
    except IndexError:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)


