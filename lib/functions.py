from sqlalchemy.orm import sessionmaker
from models import engine, Session, Expense, Category


def create_expense(amount,description,category_id, date):
    session = Session()
    new_expense = Expense(amount = amount, category_id = category_id, description = description, date = date)
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

def display_data(table):
    print("\n")
    session = Session()
    all_data = session.query(table).all()
    for row in all_data:
        print(row)


