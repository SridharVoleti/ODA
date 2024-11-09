from flask import Flask
from flask_pymongo import PyMongo

from app.config import DevelopmentConfig, TestingConfig

mongo = PyMongo()

def create_app(config_name):
    app = Flask(__name__)
    # Register Blueprints
    from app.shipment_endpoints import shipment_bp
    app.register_blueprint(shipment_bp)

    if config_name == 'development':
        app.config.from_object(DevelopmentConfig)
    elif config_name == 'testing':
        app.config.from_object(TestingConfig)
    else:
        raise ValueError("Invalid configuration name")
    
    mongo.init_app(app)
    
    return app

def register_error_handlers(app):
    from pymongo.errors import DuplicateKeyError
    from flask import jsonify

    @app.errorhandler(404)
    def handle_404_error(e):
        return jsonify(error=str(e)), 404

    @app.errorhandler(DuplicateKeyError)
    def handle_duplicate_key_error(e):
        return jsonify(error="Duplicate key error."), 400