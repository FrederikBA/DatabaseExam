from database import db_connector

def get_movie_catalog():
    conn = db_connector.get_sql_db("BockBluster")

    c1 = conn.cursor()
    c1.execute('SELECT * FROM movie')
    data = c1.fetchall()

    movies = []

    for m in data:
        movie = {"movie_id": m[0],"price_id": m[1], "title": m[2], 'release_year': m[3], 'rating': m[4], 'poster': m[5]}
        movies.append(movie)

    # Close connection
    conn.close()

    return movies