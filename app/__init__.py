from flask import Flask
from flask_pymongo import PyMongo
from flask_login import LoginManager
from config import Config

# Initialize extensions
mongo = PyMongo()  # Initialize here, but don't bind to app yet
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Bind extensions to the app
    mongo.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # Import blueprints after initializing extensions
    from .routes.auth import auth_bp
    from .routes.main import main_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    # Define the user_loader function to load a user from the user_id
    @login_manager.user_loader
    def load_user(user_id):
        from app.models.user import User  # Import here to avoid circular import issues
        return User.find_by_username(user_id)  # Assuming user_id corresponds to username

    return app
