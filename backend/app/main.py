from fastapi import FastAPI

from app.api.users import router as users_router

app = FastAPI(
    title="ReviewX API",
    description="AI-powered GitHub Pull Request Code Review Platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to ReviewX",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


app.include_router(users_router)