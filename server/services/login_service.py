from jose import JWTError, jwt
from database import db_connector
import os
import sys
import inspect
from datetime import datetime, timedelta

sql_value = os.getenv("SQL_VALUE")

currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

def get_user(username: str):
    connection = db_connector.get_sql_db('BockBluster')
    cursor = connection.cursor()

    # Fetch user based on username
    cursor.execute(f"SELECT * FROM user_login WHERE username = {sql_value}", username)
    user = cursor.fetchone()
    # Close the database connection
    connection.close()

    # Check if user exists
    if user:
        user_dict = {
            "username": user[2],
            "password": user[3]
        }
        return user_dict
    else:
        return None

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user or user['password'] != password:
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, "SUPERSECRETKEY", algorithm="HS256")
    return encoded_jwt