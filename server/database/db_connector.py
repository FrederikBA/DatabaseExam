#Imports

#MongoDB
from pymongo.mongo_client import MongoClient

#MSSQL
import pymssql
import pyodbc

def get_mongo_db():
   url = 'mongodb://localhost:27017/'

   # Create a new client and connect to the server
   client = MongoClient(url)

   return client['school']


def get_sql_db(): 

   server = r'localhost'
   user = "sa"
   password = "thisIsSuperStrong1234"
   conn = pymssql.connect(server, user, password, "Library")
   c1 = conn.cursor()
   c1.execute('SELECT * FROM Book')
   data = c1.fetchall()
   print(data)
   conn.close()
   return data

def windows_mssql_con():
   conn = pyodbc.connect('DRIVER={SQL Server};SERVER=ROOT\SQLEXPRESS;DATABASE=Libary;UID=sa;PWD=thisIsSuperStrong1234')
   fruits = ['banna', 'apple', 'coke']
   c1 = conn.cursor()
   c1.execute('SELECT * FROM Book')
   data = c1.fetchall()
   print(type(data))
   conn.close()
   return fruits