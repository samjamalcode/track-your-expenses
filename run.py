
# Define the Expense class: Created the Expense class to represent user expenses.
class Expense:
    def __init__(self, name, category, amount, budget) -> None:
        self.name = name
        self.category = category
        self.amount = amount
        self.budget = budget  

    def __repr__(self):
        return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f}, Budget: ${self.budget:.2f} >"