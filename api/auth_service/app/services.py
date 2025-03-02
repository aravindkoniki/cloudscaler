from flask import jsonify
from app.models import db, User
from app.utils import generate_token

def register_user(data):
    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"message": "User already exists"}), 400

    user = User(username=data["username"], email=data["email"])
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

def authenticate_user(data):
    user = User.query.filter_by(username=data["username"]).first()
    if user and user.check_password(data["password"]):
        token = generate_token(user)
        return jsonify({"token": token})
    return jsonify({"message": "Invalid credentials"}), 401
