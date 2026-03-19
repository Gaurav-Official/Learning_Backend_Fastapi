from fastapi import FastAPI
from src.db.session import engine
from src.db.base import Base
from src.routers import test


app = FastAPI()


app.include_router(test.router)


@app.on_event("startup")
async def startup():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        print("✅ Database connected successfully")
    except Exception as e:
        print("❌ Database connection Failed", e)


@app.get("/")
def home():
    return {"message": "API is Running"}
