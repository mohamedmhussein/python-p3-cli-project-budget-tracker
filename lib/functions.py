from sqlalchemy.orm import sessionmaker
from models import engine, Session, Expense, Category

def create_expense():
    category_id = input("Enter the expense category id")
    amount = input("Enter the expense amount")
    description = input("Enter the expense description")

    session = Session()
    new_expense = Expense(amount = amount, category_id = category_id, description = description)
    session.add(new_expense)
    session.commit()

def create_category(name):
    session = Session()
    new_category = Category(name = name)
    session.add(new_category)
    session.commit()

def delete_all_records(table):
    session = Session()
    session.query(table).delete()
    session.commit()

def display_expenses():
    session = Session()
    all_expenses = session.query(Expense).all()
    for expense in all_expenses:
        print(expense.amount)
