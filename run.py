# Added import statements for calendar and datetime modules
import calender
import datetime


# Define the Expense class: Created the Expense class to represent user expenses.
class Expense:
    def __init__(self, name, category, amount, budget) -> None:
        self.name = name
        self.category = category
        self.amount = amount
        self.budget = budget

    def __repr__(self):
        return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f}, Budget: ${self.budget:.2f} >"


# Set up the main function to organize the expense tracking process
def main():
    print(f"🎯 Running Expense Tracker!")
    expense_file_path = "expenses.csv"


# Prompted the user to input their budget for the month
budget = float(input("Enter your budget for the month: "))


# Implemented a function to gather user input for a specific expense
expense = get_user_expense(budget)


# Write the expense to a file
# Read file and summarize expenses
