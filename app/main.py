
from fastapi import FastAPI

app = FastAPI(
    title="SecureCloud API",
    description="DevSecOps Security Platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Welcome to SecureCloud API"}

@app.get("/health")
def health():
    return {"status": "healthy"}
