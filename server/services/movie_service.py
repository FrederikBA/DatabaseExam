from database import db_connector

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

