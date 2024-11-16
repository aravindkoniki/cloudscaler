from flask import Flask
from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy
from app.config.settings import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Swagger(app)  # Enable Swagger

    # Register Blueprints
    from app.api.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")

    with app.app_context():
        db.create_all()  # Initialize database
    return app
