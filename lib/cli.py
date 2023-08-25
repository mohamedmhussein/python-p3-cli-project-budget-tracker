from functions import create_category, create_expense, display_data, delete_all_records, restart_script
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
    print("2) Show categories")
    print("3) Add an expense")
    print("4) Add a new category")
    user_choice = int(input(">>  "))

    if user_choice == 1:
        display_data(Expense)
    elif user_choice == 2:
        display_data(Category)
    elif user_choice == 3:
        date = input("Enter the expense date (YYYY-MM-DD) ")
        category_id = input("Enter the expense category id ")
        amount = input("Enter the expense amount ")
        description = input("Enter the expense description ")
        create_expense(amount, description, category_id, date)
    elif user_choice == 4:
        name = input("Enter the category name: ")
        create_category(name)
    elif user_choice == 5:
        
        
        
        # restart_script("lib/cli.py")

