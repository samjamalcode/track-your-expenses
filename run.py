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


# Saved the user's expense to a CSV file for record-keeping
save_expense_to_file(expense, expense_file_path)


# Developed a function to read the expense file and provide a summary
summarize_expenses(expense_file_path, budget)


# Enhanced the expense input by including predefined categories for user selection
def get_user_expense(budget):
    print(f"🎯 Getting User Expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    expense_categories = [
        "🍔 Food",
        "🏠 Home",
        "💼 Work",
        "🎉 Fun",
        "✨ Misc",
    ]

    while True:
        # Presented expense categories for the user to choose from
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i + 1}. {category_name}")
        
        # Obtained user input for the selected expense category
        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        


















