from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.transaction import Transaction
from app.models.risk_score import RiskScore
from app.core.dependencies import get_current_user, get_db
from app.core.risk_engine import calculate_risk
from app.models.user import User

router = APIRouter(prefix="/risk", tags=["Risk"])

@router.post("/compute")
def compute_risk(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    
    income = db.query(func.sum(Transaction.amount)).filter(Transaction.user_id == user.id, Transaction.amount > 0).scalar() or 0
    expenses = abs(db.query(func.sum(Transaction.amount)).filter(Transaction.user_id == user.id, Transaction.amount < 0).scalar() or 0)

    score, level, explanation = calculate_risk(income, expenses)

    # create the risk model
    risk = RiskScore(
        user_id=user.id,
        score=score,
        level=level,
        explanation=explanation
    )

    db.add(risk)
    db.commit()
    db.refresh(risk)

    return {
        "risk_score": score,
        "risk_level": level,
        "explanation": explanation
    }

@router.get("/latest")
def latest_risk(db: Session = Depends(get_db),user: User = Depends(get_current_user)):

    # queries the database for risk score table for most recent risk score for the current user and returns it. If no risk score is found, it returns None
    risk = db.query(RiskScore).filter(
        RiskScore.user_id == user.id
    ).order_by(RiskScore.created_at.desc()).first()

    return risk