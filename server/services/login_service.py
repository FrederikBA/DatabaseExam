from jose import JWTError, jwt
from datetime import datetime, timedelta

def get_user(username: str):
    pass

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user or user.password != password:
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, "SUPERSECRETKEY", algorithm="HS256")
    return encoded_jwt