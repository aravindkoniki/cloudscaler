from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
from app.config.settings import Config

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: int = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (timedelta(minutes=expires_delta or Config.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, Config.SECRET_KEY, algorithm=Config.JWT_ALGORITHM)

def decode_access_token(token: str):
    try:
        return jwt.decode(token, Config.SECRET_KEY, algorithms=[Config.JWT_ALGORITHM])
    except jwt.PyJWTError:
        return None
