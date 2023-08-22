from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, String, Integer, Float, DateTime, create_engine, ForeignKey
from datetime import datetime

Base = declarative_base()
engine = create_engine("sqlite:///budget_tracker.db")

class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer(), primary_key = True)
    amount = Column(Float(), nullable = False)
    description = Column(String())
    category_id = Column(Integer(), ForeignKey('categories.id'))
    time = Column(DateTime, default = datetime.now())
    category = relationship("Category", back_populates="expense")
    
    def __repr__(self):
        return f"Amount: {amount}, description: {description}, category id: {category_id}"

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer(), primary_key = True)
    name = Column(String())
    expense = relationship("Expense", back_populates="category")
    
Base.metadata.create_all(bind = engine)