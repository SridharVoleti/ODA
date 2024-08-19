# app/__init__.py

from flask import Flask
from flask_pymongo import PyMongo
from flask_wtf import CSRFProtect

# Initialize Flask application
app = Flask(__name__)

# Configure MongoDB URI
app.config['MONGO_URI'] = 'mongodb://localhost:27017/freight_forwarder_db'
# Secret key for CSRF protection
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize MongoDB and CSRF protection
mongo = PyMongo(app)
csrf = CSRFProtect(app)

# Import routes to register them with the app
from app import routes
