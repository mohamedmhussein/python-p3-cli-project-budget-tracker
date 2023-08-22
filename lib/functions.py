from sqlalchemy.orm import sessionmaker
from models import engine
from models import Expense

Session = sessionmaker(bind=engine)

def create_expense():
    