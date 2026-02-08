from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from app.db.session import Base

class Transaction(Base):
    __tablename__ = "transactions"

    # transaction id
    id = Column(Integer, primary_key=True, index=True)

    # reference to user, foreign key to users table
    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float)
    category = Column(String)
    description = Column(String)
    date = Column(Date)