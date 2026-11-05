from fastapi import FastAPI

from app.api.users import router as users_router
from app.api.webhooks import router as webhooks_router
from app.api.pull_requests import router as pull_requests_router

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
app.include_router(webhooks_router)
app.include_router(pull_requests_router)