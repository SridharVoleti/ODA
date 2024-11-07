from flask import Flask,jsonify
from flask_pymongo  import PyMongo
from flask_jwt_extended import JWTManager

from app.config import DevelopmentConfig,TestingConfig

mongo = PyMongo()

def create_app(config_name):
    app = Flask(__name__)

    if config_name == "development":
        app.config.from_object(DevelopmentConfig)
    elif config_name == "testing":
        app.config.from_object(TestingConfig)
    
    app.config["JWT_SECRET_KEY"] = "7cd250f4c920ad972f9392e9d6ef07971198a8decedf607eb76455e56117c556"
    jwt = JWTManager(app)
   
    # @jwt.token_in_blocklist_loader
    # def check_if_token_in_blocklist(jwt_header, jwt_payload):
    #     return jwt_payload["jti"] in BLOCKLIST

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "The token has been revoked.", "error": "token_revoked"}
            ),
            401,
        )
    
    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {
                    "description": "The token is not fresh.",
                    "error": "fresh_token_required",
                }
            ),
            401,
        )

    @jwt.additional_claims_loader
    def add_claims_to_jwt(identity):
        user = mongo.db.Users.find_one({"_id":identity})
        if user:
            return {"role": user["role"]}

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )
    
    mongo.init_app(app)
    from app.Resourses.user_endpoints import user_bp
    app.register_blueprint(user_bp)

    return app