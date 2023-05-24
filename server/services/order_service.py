from database import db_connector
from models import dtos
from datetime import datetime, timedelta
import os
import uuid

sql_value = os.getenv("SQL_VALUE")

def create_order(order_dto: dtos.orderDTO):
    connection = db_connector.get_sql_db('BockBluster')
    cursor = connection.cursor()
    try:
        cursor.execute("BEGIN TRANSACTION")

        # Insert into the orders table
        order_id = str(uuid.uuid4())
        member_id = order_dto.member_id
        total_price = order_dto.total_price
        cursor.execute(f"INSERT INTO orders (order_id, member_id, total_price) VALUES ({sql_value}, {sql_value}, {sql_value})",
                       (order_id, member_id, total_price))

        movie_ids = ['tt0029583', 'tt0031381']
        # Insert into the loan table for each movie
        # for movie_id in movie_ids:
        #     loan_id = str(uuid.uuid4())
        #     loan_date = datetime.now()
        #     return_date = loan_date + timedelta(days=7)
        #     cursor.execute(f"INSERT INTO loan (loan_id, order_id, movie_id, loan_date, return_date) VALUES ({sql_value}, {sql_value}, {sql_value}, {sql_value}, {sql_value})",
        #                     (loan_id, order_id, movie_id, loan_date, return_date))

        if cursor.rowcount >= 1:
            cursor.execute("COMMIT")
        else:
            cursor.execute("ROLLBACK")

    except Exception as e:
        cursor.execute("ROLLBACK")

    finally:
        cursor.close()
        connection.close()
    return "Done"
