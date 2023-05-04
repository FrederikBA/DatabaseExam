#Imports
import os
from dotenv import load_dotenv

#MongoDB
from pymongo.mongo_client import MongoClient

#MSSQL
import pymssql
import pyodbc

# Load environment variables
load_dotenv() 

def get_mongo_db(os):
   url = 'mongodb://localhost:27017/'
   client = MongoClient(url)

   return client['school']

def get_sql_mac(db):
   server = os.getenv("SQL_SERVER")
   user = os.getenv("SQL_USERNAME")
   password = os.getenv("SQL_PASSWORD")
   conn = pymssql.connect(server, user, password, db)
   return conn

def get_sql_windows(db):
   server = os.getenv("SQL_SERVER")
   user = os.getenv("SQL_USERNAME")
   password = os.getenv("SQL_PASSWORD")
   conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER='+server+';DATABASE='+db+';ENCRYPT=yes;UID='+user+';PWD='+ password)
   return conn

def get_sql_db(db):
   if(os.getenv("OS") == "mac"):
      return get_sql_mac(db)
   
   if(os.getenv("OS") == "windows"):
      return get_sql_windows(db)