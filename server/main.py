#FastAPI
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer
from typing import List

#Classes
from services import movie_service, populate_service, login_service, cart_service
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
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/movies/{movie_id}")
def get_movie(movie_id: str):
    # Call the fetch_movie_data function to retrieve the movie data
    movie_data = movie_service.fetch_movie_data(movie_id)

    if movie_data:
        # Return the movie data as JSON
        return movie_data.dict()
    else:
        # Return a 404 Not Found response if the movie data is not found
        return {"error": "Movie not found"}
### This below is for the cart service ###

class Item(BaseModel):
    user_id: int
    movie_id: str
    #duration: int

@app.post("/addtocart")
def add_to_cart(item: Item):
    return cart_service.add_to_cart(item)

@app.post("/removefromcart")
def remove_from_cart(item: Item):
    return cart_service.remove_from_cart(item)

@app.get("/get_cart")
async def get_cart(user_id: int):
    cart = cart_service.get_cart(user_id)
    return {"cartItems": cart}


@app.get('/movies/title/{title}')
def search_movie(title: str):
    movie_titles = movie_service.search_filter(title)

    if movie_titles:
        return movie_titles
    else:
        return []