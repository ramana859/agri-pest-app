from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="AI Powered Pest Control App for Tomato & Brinjal"
)

@app.get("/")
def root():
    return {
        "message": "✅ AgriPest App is running!",
        "day": "Day 2 - Project Structure Complete",
        "version": settings.VERSION
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
