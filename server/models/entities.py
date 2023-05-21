from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    
from pydantic import BaseModel

class Movie(BaseModel):
    title: str
    movieId: str
    rating: float
    summary: str
    actors: list[str]
    directors: list[str]
    genres: list[str]
    publishers: list[str]

    #remember to add these to the movie
    #poster, title,genre, release_year,runtime, summary, director, actors,
