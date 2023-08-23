from models import engine, Expense, Session
from functions import delete_all_records
from faker import faker

faker = Faker()

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

# for category in common_categories:
#     create_category(category)





