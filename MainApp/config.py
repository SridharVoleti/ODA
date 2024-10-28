import os
class Config:
    SECRET_KEY = 'your_secret_key'
    MONGO_URI = os.getenv("MONGO_AUTH_URI")
