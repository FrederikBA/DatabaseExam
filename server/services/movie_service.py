from database import db_connector
from models import entities
import os

sql_value = os.getenv("SQL_VALUE")

def get_movie_catalog():
    conn = db_connector.get_graph_db()

    cypher_query = """
    MATCH (m:Movie)
    OPTIONAL MATCH (m)<-[r:`STARRED_IN`]-(actor:Actor)
    OPTIONAL MATCH (m)<-[:INSTRUCTED]-(director:Director)
    OPTIONAL MATCH (m)-[:HAS]->(genre:Genre)
    OPTIONAL MATCH (m)<-[:PUBLISHED]-(publisher:Publisher)
    RETURN m.Title AS Title, m.Id AS movieId, m.Rating AS Rating, m.Summary AS Summary,
    m.Release_year AS ReleaseYear, m.Runtime AS Runtime, m.Certificate AS Certificate, m.Poster AS Poster, m.Price AS Price,
    COLLECT(DISTINCT actor.Name) AS Actors, COLLECT(DISTINCT director.Name) AS Directors,
    COLLECT(DISTINCT genre.Genre) AS Genres, COLLECT(DISTINCT publisher.Name) AS Publishers
    """

    data = conn.run(cypher_query)

    movies = []

    for m in data:
        movie = {"title": m[0],
            "movie_id": m[1],
            "rating": m[2],
            "release_year": m[4],
            "runtime": m[5],
            "price": m[8],
            "poster": m[7],
            "genre": m[11]}
        movies.append(movie)


    return movies


#Function to retrieve data for a movie details webpage.
def get_movie_details(movie_id):
    conn = db_connector.get_graph_db()
    cypher_query = """
    MATCH (m:Movie {Id: $movieId})
    OPTIONAL MATCH (m)<-[r:`STARRED_IN`]-(actor:Actor)
    OPTIONAL MATCH (m)<-[:INSTRUCTED]-(director:Director)
    OPTIONAL MATCH (m)-[:HAS]->(genre:Genre)
    OPTIONAL MATCH (m)<-[:PUBLISHED]-(publisher:Publisher)
    OPTIONAL MATCH (m)<-[:FOR]-(review:Review)
    RETURN m.Title AS Title, m.Id AS movieId, m.Rating AS Rating, m.Summary AS Summary,
    m.Release_year AS ReleaseYear, m.Runtime AS Runtime, m.Certificate AS Certificate, m.Poster AS Poster,
    COLLECT(DISTINCT actor.Name) AS Actors, COLLECT(DISTINCT director.Name) AS Directors,
    COLLECT(DISTINCT genre.Genre) AS Genres, COLLECT(DISTINCT publisher.Name) AS Publishers,
    COLLECT(DISTINCT review.Content) AS Reviews
"""

    result = conn.run(cypher_query, movieId=movie_id)

    # Iterate over the cursor and retrieve the movie data
    for record in result:
        return entities.Movie(
            movieId=record["movieId"],
            poster=record["Poster"],
            title=record["Title"],
            rating=record["Rating"],
            summary=record["Summary"],
            actors=record["Actors"],
            directors=record["Directors"],
            genres=record["Genres"],
            publishers=record["Publishers"],
            release_year=record["ReleaseYear"],
            certificate=record["Certificate"],
            runtime=record["Runtime"],
            review=record["Reviews"],
        )

    return None


def search_filter(title: str):
    conn = db_connector.get_sql_db("BockBluster")

    c1 = conn.cursor()
    c1.execute(f"SELECT m.movie_id, m.price_id, m.title, m.release_year, m.rating, m.poster, p.price FROM movie m JOIN price p ON m.price_id = p.price_id WHERE title LIKE {sql_value}", f"%{title}%")
    data = c1.fetchall()

    # Fetch all movie titles
    movies = []
    for m in data:
        movie = {
        "movie_id": m[0],
        "price_id": m[1],
        "title": m[2],
        "release_year": m[3],
        "rating": m[4],
        "poster": m[5],
        "price": m[6]
        }
        movies.append(movie)

    return movies

def get_movies_by_genre(genre):
    conn = db_connector.get_graph_db()
    cypher_query = f"""
        MATCH (m:Movie)-[:HAS]->(g:Genre)
        WHERE g.Genre = '{genre}'
        RETURN m.Title, g.Genre AS genre
        ORDER BY m.Title
    """
    results = conn.run(cypher_query)
    movies = []
    for record in results:
        movie_title = record['m.Title']
        movie_genre = record['genre']
        movies.append({'title': movie_title, 'genre': movie_genre})
    return movies


def get_movies_by_rating():
    conn = db_connector.get_graph_db()
    cypher_query = """
    MATCH (m:Movie)
    RETURN m.Title, m.Rating
    ORDER BY m.Rating DESC
    """

    results = conn.run(cypher_query)
    movies = [(record["m.Title"], record["m.Rating"]) for record in results]

    return movies

def get_movies_by_price():
    conn = db_connector.get_sql_db("BockBluster")

    c1 = conn.cursor()
    c1.execute("""
        SELECT m.title, p.price
        FROM movie m
        JOIN price p ON m.price_id = p.price_id
        ORDER BY p.price
    """)
    data = c1.fetchall()

    # Fetch movie titles and prices
    movies = []
    for row in data:
        movie = {
            "title": row[0],
            "price": row[1]
        }
        movies.append(movie)

    return movies


# Function to sort movies by release year
def get_movies_sorted_by_release_year():
    conn = db_connector.get_graph_db()

    cypher_query = '''
    MATCH (m:Movie)
    RETURN m.Title, m.Release_year
    ORDER BY m.Release_year DESC
    '''

    results = conn.run(cypher_query)

    movies = [(record["m.Title"], record["m.Release_year"]) for record in results]

    return movies

   
# Function to sort movies by runtime
def get_movies_sorted_by_runtime():
    conn = db_connector.get_graph_db()

    cypher_query = '''
    MATCH (m:Movie)
    RETURN m.Title, m.Runtime
    ORDER BY m.Runtime DESC
    '''

    results = conn.run(cypher_query)

    movies = []
    for record in results:
        movie = {
            'title': record['m.Title'],
            'runtime': record['m.Runtime']
        }
        movies.append(movie)

    return movies