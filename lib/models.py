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
        return f"{self.id}) Amount: {self.amount}, description: {self.description}, category id: {self.category_id}, Date: {self.date}"

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer(), primary_key = True)
    name = Column(String())
    expense = relationship("Expense", back_populates="category")

    def __repr__(self):
        return f"{self.name}"
        # return f"{self.id}) {self.name}"
    
Base.metadata.create_all(bind = engine)