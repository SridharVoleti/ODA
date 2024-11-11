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
    JWT_SECRET_KEY = "7cd250f4c920ad972f9392e9d6ef07971198a8decedf607eb76455e56117c556"
    # Example configuration for Flask-Mail
    MAIL_SERVER = 'smtp.gmail.com'  # SMTP server address
    MAIL_PORT = 587  # Port number for the SMTP server
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")  # SMTP login username
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")  # SMTP login password
    MAIL_DEFAULT_SENDER = "yogeshkumarnandi@gmail.com"
    MAIL_USE_TLS = True  # Enable TLS for security
    MAIL_USE_SSL = False  # Disable SSL since we're using TLS


class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    MONGO_URI = os.getenv("MONGO_TEST_URI")  # Use a different database for testing
    JWT_SECRET_KEY = "7cd250f4c920ad972f9392e9d6ef07971198a8decedf607eb76455e56117c556"
    MAIL_SERVER = 'smtp.google.com'  # SMTP server address
    MAIL_PORT = 587  # Port number for the SMTP server
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")  # SMTP login username
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")  # SMTP login password # ebpc ljcn edcq rzgp
    MAIL_USE_TLS = True  # Enable TLS for security
    MAIL_USE_SSL = False  # Disable SSL since we're using TLS