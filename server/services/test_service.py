import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from database import db_connector

def get_data():
    #Create connection with chosen database, "Library"
    conn = db_connector.get_sql_db("Library")

    c1 = conn.cursor()
    c1.execute('SELECT * FROM Book')
    data = c1.fetchall()

    #Close connection
    conn.close()

    return data