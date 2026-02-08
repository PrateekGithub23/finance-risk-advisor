from fastapi import FastAPI

app = FastAPI(title="AI-Powered Personal Finance Risk Advisor")

@app.get("/")
def get_root():
    return {"message": "Finance Risk Advisor API is running 🚀"}