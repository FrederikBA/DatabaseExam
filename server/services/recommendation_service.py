from database import db_connector

def node_similarity():
    conn = db_connector.get_graph_db()