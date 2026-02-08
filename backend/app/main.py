from fastapi import FastAPI
from app.db.session import Base, engine
from app.models.user import User
from app.routes.auth import router as auth_router

app = FastAPI(title="AI-Powered Personal Finance Risk Advisor")

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)

@app.get("/")
def root():
    return {"status": "Auth system running 🔐"}