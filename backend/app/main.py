from fastapi import FastAPI
from app.api.user import router as user_router

app = FastAPI(
    title="BotForge API",
    version="0.1.0"
)

app.include_router(user_router)

@app.get("/")
def root():
    return {"message": "Welcome to BotForge API , credit by BARI"}

