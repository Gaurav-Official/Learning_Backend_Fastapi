import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME", "My_Db")
DATABASE_URL = os.getenv("DATABASE_URL")
APP_NAME = "VideoTube"
