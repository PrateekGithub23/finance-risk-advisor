from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from datetime import datetime
from app.db.session import Base

class RiskScore(Base):
    __tablename__ = "risk_scores"

    # every risk score is assiciated with a user, has a score value, a risk level, an explanation, and a timestamp for when it was created
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    score = Column(Float)
    level = Column(String)
    explanation = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
