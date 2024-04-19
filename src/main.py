# learning to use redis from python3

import redis
import time
from datetime import datetime


# Default expiration time for Redis keys in this demo
DEFAULT_EXPIRATION = 600  # 10 minutes


def redis_demo():
    """
    Exemplify the main functionalities of Redis
    :return: nothing
    """
    # Connect to Redis
    r0 = connect_to_redis_db()
    r1 = connect_to_redis_db(1)

    print("Strings: Saving, Modifying, and Retrieving")
    string_key = 'greeting'
    print(r0.get(string_key))                                                 # Get the string, if pre-existing
    r0.set(string_key, 'Hello, world!', ex=DEFAULT_EXPIRATION)          # Save a string
    r0.set(string_key, 'Hello, Redis!', ex=DEFAULT_EXPIRATION)          # Replace the string
    print(r0.get(string_key))                                                 # Get the string
    print_expiration(r0, string_key)                                                 
    print()

    print("Lists: Saving, Modifying, and Retrieving")
    list_key = 'mylist'
    print(r0.lrange(list_key, 0, -1))               # Get the list, if pre-existing 
    r0.lpush(list_key, 'one')                     # Save initial elements to a list
    r0.lpush(list_key, 'two', 'three')            # Add more elements to the list
    r0.lset(list_key, 0, 'four')              # Replace an element in the list
    print(r0.lrange(list_key, 0, -1))                # Get the list
    r0.expire(list_key, time=DEFAULT_EXPIRATION)          # set expiration time
    print_expiration(r0, list_key)
    print()

    print("Hashes: Saving, Modifying, and Retrieving")
    hash_key = 'mymap'
    r0.hset(hash_key, mapping={'name': 'John', 'age': '30'})  # Save a hash
    r0.hset(hash_key, 'age', '31')                 # Modify the hash
    print(r0.hgetall(hash_key))                               # Get the hash
    r0.pexpire(hash_key, 500)                            # expire this after only 500 millisecs
    print_expiration(r0, hash_key)
    print()

    print("Sets: Saving, Modifying, and Retrieving")
    set_key = 'myset'
    r0.sadd(set_key, 'a', 'b', 'c')             # Save elements to a set
    r0.sadd(set_key, 'd')                       # Add more elements to the set
    r0.srem(set_key, 'a')                       # Remove an element from the set
    print(r0.smembers(set_key))                         # Get the set
    r0.expireat(set_key, when=int(time.time()) + 60)    # expire in 1 minute from now
    print_expiration(r0, set_key)
    print()

    print("Sorted Sets: Saving, Modifying, and Retrieving")
    sortedset_key = 'mysortedset'
    r0.zadd(sortedset_key, {'a': 1, 'b': 2, 'c': 3})      # Save elements to a sorted set
    r0.zadd(sortedset_key, {'a': 5})                      # Modify the score of an element
    print(r0.zrange(sortedset_key, 0, -1, withscores=True))  # Get the sorted set
    print()

    print("HyperLogLog: Adding elements and estimating cardinality")
    hll_key = 'hll_users'
    estimated_users = r0.pfcount(hll_key)                                # Estimate cardinality
    print("Estimated number of unique users:", estimated_users)
    r0.pfadd(hll_key, 'user1', 'user2', 'user3', 'user2')  # Add elements
    r0.pfadd(hll_key, 'user1', 'user5', 'user7', 'user8')  # Add elements
    estimated_users = r0.pfcount(hll_key)                                # Estimate cardinality
    print("Estimated number of unique users:", estimated_users)
    print()

    print("Geospatial Indexes: Adding, querying distance, and querying nearby members")
    geo_key = 'cities'
    r0.geoadd(geo_key, (13.361389, 38.115556, 'Palermo'))
    r0.geoadd(geo_key, (15.087269, 37.502669, 'Catania'))
    distance = r0.geodist(geo_key, 'Palermo', 'Catania', unit='km')          # Distance b/w cities
    position = r0.geopos(geo_key, 'Palermo')                                       # Position of Palermo
    nearby_cities = r0.georadiusbymember(geo_key, 'Catania', 200, 'km') # Cities within 200 km
    print("Distance between cities:", distance)
    print("Position of Palermo:", position)
    print("Cities within 200 km of Catania:", nearby_cities)
    print()

    print("Streams: Adding entries and reading from the stream")
    stream_name = 'mystream'
    r1.xadd(stream_name, {'type': 'event1', 'content': 'Hello'})  # Add message to stream
    r1.xadd(stream_name, {'type': 'event2', 'content': 'World'})  # Add another message to stream
    messages = r1.xrange(stream_name)                                   # Read messages from stream
    last_two_messages = r1.xrevrange(stream_name, count=2)              # Last two messages
    print("Messages in stream:", messages)
    print("Last two messages in stream:", last_two_messages)
    print()


def connect_to_redis_db(db_nr: int=0):
    """
    Get a connection to a redis DB
    :param db_nr: int such that 0 <= db_nr <= 15
    :return: redis.Redis instance
    """
    # by default, a redis server has 16 DBs
    if not 0 <= db_nr <= 15:
        raise ValueError("db_nr out of bounds")
    return redis.Redis(host='localhost', port=6379,
                       db=db_nr,
                       password="insertAStrongRedisPasswordFromASecureStorage",
                       charset='utf-8', decode_responses=True  # automatic encoding/decoding to and from byte strings
                       )


def print_expiration(redis_db_conn: redis.Redis, key: str):
    """
    Print the residual Time-To-Live and planned expiration time of a key
    :param redis_db_conn: redis.Redis connection being used
    :param key: str - desired key
    :return: nothing
    """
    pttl = redis_db_conn.pttl(key)
    ttl = redis_db_conn.ttl(key)
    unix_expire_at = redis_db_conn.expiretime(key)
    expire_at = datetime.fromtimestamp(unix_expire_at)
    print(f'The Time-To-Live of key "{key}" is {pttl} millisecs ~= {ttl} secs; it will expire at {expire_at}.')


if __name__ == "__main__":
    redis_demo()
