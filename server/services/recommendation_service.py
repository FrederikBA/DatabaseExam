from database import db_connector
from py2neo import Graph


def node_similarity():
    
    # Connect to the Neo4j database
    graph = db_connector.get_graph_db()

    # Your list of movie ids
    movie_ids = ['tt4881806', 'tt2527336', 'tt3498820']

    # Convert list to format suitable for Cypher query
    formatted_ids = ', '.join(f"'{id}'" for id in movie_ids)

    # The Cypher query to find the 5 movies with highest average similarity to those in your list
    query = f"""
    MATCH (m:Movie)-[r:SIMILAR]-(n:Movie)
    WHERE m.Id IN [{formatted_ids}] AND NOT n.Id IN [{formatted_ids}]
    RETURN n.Id AS movie_id, AVG(r.Score) AS average_similarity
    ORDER BY average_similarity DESC
    LIMIT 5
    """

    # Run the query
    result = graph.run(query)

    # Print the movie ids
    for record in result:
        print(record["movie_id"])
