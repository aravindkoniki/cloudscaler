from flask import Blueprint, request, jsonify
from app.models import db, User
from app.utils import generate_token
from app.services import register_user, authenticate_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    """Register a new user"""
    data = request.get_json()
    return register_user(data)

@auth_bp.route("/login", methods=["POST"])
def login():
    """User Login"""
    data = request.get_json()
    return authenticate_user(data)
