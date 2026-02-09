from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.transaction import Transaction
from app.core.dependencies import get_current_user, get_db
from app.models.user import User

router = APIRouter(prefix="/analytics", tags=["Analytics"])

@router.get("/summary")

def get_summary(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    income = db.query(func.sum(Transaction.amount).filter(Transaction.user_id == user.id, Transaction.amount > 0)).scalar() or 0

    expenses = db.query(func.sum(Transaction.amount)).filter(Transaction.user_id == user.id, Transaction.amount < 0).scalar() or 0

    net_cashflow = income + expenses

    return {
        
        "total_income": income,
        "total_expenses": abs(expenses),
        "net_cashflow": net_cashflow
    }

@router.get("/categories")
def category_breakdown(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    results = db.query(Transaction.category, func.sum(Transaction.amount)).filter(Transaction.user_id == user.id).group_by(Transaction.category).all()

    # formats the results into a list of dictionaries with category and amount keys
    return [
        {"category": r[0], "amount": r[1]}
        for r in results
    ]



