from app.models.user import User
from app.utils.security import hash_password, verify_password
from app import db

def create_user(username: str, email: str, password: str):
    hashed_password = hash_password(password)
    user = User(username=username, email=email, hashed_password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return user

def authenticate_user(username: str, password: str):
    user = User.query.filter_by(username=username).first()
    if user and verify_password(password, user.hashed_password):
        return user
    return None
