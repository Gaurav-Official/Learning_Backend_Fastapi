from fastapi import FastAPI  
from src.routes.health import router as health_router

app = FastAPI(title="Learning the backend fastapi")

app.include_router(health_router)