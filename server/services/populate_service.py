from database import db_connector
import os
import sys
import inspect
import pandas as pd
from datetime import datetime
import uuid
from ast import literal_eval
from py2neo import Node, Relationship
import re

currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

sql_value = os.getenv("SQL_VALUE")

def get_fresh_df():
    df = pd.read_csv('../data/movies.csv')
    
    return df

def get_unique_strings(list_of_lists):
    unique_strings = set()
    for sublist in list_of_lists:
        for item in sublist:
            if isinstance(item, str):
                unique_strings.add(item)
    return list(unique_strings)


def populate_prices_sql():
    df = get_fresh_df()
    prices = []
    count = 0

    for index, row in df.iterrows():
        count += 1
        price = {"price_id": count, 'price': row['price']}
        prices.append(price)

    #Get connection
    connection = db_connector.get_sql_db('BockBluster')

    # Insert dictionaries into the table
    cursor = connection.cursor()
    for price in prices:
        cursor.execute(f"INSERT INTO price (price_id, price) VALUES ({sql_value}, {sql_value})", (price['price_id'], price['price']))

    # Commit the changes and close the connection
    connection.commit()
    connection.close()

def populate_movies_sql():
    df = get_fresh_df()
    df = df[['id', 'title', 'release year', 'rating', 'Poster']]

    movies = []

    for i in range(len(df['release year'])):
        df.at[i, 'release year'] = ''.join(filter(str.isdigit, str(df.at[i, 'release year'])))

    count = 0
    for index, row in df.iterrows():
        count += 1
        year_date = datetime.strptime(row['release year'], '%Y').year
        movie = {"id": row['id'],'price_id': count, 'title': row['title'], 'release_year': year_date, 'rating': float(row['rating']), 'poster': row['Poster']}
        movies.append(movie)

    connection = db_connector.get_sql_db("BockBluster")

    # Insert dictionaries into the table
    cursor = connection.cursor()
    for dictionary in movies:
        cursor.execute(f"INSERT INTO movie (movie_id, price_id, title, release_year, rating, poster) VALUES ({sql_value}, {sql_value}, {sql_value}, {sql_value}, {sql_value}, {sql_value})", (dictionary['id'], dictionary['price_id'], dictionary['title'], dictionary['release_year'], dictionary['rating'], dictionary['poster']))

    # Commit the changes and close the connection
    connection.commit()
    connection.close()

def populate_members_sql():
    current_datetime = datetime.now()

    members = [{
    "member_id": str(uuid.uuid4()),
    "first_name": "John",
    "last_name": "Doe",
    "join_date": current_datetime
    },
    {
    "member_id": str(uuid.uuid4()),
    "first_name": "Jane",
    "last_name": "Smith",
    "join_date": current_datetime
    },
    {
    "member_id": str(uuid.uuid4()),
    "first_name": "Robert",
    "last_name": "Johnson",
    "join_date": current_datetime
    }]

    connection = db_connector.get_sql_db('BockBluster')

    # Insert dictionaries into the table
    cursor = connection.cursor()
    for member in members:
        cursor.execute(f"INSERT INTO member (member_id, first_name, last_name, join_date) VALUES ({sql_value},{sql_value},{sql_value},{sql_value})", (member['member_id'], member['first_name'], member['last_name'], member['join_date']))

    # Commit the changes and close the connection
    connection.commit()
    connection.close()

def populate_users_sql():
    connection = db_connector.get_sql_db('BockBluster')
    cursor = connection.cursor()
    query = "SELECT * FROM member"
    cursor.execute(query)
    rows = cursor.fetchall()
    member_ids = []

    for row in rows:
        member_id = row[0]
        member_ids.append(member_id)

    cursor.close()
    connection.close()

    users = [{
        "user_id": 1,
        "member_id": member_ids[0],
        "username": "user1",
        "password": "123"
    },
    {
        "user_id": 2,
        "member_id": member_ids[1],
        "username": "user2",
        "password": "123"
    },
    {
        "user_id": 3,
        "member_id": member_ids[2],
        "username": "user3",
        "password": "123"
    }]

    connection = db_connector.get_sql_db('BockBluster')
    cursor = connection.cursor()

    # Insert dictionaries into the table
    cursor = connection.cursor()
    for user in users:
        cursor.execute(f"INSERT INTO user_login (user_id, member_id, username, password) VALUES ({sql_value},{sql_value},{sql_value},{sql_value})", (user['user_id'], user['member_id'], user['username'], user['password']))

    # Commit the changes and close the connection
    connection.commit()
    connection.close()



def populate_sql():

    #Prices
    #populate_prices_sql()

    #Movies
    #populate_movies_sql()

    #Members
    populate_members_sql()

    #Users
    populate_users_sql()

    
    return "Database populate successful!"


def populate_graphdb():
    df = get_fresh_df()

    df['reviews'] = df['reviews'].apply(literal_eval)
    df['review_user'] = df['review_user'].apply(literal_eval)
    df['review_score'] = df['review_score'].apply(literal_eval)
    df['directors'] = df['directors'].apply(lambda x: x.split(', '))
    df['genre'] = df['genre'].apply(lambda x: x.split(', '))
    df['actors'] = df['actors'].apply(lambda x: x.split(', '))
    df['publishers'] = df['publishers'].apply(literal_eval)
    df['release year'] = df['release year'].apply(lambda x: re.sub(r'\D', '', x)).astype(int)
    df['runtime'] = df['runtime'].apply(lambda x: re.sub(r'\D', '', x)).astype(int)



    review_dict_list = []
    for reviews, scores in zip(df['reviews'], df['review_score']):
        for review, rating in zip(reviews, scores):
            review_dict_list.append({'review': review, 'rating': rating})

            # Connect to the Neo4j database
    graph = db_connector.get_graph_db()

    # Create nodes for movies, reviews, and users
    count = 0
    for index, row in df.iterrows():
        count += 1
        # Create a movie node
        movie_node = Node("Movie", Id=row['id'], Title=row['title'], Rating=row['rating'], Summary=row['summary'], Release_year=row['release year'], Runtime=row['runtime'], Certificate=row['certificate'], Poster=row['Poster'], Price=row['price'])
        graph.create(movie_node)

        # Create review and user nodes and relationships
        for review, rating, user in zip(row['reviews'], row['review_score'], row['review_user']):
            review_node = Node("Review", Content=review, Rating=rating)
            graph.create(review_node)

            relationship = Relationship(review_node, "FOR", movie_node)
            graph.create(relationship)

            user_node = Node("User", Username=user)
            graph.create(user_node)

            relationship = Relationship(user_node, "WROTE", review_node)
            graph.create(relationship)

        # Create genre nodes and relationships
        genres = row['genre']
        genre_nodes = {}
        for genre in genres:
            genre_node = Node("Genre", Genre=genre)
            graph.create(genre_node)
            genre_nodes[genre] = genre_node

            relationship = Relationship(movie_node, "HAS", genre_node)
            graph.create(relationship)

        # Create director nodes and relationships
        directors = row['directors']
        director_nodes = {}
        for director in directors:
            director_node = Node("Director", Name=director)
            graph.create(director_node)
            director_nodes[director] = director_node

            relationship = Relationship(director_node, "INSTRUCTED", movie_node)
            graph.create(relationship)

        # Create actor nodes and relationships
        actors = row['actors']
        actor_nodes = {}
        for actor in actors:
            actor_node = Node("Actor", Name=actor)
            graph.create(actor_node)
            actor_nodes[actor] = actor_node

            relationship = Relationship(actor_node, "STARRED_IN", movie_node)
            graph.create(relationship)

        # Create publisher nodes and relationships
        publishers = row['publishers']
        publisher_nodes = {}
        for publisher in publishers:
            publisher_node = Node("Publisher", Name=publisher)
            graph.create(publisher_node)
            publisher_nodes[publisher] = publisher_node

            relationship = Relationship(publisher_node, "PUBLISHED", movie_node)
            graph.create(relationship)



    return "Database populate successful!"