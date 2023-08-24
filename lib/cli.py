from functions import create_category, create_expense, display_expenses, delete_all_records
from models import Expense, Category

if __name__ == "__main__":

    print("******BUDGET TRACKER******")
    print("-----------------------------------")
    print("Welcome to the Budget Tracker CLI!")
    print("-----------------------------------")
    print("Manage your finances and track your expenses easily.")
    print("-----------------------------------")

    print("Choose one of the following options (enter the number chosen):\n \n")

    print("1) Show all expenses")
    print("2) show categories")
    print("3) Add an expense")
    print("4) Add a new category")
    user_choice = int(input("> "))

    if user_choice is 1:
        display_expenses()
    # elif user_choice is 2:




    # name = input("Enter the category name: ")
    # create_category(name)

    # date = input("Enter the expense date (YYYY-MM-DD) ")
    # category_id = input("Enter the expense category id ")
    # amount = input("Enter the expense amount ")
    # description = input("Enter the expense description ")
    # create_expense(amount, description, category_id, date)
