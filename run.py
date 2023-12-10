# Added import statements for calendar and datetime modules
import calendar
import datetime


# Created the Expense class to represent user expenses
class Expense:
    def __init__(self, name, category, amount, budget) -> None:
        self.name = name
        self.category = category
        self.amount = amount
        self.budget = budget

    def __repr__(self):
        return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f}, Budget: ${self.budget:.2f} >"


# Enhanced the expense input 
# by including predefined categories for user selection
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

        # Ensured the selected category is valid and created an Expense object
        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amount, budget=budget
            )
            return new_expense
        else:
            print("Invalid category. Please try again!")


# Appended the user's expense to the CSV file for future reference
def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"🎯 Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category},{expense.budget}\n")
        


# Calculated and displayed a summary of expenses 
# by category and overall spending
def summarize_expenses(expense_file_path, budget):
    print(f"🎯 Summarizing User Expense")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        # Improved the file reading process for better expense parsing
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category, expense_budget = line.strip().split(",")
            line_expense = Expense(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category,
                budget=float(expense_budget),
            )
            expenses.append(line_expense)
    
    # Enhanced the summary display 
    # with total spending, remaining budget, and daily budget
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expenses By Category 📈:")
    for key, amount in amount_by_category.items():
        print(f"  {key}: ${amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(f"💵 Total Spent: ${total_spent:.2f}")

    remaining_budget = budget - total_spent
    print(f"✅ Budget Remaining: ${remaining_budget:.2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    daily_budget = remaining_budget / remaining_days
    print(green(f"👉 Budget Per Day: ${daily_budget:.2f}"))


# Added a function to colorize console output for better user experience
def green(text):
    return f"\033[92m{text}\033[0m"


# Added a function to check if the user wants to add another expense
def ask_add_another_expense():
    response = input("Do you want to add another expense? (yes/no): ").lower()
    return response == 'yes'



# Set up the main function to organize the expense tracking process
def main():
    print(f"🎯 Running Expense Tracker!")


# Prompted the user to input their budget for the month
budget = float(input("Enter your budget for the month: "))


# Implemented a function to gather user input for a specific expense
expense = get_user_expense(budget)

# Define expenses_file_path
expense_file_path = "expenses.csv"


# Saved the user's expense to a CSV file for record-keeping
save_expense_to_file(expense, expense_file_path)


# Developed a function to read the expense file and provide a summary
summarize_expenses(expense_file_path, budget)


# Ensured the main function runs when the script is executed directly
if __name__ == "__main__":
    main()











