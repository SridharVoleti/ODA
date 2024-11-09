import os
import dotenv

dotenv.load_dotenv()

class Config:
    """Base configuration."""
    SECRET_KEY = 'your_secret_key'
    MONGO_URI = os.getenv("MONGO_DEV_URI")  # Default database

class DevelopmentConfig(Config):
    """Development configuration."""
    MONGO_URI = os.getenv("MONGO_DEV_URI")

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    MONGO_URI = os.getenv("MONGO_TEST_URI")  # Use a different database for testing