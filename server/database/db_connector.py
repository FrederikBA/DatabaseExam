# Imports
import os
from dotenv import load_dotenv

# MSSQL
import pymssql
import pyodbc

# Neo4j
from py2neo import Graph

# Load environment variables
load_dotenv()


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
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' +
                          server+';DATABASE='+db+';UID='+user+';PWD=' + password)
    return conn


def get_sql_db(db):
    if(os.getenv("OPERATING_SYSTEM") == "windows"):
        return get_sql_windows(db)

    if(os.getenv("OPERATING_SYSTEM") == "mac"):
        return get_sql_mac(db)

def get_graph_db():
    port = os.getenv("NEO4J_PORT")
    password = os.getenv("NEO4J_PASSWORD")
    graph = Graph(f"bolt://localhost:{port}", auth=("neo4j", password))
    return graph