# app/__init__.py
import pytest
from flask import Flask
from flask_pymongo import PyMongo
from flask_wtf import CSRFProtect
from dotenv import load_dotenv # imported environmental variables from .env file : Added by yogesh kumar
# Load environmental vairables
load_dotenv()
import os
# Initialize Flask application
app = Flask(__name__)

# Configure MongoDB URI
app.config['MONGO_URI'] = os.getenv("DB_CONNECTION") #dotenv_values("db_connection_string") # Added the connection string to environmental variables : changed by yogesh kumar 
# Secret key for CSRF protection
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['ENV'] = 'development'

# Initialize MongoDB and CSRF protection
mongo = PyMongo(app)
csrf = CSRFProtect(app)

# Import routes to register them with the app
from app import routes

def run_tests():
    """Function to run PyTest when the app starts."""
    # Run pytest with specified options
    pytest_args = ["--disable-warnings", "tests/"]
    return pytest.main(pytest_args)

# Only run tests when running in development mode
if app.config['ENV'] == 'development':
    result = run_tests()
    if result != 0:
        print("Tests failed!")
        # Optional: You can choose to raise an error or exit the application here
        # sys.exit(1)
    else:
        print("All tests passed successfully!")