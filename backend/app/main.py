from fastapi import FastAPI

from app.db.session import Base, engine
from app.models.user import User 

app = FastAPI(title="AI-Powered Personal Finance Risk Advisor")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"status": "Backend + DB connected 🚀"}
