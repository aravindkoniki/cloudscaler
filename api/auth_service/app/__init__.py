from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flasgger import Swagger
from app.config import config

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        from app.routes import auth_bp
        app.register_blueprint(auth_bp, url_prefix="/auth")

    # Initialize Swagger from JSON
    Swagger(app, template=config.SWAGGER_CONFIG)

    return app
