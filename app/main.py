from fastapi import FastAPI

app = FastAPI(title="AgriPest - Tomato & Brinjal Advisor")

@app.get("/")
def root():
    return {
        "message": "✅ Agri Pest App is running! (Day 1 Complete)",
        "status": "Setup successful",
        "note": "We are building step by step"
    }
