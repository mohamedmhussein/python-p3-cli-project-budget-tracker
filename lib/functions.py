from sqlalchemy.orm import sessionmaker
from sqlalchemy import desc, func
from models import engine, Session, Expense, Category
import subprocess
import sys
import os
from rich.console import Console
from rich.table import Table
from rich.text import Text
import random

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

def display_data(model_cls):
    print("\n")
    session = Session()
    console = Console()
    colors = ["cyan", "magenta", "bright_yellow", "white", "bright_green"]
    all_data = session.query(model_cls).all()
    table_title = Text(f"All {model_cls.__name__}s Data")
    table_title.stylize("bold bright_yellow")
    console.print(table_title)
    table = Table(show_header=True, header_style="bold")
    for column in model_cls.__table__.columns:
        table.add_column(column.name, style=random.choice(colors), header_style="bold")
    for data in all_data:
        table.add_row(*[str(getattr(data, column.name)) for column in model_cls.__table__.columns])
    console.print(table)

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



