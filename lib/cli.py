from functions import create_category, create_expense, display_data, delete_all_records, sum_expenses, expense_by_month
from models import Expense, Category, Session
from sqlalchemy import desc
from sqlalchemy.orm import joinedload, relationship
import subprocess
import sys
import os
from simple_term_menu import TerminalMenu

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

    print("Choose one of the following options:\n \n")

    options = ["Show all expenses","Show categories","Add an expense","Add a new category","Sort expenses", "Sum expenses", "Monthly Expenses", "Sum of monthly expenses"]
    terminal_menu = TerminalMenu(options)
    user_choice = terminal_menu.show()
    print(options[user_choice])

    if user_choice == 0:
        session = Session()
        all_data = session.query(Expense).options(joinedload(Expense.category)).all()
        display_data(Expense, all_data)
        # restart_script()
    elif user_choice == 1:
        session = Sessoin()
        all_data = session.query(Category).all()
        display_data(Category, all_data)
        # restart_script()
    elif user_choice == 2:
        date = input("Enter the expense date (YYYY-MM-DD) ")
        category_id = input("Enter the expense category id ")
        amount = input("Enter the expense amount ")
        description = input("Enter the expense description ")
        create_expense(amount, description, category_id, date)
        # restart_script()
    elif user_choice == 3:
        name = input("Enter the category name: ")
        create_category(name)
        # restart_script()
    elif user_choice == 4:
        sort_choice = int(input("1) Ascending\n2) Descending \n>>"))
        session = Session()
        if sort_choice == 1:
            sorted_data = session.query(Expense).order_by(Expense.amount).all()
            display_data(Expense, sorted_data)
            # sort_by_amount("ascending")
        elif sort_choice == 2:
            sorted_data = session.query(Expense).order_by(desc(Expense.amount)).all()
            display_data(Expense, sorted_data)            
            # sort_by_amount("descending")
        # restart_script()
    elif user_choice == 5:
        sum_expenses()
    elif user_choice ==6:
        month = int(input("Enter the target month:\n >> "))
        year = int(input("Enter the target year:\n >> "))
        display_data(Expense, expense_by_month(month, year))
    elif user_choice == 7:
        month = int(input("Enter the target month:\n >> "))
        year = int(input("Enter the target year:\n >> "))
        sum_expenses(month, year)


