from database import db_connector

def get_movie_catalog():
    conn = db_connector.get_sql_db("BockBluster")

    c1 = conn.cursor()
    c1.execute('SELECT * FROM movie')
    data = c1.fetchall()

    movies = []

    for m in data:
        movie = {"movie_id": m[0], "title": m[1], 'release_year': m[2], 'rating': m[3], 'poster': m[4]}
        movies.append(movie)

    # Close connection
    conn.close()

    return movies