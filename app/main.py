from fastapi import FastAPI
from app.core.config import settings
from app.api.disease import router as disease_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="AI Powered Pest Control App for Tomato & Brinjal"
)

# Include routers
app.include_router(disease_router)

@app.get("/")
def root():
    return {
        "message": "✅ AgriPest App is running!",
        "day": "Day 3 - API Structure Added",
        "version": settings.VERSION
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
