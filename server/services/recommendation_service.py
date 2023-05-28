from database import db_connector


def node_similarity():
    
    # Connect to the Neo4j database
    graph = db_connector.get_graph_db()

    # Your list of movie ids
    movie_ids = ['tt0267913', 'tt4154796']

    # The Cypher query to find the 5 movies with highest average similarity to those in your list
    query = f"""
    MATCH (m:Movie)-[r:SIMILAR]-(n:Movie)
    WHERE m.Id IN $ids AND NOT n.Id IN $ids
    RETURN n.Title AS movie_title, n.Id AS movie_id, n.Release_year AS ReleaseYear, n.Poster AS Poster, AVG(r.Score) AS average_similarity
    ORDER BY average_similarity DESC
    LIMIT 5
    """

    # Run the query
    result = graph.run(query, ids=movie_ids)

    movies = []
    for m in result:
        movie = {
            "title": m[0],
            "id": m[1],
            "release_year": m[2],
            "posters": m[3]
                }
        movies.append(movie)
    return movies
