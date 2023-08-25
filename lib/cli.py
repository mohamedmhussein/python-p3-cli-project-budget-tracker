from functions import create_category, create_expense, display_data, delete_all_records, sort_by_amount, sum_expenses
from models import Expense, Category
import subprocess
import sys
import os

def restart_script():
    script_path = os.path.abspath(__file__)  # Get the absolute path of the current script
    script_directory = os.path.dirname(script_path)  # Get the directory of the script
    python = sys.executable  # Get the path to the current Python interpreter
    script_name = os.path.basename(__file__)  # Get the name of the script
    subprocess.call([python, os.path.join(script_directory, script_name)])

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
    print("5) Sort expenses")
    print("6) Sum expenses")
    user_choice = int(input(">>  "))

    if user_choice == 1:
        display_data(Expense)
        restart_script()
    elif user_choice == 2:
        display_data(Category)
        restart_script()
    elif user_choice == 3:
        date = input("Enter the expense date (YYYY-MM-DD) ")
        category_id = input("Enter the expense category id ")
        amount = input("Enter the expense amount ")
        description = input("Enter the expense description ")
        create_expense(amount, description, category_id, date)
        restart_script()
    elif user_choice == 4:
        name = input("Enter the category name: ")
        create_category(name)
        restart_script()
    elif user_choice == 5:
        sort_choice = int(input("1) Ascending\n2) Descending \n>>"))
        if sort_choice == 1:
            sort_by_amount("ascending")
        elif sort_choice == 2:
            sort_by_amount("descending")
        restart_script()
    elif user_choice == 6:
        sum_expenses()



