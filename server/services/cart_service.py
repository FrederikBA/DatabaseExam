import redis
from database import db_connector
import os

sql_value = os.getenv("SQL_VALUE")

# Our redis connection string, might be a bit different when we need to connect to a redis cluster later.
r = redis.Redis(host='localhost', port=6379, db=0) # adjust to your Redis settings

def add_to_cart(item):
    rental_duration = 7 # Rental duration set to 7 days
    """ We are using Redis HSET for efficient storage and easy updates of cart items. """
    key = f"cart:{item.user_id}"
    r.hset(key, item.movie_id, rental_duration)
    return {'message': 'Item added to cart'}


def remove_from_cart(item):
    """ We are using Redis HDEL for easy and atomic removal of specific cart items. """
    key = f"cart:{item.user_id}"
    r.hdel(key, item.movie_id)
    return {'message': 'Item removed from cart'}

# def clear_cart(items):
#     for item in items:
#         remove_from_cart(item[1][0])
#     return items

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
    movies = []
    totalPrice = 0


    if(len(items) == 1):
        connection = db_connector.get_sql_db('BockBluster')
        cursor = connection.cursor()
        print(items)
        query = f"""
            SELECT m.movie_id, m.price_id, m.title, m.release_year, m.rating, m.poster, p.price
            FROM movie m
            JOIN price p ON m.price_id = p.price_id
            WHERE m.movie_id = '{list(items)[0]}'
        """

        cursor.execute(query)

        rows = cursor.fetchall()


        for m in rows:
            movie = {"movie_id": m[0],
                "price_id": m[1],
                "title": m[2],
                "release_year": m[3],
                "rating": m[4],
                "poster": m[5],
                "price": m[6]}
            totalPrice = totalPrice + m[6]
            movies.append(movie)


    if(len(items) > 1):
        connection = db_connector.get_sql_db('BockBluster')
        cursor = connection.cursor()

        query = """
        SELECT m.movie_id, m.price_id, m.title, m.release_year, m.rating, m.poster, p.price
        FROM movie m
        JOIN price p ON m.price_id = p.price_id
        WHERE m.movie_id IN ({})
    """.format(', '.join('%s' for _ in items))

        cursor.execute(query, tuple(items))

        rows = cursor.fetchall()

        for m in rows:
            movie = {"movie_id": m[0],
                "price_id": m[1],
                "title": m[2],
                "release_year": m[3],
                "rating": m[4],
                "poster": m[5],
                "price": m[6]}
            totalPrice = totalPrice + m[6]
            
            movies.append(movie)

    viewModel = {"movies": movies, "totalPrice": totalPrice}


    return viewModel
