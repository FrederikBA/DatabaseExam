from jose import jwt
from database import db_connector
import os
from datetime import datetime, timedelta

sql_value = os.getenv("SQL_VALUE")

def get_user(username: str):
    connection = db_connector.get_sql_db('BockBluster')
    cursor = connection.cursor()

    # Fetch user based on username
    cursor.execute(f"SELECT * FROM user_login WHERE username = {sql_value}", (username,))
    user = cursor.fetchone()
    
    # Check if user exists
    if user:
        # Extract the user ID
        user_id = user[0]
        
        # Fetch member ID based on user ID
        cursor.execute(f"SELECT member_id FROM user_login WHERE user_id = {sql_value}", (user_id,))
        member_id = cursor.fetchone()[0]
        
        # Close the database connection
        connection.close()

        user_dict = {
            "id": user_id,
            "username": user[2],
            "password": user[3],
            "member_id": member_id
        }
        return user_dict
    else:
        # Close the database connection
        connection.close()
        
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

def get_member_id(user_id):
    connection = db_connector.get_sql_db('BockBluster')
    cursor = connection.cursor()
    
    query = f"SELECT m.member_id FROM member m JOIN user_login ul ON m.member_id = ul.member_id WHERE ul.user_id = {sql_value};"
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    if result:
        member_id = result[0]
        return member_id
    else:
        return "User ID not found"
