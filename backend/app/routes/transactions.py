from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date

from app.models.transaction import Transaction
from app.core.dependencies import get_current_user, get_db
from app.models.user import User

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.post("/")
def add_transaction(amount:float,category:str,description:str,tx_date: date,db: Session = Depends(get_db),user: User = Depends(get_current_user)):
    tx = Transaction(user_id=user.id, amount=amount, category=category, description=description, date=tx_date)
    
    db.add(tx)
    db.commit()
    db.refresh(tx)
    return tx

@router.get("/")
def get_transactions(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    # queries the database for transactions that belong to the current user and returns them as a list
    return db.query(Transaction).filter(
        Transaction.user_id == user.id
    ).all()
    