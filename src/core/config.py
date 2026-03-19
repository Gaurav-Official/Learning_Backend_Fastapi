import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME", "My_Db")
DATABASE_URL = os.getenv("DATABASE_URL")
APP_NAME = "VideoTube"

raw_origins = os.getenv("CORS_ORIGINS", "*")

if raw_origins == "*":
    CORS_ORIGINS = ["*"]
else:
    CORS_ORIGINS = [origin.strip() for origin in raw_origins.split(",")]
