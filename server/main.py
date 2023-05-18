#FastAPI
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer

#Classes
from services import test_service, populate_service, login_service
from models import dtos, entities

#Misc
from datetime import timedelta

app = FastAPI()

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

@app.get("/")
def read_root():
    return test_service.get_data()

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