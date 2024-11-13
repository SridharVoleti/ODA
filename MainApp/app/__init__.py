from flask import Flask,session
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
    from .routes.user_management import um_bp
    from .routes.errors import errors_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(errors_bp)
    app.register_blueprint(um_bp)

    @login_manager.user_loader
    def load_user(user_id):
        from app.models.user import User
        user = session.get('user',None)
        return User(**user) if user else None
    return app
