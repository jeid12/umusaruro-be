import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL")

# Create an instance of the Settings class to access the configuration
settings = Settings()
