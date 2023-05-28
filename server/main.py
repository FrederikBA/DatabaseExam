#FastAPI
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer

#Classes
from services import movie_service, populate_service, login_service, cart_service, order_service, profile_service, recommendation_service
from models import dtos, entities
from database import db_connector

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
    return {"access_token": access_token, "token_type": "bearer", "user_id": authenticated_user['id'], "member_id": authenticated_user['member_id'] }

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

@app.get('/movies/filter/genre/{genre}')
def filter_movies_by_genre(genre: str):
    return movie_service.get_movies_by_genre(genre)
    
@app.get('/movies/sort/')
def get_movies_sorted(sort_value: str, sort_order: str):
    return movie_service.get_movies_sorted(sort_value, sort_order)

@app.get("/member/{user_id}")
def get_member_id(user_id: int):
    return login_service.get_member_id(user_id)

@app.get("/loans/")
def get_member_id(member_id: str):
    return profile_service.get_user_loans(member_id)

@app.get("/cluster")
def get_redis_nodes():
    rc = db_connector.get_redis_clustered_db()
    print(rc.get_nodes())
    return "fisk"
    
@app.post("/nodesimilarity")
def populate_graph_projection():
    return populate_service.create_and_write_node_similarity()

@app.get("/recommendations/")
def get_node_similarity(movie_ids: str):
    movie_ids = movie_ids.split(",")
    print(movie_ids)
    return recommendation_service.recommend_movies(movie_ids)

@app.post('/register')
def register_user(registerDTO: dtos.registerDTO):
    return login_service.register_user(registerDTO)
