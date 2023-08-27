from functions import create_category, create_expense, display_data, delete_all_records, sum_expenses, expense_by_month, delete_record, get_expenses_by_category_month, update_record, delete_all
from models import Expense, Category, Session
from sqlalchemy import desc
from sqlalchemy.orm import joinedload, relationship
import subprocess
import sys
import os
from simple_term_menu import TerminalMenu
from rich.console import Console
console = Console()


def restart_script(): #Restarting script function
    os.execl(sys.executable, python, sys.argv)
    #source: https://gist.github.com/plieningerweb/39e47584337a516f56da105365a2e4c6

def restart_script(): # A func
    script_path = os.path.abspath(__file__)  # Get the absolute path of the current script
    script_directory = os.path.dirname(script_path)  # Get the directory of the script
    python = sys.executable  # Get the path to the current Python interpreter
    script_name = os.path.basename(__file__)  # Get the name of the script
    subprocess.call([python, os.path.join(script_directory, script_name)])

if __name__ == "__main__":
    
    
    #Introductory text display
    console.print("\n******B U D G E T  T R A C K E R******", style ="bold underline bright_green", justify = "center")
    console.print("Welcome to the Budget Tracker CLI, where you can manage your finances and track your expenses easily.", style ="bold underline bright_green", justify = "center")
    console.print("\nChoose one of the following options to start:\n \n", style ="bold underline bright_yellow", )

    #App options
    options = ["Display Table","Add an expense","Add a new category","Sort expenses", "Sum expenses", "Monthly Expenses", "Sum of monthly expenses", "Get expenses by Category", "Update data", "Delete data row", "Delete an entire table records", "Seed Sample data (for testing purpose)"]
    
    user_choice = TerminalMenu(options).show()

    if user_choice == 0: #Display Table
        console.print("Which of the following table you want to display? \n", style = "bold bright_cyan")
        choice = TerminalMenu(["Expenses", "Categories"]).show() + 1
        if choice == 1: #Display expenses table
            session = Session()
            all_expenses = session.query(Expense).options(joinedload(Expense.category)).all()
            display_data(Expense, all_expenses)

        elif choice == 2: #Display categories table
            session = Session()
            all_categories = session.query(Category).all()
            display_data(Category, all_categories)

    elif user_choice == 1: #Adds a new expene
        date = input("Enter the expense date (YYYY-MM-DD) ")
        category_id = input("Enter the expense category id ")
        amount = input("Enter the expense amount ")
        description = input("Enter the expense description ")
        
        create_expense(amount, description, category_id, date)
        # restart_script()
    elif user_choice == 2: #Adds a new category
        name = input("Enter the category name: ")

        create_category(name)

    elif user_choice == 3: #Display sorted data
        sort_choice = int(input("1) Ascending\n2) Descending \n>>"))
        
        session = Session()
        if sort_choice == 1: #Ascending sorting
            sorted_data = session.query(Expense).order_by(Expense.amount).all()
            display_data(Expense, sorted_data)

        elif sort_choice == 2: #Descending sorting
            sorted_data = session.query(Expense).order_by(desc(Expense.amount)).all()
            display_data(Expense, sorted_data)

    elif user_choice == 4:
        sum_expenses()
    elif user_choice == 5: # Display expenses in a specific month
        #User input for month and year
        month = int(input("Enter the target month:\n >> "))
        year = int(input("Enter the target year:\n >> "))

        display_data(Expense, expense_by_month(month, year))

    elif user_choice == 6: #sum expenses in a specific month
        #User input for month and year
        month = int(input("Enter the target month:\n >> "))
        year = int(input("Enter the target year:\n >> "))

        sum_expenses(month, year)

    elif user_choice == 7: #Display expenses for a specific category
        #User choice of category
        print("Select the desired category: \n")
        session = Session()
        all_categories = session.query(Category).all()
        options = [str(category) for category in all_categories]
        category_id_choice = TerminalMenu(options).show() + 1
        print(category_id_choice)

        #Sort and display data
        sorted_data = get_expenses_by_category_month(category_id_choice)
        display_data(Expense,sorted_data)

    elif user_choice == 8: #Update a record
        #User input of the table
        console.print("Which of the following table you want to update: \n", style = "bold bright_cyan")
        choice = TerminalMenu(["Expenses", "Categories"]).show() + 1
        
        if choice == 1: #Update an expense record
            #The following 3 lines display the table
            session = Session()
            all_expenses = session.query(Expense).options(joinedload(Expense.category)).all()
            display_data(Expense, all_expenses)
            
            record_id = input("Enter the Expense id you desire to update >> ")
            #User input for the updated data
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
            #The following 3 lines display the table
            session = Session()
            all_categories = session.query(Category).all()
            display_data(Category, all_categories)
            
            record_id = input("Enter the Category id you desire to update >> ")

            #User input for the updated data
            category_name = input("\nEnter the updated category name >> ")
            new_data = {
                "name": category_name
            }

            update_record(Category, record_id, new_data)
        #Confirming the update to the user
        console.print("The record has been updated :white_heavy_check_mark: :white_heavy_check_mark:", style = "bold bright_green")

    elif user_choice == 9: #Delete a record

        console.print("Which of the following tables you want to delete: \n", style = "bold bright_cyan")
        choice = TerminalMenu(["Expenses", "Categories"]).show() + 1
        if choice == 1:
            #The following 3 lines display the table
            session = Session()
            all_expenses = session.query(Expense).options(joinedload(Expense.category)).all()
            display_data(Expense, all_expenses)

            record_id = input("Enter the Expense id you desire to delete >> ")

            delete_record(Expense, record_id)
        elif choice == 2:
            #The following 3 lines display the table
            session = Session()
            all_categories = session.query(Category).all()
            display_data(Category, all_categories)
            
            record_id = input("Enter the Category id you desire to update >> ")

            delete_record(Category, record_id)

        console.print("The record has been deleted :white_heavy_check_mark: :white_heavy_check_mark:", style = "bold bright_green")
    
    elif user_choice == 10:
        console.print("Choose the able where all records need to be deleted\n", style="bold underline cyan")
        options = ["Expenses table", "Categories table", "Both tables"]
        choice = TerminalMenu(options).show() + 1
        if choice == 1:
            delete_all(True, False)
        elif choice == 2:
            delete_all(False, True)
        else:
            delete_all()
    
    elif user_choice == 11: #Seed data for testing
        #Running seed files
        subprocess.run(['python', 'lib/seed_categories.py'])
        subprocess.run(['python', 'lib/seed_expenses.py'])
        
        
        console.print("Seed data has been successfully added to the database :white_heavy_check_mark: :white_heavy_check_mark:\n", style = "bold underline bright_yellow")
    
    #Promoting the user to re-run the app or exit
    console.print("Do you want to re-run the app or exit?\n", style="bold underline cyan")
    options = ["Re-run the app", "Exit"]
    final_choice = TerminalMenu(options).show() + 1
    if final_choice == 1:
        restart_script()
    else:
        console.print("Thank you for using the budget tracker CLI :green_heart::green_heart:\nTo run the app again, type 'python lib/cli.py'", style = "bold green3")