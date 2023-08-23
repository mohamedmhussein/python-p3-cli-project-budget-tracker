from sqlalchemy.orm import sessionmaker
from models import engine, Category
from functions import create_category

Session = sessionmaker(bind=engine)

common_categories = [
    "Housing",
    "Transportation",
    "Food",
    "Entertainment",
    "Healthcare",
    "Debt Payments",
    "Savings",
    "Utilities",
    "Personal Care",
    "Clothing",
    "Gifts and Donations",
    "Education",
    "Travel",
    "Childcare",
    "Miscellaneous"
]

for category in common_categories:
    create_category(category)





