from functions import create_category, create_expense, display_data, delete_all_records, sum_expenses, expense_by_month, delete_record, get_expenses_by_category_month, update_record
from models import Expense, Category, Session
from sqlalchemy import desc
from sqlalchemy.orm import joinedload, relationship
import subprocess
import sys
import os
from simple_term_menu import TerminalMenu
from rich.console import Console
console = Console()

def restart_script():
    script_path = os.path.abspath(__file__)  # Get the absolute path of the current script
    script_directory = os.path.dirname(script_path)  # Get the directory of the script
    python = sys.executable  # Get the path to the current Python interpreter
    script_name = os.path.basename(__file__)  # Get the name of the script
    subprocess.call([python, os.path.join(script_directory, script_name)])

if __name__ == "__main__":

    console.print("******B U D G E T  T R A C K E R******", style ="bold underline bright_green", justify = "center")

    # print("******BUDGET TRACKER******")
    # print("-----------------------------------")
    # print("Welcome to the Budget Tracker CLI!")
    # print("-----------------------------------")
    # print("Manage your finances and track your expenses easily.")
    # print("-----------------------------------")

    # print("Choose one of the following options:\n \n")

    options = ["Show all expenses","Show categories","Add an expense","Add a new category","Sort expenses", "Sum expenses", "Monthly Expenses", "Sum of monthly expenses", "Get expenses by Category", "Update data", "Delete data row"]
    user_choice = TerminalMenu(options).show()
    print(options[user_choice])

    if user_choice == 0:
        session = Session()
        all_expenses = session.query(Expense).options(joinedload(Expense.category)).all()
        display_data(Expense, all_expenses)
        # restart_script()
    elif user_choice == 1:
        session = Session()
        all_categories = session.query(Category).all()
        display_data(Category, all_categories)
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
    elif user_choice == 8:
        print("Select the desired category: \n")
        session = Session()
        all_categories = session.query(Category).all()
        options = [str(category) for category in all_categories]
        category_id_choice = TerminalMenu(options).show() + 1
        print(category_id_choice)
        sorted_data = get_expenses_by_category_month(category_id_choice)
        display_data(Expense,sorted_data)
    elif user_choice == 9:
        console.print("Which of the following table you want to update: \n", style = "bold bright_cyan")
        choice = TerminalMenu(["Expenses", "Categories"]).show() + 1
        if choice == 1:
            #The following 3 lines display the table
            session = Session()
            all_expenses = session.query(Expense).options(joinedload(Expense.category)).all()
            display_data(Expense, all_expenses)
            record_id = input("Enter the Expense id you desire to update >> ")

            date = input("\nEnter the expense date (YYYY-MM-DD) >> ")
            category_id = input("\nEnter the expense category id >> ")
            amount = input("\nEnter the expense amount >> ")
            description = input("\nEnter the expense description >> ")
            new_data = {
                "amount": amount,
                "description": description,
                "category_id": category_id,
                "date": date
            }
            update_record(Expense, record_id, new_data)
        
        elif choice == 2:
            session = Session()
            all_categories = session.query(Category).all()
            display_data(Category, all_categories)
            record_id = input("Enter the Category id you desire to update >> ")

            category_name = input("\nEnter the updated category name >> ")
            new_data = {
                "name": category_name
            }
            update_record(Category, record_id, new_data)

        console.print("The record has been updated :white_heavy_check_mark: :white_heavy_check_mark:", style = "bold bright_green")

    elif user_choice == 10:

        console.print("Which of the following tables you want to update: \n", style = "bold bright_cyan")
        choice = TerminalMenu(["Expenses", "Categories"]).show() + 1
        if choice == 1:
            #The following 3 lines display the table
            session = Session()
            all_expenses = session.query(Expense).options(joinedload(Expense.category)).all()
            display_data(Expense, all_expenses)
            record_id = input("Enter the Expense id you desire to delete >> ")

            delete_record(Expense, record_id)
        elif choice == 2:
            session = Session()
            all_categories = session.query(Category).all()
            display_data(Category, all_categories)
            record_id = input("Enter the Category id you desire to update >> ")

            delete_record(Category, record_id)

        console.print("The record has been deleted :white_heavy_check_mark: :white_heavy_check_mark:", style = "bold bright_green")