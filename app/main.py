from fastapi import FastAPI
from app.api.v1.users import router as user_router

app = FastAPI(title="Production FastAPI")

app.include_router(user_router, prefix="/api/v1")


@app.get("/health")
def health():
    return {"status": "ok"}
