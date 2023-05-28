from database import db_connector
from services import recommendation_service
import os

sql_value = os.getenv("SQL_VALUE")

def get_user_loans(member_id):
    connection = db_connector.get_sql_db('BockBluster')
    cursor = connection.cursor()

    query = f"""
    SELECT loan_id, movie_id, loan_date, return_date
    FROM loan
    JOIN orders ON loan.order_id = orders.order_id
    WHERE orders.member_id = {sql_value};
    """
    cursor.execute(query, (member_id,))
    rows = cursor.fetchall()

    movie_ids = []

    for row in rows:
        movie_ids.append(row[1])

    cursor.close()
    connection.close()

    #Get Graph movie data for loaned movies
    graph = db_connector.get_graph_db()

    cypher_query = """
    UNWIND $movieIds AS movieId
    MATCH (m:Movie)
    WHERE m.Id = movieId
    RETURN m.Title AS Title, m.Id AS movieId, m.Rating AS Rating, m.Summary AS Summary,
           m.Release_year AS ReleaseYear, m.Runtime AS Runtime, m.Certificate AS Certificate, m.Poster AS Poster, m.Price AS Price
    """

    data = graph.run(cypher_query, movieIds=movie_ids)

    movies = []
    for i, m in enumerate(data):
            movie = {
                "title": m[0],
                "movie_id": m[1],
                "rating": m[2],
                "release_year": m[4],
                "runtime": m[5],
                "price": m[8],
                "poster": m[7],
                "loan_date": rows[i][2], 
                "return_date": rows[i][3],
                "loan_id": rows[i][0]
            }
            movies.append(movie)

    # Recommended movies
    recommended_movies = recommendation_service.recommend_movies(movie_ids)


    viewModel = {"loans": movies, "recommendations": recommended_movies}

    return viewModel