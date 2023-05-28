import redis
from database import db_connector

r = db_connector.get_redis_db()

def add_to_cart(item):
    rental_duration = 7
    """ We are using Redis HSET for efficient storage and easy updates of cart items. """
    key = f"cart:{item.user_id}"
    r.hset(key, item.movie_id, rental_duration)
    return {'message': 'Item added to cart'}

def remove_from_cart(item):
    rental_duration = 7
    """ We are using Redis HDEL for easy and atomic removal of specific cart items. """
    key = f"cart:{item.user_id}"
    r.hdel(key, item.movie_id, rental_duration)
    return {'message': 'Item removed from cart'}

def clear_cart(user_id):
    """ Clears the entire cart for a given user. """
    key = f"cart:{user_id}"
    r.delete(key)
    return {'message': 'Cart cleared'}

def get_cart(user_id: int):
    """ Fetch all items from a specific cart in Redis using HGETALL. """
    key = f"cart:{user_id}"
    items = r.hgetall(key)
    items = {k.decode(): v.decode() for k, v in items.items()}

    #Get movie data from cart items
    conn = db_connector.get_graph_db()
    movie_ids = list(items)

    cypher_query = """
    MATCH (m:Movie)
    WHERE m.Id IN $movieIds
    OPTIONAL MATCH (m)<-[r:`STARRED_IN`]-(actor:Actor)
    OPTIONAL MATCH (m)<-[:INSTRUCTED]-(director:Director)
    OPTIONAL MATCH (m)-[:HAS]->(genre:Genre)
    OPTIONAL MATCH (m)<-[:PUBLISHED]-(publisher:Publisher)
    RETURN m.Title AS Title, m.Id AS movieId, m.Rating AS Rating, m.Summary AS Summary,
           m.Release_year AS ReleaseYear, m.Runtime AS Runtime, m.Certificate AS Certificate, m.Poster AS Poster, m.Price AS Price,
           COLLECT(DISTINCT actor.Name) AS Actors, COLLECT(DISTINCT director.Name) AS Directors,
           COLLECT(DISTINCT genre.Genre) AS Genres, COLLECT(DISTINCT publisher.Name) AS Publishers
    """

    data = conn.run(cypher_query, movieIds=movie_ids)

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

    # Calculate total price

    cypher_query = """
    MATCH (m:Movie)
    WHERE m.Id IN $movieIds
    RETURN SUM(m.Price) AS TotalPrice
    """

    totalPrice = conn.run(cypher_query, movieIds=movie_ids).evaluate()

    viewModel = {"movies": movies, "totalPrice": totalPrice}

    return viewModel
