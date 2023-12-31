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
        console.print("\nCategory does not exist :x: :x:, please try again\n", style = "bold underline bright_red")
    else:
        new_expense = Expense(amount = amount, category_id = category_id, description = description, date = date)
        session.add(new_expense)
        session.commit()
    console.print(f"\n The new Expense has been added :white_heavy_check_mark: :white_heavy_check_mark:\n", style = "bold bright_green")

def create_category(name):
    console = Console()
    session = Session()
    new_category = Category(name = name)
    session.add(new_category)
    session.commit()
    console.print(f"\n Category {name} has been added :white_heavy_check_mark: :white_heavy_check_mark:\n", style = "bold bright_green")

def delete_all_records(model_cls):
    session = Session()
    session.query(model_cls).delete()
    session.commit()

def delete_record(model_cls, id):
    session = Session()
    record = session.query(model_cls).filter(model_cls.id == id).first()
    session.delete(record)
    session.commit()

def display_data(model_cls, all_data):
    print("\n")

    console = Console()
    colors = ["cyan", "magenta", "bright_yellow", "white", "bright_green", "bright_yellow", "bright_magenta", "green3"]
    table_title = Text(f"{model_cls.__name__}s Data")
    table_title.stylize("bold bright_yellow")
    console.print(table_title)
    table = Table(show_header=True, header_style="bold")
    for column in model_cls.__table__.columns:
        table.add_column(column.name, style=f"{random.choice(colors)} bold", header_style="bold")

    # Add an additional column for 'category'
    if model_cls != Category:
        table.add_column("Category", style=f"{random.choice(colors)} bold", header_style="bold")

    for data in all_data:
        # Retrieve category name using the relationship attribute 'category'
        if model_cls != Category:
            category_name = data.category.name if hasattr(data, 'category') else ""

        row_values = [str(getattr(data, column.name)) for column in model_cls.__table__.columns]
        if model_cls != Category:
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

def update_record(model_cls, id, new_data):
    session = Session()
    query = session.query(model_cls).filter(model_cls.id == id)

    new_dict = {
        getattr(model_cls, column): value
        for column, value in new_data.items()
        if value != ""  # Do not update empty values
    }
    if new_dict:
        query.update(new_dict)
    session.commit()
def delete_all(delete_expenses = True, delete_categories = True):
    console = Console()
    session = Session()
    if delete_expenses:
            session.query(Expense).delete()
            session.commit()
    if delete_categories:
            session.query(Category).delete()
            session.commit()
    console.print("Records have been deleted", style = "bold bright_green")




