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
    console = Console()
    categories_count = session.query(func.count(Category.id)).first()[0]

    if int(category_id) > categories_count:
        console.print("\nCategory does not exist, please try again", style = "bold underline bright_red")
    else:
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

def display_data(model_cls, all_data):
    print("\n")

    console = Console()
    colors = ["cyan", "magenta", "bright_yellow", "white", "bright_green"]
    table_title = Text(f"{model_cls.__name__}s Data")
    table_title.stylize("bold bright_yellow")
    console.print(table_title)
    table = Table(show_header=True, header_style="bold")
    for column in model_cls.__table__.columns:
        table.add_column(column.name, style=random.choice(colors), header_style="bold")

    # Add an additional column for 'category'
    table.add_column("Category", style=random.choice(colors), header_style="bold")

    for data in all_data:
        # Retrieve category name using the relationship attribute 'category'
        category_name = data.category.name if hasattr(data, 'category') else ""

        row_values = [str(getattr(data, column.name)) for column in model_cls.__table__.columns]
        row_values.append(category_name)
        table.add_row(*row_values)
    console.print(table)

def sum_expenses(month = None, year = None):
    session = Session()
    expenses_sum = session.query(func.sum(Expense.amount))

    if month is not None and year is not None:
        expenses_sum = expenses_sum.filter(Expense.date.like(f"{year}-{month:02d}-%"))
    expenses_sum = expenses_sum.first()
    console = Console()
    console.print(f"\n${round(expenses_sum[0],2)}", style = "bold")

def expense_by_month(month, year):
    session = Session()
    return session.query(Expense).filter(Expense.date.like(f"{year}-{month:02d}-%")).all()

def get_expenses_by_category_month(category_id, month = None, year = None):
    session = Session()
    data = session.query(Expense).filter(Expense.category_id == category_id)

    if month and year:
        data = data.date.like(f"{year}-{month:02d%}-%")
    return data.all()




