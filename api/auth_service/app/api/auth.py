from flask import Blueprint, request, jsonify
from app.services.user_service import create_user, authenticate_user
from app.utils.security import create_access_token
from flasgger.utils import swag_from

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
@swag_from({
    "responses": {
        201: {"description": "User registered successfully"},
        400: {"description": "Validation error"}
    }
})
def register():
    data = request.json
    if not all(k in data for k in ("username", "email", "password")):
        return jsonify({"error": "Missing required fields"}), 400
    user = create_user(data["username"], data["email"], data["password"])
    return jsonify({"id": user.id, "username": user.username, "email": user.email}), 201

@auth_bp.route("/login", methods=["POST"])
@swag_from({
    "responses": {
        200: {"description": "Authentication successful"},
        401: {"description": "Invalid credentials"}
    }
})
def login():
    data = request.json
    user = authenticate_user(data["username"], data["password"])
    if not user:
        return jsonify({"error": "Invalid credentials"}), 401
    token = create_access_token({"sub": user.username})
    return jsonify({"access_token": token, "token_type": "bearer"}), 200
