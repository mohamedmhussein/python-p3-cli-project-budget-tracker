from functions import create_category, create_expense, display_expenses, delete_all_records
from models import Expense, Category

if __name__ == "__main__":

    # name = input("Enter the category name: ")
    # create_category(name)

    # date = input("Enter the expense date (YYYY-MM-DD) ")
    # category_id = input("Enter the expense category id ")
    # amount = input("Enter the expense amount ")
    # description = input("Enter the expense description ")
    # create_expense(amount, description, category_id, date)

    delete_all_records(Expense)