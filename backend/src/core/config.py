from dotenv import load_dotenv
import os

# Load the .env from the project root
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../../.env"))

class Settings:
    PROJECT_NAME: str = "RepAI Backend"
    DATABASE_URL: str = os.getenv("DATABASE_URL")

settings = Settings()
