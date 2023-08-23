from models import engine, Category, Session
from functions import create_category

#Delete all existing category records
session = Session()
session.query(Category).delete()
session.commit()

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





