import redis

# Our redis connection string, might be a bit different when we need to connect to a redis cluster later.
r = redis.Redis(host='localhost', port=6379, db=0) # adjust to your Redis settings

def add_to_cart(item):
    """ We are using Redis HSET for efficient storage and easy updates of cart items. """
    key = f"cart:{item.user_id}"
    r.hset(key, item.movie_id, item.duration)
    return {'message': 'Item added to cart'}


def remove_from_cart(item):
    """ We are using Redis HDEL for easy and atomic removal of specific cart items. """
    key = f"cart:{item.user_id}"
    r.hdel(key, item.movie_id)
    return {'message': 'Item removed from cart'}


def get_cart(user_id: int):
    """ Fetch all items from a specific cart in Redis using HGETALL. """
    key = f"cart:{user_id}"
    items = r.hgetall(key)
    # Since the way Redis returns is in bytes, we needed to decode them in order to make it work.
    items = {k.decode(): v.decode() for k, v in items.items()}
    return items
