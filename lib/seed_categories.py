from models import engine, Category, Session
from functions import create_category, delete_all_records

#Delete all existing category records
delete_all_records(Category)

#Adds common categories
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
    "Miscellaneous",
    "Groceries",
    "Rent",
    "Insurance",
    "Subscriptions",
    "Investments"
]

for category in common_categories:
    create_category(category)





