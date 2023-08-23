from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import Column, String, Integer, Float, DateTime, create_engine, ForeignKey

Base = declarative_base()
engine = create_engine("sqlite:///budget_tracker.db")

Session = sessionmaker(bind=engine)

class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer(), primary_key = True)
    amount = Column(Float(), nullable = False)
    description = Column(String())
    category_id = Column(Integer(), ForeignKey('categories.id'))
    date = Column(String())
    category = relationship("Category", back_populates="expense")
    
    # def __init__(self, amount, description,ca)
    def __repr__(self):
        return f"Amount: {amount}, description: {description}, category id: {category_id}"

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer(), primary_key = True)
    name = Column(String())
    expense = relationship("Expense", back_populates="category")
    
Base.metadata.create_all(bind = engine)