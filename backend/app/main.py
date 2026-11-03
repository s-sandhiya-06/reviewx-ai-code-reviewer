from fastapi import FastAPI

app = FastAPI(
    title="ReviewX API",
    description="AI-powered GitHub Code Review Platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to ReviewX"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }