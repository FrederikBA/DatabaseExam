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
    connection = db_connector.get_graph_db()

    cypher_query = f"""
    MATCH (m:Movie)
    WHERE m.Title =~ "(?i).*{title}.*"
    OPTIONAL MATCH (m)<-[r:`STARRED_IN`]-(actor:Actor)
    OPTIONAL MATCH (m)<-[:INSTRUCTED]-(director:Director)
    OPTIONAL MATCH (m)-[:HAS]->(genre:Genre)
    OPTIONAL MATCH (m)<-[:PUBLISHED]-(publisher:Publisher)
    RETURN m.Title AS Title, m.Id AS movieId, m.Rating AS Rating, m.Summary AS Summary,
    m.Release_year AS ReleaseYear, m.Runtime AS Runtime, m.Certificate AS Certificate, m.Poster AS Poster, m.Price AS Price,
    COLLECT(DISTINCT actor.Name) AS Actors, COLLECT(DISTINCT director.Name) AS Directors,
    COLLECT(DISTINCT genre.Genre) AS Genres, COLLECT(DISTINCT publisher.Name) AS Publishers
    """
   
    data = connection.run(cypher_query)
   
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

def filter_movies_by_genre(genre):
    conn = db_connector.get_graph_db()
    cypher_query = f"""
    MATCH (m:Movie)-[:HAS]->(g:Genre)
    WHERE g.Genre = '{genre}'
    OPTIONAL MATCH (m)<-[r:`STARRED_IN`]-(actor:Actor)
    OPTIONAL MATCH (m)<-[:INSTRUCTED]-(director:Director)
    OPTIONAL MATCH (m)-[:HAS]->(genre:Genre)
    OPTIONAL MATCH (m)<-[:PUBLISHED]-(publisher:Publisher)
    RETURN m.Title AS Title, m.Id AS movieId, m.Rating AS Rating, m.Summary AS Summary,
    m.Release_year AS ReleaseYear, m.Runtime AS Runtime, m.Certificate AS Certificate, m.Poster AS Poster, m.Price AS Price,
    COLLECT(DISTINCT actor.Name) AS Actors, COLLECT(DISTINCT director.Name) AS Directors,
    COLLECT(DISTINCT genre.Genre) AS Genres, COLLECT(DISTINCT publisher.Name) AS Publishers
    ORDER BY m.Title
    """
    results = conn.run(cypher_query)
    movies = []
    for record in results:
        movie_title = record['m.Title']
        movie_genre = record['genre']
        movies.append({'title': movie_title, 'genre': movie_genre})
    return movies


def get_movies_sorted(sort_value, sort_order):
    conn = db_connector.get_graph_db()
    cypher_query = f'''
    OPTIONAL MATCH (m)<-[r:`STARRED_IN`]-(actor:Actor)
    OPTIONAL MATCH (m)<-[:INSTRUCTED]-(director:Director)
    OPTIONAL MATCH (m)-[:HAS]->(genre:Genre)
    OPTIONAL MATCH (m)<-[:PUBLISHED]-(publisher:Publisher)
    RETURN m.Title AS Title, m.Id AS movieId, m.Rating AS Rating, m.Summary AS Summary,
    m.Release_year AS ReleaseYear, m.Runtime AS Runtime, m.Certificate AS Certificate, m.Poster AS Poster, m.Price AS Price,
    COLLECT(DISTINCT actor.Name) AS Actors, COLLECT(DISTINCT director.Name) AS Directors,
    COLLECT(DISTINCT genre.Genre) AS Genres, COLLECT(DISTINCT publisher.Name) AS Publishers
    ORDER BY {sort_value} {sort_order}
    '''
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
