from sqlalchemy.orm import sessionmaker
from sqlalchemy import desc, func
from models import engine, Session, Expense, Category
import subprocess
import sys
import os

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

def sort_by_amount(mode):
    session = Session()
    if mode == "ascending":
        sorted_data = session.query(Expense).order_by(Expense.amount).all()
    elif mode == "descending":
        sorted_data = session.query(Expense).order_by(desc(Expense.amount)).all()
    for row in sorted_data:
        print(row)
def sum_expenses():
    session = Session()
    expenses_sum = session.query(func.sum(Expense.amount)).first()
    print(f"${round(expenses_sum[0],2)}")



