from database import db_connector


def recommend_movies(movie_ids):
    graph = db_connector.get_graph_db()


    query = f"""
    MATCH (m:Movie)-[r:SIMILAR]-(n:Movie)
    WHERE m.Id IN $ids AND NOT n.Id IN $ids
    RETURN n.Title AS movie_title, n.Id AS movie_id, n.Release_year AS ReleaseYear, n.Poster AS Poster, n.Price AS Price, n.Rating AS Rating, AVG(r.Score) AS average_similarity
    ORDER BY average_similarity DESC
    LIMIT 5
    """

    result = graph.run(query, ids=movie_ids)

    movies = []
    for m in result:
        movie = {
            "title": m[0],
            "id": m[1],
            "release_year": m[2],
            "poster": m[3],
            "price": m[4],
            "rating": m[5]
                }
        movies.append(movie)
    return movies
