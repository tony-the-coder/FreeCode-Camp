### Gather the expense and category after user selection and add it to the expense discionary
def add_expense(expenses, amount, category):
    expenses.append({"amount": amount, "category": category})


### loop through the items in the dictionary and print the information.


def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')


### using a lambda to create an anonymous through away function to get the total of expenses, then using map to gather the items in the dictionary, and sum it with the sum function.


def total_expenses(expenses):
    return sum(map(lambda expense: expense["amount"], expenses))


### Look more into Python Filters


def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense["category"] == category, expenses)


### The main function that starts everything off.
def main():
    expenses = []
    while True:
        print("\nExpense Tracker")
        print("1. Add an expense")
        print("2. List all expenses")
        print("3. Show total expenses")
        print("4. Filter expenses by category")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            add_expense(expenses, amount, category)

        elif choice == "2":
            print("\nAll Expenses:")
            print_expenses(expenses)

        elif choice == "3":
            print("\nTotal Expenses: ", total_expenses(expenses))

        elif choice == "4":
            category = input("Enter category to filter: ")
            print(f"\nExpenses for {category}:")
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)

        elif choice == "5":
            print("Exiting the program.")
            break
