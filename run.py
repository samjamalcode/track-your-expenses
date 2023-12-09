class Expense:
    def __init__(self, name, category, amount) -> None:
        # Initializes an Expense object with a name, category, and amount.
        self.name = name
        self.category = category
        self.amount = amount

    def __repr__(self):
        # Returns a string representation of the Expense object.
        return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f} >"