from fastapi import FastAPI
from src.db.session import engine
from src.db.base import Base
from src.routers import test
from fastapi.middleware.cors import CORSMiddleware
from src.core.config import CORS_ORIGINS
from fastapi.staticfiles import StaticFiles

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(test.router)


@app.on_event("startup")
async def startup():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        print("✅ Database connected successfully")
    except Exception as e:
        print("❌ Database connection Failed", e)

#* Static Files will be stored here 
app.mount("/Public",StaticFiles(directory="Public"), name="Public")
# @app.get("/")
# def home():
#     return {"message": "API is Running"}
