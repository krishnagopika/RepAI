import os
from dotenv import load_dotenv

# Load the .env file from project root
dotenv_path = os.path.join(os.path.dirname(__file__), "../../.env")
load_dotenv(dotenv_path=dotenv_path)

class Settings:
    PROJECT_NAME: str = "RepAI Backend"
    DATABASE_URL: str = os.getenv("DATABASE_URL")

settings = Settings()

# Debug check
if not settings.DATABASE_URL:
    print("⚠️ DATABASE_URL not found! Check .env path or variable name.")
