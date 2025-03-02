import os
import json
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwtsecret")
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Load Swagger JSON Configuration
    SWAGGER_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "swagger_config.json")
    with open(SWAGGER_CONFIG_PATH, "r") as f:
        SWAGGER_CONFIG = json.load(f)

config = Config()
