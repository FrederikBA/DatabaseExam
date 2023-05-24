from database import db_connector
from models import dtos
from datetime import datetime, timedelta
import os
import uuid

sql_value = os.getenv("SQL_VALUE")

def create_order(order_dto: dtos.orderDTO):
    connection = db_connector.get_sql_db('BockBluster')
    cursor = connection.cursor()

    order_id = str(uuid.uuid4())

    query = f'''    
    BEGIN TRY
        BEGIN TRANSACTION;

        DECLARE @order_id VARCHAR(255);
        DECLARE @loan_id VARCHAR(255);

        INSERT INTO orders (order_id, member_id, total_price)
        VALUES ('{order_id}', '{order_dto.member_id}', {order_dto.total_price});

        SELECT @order_id = '{order_id}';

        '''
    
    for movie in order_dto.movies:
        loan_date = datetime.now()
        return_date = loan_date + timedelta(days=7)
        query += f'''
        INSERT INTO loan (loan_id, order_id, movie_id, loan_date, return_date)
        VALUES ('{str(uuid.uuid4())}', @order_id, '{movie.movie_id}', '{loan_date}', '{return_date}');
        '''
    
    query += '''
        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        ROLLBACK TRANSACTION;
    END CATCH;
    '''
    
    cursor.execute(query)
    connection.commit()

    # Close the cursor and connection
    cursor.close()
    connection.close()
    return "Done"




