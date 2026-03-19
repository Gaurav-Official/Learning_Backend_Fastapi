from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.dependencies import get_db

router = APIRouter()


@router.get("/")
async def home(db: AsyncSession = Depends(get_db)):
    try:
        return {"message": "Db Connected & API is running "}
    except Exception as e:
        return {"error": str(e)}
