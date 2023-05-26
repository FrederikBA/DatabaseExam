#FastAPI
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer
from typing import List

#Classes
from services import movie_service, populate_service, login_service, cart_service, order_service
from models import dtos, entities

#Misc
from datetime import timedelta
from pydantic import BaseModel
import os
import sys
import inspect

app = FastAPI()

#Cors
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#Set correct path for folder structure
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

#Endpoints
@app.get("/")
def read_root():
    return "Welcome to the database course exam API!"

@app.get("/movies")
def get_movies():
    return movie_service.get_movie_catalog()

@app.post("/populatesql")
def populate_sql_db():
    return populate_service.populate_sql()

@app.post("/populategraph")
def populate_graph_db():
    return populate_service.populate_graphdb()

@app.post("/login")
def login_for_access_token(user: entities.User):
    authenticated_user = login_service.authenticate_user(user.username, user.password)
    if not authenticated_user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=60)
    access_token = login_service.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer", "user_id": authenticated_user['id']}

@app.get("/movies/id/{movie_id}")
def get_movie(movie_id: str):
    movie_data = movie_service.get_movie_details(movie_id)

    if movie_data:
        return movie_data.dict()
    else:
        return {"error": "Movie not found"}

@app.post("/addtocart")
def add_to_cart(item: dtos.cartDTO):
    return cart_service.add_to_cart(item)

@app.post("/removefromcart")
def remove_from_cart(item: dtos.cartDTO):
    return cart_service.remove_from_cart(item)

@app.post("/clearcart")
def clear_cart(user_id: int):
    return cart_service.clear_cart(user_id)


@app.get("/get_cart")
async def get_cart(user_id: int):
    return cart_service.get_cart(user_id)

# Endpoint to retrieve movies sorted by title
@app.get('/movies/title/{title}')
def search_movie(title: str):
    movie_titles = movie_service.search_filter(title)

    if movie_titles:
        return movie_titles
    else:
        return []
    
@app.post('/order')
def create_order_test(order_dto: dtos.orderDTO):
    return order_service.create_order(order_dto)

# Endpoint to retrieve movies sorted by genre
@app.get('/movies/sort/genre/{genre}')
def get_movies_by_genre(genre: str):
    movies = movie_service.get_movies_by_genre(genre)
    if movies:
        return movies
    else:
        return []
    

# Endpoint to retrieve movies sorted by rating
@app.get("/movies/sort/rating/{sort_order}")
def get_movies_by_rating(sort_order: str):
    return movie_service.get_movies_by_rating(sort_order.upper())

# Endpoint to retrieve movies sorted by price
@app.get('/movies/sort/price/{sort_order}')
def get_movies_sorted_by_price(sort_order: str):
    return movie_service.get_movies_by_price(sort_order.upper())
    
# Endpoint to retrieve movies sorted by release year
@app.get('/movies/sort/releaseyear/{sort_order}')
def get_movies_sorted_by_release_year_endpoint(sort_order: str):
    return movie_service.get_movies_sorted_by_release_year(sort_order.upper())

# Endpoint to retrieve movies sorted by runtime
@app.get('/movies/sort/runtime/{sort_order}')
def get_movies_sorted_by_runtime_endpoint(sort_order: str):
    return movie_service.get_movies_sorted_by_runtime(sort_order.upper())

@app.get("/member/{user_id}")
def get_member_id(user_id: int):
    return login_service.get_member_id(user_id)
    

