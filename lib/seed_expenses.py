from models import engine, Expense, Session
from functions import delete_all_records, create_expense
import random
from datetime import datetime, timedelta

#Delete all existing expense records
delete_all_records(Expense)

#Adds csample expenses
sample_expenses = [
    "Fresh Produce from Local Market",
    "Dinner at Italian Restaurant",
    "Movie Night with Friends",
    "Monthly Electricity Bill",
    "City Bus Fare",
    "Summer T-shirt",
    "Prescription Medication",
    "Weekend Getaway to the Beach",
    "Birthday Gift for a Friend",
    "Plumbing Repair for Leaky Faucet",
    "Online Language Course",
    "New Smartphone Charger",
    "Quarterly Gym Membership",
    "Car Insurance Premium",
    "Cat Food and Litter",
    "Monthly Apartment Rent",
    "Donation to Red Cross",
    "Oil Painting Supplies",
    "Streaming Music Subscription",
    "Haircut and Styling"
]

for description in sample_expenses:
    amount = round(random.uniform(1, 100),2) # random amount
    category_id = random.randint(1,20)

    start_date = datetime(2020, 1, 1)
    end_date = datetime(2022, 12, 31)
    random_num_days = random.randint(0, (end_date - start_date).days)
    date = start_date + timedelta(days=random_num_days)
    formatted_date = date.strftime("%Y-%m-%d")

    create_expense(amount, description,category_id, formatted_date)





