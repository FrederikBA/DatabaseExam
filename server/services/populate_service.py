from database import db_connector
import os
import sys
import inspect
import pandas as pd
from datetime import datetime
import uuid
from ast import literal_eval
from py2neo import Node, Relationship

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

def populate_sql():
    #Movies
    df = get_fresh_df()

    df = df[['id', 'title', 'release year', 'rating', 'Poster']]

    movies = []

    for i in range(len(df['release year'])):
        df.at[i, 'release year'] = ''.join(filter(str.isdigit, str(df.at[i, 'release year'])))


    for index, row in df.iterrows():
        year_date = datetime.strptime(row['release year'], '%Y').year
        movie = {"id": row['id'], 'title': row['title'], 'release_year': year_date, 'rating': float(row['rating']), 'poster': row['Poster']}
        movies.append(movie)

    connection = db_connector.get_sql_db("BockBluster")

    cursor = connection.cursor()
    for dictionary in movies:
        cursor.execute(f"INSERT INTO movie (movie_id, title, release_year, rating, poster) VALUES ({sql_value}, {sql_value}, {sql_value}, {sql_value}, {sql_value})", (dictionary['id'], dictionary['title'], dictionary['release_year'], dictionary['rating'], dictionary['poster']))

    connection.commit()
    connection.close()

    #Actors
    df = get_fresh_df()
    df['actors'] = df['actors'].apply(lambda x: x.split(', '))

    strings = get_unique_strings(df['actors'])

    dict_list = []
    for i, string in enumerate(strings, start=1):
        dictionary = {'id': i, 'name': string}
        dict_list.append(dictionary)

    connection = db_connector.get_sql_db("BockBluster")
    cursor = connection.cursor()
    for dictionary in dict_list:
        cursor.execute(f"INSERT INTO actor (actor_id, name) VALUES ({sql_value}, {sql_value})", (dictionary['id'], dictionary['name']))

    connection.commit()
    connection.close()

    #Genres
    df = get_fresh_df()
    df['genre'] = df['genre'].apply(lambda x: x.split(', '))

    strings = get_unique_strings(df['genre'])

    dict_list = []
    for i, string in enumerate(strings, start=1):
        dictionary = {'id': i, 'name': string}
        dict_list.append(dictionary)
    dict_list

    connection = db_connector.get_sql_db("BockBluster")
    cursor = connection.cursor()
    for dictionary in dict_list:
        cursor.execute(f"INSERT INTO genre(genre_id, genre_name) VALUES ({sql_value}, {sql_value})", (dictionary['id'], dictionary['name']))

    connection.commit()
    connection.close()

    #Directors
    df = get_fresh_df()
    df['directors'] = df['directors'].apply(lambda x: x.split(', '))

    strings = get_unique_strings(df['directors'])

    dict_list = []
    for i, string in enumerate(strings, start=1):
        dictionary = {'id': i, 'name': string}
        dict_list.append(dictionary)

    connection = db_connector.get_sql_db("BockBluster")
    cursor = connection.cursor()
    for dictionary in dict_list:
        cursor.execute(f"INSERT INTO director (director_id, name) VALUES ({sql_value}, {sql_value})", (dictionary['id'], dictionary['name']))

    connection.commit()
    connection.close()

    #Publishers
    df = get_fresh_df()
    df['publishers'] = df['publishers'].apply(literal_eval)

    strings = get_unique_strings(df['publishers'])

    dict_list = []
    for i, string in enumerate(strings, start=1):
        dictionary = {'id': i, 'name': string}
        dict_list.append(dictionary)


    connection = db_connector.get_sql_db("BockBluster")

    cursor = connection.cursor()
    for dictionary in dict_list:
        cursor.execute(f"INSERT INTO publisher (publisher_id, name) VALUES ({sql_value}, {sql_value})", (dictionary['id'], dictionary['name']))

    connection.commit()
    connection.close()
    

    #MovieActors link table
    connection = db_connector.get_sql_db("BockBluster")
    cursor = connection.cursor()

    query = "SELECT * FROM actor"
    cursor.execute(query)
    rows = cursor.fetchall()
    data_list = []
    for row in rows:
        value1 = row[0]
        value2 = row[1]
        dictionary = {'id': value1, 'name': value2}
        data_list.append(dictionary)
    cursor.close()
    connection.close()

    df = get_fresh_df()
    df['actors'] = df['actors'].apply(lambda x: x.split(', '))

    df['actors'] = df['actors'].apply(lambda x: list(set(x)))

    df_new = df[['id', 'actors']]

    df_new = df_new.explode('actors')

    movies_list = df_new.to_dict(orient='records')

    mapping = []
    for movie in movies_list:
        movie_id = movie['id']
        actor_name = movie['actors']
        for actor in data_list:
            if actor['name'] == actor_name:
                actor_id = actor['id']
                new_movie = {'movie_id': movie_id, 'actor_id': actor_id}
                mapping.append(new_movie)
                break

    connection = db_connector.get_sql_db("BockBluster")
    cursor = connection.cursor()
    for dictionary in mapping:
        cursor.execute(f"INSERT INTO movie_actor (movie_id, actor_id) VALUES ({sql_value}, {sql_value})", (dictionary['movie_id'], dictionary['actor_id']))

    connection.commit()
    connection.close()

    #MovieDirectors link table
    connection = db_connector.get_sql_db("BockBluster")
    cursor = connection.cursor()
    query = "SELECT * FROM director"
    cursor.execute(query)
    rows = cursor.fetchall()

    data_list = []
    for row in rows:
        value1 = row[0]
        value2 = row[1]
        dictionary = {'id': value1, 'name': value2}
        data_list.append(dictionary)

    cursor.close()
    connection.close()

    df = get_fresh_df()
    df['directors'] = df['directors'].apply(lambda x: [x] if ',' not in x else x.split(','))

    df['directors'] = df['directors'].apply(lambda x: list(set(x)))

    df_new = df[['id', 'directors']]

    df_new = df_new.explode('directors')

    movies_list = df_new.to_dict(orient='records')

    mapping = []
    for movie in movies_list:
        movie_id = movie['id']
        director_name = movie['directors']
        for director in data_list:
            if director['name'] == director_name:
                director_id = director['id']
                new_movie = {'movie_id': movie_id, 'director_id': director_id}
                mapping.append(new_movie)
                break

    connection = db_connector.get_sql_db("BockBluster")
    cursor = connection.cursor()
    for dictionary in mapping:
        cursor.execute(f"INSERT INTO movie_director (movie_id, director_id) VALUES ({sql_value}, {sql_value})", (dictionary['movie_id'], dictionary['director_id']))
    connection.commit()
    connection.close()

    #MoviePublishers link table
    connection = db_connector.get_sql_db("BockBluster")
    cursor = connection.cursor()

    query = "SELECT * FROM publisher"
    cursor.execute(query)
    rows = cursor.fetchall()
    data_list = []

    for row in rows:
        value1 = row[0]
        value2 = row[1]
        dictionary = {'id': value1, 'name': value2}
        data_list.append(dictionary)

    cursor.close()
    connection.close()

    df = get_fresh_df()
    df['publishers'] = df['publishers'].apply(literal_eval)

    df['publishers'] = df['publishers'].apply(lambda x: list(set(x)))

    df_new = df[['id', 'publishers']]

    df_new = df_new.explode('publishers')

    movies_list = df_new.to_dict(orient='records')

    mapping = []
    for movie in movies_list:
        movie_id = movie['id']
        publisher_name = movie['publishers']
        for publisher in data_list:
            if publisher['name'] == publisher_name:
                publisher_id = publisher['id']
                new_movie = {'movie_id': movie_id, 'publisher_id': publisher_id}
                mapping.append(new_movie)
                break
    
    connection = db_connector.get_sql_db("BockBluster")
    cursor = connection.cursor()
    for dictionary in mapping:
        cursor.execute(f"INSERT INTO movie_publishers (movie_id, publisher_id) VALUES ({sql_value}, {sql_value})", (dictionary['movie_id'], dictionary['publisher_id']))

    connection.commit()
    connection.close()

    #MovieGenres link table
    connection = db_connector.get_sql_db("BockBluster")
    cursor = connection.cursor()

    query = "SELECT * FROM genre"
    cursor.execute(query)
    rows = cursor.fetchall()
    data_list = []

    for row in rows:
        value1 = row[0]
        value2 = row[1]
        dictionary = {'id': value1, 'name': value2}
        data_list.append(dictionary)

    cursor.close()
    connection.close()

    df = get_fresh_df()

    df['genre'] = df['genre'].apply(lambda x: x.split(', '))

    df['genre'] = df['genre'].apply(lambda x: list(set(x)))

    df_new = df[['id', 'genre']]

    df_new = df_new.explode('genre')

    movies_list = df_new.to_dict(orient='records')


    mapping = []
    for movie in movies_list:
        movie_id = movie['id']
        genre_name = movie['genre']
        for genre in data_list:
            if genre['name'] == genre_name:
                genre_id = genre['id']
                new_movie = {'movie_id': movie_id, 'genre_id': genre_id}
                mapping.append(new_movie)
                break

    connection = db_connector.get_sql_db("BockBluster")
    cursor = connection.cursor()
    for dictionary in mapping:
        cursor.execute(f"INSERT INTO movie_genre (movie_id, genre_id) VALUES ({sql_value}, {sql_value})", (dictionary['movie_id'], dictionary['genre_id']))

    connection.commit()
    connection.close()

    #Members
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
        cursor.execute("INSERT INTO member (member_id, first_name, last_name, join_date) VALUES (%s, %s, %s, %s)", (member['member_id'], member['first_name'], member['last_name'], member['join_date']))

    # Commit the changes and close the connection
    connection.commit()
    connection.close()

    #Users
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
        cursor.execute("INSERT INTO user_login (user_id, member_id, username, password) VALUES (%s, %s, %s, %s)", (user['user_id'], user['member_id'], user['username'], user['password']))

    # Commit the changes and close the connection
    connection.commit()
    connection.close()
    
    return "Database populate successful!"


def populate_graphdb():
    df = get_fresh_df()

    #Prepare data
    df['reviews'] = df['reviews'].apply(literal_eval)
    df['review_user'] = df['review_user'].apply(literal_eval)
    df['review_score'] = df['review_score'].apply(literal_eval)

    review_dict_list = []
    for reviews, scores in zip(df['reviews'], df['review_score']):
        for review, rating in zip(reviews, scores):
            review_dict_list.append({'review': review, 'rating': rating})

    #Create graph
    graph = db_connector.get_graph_db()
    for index, row in df.iterrows():
        # Create a movie node
        movie_node = Node("Movie", title=row['title'])
        graph.create(movie_node)

        # Create review nodes and relationships
        for review, rating, user in zip(row['reviews'], row['review_score'], row['review_user']):
            review_node = Node("Review", content=review, rating=rating)
            graph.create(review_node)

            relationship = Relationship(review_node, "FOR", movie_node)
            graph.create(relationship)

            user_node = Node("User", name=user)
            graph.create(user_node)

            relationship = Relationship(user_node, "WROTE", review_node)
            graph.create(relationship)

    return "Database populate successful!"