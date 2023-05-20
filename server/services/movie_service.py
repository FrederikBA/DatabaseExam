from database import db_connector
from models import entities

def get_movie_catalog():
    conn = db_connector.get_sql_db("BockBluster")

    c1 = conn.cursor()
    c1.execute('SELECT m.movie_id, m.price_id, m.title, m.release_year, m.rating, m.poster, p.price FROM movie m JOIN price p ON m.price_id = p.price_id')
    data = c1.fetchall()

    movies = []

    for m in data:
        movie = {"movie_id": m[0],
            "price_id": m[1],
            "title": m[2],
            "release_year": m[3],
            "rating": m[4],
            "poster": m[5],
            "price": m[6]}
        movies.append(movie)

    # Close connection
    conn.close()

    return movies


# Define a model for movie details






# def fetch_movie_data(movie_id):
#         conn = db_connector.get_graph_db("BockBluster")

#         # Create a session from the connection
#         session = conn.session()

#         # Execute the Cypher query
#         cypher_query = """
#             MATCH (m:Movie {id: $movieId})
#             RETURN m.title AS title, m.release_year AS releaseYear, m.rating AS rating
#             """
#         result = session.run(cypher_query, movieId=movie_id)
#         movie_data = result.single()

#         if movie_data:
#             return entities.Movie(
#                 title=movie_data["title"],
#                 release_year=movie_data["releaseYear"],
#                 rating=movie_data["rating"]
#             )

#         return None

def fetch_movie_data(movie_id):
    conn = db_connector.get_graph_db()

    # Execute the Cypher query
    cypher_query = """
        MATCH (m:Movie {Id: $movieId})
        RETURN m.Title AS Title, m.Id AS movieId
    """

    result = conn.run(cypher_query, movieId=movie_id)

    # Iterate over the cursor and retrieve the movie data
    for record in result:
        return entities.Movie(
            title=record["Title"],
            movieId=record["movieId"]
        )

    return None

