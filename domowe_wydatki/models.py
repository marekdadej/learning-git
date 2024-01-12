import json

class Expenses:
    def __init__(self):
        self.load_data()

    def load_data(self):
        try:
            with open("expenses.json", "r") as file:
                self.expenses = json.load(file)
        except FileNotFoundError:
            self.expenses = []

    def save_data(self):
        with open("expenses.json", "w") as file:
            json.dump(self.expenses, file)

    def get_all(self):
        return self.expenses

    def add(self, expense):
        self.expenses.append(expense)
        self.save_data()

    def get(self, id):
        return self.expenses[id]

    def update(self, id, data):
        self.expenses[id] = data
        self.save_data()
